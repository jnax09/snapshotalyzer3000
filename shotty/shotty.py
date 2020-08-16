import boto3

# put script code inside name block
if __name__ == '__main__':
    session = boto3.Session(profile_name='awsCertifiedDev')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)
