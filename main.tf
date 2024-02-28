provider "aws" {
  region = "us-east-1"
  access_key = ""
  secret_key = ""
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
