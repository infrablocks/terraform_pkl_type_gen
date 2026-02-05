variable "plain_number" {
  type = number
}

variable "plain_string" {
  type = string
}

variable "nullable_number" {
  type     = number
  nullable = true
}

variable "nullable_string" {
  type     = string
  nullable = true
}

variable "default_null_number" {
  type    = number
  default = null
}

variable "default_null_string" {
  type    = string
  default = null
}

variable "default_value_number" {
  type    = number
  default = 10
}

variable "default_value_string" {
  type    = string
  default = "hello"
}
