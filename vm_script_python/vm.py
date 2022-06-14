from typing import List
from google.cloud import compute_v1
#from psutil import boot_time
from wait import wait_for_extended_operation




def disk_from_image(disk_type: str, disk_size_ingb: int, 
boot: bool, 
base_image: str, 
auto_delete: bool = True) -> compute_v1.AttachedDisk:

    """
    This method reates a disk from an image.
    Args:
        disk_type: The type of disk to create.
        disk_size_ingb: The size of the disk in GB.
        boot: Whether the disk will be used as the boot disk.
        base_image: The name of the image to use.
        auto_delete: Whether the disk will be automatically deleted when the instance is deleted.
    Retruns:
        The disk object.
    """

    boot_disk = compute_v1.AttachedDisk()
    initialize_params = compute_v1.AttachedDiskInitializeParams()
    initialize_params.source_image = base_image
    initialize_params.disk_size_gb = disk_size_ingb
    initialize_params.disk_type = disk_type
    boot_disk.initialize_params = initialize_params
    boot_disk.auto_delete = auto_delete
    boot_disk.boot = boot

    return boot_disk



def create_instance(
    project_id: str,
    zone: str,
    instance_name: str,
    disks: List[compute_v1.AttachedDisk],
    machine_type: str,
    network_link: str,
    subnetwork_link: str,
    external_access: bool = False,
    external_ipv4: str = None,
    preemptible: bool = False,
    delete_protection: bool = False
) -> compute_v1.Instance:

    """
    This method creates an vm instance.
    Args:
        project_id: The ID of the project.
        zone: The zone of the instance.
        instance_name: The name of the instance.
        disks: The disks to attach to the instance.
        machine_type: The machine type of the instance.
        network_link: The network link(VPC) of the instance.
        subnetwork_link: The subnetwork link(subnet) of the instance.
        external_access: Whether the instance should be accessible from outside.
        external_ipv4: The external IPv4 address of the instance.
        preemptible: Whether the instance should be preemptible.
        delete_protection: Whether the instance should be protected from deletion.
    Returns:
        The instance object.
    
    """


    instance_client = compute_v1.InstancesClient()

    # Use the network interface provided in the network_link argument for
    # confuguring the network.
    network_interface = compute_v1.NetworkInterface()
    network_interface.name = network_link # attach to the network (VPC)

    if subnetwork_link:
        network_interface.subnetwork = subnetwork_link # attach to the subnetwork (subnet)

    # Configure the network access configuration.
    if external_access:
        access = compute_v1.AccessConfig()
        access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
        access.name = "External NAT"
        access.network_tier = access.NetworkTier.PREMIUM.name
        if external_ipv4:
            access.nat_i_p = external_ipv4
        network_interface.access_configs = [access]

    # Collect information into the Instance object.
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.disks = disks
    
    instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"

    instance.network_interfaces = [network_interface]

    if preemptible:
        # Set the preemptible setting
        instance.scheduling = compute_v1.Scheduling()
        instance.scheduling.preemptible = True

    if delete_protection:
        # Set the delete protection for accidentally deleting the instance.
        instance.deletion_protection = True

    # make the request to create an instance.
    request = compute_v1.InsertInstanceRequest()
    request.zone = zone
    request.project = project_id
    request.instance_resource = instance

    # Wait for the create operation to complete.
    print(f"Creating the {instance_name} instance in {zone}...")

    # Create the instance request.
    operation = instance_client.insert(request=request)

    # Wait for the operation to complete.
    wait_for_extended_operation(operation, "instance creation")

    print(f"Instance {instance_name} created.")
    
    # Get the response.
    return instance_client.get(project=project_id, zone=zone, instance=instance_name)



win = "Windows Server 2019 Datacenter"

boot_disk = disk_from_image(disk_type='https://www.googleapis.com/compute/v1/projects/project_id/zones/us-central1-a/diskTypes/pd-standard', disk_size_ingb=10, boot=True, 
base_image="projects/windows-cloud/global/images/windows-server-2019-dc-v20190828")


create_instance(project_id="demo-project", zone="us-central1-a",
instance_name="vm-python",
machine_type="n1-standard-1", 
network_link="global/networks/demo-vpc", 
subnetwork_link="regions/us-central1/subnetworks/demo-subnet",
disks= [boot_disk])