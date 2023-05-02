variable "slack_token" {
  type = string
}

variable "openai_api_key" {
  type = string
}

locals {
  name                 = "precure-bot"
  SLACK_TOKEN          = var.slack_token
  SLACK_SIGNING_SECRET = var.slack_signing_secret
  OPENAI_API_KEY       = var.openai_api_key
}
