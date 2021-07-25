import gspread, json, pandas as pd, numpy as np
from oauth2client.service_account import ServiceAccountCredentials

with open('config.json', 'r') as file:
    credentials = json.load(file)
    feeds = credentials['feeds']
    auth = credentials['auth']

while True:
    #input sheet to be validated
    main_sheets_input = str(input('Enter main sheet name (5XX): '))
    response_sheets_input = main_sheets_input +' (Responses)'

    #setting up scope and authorise credential
    scope = [feeds, auth]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
    gc = gspread.authorize(credentials)

    #fetching main google sheet
    main_sheets, response_sheets = gc.open(main_sheets_input).sheet1, gc.open(response_sheets_input).sheet1
    main_data, response_data = main_sheets.get_all_values(), response_sheets.get_all_values()

    #Arrange and clean data
    main_df, response_df = pd.DataFrame(main_data).drop([0, 1]).replace(r'^\s*$', np.nan, regex=True).dropna().reset_index(drop=True), pd.DataFrame(response_data).drop(0).reset_index(drop=True)
    main_df.columns, response_df.columns = ['No', 'Name', 'Image Number'], ['Timestamp', 'Agreement', 'Name', 'Gender', 'Position', 'Image Number', 'Phone Number', 'Home Number', 'Email', 'Adress']
    main_image_number, response_image_number = main_df['Image Number'], response_df['Image Number']

    #validating data
    validation = main_image_number == response_image_number
    for index, count in enumerate(validation):
        print(index+1, count)

    #continue loop
    continue_break = str(input('Continue? (y/n): '))

    if (continue_break == 'y'):
        continue
    elif (continue_break == 'n'):
        break
    else:
        print('Invalid Input')
        break