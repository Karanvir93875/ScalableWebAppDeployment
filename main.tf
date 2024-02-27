provider "aws" {
  region = "us-east-1"
  access_key = "AKIAYS2NXHOP7HMF2DZM"
  secret_key = "uGiKH62NtwBYP5SwIdluvOn5vQzWopIz9mnHWnug"
}

resource "aws_instance" "example" {
  ami           = "ami-01952eddad7516aa7"
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash  
              apt-get update
              apt-get install -y telnet curl wget git
              EOF

  tags = {
    Name = "UbuntuServer"
  }
}