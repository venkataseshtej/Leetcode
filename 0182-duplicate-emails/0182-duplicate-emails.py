import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df=person
    df=df[df.duplicated(subset=['email'])]
    my_list=df['email'].unique()
    df = pd.DataFrame(my_list, columns=['email'])

    return df

    