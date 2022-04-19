terraform {
  backend "gcs" {
    bucket = "qwiklabs-gcp-03-33927fcdcd62-terraform-state-test-bucket-1"
    prefix = "qwiklabs-gcp-03-33927fcdcd62-terraform-state-test-bucket-1"
    credentials = "key.json"
  }
}

provider "google" {

    project = "qwiklabs-gcp-03-33927fcdcd62"
    credentials = file("key.json")
  
}

resource "google_compute_instance" "gce-1" {

    name = var.gce-1
    machine_type = var.machine_type
    zone = var.zone
    
    boot_disk {
        initialize_params {
            image = var.disk
        }
    }
    metadata_startup_script = file("startup.sh")

    tags = ["http-server","web"]

    network_interface {
        network = var.network
       
    }

  
}


resource "google_compute_instance" "gce-2" {

    name = var.gce-2
    machine_type = var.machine_type
    zone = var.zone
   
    boot_disk {
        initialize_params {
            image = var.disk
        }
    }
    metadata_startup_script = file("startup.sh")

    tags = ["http-server","web"]


    network_interface {
        network = var.network
       
       
      
    }

  
}


resource "google_compute_firewall" "default" {
 name    = "web-firewall"
 network = "default"

 allow {
   protocol = "icmp"
 }

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "8080", "1000-4000"]
  }

 source_ranges = ["0.0.0.0/0"]
 target_tags = ["web"]
}




