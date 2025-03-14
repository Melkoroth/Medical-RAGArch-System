
resource "aws_api_gateway_stage" "prod" {
  deployment_id = aws_api_gateway_deployment.prod.id
  rest_api_id   = aws_api_gateway_rest_api.prod.id
  stage_name    = "prod"

  documentation_version = "1.0"

  variables = {
    "lambda_alias" = "live"
  }

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_logs.arn
    format = jsonencode({
      requestId = "$context.requestId",
      ip        = "$context.identity.sourceIp",
      userAgent = "$context.identity.userAgent",
      caller    = "$context.identity.caller"
    })
  }
}
