import subprocess


def authorize_account(account_name: str, key_file: str):
    
        """
        This method authorizes an account.
        Args:
            account_name: The name of the account.
            key_file: The path to the json key file.
        """

        # authorize the account.
        subprocess.run(['gcloud', 'auth', 'activate-service-account', account_name, '--key-file', key_file], shell=True, stdout=subprocess.PIPE)





def create_appengine(project_id: str):

    """
    This method creates an app.
    Args:
        project_id: The ID of the project.
    """

    # Enable appengine service api
    subprocess.run(['gcloud','services','enable','appengine.googleapis.com'], shell=True, stdout=subprocess.PIPE)

    # list of regions available in appengine.
    subprocess.run(['gcloud', 'compute', 'regions', 'list'], shell=True, stdout=subprocess.PIPE)

    region_number = int(input('Enter the region number from 1 - 20:'))

    # Create app
    if region_number <= 20:
        subprocess.run(['gcloud', 'app', 'create', '--project', project_id], shell=True, stdout=subprocess.PIPE, input=str(region_number).encode()) 

    else:
        print('Invalid region number')



def deploy_app(project_files: str, yaml_file: str, version_name: str):

    """
    This method deploys an app in app engine.
    Args:
        project_files: the path to the folder where all your deployment files reside.
        yaml_file: The name of the yaml file whcih contains the deployment configuration and runtime.
    """

    # Deploy app
    if version_name != '':

        subprocess.run(['gcloud', 'app', 'deploy', '--project', project_files,'--appyaml', yaml_file, '--version', version_name], shell=True, stdout=subprocess.PIPE, input='Y'.encode())

    else:
        subprocess.run(['gcloud', 'app', 'deploy', '--appyaml', yaml_file, '--project', project_files], shell=True, stdout=subprocess.PIPE)



def traffic_control(version_name: str, ratio: float):

    """
    This method controls the traffic of the app between its versions.
    Args:
        version_name: The name of the version.
        traffic_split: The traffic split of the version.
    """


    # control the traffic across the version.
    subprocess.run(['gcloud', 'app', 'services', 'set-trafffic', '--splits','=', version_name+'=', str(ratio)], shell=True, stdout=subprocess.PIPE)



#authorize_account('demo', './key.json')
#create_appengine('demo')
deploy_app('demo', 'app.yaml', 'v1')