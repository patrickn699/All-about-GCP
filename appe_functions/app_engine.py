import subprocess


def authorize_account(account_name: str, key_file: str):
    
        """
        This method authorizes the account with gcp.
        Args:
            account_name: The name of the account.
            key_file: The path to the json key file.
        """

        # authorize the current account with gcp.
        subprocess.run(['gcloud', 'auth', 'activate-service-account', account_name, '--key-file', key_file], shell=True)



def create_appengine_env(project_id: str, region: str):

    """
    This method creates an app.
    Args:
        project_id: The ID of the project.
    """

    # Enable appengine service api
    subprocess.run(['gcloud','services','enable','appengine.googleapis.com'], shell=True)

    # Create app in the sepcified region.
    subprocess.run(['gcloud', 'app', 'create', '--project', project_id, '--region', region], shell=True) 



def deploy_app(project_files: str, yaml_file: str, version_name: str):

    """
    This method deploys an app in app engine.
    Args:
        project_files: the path to the folder where all your deployment files reside.
        yaml_file: The name of the yaml file which contains the deployment configuration and runtime.
        version_name: The name of the version for your current deployment.
    """

    # Deploy app with sepicified version if provided else deploys the latest version.
    subprocess.run(['gcloud', 'app', 'deploy', '--project', project_files,'--appyaml', yaml_file, '--version', version_name], shell=True, input='Y'.encode())

   

def traffic_control( ratio: float,version_name_1: str, version_name_2: str):

    """
    This method controls the incomming traffic of the app between its versions.
    Args:
        version_name: The name of the version.
        traffic_split: The traffic split ratio between the versions.
    """

    # control the traffic across the version.
    subprocess.run(['gcloud', 'app', 'services', 'set-traffic', '--splits='+version_name_1+'='+str(ratio)+','+version_name_2+'='+str(ratio)], shell=True)



authorize_account('demo-aacount', 'key.json')
create_appengine_env('demo-1890', 'us-central1')
deploy_app('my-demo-app', 'app.yaml', 'v1')
traffic_control(0.5,'v1','v2')