from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time
from wait import wait_for_extended_operation
from google.cloud import compute_v1

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)



def create_vpc(region: str, project_id: str, vpc_name: str, subnet_name: str):


    """
    This method creates a VPC.
    Args:
        region: The region in which to create the VPC.
        project_id: The project ID in which to create the VPC.
        vpc_name: The name of the VPC.
        subnet_name: The name of the subnet.
    """

    vpc = compute_v1.Vpc()
    vpc.name = vpc_name


    vpc_network_body = {
        "routingConfig": {
            "routingMode": "REGIONAL"
        },
        "autoCreateSubnetworks": False,
        "name": vpc_name,
        "mtu": 1460,
        "region": f"{region}"
    }

    subnetwork_body = {
        "enableFlowLogs": False,
        'ipCidrRange': "10.0.0.0/24",
        "name": subnet_name,
        "network": "projects/"+project_id+"/global/networks/"+vpc_name,
        "privateIpGoogleAccess": False,
        "region": f"{region}"
        
    }
    #"projects/network-demo-1-332510/global/networks/pnetwork"

    request1 = service.networks().insert(project=project_id, body=vpc_network_body)
    response1 = request1.execute()

    pprint(response1)

    print("creating network...\n")
    time.sleep(30)

    request2 = service.subnetworks().insert(project=project_id, region=region, body=subnetwork_body)
    response2 = request2.execute()

    pprint(response2)

    print("creating subnetwork...\n")



def create_firewall_rule(project_id: str, firewall_rule_name: str, network: str) -> compute_v1.Firewall:

    """
    Creates a simple firewall rule allowing for incoming HTTP and HTTPS access from the entire Internet.
    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        firewall_rule_name: name of the rule that is created.
        network: name of the network the rule will be applied to. Available name formats:
            * https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/{network}
            * projects/{project_id}/global/networks/{network}
            * global/networks/{network}
    Returns:
        A Firewall object.
    """

    firewall_rule = compute_v1.Firewall()
    firewall_rule.name = firewall_rule_name
    firewall_rule.direction = "INGRESS"

    allowed_ports = compute_v1.Allowed()
    allowed_ports.I_p_protocol = ["rdp","http"]
    allowed_ports.ports = ["80","3389"]

    firewall_rule.allowed = [allowed_ports]
    firewall_rule.source_ranges = ["0.0.0.0/0"]
    firewall_rule.network = network
    firewall_rule.description = "Allowing rdp on port 3389 from Internet."

    firewall_rule.target_tags = ["web"]

    # Note that the default value of priority for the firewall API is 1000.
    # If you check the value of `firewall_rule.priority` at this point it
    # will be equal to 0, however it is not treated as "set" by the library and thus
    # the default will be applied to the new rule. If you want to create a rule that
    # has priority == 0, you need to explicitly set it so:
    # TODO: Uncomment to set the priority to 0
    firewall_rule.priority = 500

    firewall_client = compute_v1.FirewallsClient()
    operation = firewall_client.insert(
        project=project_id, firewall_resource=firewall_rule
    )

    wait_for_extended_operation(operation, "firewall rule creation")

    return firewall_client.get(project=project_id, firewall=firewall_rule_name)



create_vpc(region = 'us-crentral1', project_id = 'demo-project',vpc_name='demo-vpc', 
subnet_name='demo-subnet')

create_firewall_rule(project_id='demo-project', firewall_rule_name='demo-firewall', 
network='global/networks/demo-vpc')
