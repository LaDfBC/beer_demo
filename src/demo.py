import pandas

def load_file(filename):
    return pandas.read_csv(filename)

def join_dataframes(left_df, right_df, column_name):
    return left_df.set_index(column_name).join(right_df.set_index(column_name), on=column_name, how='left')

def process_dataframe(dataframe):
    print("Average ABV across all beers: " + str((100.0 * dataframe.mean(axis = 0)['abv'])))

    mask = df['style'].str.contains('American Pale Ale', na=False)
    apa_filter_df = df[mask]
    print("Average ABV across American Pale Ales: " + str((100.0 * apa_filter_df.mean(axis=0)['abv'])))

    missouri_filter_df = df[df['state'].str.strip() == 'MO']['brewery_name'].unique()
    print("Breweries recognized in Missouri: ")
    print(missouri_filter_df)

    schlafly_beers_df = df[df['brewery_name'].str.strip() == 'Schlafly Brewing Company']
    print("Beers made by Schlafly: ")
    print(schlafly_beers_df['beer_name'].unique())

    print("And the query you might use for a true business purpose: Average ABV for Schlafly Brewing: ")
    print(str(100.0 * schlafly_beers_df.mean(axis=0)['abv']))


if __name__ == '__main__':
    beers_df = load_file("/home/george/beer_stuff/beers.csv")
    breweries_df = load_file("/home/george/beer_stuff/breweries.csv")
    df = join_dataframes(beers_df, breweries_df, 'brewery_id')
    process_dataframe(df)