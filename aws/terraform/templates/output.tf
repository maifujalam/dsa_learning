output "all_zones" {
  value = data.aws_availability_zones.available.names
}
