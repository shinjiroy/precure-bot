provider "aws" {
  region  = "ap-northeast-1"
  profile = "precure-bot-profile"
}

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.12.0"
    }
  }
  #   backend "s3" {
  #     bucket = "S3バケット名"
  #     key    = "precure-bot/terraform.tfstate"
  #     region = "ap-northeast-1"
  #   }
  backend "local" {
    path = "terraform.tfstate"
  }
}
