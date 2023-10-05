import subprocess


def extract_wifi_passwords():
    data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')    
    profiles = [row.split(':')[1].strip() for row in data if 'Все профили пользователей' in row]
    hostname = subprocess.check_output('hostname').decode('cp866')
    #  print(profiles)
    with open(file='wifi_passwords.txt', mode='a', encoding='cp866') as f:
        f.write(f'Hostname:{hostname}')
        f.write('----------------------------------------------\n')
    #  print(f'Имя сети\tПароль\n')
    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key = clear').decode('cp866').split('\n')
        try:
            password = [row.split(':')[1].strip() for row in profile_info if 'Содержимое ключа' in row]
        except IndexError:
            password = None
        #  print(f'{profile}\t{password}')
        with open(file='wifi_passwords.txt', mode = 'a', encoding='cp866') as f:
            f.write(f'{profile}\t\t{password[0]}\n')


def main():
    extract_wifi_passwords()
    

if __name__ == '__main__':
    main()
