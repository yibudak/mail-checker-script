import requests
import json


def main():
    url = "http://95.179.185.209:3000"
    csv_file = open('emails.csv', 'r')
    checked_mails = open('checked_emails.csv', 'a+')
    invalid_mails = open('invalid.csv', 'a+')
    unknown_mails = open('unknown.csv', 'a+')
    emails = csv_file.readlines()
    count = 1
    for email in emails:
        payload = {
            "to_emails": [email.strip()]
        }
        response = requests.post(url, json=payload)
        parsed_data = json.loads(response.text)
        print(f'{count}. request sent to {parsed_data[0]["input"]} and result is: {parsed_data[0]["is_reachable"]}')
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
