import pandas as pd 
data={
    'product':['A','B','C','D'],
    'price':['$10','$20','$30','$40']
}
df=pd.DataFrame(data)
def clean_prices(df):
    df['price']=df['price'].str.replace('$').astype(float)
    return df
    cleaned_df=clean_prices(df)
    print(cleaned_df)

     