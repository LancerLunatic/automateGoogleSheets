# automateGoogleSheets
Python script 
This script uses the openai Python module to paraphrase each paragraph using the ChatGPT API, and the google-auth, google-api-python-client, and google.oauth2 Python modules to interact with the Google Docs API.
When you run the script, it will create a new Google Docs document with the paraphrased content, including page numbers and the original page numbers. The script assumes that the Google Docs document is publicly accessible and you have the appropriate API credentials to access it.

google calc score sheets automated openai python script readme
Here's how to use this script:
Open the Google Sheet that you want to use for this task.
Click on the "Tools" menu and select "Script editor".
In the script editor, copy and paste the above code.
Replace 'SHEET_NAME' with the name of the sheet you want to use in the calculateScores() function.
Replace the calculateScoreWithChatGPT(url) function with your own implementation of the ChatGPT API to calculate the score for a given URL.
Save the script by clicking on the "Save" button.
Close the script editor.
Go back to the Google Sheet and click on the "Tools" menu and select "Script editor" again.
Run the calculateScores() function by clicking on the "Run" button or by selecting "calculateScores" from the "Select function" dropdown and clicking on the "Run" button.
Wait for the script to finish running. The scores will be outputted in column B of your sheet.
Note: Make sure that your Google Sheet has permission to access the ChatGPT API.
