from typing import Any, Dict, Optional

import boto3
from botocore.config import Config

from .table import Table


class Database:
    """
    The Class to manage all DynamoDB tables.
    """
    DEFAULT_REGION = 'ap-southeast-1'

    def __init__(
        self,
        max_pool_connections: Optional[int] = None,
        region: str = None,
    ) -> None:
        kwargs: Dict[str, Any] = {'region_name': region or self.DEFAULT_REGION}
        if max_pool_connections:
            # Fix "Connection pool is full, discarding connection:
            # dynamodb.us-west-2.amazonaws.com" issue
            config = Config(user_agent_extra='Resource',
                            max_pool_connections=max_pool_connections)
            kwargs['config'] = config
        self.dynamodb = boto3.resource('dynamodb', **kwargs)

    @property
    def tables(self) -> Dict[str, Table]:
        return {
            table.name: Table(table) for table in self.dynamodb.tables.all()
        }

    def load_table(
        self,
        table_name: str,
    ) -> Table:
        return Table(self.dynamodb.Table(table_name))

    # Load tables:
    '''
    # Replace DYNAMODB_TABLE_1, DYNAMODB_TABLE_2 with the actual table names
    def load_table_1(self) -> Table:
        return self.load_table(table_name='DYNAMODB_TABLE_1')

    def load_table_2(self) -> Table:
        return self.load_table(table_name='DYNAMODB_TABLE_2')
    '''
