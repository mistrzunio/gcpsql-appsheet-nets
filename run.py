import uuid

# you want to customize it:
instance_id = 'app-db'+uuid.uuid4().hex[:8]

storage = 'HDD'
# storage = 'SSD'

# tier = 'db-f1-micro'
# tier = 'db-g1-small'
tier = 'db-n1-standard-1'

region = 'europe-west1'

ip_lst = '''20.189.130.98
20.189.132.63
40.67.216.152
40.67.216.182
40.67.219.84
138.91.195.239
20.189.139.27
20.189.138.55
20.189.138.139
20.189.139.109
20.189.139.123
20.189.138.180
20.189.138.40
52.149.110.221
52.149.111.209
52.149.111.211
52.149.111.248
51.144.56.20
51.144.57.117
52.138.118.136
52.138.118.137
34.87.131.237
34.87.103.64
35.197.185.203
35.244.126.141
35.204.213.55
34.91.161.74
35.222.253.144
34.71.7.214
35.194.89.186
35.245.209.204
35.203.191.15
35.247.56.116
35.240.247.148
34.87.159.166
34.87.233.115
35.244.107.184
35.204.102.20
35.204.159.159
35.239.203.99
35.239.112.17
34.86.96.199
35.245.229.252
34.83.247.7
35.247.40.210'''

comma_ip_lst = ip_lst.replace("\n",",");

print(f"gcloud sql instances create {instance_id} --storage-type={storage} --tier={tier} --region={region} --authorized-networks={comma_ip_lst}")
