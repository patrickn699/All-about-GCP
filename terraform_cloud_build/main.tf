provider "google" {
    project = "qwiklabs-gcp-02-929419494fe4"
   

  
}

resource "google_cloudbuild_trigger" "demo" {

    provider = google



    project = "qwiklabs-gcp-02-929419494fe4"

    trigger_template {
        branch_name = "master"
        repo_name = "run"
    }
   
    build {
        step {
            name = "gcr.io/cloud-builders/docker"
            args = ["build", "-t", "gcr.io/qwiklabs-gcp-02-929419494fe4/run", "."]
            id = "build"


        }
        step {
            name = "gcr.io/cloud-builders/docker"
            args = ["push", "gcr.io/qwiklabs-gcp-02-929419494fe4/run"]
            id = "push"
    }
        step {
            name = "gcr.io/cloud-builders/gcloud"
            args = ["run", "deploy", "pyweb", "--image", "gcr.io/qwiklabs-gcp-02-929419494fe4/run", "--port", "8800", "--allow-unauthenticated", "--region", "us-central1"]
            id = "deploy"
            

        }

    
    
}
}