block_web_site_list = ['www.google.com', 'www.facebook.com']

host_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts"


def add_to_block_list():
    with open(host_path, 'a') as file:
        if host_path:
            for website in block_web_site_list:
                file.write(f'127.0.0.1 {website}\n')

                print('Website Added', website)
            else:
                print('No website added')


def remove_from_block_list(website):
    if host_path:
        unblock_site = entry_1.get()
        with open(host_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if unblock_site not in line:
                    file.write(line)

            file.truncate()
        print('Website unblocked', unblock_site)
    else:
        print('Error: No website added')


# blocked website list

def check_website_block(website):
    blocked_List = []
    if host_path:
        with open(host_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('127.0.0.1'):
                    part = line.split()
                    if len(part) > 1:
                        blocked_List.append(part[1])
                    else:
                        pass
                else:
                    print('Error: No website currently blocked')
    else:
        print('Error: No')
