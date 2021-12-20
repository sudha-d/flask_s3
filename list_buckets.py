import boto3

s3 = boto3.client('s3')



# client=boto3.client('s3')
# response1 = s3.create_bucket(
#     ACL='public-read',
#     Bucket='bucket-sudha4',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1'
#         },
#     GrantFullControl='string',
#     GrantRead='string',
#     GrantReadACP='string',
#     GrantWrite='string',
#     GrantWriteACP='string',
#     ObjectLockEnabledForBucket=False,
#     ObjectOwnership='ObjectWriter'
#     )
# print(response1)
# import boto3
s3 = boto3.client("s3")
# bucket = s3.create_bucket(Bucket='bucket-sudha4',CreateBucketConfiguration={'LocationConstraint':'ap-south-1'},
#                              ACL='public-read')
# print(bucket)
response = s3.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
res1=boto3.resource("s3")
res1.Bucket("bucket-sudha4").upload_file("hello.txt", "one.txt")


##list all objects from bucket
my_bucket = res1.Bucket('bucket-sudha4')
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)

res1.Bucket('bucket-sudha4').download_file('one.txt', 'hai.txt')
# s3.download_file('bucket-sudha4', 'hello.tht', 's1.txt')

print(' download success')