import os

def test_env():
    
    env_str = f'''
        {os.getenv("hostname")}
        {os.getenv("user")}
        {os.getenv("password")}
        {os.getenv("database")}
        {os.getenv("port")}

    
    '''
    print(env_str)