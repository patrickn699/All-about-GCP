import subprocess


def authorize_account(account_name: str, key_file: str):
    
        """
        This method authorizes the account.
        Args:
            account_name: The name of the account.
            key_file: The path to the json key file.
        """

        # authorize the account.
        subprocess.run(['gcloud', 'auth', 'activate-service-account', account_name, '--key-file', key_file], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)



def create_function(name: str, region: str, runtime: str,
                     entry_point: str = None):


    """
    This method creates a function.
    Args:
        name: The name of the function.
        region: The region where the function must be deployed.
        runtime: The runtime(language) of the function.
        trigger-http: The trigger type of the function.
        entry_point: The entry point(name of function).

    """

    # enable the function api.
    subprocess.run(['gcloud','services','enable','cloudfunctions.googleapis.com'],shell=True,stdout=subprocess.PIPE)

    # create the function with required details.
    subprocess.run(['gcloud', 'functions', 'deploy', name, '--region', region, '--runtime', runtime,
     '--trigger-http',  '--entry-point', 
     entry_point], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)



def get_details(name: str, region: str):

    """
    This method gets the details of a function.
    Args:
        name: The name of the function.
    """
    # get the details of the function.
    subprocess.run(['gcloud', 'functions', 'describe', name,'--region', region], shell=True,stdout=subprocess.PIPE)



def delete_function(name: str, region: str):
    
    """
    This method deletes a function.
    Args:
        name: The name of the function.
    """
    # delete the function.
    subprocess.run(['gcloud', 'functions', 'delete', name, '--region', region], shell=True, stdout=subprocess.PIPE)



#get_details('test-function', 'us-central1')
#delete_function('test-function', 'us-central1')
#create_function(name = 'test-function', region = 'us-central1', runtime= 'nodejs8', entry_point='test-function')  
#authorize_account('test-account', 'test-key.json')