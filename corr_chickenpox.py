def corr_chickenpox():
    import scipy.stats as stats
    import pandas as pd
    
    df = pd.read_csv("assets/NISPUF17.csv")
    df = df[['HAD_CPOX', 'P_NUMVRC']].dropna()
    # Looking for correlation between HAD_CPOX Yes (1), No (2); and number of varicella vaccines.
    df = df[(df['HAD_CPOX'] == 1) | (df['HAD_CPOX'] == 2)]
    corr, pval = stats.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])
    return corr

if __name__ == '__main__':
    print(corr_chickenpox())