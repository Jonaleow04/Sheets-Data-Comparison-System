# Sheets Data Comparison System
## The Whats
- This is a Python program that fetches two Google Sheets and loads it into Python to compare and validate. 
  - The Google Sheets is fetched using Google Sheet API and gspread module
  - Pandas DataFrame is used to load the Google Sheets into Python
  - Numpy is used to manipulate the arrays

## The Whys
- I have two separate sets of Google Sheets (one is the main spreadsheet and another is from google forms response) I need to compare the datas of to make sure it is correct.
- Something clicked in me and I told myself 'Surely I can write a program to automate this right?'

## The Hows
![flowchart](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4cc354ad-13a1-4beb-a7fe-b8e64f053c1b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210725T131942Z&X-Amz-Expires=86400&X-Amz-Signature=7526798124587ff0891caa309bcada5fc893e09eb1fc917844d0f5504caeaa16&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D"Untitled.png")
- Here's a simple flowchart that I created for the sake of helping me structure my program and understand it better
## Setup
- Install Python 3.8 or above
- Install the following Python modules: gspread, pandas, numpy
``` 
python -m pip install gspread
python -m pip install pandas
python -m pip install numpy
python -m pip install oauth2client
python -m pip install PyOpenSSL
```
- Create a new project in [Google Cloud Console](https://console.cloud.google.com) 
- [You may check out this article if you are new in working with Google Cloud Console and its APIs](https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf)
- Enable Google Drive API and Google Sheet API
- Download your credential key in JSON format
- Inside the JSON file, search for your client email and copy it
- Share the google sheets you are fetching to your client email
  ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0b268526-3cec-494b-a45e-e430b91bc343/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210725T131939Z&X-Amz-Expires=86400&X-Amz-Signature=065dad52d20d9fe9a4f44aa68f7d66d4a3b15d8cd3ae3d665268ac72f3148df7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D"Untitled.png")

## Usage
- Clone the repository
- Line 11 is to let the user input the name of the google sheets
- At line 12, since the other google sheet I'm comparing with is of the same name as the main google sheet but with '(Responses)' at the end, so I concatenate the string to the google sheets name that the user input at line 11
``` python
main_sheets_input = str(input('Enter main sheet name (5XX): '))
response_sheets_input = main_sheets_input +' (Responses)'
```
- At line 16, replace the credential json file name with your own
``` python
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
```
- From line 24 to line 26 is where it loads the google sheets into a pandas DataFrame, arrange the datas and get the datas that needs to be validated. You will need to change it according to your own needs
``` python
main_df, response_df = pd.DataFrame(main_data).drop([0, 1]).replace(r'^\s*$', np.nan, regex=True).dropna().reset_index(drop=True), pd.DataFrame(response_data).drop(0).reset_index(drop=True)
main_df.columns, response_df.columns = ['No', 'Name', 'Image Number'], ['Timestamp', 'Agreement', 'Name', 'Gender', 'Position', 'Image Number', 'Phone Number', 'Home Number', 'Email', 'Adress']
main_image_number, response_image_number = main_df['Image Number'], response_df['Image Number']
```
- From line 29 to 31 is the validation part. It will return a boolean value on whether if the data is correct
``` python
validation = main_image_number == response_image_number
    for index, count in enumerate(validation):
        print(index+1, count)
```
- Run the program in an IDE or in command propmt by typing:
``` 
python main.py
```

## References
- https://developers.google.com/sheets/api/quickstart/python
- https://docs.gspread.org/en/latest/
- https://pandas.pydata.org/docs/
- https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf
