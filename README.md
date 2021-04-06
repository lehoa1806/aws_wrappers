# aws_wrappers
Internal library for AWS services
## DynamoDB
### Introduction
#### 1. Database:
- An adapter to manage all DynamoDB tables
```python
from aws_wrappers.dynamodb.database import Database

database = Database.load_database()
table = database.load_xxx_table()
```
#### 2. Table:
- A wrapper to manage DynamoDB table behavior: get_item, delete_item, put_item, update_item, scan, query.
```python
partition_key = table.schema['partition_key']
sort_key = table.schema.get('sort_key')

item = table.get(
    partition_key='...',
    sort_key='...',
)

item.update({'last_modified': datetime.utcnow()})
table.update_item(
    add_data=item
)
```
