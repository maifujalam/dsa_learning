locals {
  abc=["two","three"]
}
resource "null_resource" "with_count" {
  count = length(local.abc)
  triggers = {
    index = count.index
    value = local.abc[count.index]
  }
}
resource "null_resource" "with_foreach" {
  for_each = toset(local.abc)
  triggers = {
    index = each.key
    value = each.value
  }
}