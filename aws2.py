
import boto3

#bucket=jayeshsample
bucket = input('Enter bucket Name:')

#path=1.png
path = input('Enter object path:')

s3 = boto3.resource('s3')

versions = s3.Bucket(bucket).object_versions.filter(Prefix=path)

#list of version id 
ver_list=[]

for version in versions:
    obj = version.get()
    print(obj.get('VersionId'), obj.get('ContentLength'), obj.get('LastModified))
    ver_list.append(obj.get('VersionId'))

#second latest version id
id=ver_list[1]
print(id)

#downloading second latest version
s3.meta.client.download_file(bucket, path,'/tmp/1.png', ExtraArgs={'VersionId': id})





           
