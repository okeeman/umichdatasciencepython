def average_influenza_doses():
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv")
    
    breast_fed = df[df['CBF_01'] == 1]
    not_breast_fed = df[df['CBF_01'] == 2]

    avg_shots_bf = breast_fed['P_NUMFLU'].mean()
    avg_shots_nbf = not_breast_fed['P_NUMFLU'].mean()

    return (avg_shots_bf, avg_shots_nbf)
