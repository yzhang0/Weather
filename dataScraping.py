import pandas as pd

def createCityRow(dataset, city):
    fname = city + ".csv"
    raw_data = pd.read_csv(fname, header=None)
    raw_data = raw_data[[0, 2]]
    df = pd.DataFrame(columns=['Date', city])
    date = ""
    index = 0
    for i, r in raw_data.iterrows():
        if not raw_data.loc[i][0].isdigit():
            mmyy = raw_data.loc[i][0] + " 2017"
        elif raw_data.loc[i][0].isdigit() and raw_data.loc[i][0] != "2017":
            df.loc[index] = [str(raw_data.loc[i][0]) + " " + mmyy, raw_data.loc[i][2]]
            index += 1
    if dataset.empty:
        return df
    else:
        dataset = pd.merge(dataset, df, on="Date", how="left")
        return dataset

def main():
    cities = ['Montreal', 'newYork', 'sanFrancisco', 'Toronto', 'Vancouver']
    df = pd.DataFrame()
    for city in cities:
        df = createCityRow(df, city)
    df.to_csv('All.csv', index=False)

main()
