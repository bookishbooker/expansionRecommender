import pandas as pds

# Creates a global variable to search
games = pds.read_csv("bgg_GameItem.csv")


# Search function checks the .csv file for a game by name
def search_by_name(string):
    """
    Searches bgg_GameItem.csv for a game using a name passed as a string.
    :param string:
    :return: DataFrame
    """
    game_info = games[games["name"] == string]
    if game_info.empty:
        print("game not found")
        return None
    game_info.reset_index(inplace=True, drop=True)
    return game_info
