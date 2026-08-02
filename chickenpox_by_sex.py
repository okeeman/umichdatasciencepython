def chickenpox_by_sex():
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv")

    # Number of varicella containing doses. Using greater than zero avoids 0.0 and Nan.
    had_varicella = df[df["P_NUMVRC"] > 0]

    # HAD_CPOX, 1 = Yes, 2 = No.
    had_varicella_hadcpox = had_varicella[had_varicella["HAD_CPOX"] == 1]
    had_varicella_nocpox = had_varicella[had_varicella["HAD_CPOX"] == 2]

    # Breakdown by sex. SEX, 1 = Male, 2 = Female.
    had_varicella_hadcpox_male = had_varicella_hadcpox[had_varicella_hadcpox["SEX"] == 1]
    had_varicella_nocpox_male = had_varicella_nocpox[had_varicella_nocpox["SEX"] == 1]
    ratio_male = len(had_varicella_hadcpox_male) / len(had_varicella_nocpox_male)

    had_varicella_hadcpox_female = had_varicella_hadcpox[had_varicella_hadcpox["SEX"] == 2]
    had_varicella_nocpox_female = had_varicella_nocpox[had_varicella_nocpox["SEX"] == 2]
    ratio_female = len(had_varicella_hadcpox_female) / len(had_varicella_nocpox_female)

    return {"male":ratio_male,
            "female":ratio_female}

if __name__ == '__main__':
   assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."
