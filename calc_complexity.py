import pandas as pd
from ecomplexity import ecomplexity

def main():
    print("Loading data...")
    df = pd.read_csv('matriz_ciuo_por_comuna.csv')
    
    # The first column is 'comuna', the rest are CIUO categories.
    print("Reshaping data to long format...")
    df_long = df.melt(id_vars='comuna', var_name='ciuo', value_name='count')
    
    # ecomplexity requires a time dimension, so we add a dummy year
    df_long['year'] = 2024
    
    # Define the mapping for ecomplexity
    cols_input = {
        'time': 'year',
        'loc': 'comuna',
        'prod': 'ciuo',
        'val': 'count'
    }
    
    print("Calculating complexity metrics...")
    # Calculate ecomplexity (returns a dataframe containing RCA, ECI, PCI, etc.)
    cdata = ecomplexity(df_long, cols_input)
    
    output_file = 'complexity_results.csv'
    print(f"Saving results to {output_file}...")
    cdata.to_csv(output_file, index=False)
    print("Done! Complexity calculation completed.")

if __name__ == '__main__':
    main()
