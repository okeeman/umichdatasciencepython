def proportion_of_education():
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv")
    # Normalize gives proportions.
    value_counts = df['EDUC1'].value_counts(normalize=True)

    return {"less than high school":value_counts[1],
            "high school":value_counts[2],
            "more than high school but not college":value_counts[3],
            "college":value_counts[4]}
    
if __name__ == '__main__':
    print(proportion_of_education())
