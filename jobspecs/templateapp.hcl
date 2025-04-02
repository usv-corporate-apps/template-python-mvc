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

variable "APP_NAME" {
  description = "The name of the application"
  type        = string
}

job "python-mvc-job" {
  name = "${var.APP_NAME}"
  datacenters = [var.NOMAD_DATACENTER]
  type        = "service"

  group "main" {
    count = 1

    network {
      port "http" {
        to = 5000
      }
    }

    task "main" {
      driver = "docker"

      config {
        image = "${var.REGISTRY_SERVER}/${var.APP_NAME}:latest"

        auth {
          username = "${var.REGISTRY_USERNAME}"
          password = "${var.REGISTRY_PASSWORD}"
        }
      }

      env {
        FLASK_ENV=test
      }

      service {
        name = "${var.APP_NAME}"
        tags = ["logging"]
        port = "http"

        check {
          name     = "${var.APP_NAME}"
          type     = "http"
          path     = "/"
          interval = "10s"
          timeout  = "2s"
        }
      }
    }
  }
}