
def create_engine(config):
    import snowflake.connector
    from snowflake.connector.pandas_tools import write_pandas
    
    account = config['snowflake']['account']
    username = config['snowflake']['username'] 
    password = config['snowflake']['password']
    role = config['snowflake']['role']
    database = config['snowflake']['database']
    schema = config['snowflake']['schema']
    warehouse = config['snowflake']['warehouse']
    engine = snowflake.connector.connect(account =account,
                                user = username,
                                password = password,
                                role = role,
                                database = database,
                                schema = schema,
                                warehouse = warehouse
                                )
    return engine