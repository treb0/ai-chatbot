import pygsheets
from google.oauth2 import service_account

import pandas as pd
import numpy as np

def set_up_gsheets():

    # Set up gSheets

    # service account
    # mtrebinonixon@favorable-tree-335800.iam.gserviceaccount.com

    creds = service_account.Credentials.from_service_account_file(
        '/Users/matias/Documents/Python/google_service_account_credentials/favorable-tree-335800-d2f923d740da.json',
        scopes=('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'),
        subject='mtrebinonixon@favorable-tree-335800.iam.gserviceaccount.com'
    )

    gs = pygsheets.authorize(custom_credentials=creds)

    return gs


def sheet_to_df(sheet_array, index_col_array = []):
    
    aux_df = pd.DataFrame(sheet_array)
    aux_df = aux_df.replace('',np.nan)
    aux_df = aux_df.dropna(how = "all", axis = 0)
    aux_df = aux_df.dropna(how = "all", axis = 1)
    aux_df.columns = aux_df.loc[0]
    aux_df = aux_df.drop(index = [0], axis = 0).reset_index(drop = True)
    
    if len(index_col_array) > 0:
        
        aux_keys = []
        
        for i in index_col_array:
            aux_keys.append(aux_df.columns[i])
                
        aux_df = aux_df.set_index(keys = aux_keys, drop = True)
    
    aux_df = aux_df.replace(np.nan,'')
    
    return aux_df 