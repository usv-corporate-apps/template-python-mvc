variable "NOMAD_DATACENTER" {
  description = "The datacenter where the job will be deployed"
  type        = string
}

variable "REGISTRY_SERVER" {
  description = "The registry server to pull the image from"
  type        = string
  default = "usva1nprdidpacr01.azurecr.io"
}

variable "REGISTRY_USERNAME" {
  description = "The username for the githubactions user in Nexus"
  type        = string
}

variable "REGISTRY_PASSWORD" {
  description = "The password for the githubactions user in Nexus"
  type        = string
}

job "template-python-mvc" {
  datacenters = [var.NOMAD_DATACENTER]
  type        = "service"

  group "template-python-mvc" {
    count = 1

    network {
      port "template-python-mvc" {
        to = 5000
      }
    }

    task "template-python-mvc" {
      driver = "docker"

      config {
        image = "${var.REGISTRY_SERVER}/template-python-mvc:latest"

        auth {
          username = "${var.REGISTRY_USERNAME}"
          password = "${var.REGISTRY_PASSWORD}"
        }
      }

      env {
        FLASK_ENV=test
      }

      service {
        name = "template-python-mvc"
        tags = ["logging"]
        port = "template-python-mvc"

        check {
          name     = "template-python-mvc"
          type     = "http"
          path     = "/"
          interval = "10s"
          timeout  = "2s"
        }
      }
    }
  }
}