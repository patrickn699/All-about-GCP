variable "gcs_bucket" {

    default = "qwiklabs-gcp-03-33927fcdcd62-terraform-state-test-bucket-1"
    description = "name of gcs_bucket for terraform state"
    type = string
  
}

variable "gce-1" {

    default = "terraform-pn-instance-test-1"
    description = "The name of the first GCE instance"
    type = string

}

variable "gce-2" {

    default = "terraform-pn-instance-test-2"
    description = "The name of the second GCE instance"
    type = string
  
}

variable "machine_type" {
    
        default = "n1-standard-1"
        description = "The machine type of the GCE instance"
        type = string
    
}

variable "zone" {

    default = "us-central1-a"
    description = "The zone of the GCE instance"
    type = string
  
}

variable "disk" {
    
        default = "debian-8-jessie-v20160803"
        description = "The disk image of the GCE instance"
        type = string
    
  
}

variable "network" {

    default = "default"
    description = "The network of the GCE instance"
    type = string
  
  
}


