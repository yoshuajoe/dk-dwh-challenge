from pandas import pandas as pd
from tabulate import tabulate
import os
import json 
import sys

tables = {}

def walk(dir):
    for dirpath, dnames, fnames in os.walk(dir):
        for f in fnames:
            yield f

def list_dir(root):
    return os.listdir(root)

def eater(file, table_name):
    global tables
    with open(file, "r") as f:
        j = json.loads(f.read())
        if j["op"] == "c":
            basic_dict = {"id":j["id"], "ts":j["ts"]}
            basic_dict.update(j["data"])
            if tables[table_name].empty:
                tables[table_name] = pd.DataFrame(basic_dict, columns = basic_dict.keys(), index = [basic_dict["id"]])
            else:
                t_df = pd.DataFrame(basic_dict, columns = basic_dict.keys(), index = [basic_dict["id"]])
                tables[table_name] = pd.concat([tables[table_name], t_df])
        else:
            for k,v in j["set"].items():
                if k in tables[table_name].columns:
                    tables[table_name][k] = tables[table_name][k].where(tables[table_name]['id'] != j['id'], v)
                else:
                    tables[table_name][k] = [None]
                    tables[table_name][k] = tables[table_name][k].where(tables[table_name]['id'] != j['id'], v)

def logic():
    global tables
    data_path = os.getenv("DATA_PATH")
    if data_path is None:
        raise RuntimeError("Please set the DATA_PATH by using \n\n export DATA_PATHS=<your path> \n\n")
    
    ldir = list_dir(data_path)
    for d in ldir:
        tables.setdefault(d, pd.DataFrame())  
        for row in sorted(walk("{}/{}".format(data_path, d))):
            eater("{}/{}/{}".format(data_path, d, row), d)
   
if __name__ == "__main__":
    logic()
    
    for args in sys.argv:
        spl = args.split("=")
        if spl[0] == "--tabulate":
            for table in tables:
                print("\nTable: {}".format(table))
                print(tabulate(tables[table], headers='keys', tablefmt='psql')) 
        if spl[0] == "--join":
            joined = pd.merge(tables["accounts"], tables["savings_accounts"],
                        how="left", on=["savings_account_id"])
            joined = pd.merge(joined, tables["cards"],
                        how="left", on=["card_id"])
            
            print(tabulate(joined, headers='keys', tablefmt='psql')) 