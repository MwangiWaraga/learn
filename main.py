from thefuzz import process, fuzz

def correct_typos(df, column_name, valid_list, threshold=80):
    """
    Fix typos in a column of a DataFrame using fuzzy matching.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the column to clean.
        column_name (str): The name of the column to correct.
        valid_list (list or pd.Series): List of valid/correct values.
        threshold (int): Minimum similarity score to accept a match.

    Returns:
        pd.DataFrame: A copy of the DataFrame with corrected values.
    """
    corrections = {}
    unique_values = df[column_name].unique()

    for typo in unique_values:
        match, score, _ = process.extractOne(typo, valid_list, scorer=fuzz.ratio)
        if score >= threshold:
            corrections[typo] = match

    # Apply corrections
    df[column_name] = df[column_name].replace(corrections)
    return df


# the below creates a new column with the corrected values instead of modifying the original column

def correct_typos_with_new_column(df, column_name, valid_list, new_column_name, threshold=80):
    """
    Fix typos in a column of a DataFrame using fuzzy matching and create a new column for corrected values.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the column to clean.
        column_name (str): The name of the column to correct.
        valid_list (list or pd.Series): List of valid/correct values.
        new_column_name (str): Name of the new column for corrected values.
        threshold (int): Minimum similarity score to accept a match.

    Returns:
        pd.DataFrame: A copy of the DataFrame with a new column for corrected values.
    """
    corrections = {}
    unique_values = df[column_name].unique()

    for typo in unique_values:
        match, score, _ = process.extractOne(typo, valid_list, scorer=fuzz.ratio)
        if score >= threshold:
            corrections[typo] = match

    # Create new column with corrected values
    df[new_column_name] = df[column_name].replace(corrections)
    return df
    