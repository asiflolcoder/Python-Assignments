#defining the pipeline configs
pipeline_name = "sales_pipeline"
source_name = "MySQL Database"
source_format = "CSV"
destination = "Amazon S3"
batch_size = 1000
delimeter = ','
schedule = "daily"
active = True
status = "Active" if active else "Inactive"
version = 1.2
owner = "data_team"
#printing the values
print(f"Pipeline Name : {pipeline_name}")
print(f"Source        : {source_name}")
print(f"Source Format : {source_format}")
print(f"Destination   : {destination}")
print(f"Batch Size    : {batch_size}")
print(f"Delimiter     : {delimeter}")
print(f"Schedule      : {schedule}")
print(f"Active        : {status} ")
print(f"Version       : {version}")
print(f"Owner         : {owner}")