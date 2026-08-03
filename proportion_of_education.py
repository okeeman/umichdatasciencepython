def proportion_of_education():
    import pandas as pd
    # df = pd.read_csv("NISPUF17.csv")
    # on Coursera the file is in assets/
    df = pd.read_csv("assets/NISPUF17.csv")
    value_counts = df['EDUC1'].value_counts(normalize=True) # normalize gives proportions.

    return {"less than high school":value_counts[1],
            "high school":value_counts[2],
            "more than high school but not college":value_counts[3],
            "college":value_counts[4]}
    
if __name__ == '__main__':
    print(proportion_of_education())
    print("Executed.")