data "archive_file" "invoke_function" {
  type        = "zip"
  source_dir  = "/app/app"
  output_path = "app.zip"
}

resource "aws_lambda_function" "invoke_function" {
  filename         = data.archive_file.invoke_function.output_path
  function_name    = "${local.name}-invoke-function"
  role             = aws_iam_role.lambda_role.arn
  handler          = "app.lambda_handler"
  source_code_hash = data.archive_file.invoke_function.output_base64sha256
  runtime          = "python3.9"
  architectures    = ["arm64"]

  memory_size = 128
  timeout     = 30

  environment {
    variables = {
      SLACK_TOKEN          = local.SLACK_TOKEN
      OPENAI_API_KEY       = local.OPENAI_API_KEY
      SLACK_SIGNING_SECRET = local.SLACK_SIGNING_SECRET
    }
  }
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lambda_role" {
  name               = "${local.name}-invoke-lambda-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function_url" "lambda_url" {
  function_name      = aws_lambda_function.invoke_function.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = true
    allow_origins     = ["*"]
    allow_methods     = ["*"]
    allow_headers     = ["date", "keep-alive"]
    expose_headers    = ["keep-alive", "date"]
    max_age           = 86400
  }
}
