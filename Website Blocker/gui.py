import os
import re
import tkinter as tk
import tkinter.messagebox as messagebox

host_path = r"C:\Windows\System32\drivers\etc\hosts"
block_list = []


def validate_url(url):
    pattern = r'^(?:https?://)?(?:www\.)?[\w.-]+\.\w+$'
    return bool(re.match(pattern, url))


# function to add website to blocklist
def add_to_block_list():
    web_site_name = entry_1.get()

    if len(web_site_name) > 1:
        if validate_url(web_site_name):
            try:
                if os.path.exists(host_path):
                    found = False
                    with open(host_path, 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if web_site_name in line:
                                found = True
                                break

                    if not found:
                        with open(host_path, 'a') as file:
                            file.write(f'127.0.0.1 {web_site_name}\n')
                        diplay_output_label.config(text=f'Successfully added to the BlockList\n{web_site_name} ')
                    else:
                        messagebox.showinfo('Info', f"Website {web_site_name} already exists in the block list!")
                else:
                    diplay_output_label.config(text='ERROR host file does not exist')
            except Exception as e:
                messagebox.showerror('ERROR', f'ERROR {e}')
        else:
            messagebox.showerror('ERROR', f'Invalid URL: {web_site_name}')
    else:
        messagebox.showerror('ERROR', f'Please enter URL')


# function to remove website
def remove_from_block_list():
    website_name = entry_1.get()
    if len(website_name) > 1:
        if validate_url(website_name):
            try:
                if os.path.exists(host_path):
                    with open(host_path, 'r+') as file:
                        lines = file.readlines()
                        file.seek(0)
                        print(len(lines))
                        if len(lines) > 0:
                            for line in lines:
                                if website_name not in line:
                                    file.write(line)
                                    diplay_output_label.config(text=f'Website Removed: {website_name}')
                                else:
                                    pass
                        else:
                            diplay_output_label.config(text="Block List is empty !!")
                        file.truncate()

                else:
                    pass
            except Exception as e:
                messagebox.showerror('ERROR', f'ERROR host file {e}')
        else:
            messagebox.showerror('ERROR', f'Invalid URL: {website_name}')
    else:
        messagebox.showerror('ERROR', f'Please enter URL')


def check_website_block():
    try:
        if os.path.exists(host_path):
            with open(host_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith('127.0.0.1'):
                        part = line.split()
                        if len(part) > 1:
                            block_list.append(part[1])

                        else:
                            pass
                    else:
                        diplay_output_label.config(text="Currently No website blocked!")
        else:
            pass
        if block_list:
            diplay_output_label.config(text='\n'.join(block_list))
        if len(block_list) == 0:
            diplay_output_label.config(text='No website blocked!')

    except Exception as e:
        messagebox.showerror('ERROR', f'ERROR host file {e}')


root = tk.Tk()
root.title("Website Blocker")
root.geometry("400x150+450+100")
root.resizable(False, False)

label_1 = tk.Label(relief='flat', text="Enter website URL", font='Arial 10 bold')
label_1.place(anchor='w', x=10, y=10)
entry_1 = tk.Entry(root, width=35, font='Arial 11 bold')
entry_1.place(anchor='w', x=10, y=30)
# buttons
add_button = tk.Button(root, text="ADD", font='Arial 10 bold', width=8, height=1, command=add_to_block_list)
add_button.place(x=300, y=15)

remove_button = tk.Button(root, text="Remove", font='Arial 10 bold', width=8, command=remove_from_block_list)
remove_button.place(x=300, y=55)

check_button = tk.Button(root, text="Check", font='Arial 10 bold', width=8, command=check_website_block)
check_button.place(x=300, y=95)

# display output
diplay_output_label = tk.Label(relief='groove', borderwidth=2, height=5, width=31, font='Arial 11 bold')
diplay_output_label.place(x=10, y=50)

root.mainloop()
