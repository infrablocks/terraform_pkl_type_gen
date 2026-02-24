variable "string" {
  type = string
}

variable "number" {
  type = number
}

variable "bool" {
  type = bool
}

variable "list" {
  type = list(any)
}

variable "list_of_any" {
  type = list(any)
}

variable "list_of_strings" {
  type = list(string)
}

variable "list_of_numbers" {
  type = list(number)
}

variable "list_of_booleans" {
  type = list(bool)
}

variable "map_of_any" {
  type = map(any)
}

variable "map_of_strings" {
  type = map(string)
}

variable "map_of_numbers" {
  type = map(number)
}

variable "map_of_booleans" {
  type = map(bool)
}

variable "object_of_things" {
  type = object({
    name    = string
    count   = number
    enabled = bool
  })
}
