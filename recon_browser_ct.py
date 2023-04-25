import os
import sqlite3
import sys
from getpass import getuser

def get_chrome_cookies_db_path():
    if sys.platform.startswith('win'):
        path = f'C:\\Users\\{getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'
    elif sys.platform.startswith('linux'):
        path = f'/home/{getuser()}/.config/google-chrome/Default/Cookies'
    elif sys.platform.startswith('darwin'):
        path = f'/Users/{getuser()}/Library/Application Support/Google/Chrome/Default/Cookies'
    else:
        raise Exception('Unsupported OS.')

    if not os.path.exists(path):
        raise Exception('Cookies database not found. Make sure Chrome is installed.')

    return path

def get_tokens_from_db(db_path, token_cookie_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT host_key, name, value, encrypted_value FROM cookies WHERE name = ?', (token_cookie_name,))
    tokens = cursor.fetchall()

    cursor.close()
    conn.close()

    return tokens

def main():
    try:
        token_cookie_name = "auth_token"  # Replace this with the actual cookie name for the token
        db_path = get_chrome_cookies_db_path()
        tokens = get_tokens_from_db(db_path, token_cookie_name)

        for token in tokens:
            host_key, name, value, encrypted_value = token
            print(f'{host_key}: {name} = {value}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
