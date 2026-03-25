module "child" {
  source = "./modules/child"

  sub_variable = "foo"
}
