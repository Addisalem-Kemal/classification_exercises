def prep_telco_data(df):

    df[df.total_charges.str.match(
        r'(^[0-9]+\.*[0-9]*$)') == False][['tenure', 'monthly_charges', 'total_charges']]
    df.total_charges.str.replace(r'(^ $)', '0.00')
    pd.to_numeric(df['total_charges'])
    df['Female'] = df['gender'].apply(lambda x: 1 if x == 'Female' else 0)
    cols_to_encode = ['partner', 'dependents', 'paperless_billing']
    df[cols_to_encode] = df[cols_to_encode].replace({'No': 0, 'Yes': 1})
    df['churn'] = df[['churn']].replace({'Yes': 1, 'No': 0})
    df['phone_service'] = df[['phone_service']].replace({'Yes': 1, 'No': 0})
    df['multiple_lines'] = df[['multiple_lines']].replace(
        {'Yes': 1, 'No phone service': 0, 'No': 0})
    df['online_security'] = df[['online_security']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    df['online_backup'] = df[['online_backup']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    df['device_protection'] = df[['device_protection']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    df['tech_support'] = df[['tech_support']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    df['streaming_tv'] = df[['streaming_tv']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    df['streaming_movies'] = df[['streaming_movies']].replace(
        {'Yes': 1, 'No internet service': 0, 'No': 0})
    train, validate, test = split_telco_data(df)

    return train, validate, test


def split_telco_data(df):
    '''
    This function performs split on telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2,
                                            random_state=42,
                                            stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3,
                                       random_state=42,
                                       stratify=train_validate.churn)
    return train, validate, test
