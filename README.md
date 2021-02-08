# gcpsql-appsheet-nets

When you want to use Google Cloud SQL database as data source in AppSheet, 
you need to authorize long list of AppSheet servers IPs. 
If your database is yet to be created, using this script will save you manual adding AppSheet IPs.

Script includes AppSheet public IPs as listed in: https://help.appsheet.com/en/articles/1658319-managing-ip-addresses-and-firewall-information 

Google Cloud SDK is **Required** (https://cloud.google.com/sdk/docs/install)


#### 1. Clone repo or download `run.py` 

#### 2. Confirm if you are logged to gcp:
```
gcloud auth list
```
#### 3. (Optional) edit `run.py` 
You can customize `instance_id`, `storage`, `tier` and `region`.
Add additional parameters as in: https://cloud.google.com/sdk/gcloud/reference/sql/instances/create

#### 4. Run
 
```
python3 run.py | sh
```

On following ERROR: 
`Operation https://sqladmin.googleapis.com/sql/v1beta4/projects/blah-blah-blah is taking longer than expected.` just 
go to gcp console, usually 'Creating Cloud SQL instance' continues normally
