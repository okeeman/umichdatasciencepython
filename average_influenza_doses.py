def average_influenza_doses():
    # one tuple (avg no flu shots breastfed, not breastfed no. flu shots)
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv")

    breast_fed = df[df['BF_ENDR06'].notna()]     # retain whole row based on condition in one column.
    not_breast_fed = df[df['BF_ENDR06'].isna()]

    num_breast_fed = len(breast_fed)
    num_not_breast_fed = len(not_breast_fed)
    
    # easier way - use P_NUMFLU, gives a number
    total_shots_bf = breast_fed['P_NUMFLU'].sum()
    total_shots_nbf = not_breast_fed['P_NUMFLU'].sum()

    avg_shots_bf = total_shots_bf / num_breast_fed
    avg_shots_nbf = total_shots_nbf / num_not_breast_fed

    return (avg_shots_bf, avg_shots_nbf)

if __name__ == '__main__':
    #print(average_influenza_doses())
    assert len(average_influenza_doses()) == 2, "Return two values in a tuple, the first for yes and the second for no."
    print("Executed.")