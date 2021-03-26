
# Configure the Azure provider
###For AWS
#export AWS_ACCESS_KEY_ID 
#export AWS_SECRET_ACCESS_KEY 
#export AWS_DEFAULT_REGION

###For Azure
#export AZURE_SUBSCRIPTION_ID=''
#export AZURE_TENANT_ID=''
#export AZURE_CLIENT_ID=''
#export AZURE_CLIENT_SECRET=''

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.53.0"
    }
  }
}

terraform {
  backend "s3" {
    bucket = "terraform-bucket-jenkins"
    key    = "statefile"
    region = "us-west-2"
  }
}