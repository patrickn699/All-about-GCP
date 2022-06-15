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



def create_function(name: str, region: str, runtime: str, entry_point: str):


    """
    This method creates a cloud function.
    Args:
        name: The name of the function.
        region: The region where the function must be deployed.
        runtime: The runtime(language) of the function which is to be written.
        trigger-http: The function will trigger on http events.
        entry_point: The entry point(name of function which should be run).
    """

    # enable the cloud function api.
    subprocess.run(['gcloud','services','enable','cloudfunctions.googleapis.com'],shell=True)

    # create the function with required parameters.
    subprocess.run(['gcloud', 'functions', 'deploy', name, '--region', region, '--runtime', runtime,
     '--trigger-http',  '--entry-point',  entry_point], shell=True)



def get_details(name: str, region: str):

    """
    This method gets all the details of a deployed function.
    Args:
        name: The name of the function.
        region: The region where the function is deployed.
    """
    # get the details of the function.
    subprocess.run(['gcloud', 'functions', 'describe', name,'--region', region], shell=True)



def delete_function(name: str, region: str):
    
    """
    This method deletes a function.
    Args:
        name: The name of the function to be deleted.
    """
    # delete the function.
    subprocess.run(['gcloud', 'functions', 'delete', name, '--region', region], shell=True)


authorize_account('test-account', 'test-key.json')
create_function(name = 'test-function-1', region = 'us-central1', runtime= 'python38', entry_point='test-function')  
get_details('test-function-1', 'us-central1')
delete_function('test-function-1', 'us-central1')