# Lambdaで発行されたURLを出力する
output "invoke_url" {
  value = aws_lambda_function_url.lambda_url.function_url
}
