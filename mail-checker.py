import requests
import json
import os
import fnmatch


# 29.09.2020
# Author: Yiğit BUDAK
# github.com/yibudak

def main():
    csv_list = os.listdir('.')
    pattern = "*.csv"
    count = 1
    for csv in csv_list:
        if fnmatch.fnmatch(csv, pattern):  # gets all csv files in current dir
            url = "http://localhost:3000"  # your backend ip address
            csv_file = open(csv, 'r')  # email list
            checked_mails = open(csv.split('.csv')[0] + '_checked.csv',
                                 'a+')
            invalid_mails = open(csv.split('.csv')[0] + '_invalid.csv',
                                 'a+')
            unknown_mails = open(csv.split('.csv')[0] + '_unknown.csv',
                                 'a+')
            emails = csv_file.readlines()
            for email in emails:
                payload = {
                    "to_emails": [email.strip()]
                }
                response = requests.post(url, json=payload)
                parsed_data = json.loads(response.text)
                print(f'[{count}][{csv.split(".csv")[0]}] {parsed_data[0]["input"]}\
                                         {parsed_data[0]["is_reachable"]}')
                count += 1
                if parsed_data[0]["is_reachable"] == "invalid":
                    invalid_mails.writelines(email)

                elif parsed_data[0]["is_reachable"] == "unknown":
                    unknown_mails.writelines(email)

                else:
                    checked_mails.writelines(email)

            checked_mails.close()
            invalid_mails.close()
            unknown_mails.close()
    print("EOF")


if __name__ == "__main__":
    main()
