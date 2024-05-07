import json
import os


PATH = os.path.dirname(os.path.abspath(__file__))

def insert_account(account_info: dict):
    """insert datas in txt file"""
    with open(f"{PATH}\\account.txt", "w") as file:
        file.write(f'{account_info["pin"]}\n{account_info["ref_account"]}')
        file.close()

def get_account():
    """get and delete datas in txt file"""
    with open(f"{PATH}\\account.txt", "r") as file:
        result = file.readlines()
        file.close()
    open(f"{PATH}\\account.txt", "w")
    return result
