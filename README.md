# Notification Bot - Cloud Integration

To make the scripts run in the cloud (AWS in this case), follow these steps:

1. **Create a file named `anime_list_i_watching.txt`** (or any name you prefer, but make sure to update the file path in the script accordingly). Fill it with the anime series you are watching.

2. **Create a file named `e_mail_credentials.json`**. It should have the following structure:
    ```json
    {
        "Email_Address": "bot_email_address",
        "Password": "gmail_app_credentials (It’s recommended to use Gmail)",
        "To": "your_email_address"
    }
    ```

3. **Create a file named `sensitive_infos.json`** to store additional information. The file should be structured like this:
    ```json
    {
        "User-Agent": "your user agent", 
        "website": "website", 
        "first_time": "True"
    }
    ```

4. **Create an AWS account** (or choose any cloud service provider of your choice).

5. **Create an EC2 instance** on AWS.

6. **Configure security settings** and other configurations for your instance.

7. **Upload the required files to your cloud instance**.

8. **Set up a crontab** to schedule the scripts to run at specified times. Runs scripts every day at 10am
    Example crontab:  
    ```
    0 10 * * * /usr/bin/python3 /path_to_your_script/scrapper.py && /usr/bin/python3 /path_to_your_script/e-mail_sender.py
    ```
    

