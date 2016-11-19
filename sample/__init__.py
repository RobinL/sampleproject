import pandas as pd 
import numpy as np
def main():
    """Entry point for the application script"""
    print("Call your main application code here")

def get_random_df():
	return pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
