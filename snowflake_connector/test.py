import snowflake_connector

def create_engine(config):
    account = config['snowglake']['account']
    username = config['snowglake']['username'] 
    password = config['snowglake']['password']
    role = config['snowglake']['role']
    database = config['snowglake']['database']
    schema = config['snowglake']['schema']
    warehouse = config['snowglake']['warehouse']
    engine = snowflake_connector.connect(account =account,
                                user = username,
                                password = password,
                                role = role,
                                database = database,
                                schema = schema,
                                warehouse = warehouse
                                )
    return engine