from google.cloud import compute_v1


def create_instance(project_id, zone, instance_name, instance_type):

    compute = compute_v1.ComputeEngine()
    operation = compute.instances().insert(
        project=project_id,
        zone=zone,
        body={
            'name': instance_name,
            'machineType': 'zones/%s/machineTypes/%s' % (zone, instance_type),
            'disks': [
                {'boot': True,
                 'autoDelete': True,
                 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'}
                    }
                ],
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [
                    {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
                ]
            }],
            'serviceAccounts': [{
                'email': 'default',
                'scopes': [
                    'https://www.googleapis.com/auth/compute',
                    'https://www.googleapis.com/auth/devstorage.full_control',
                    'https://www.googleapis.com/auth/servicecontrol',
                    'https://www.googleapis.com/auth/logging.write',
                    'https://www.googleapis.com/auth/monitoring.write',
                ]
            }],
            'metadata': {
                'items': [{
                    'key': 'startup-script',
                    'value': '#! /bin/bash\n'
                                'apt-get update\n'
                                'apt-get install -y python3-pip\n'
                                'pip3 install google-cloud-vision\n'
                                'python3 demo.py\n'
                }]
            },
            'tags': {
                'items': ['http-server']
            },
            'scheduling': {
                'preemptible': False
            }
        }
    ).execute()



