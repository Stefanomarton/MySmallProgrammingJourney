import subprocess

programs = ['btop',
            'htop'
           ]  # List of programs to install

for program in programs:
    command = f"sudo pacman -S --noconfirm --needed {program}"  # Pacman command to install the program
    subprocess.run(command.split(), check=True)  # Run the command and check for errors

aurprograms = ['neovim',
            'htop'
           ]  # List of programs to install

for aurprogram in aurprograms:
    command = f"yay -S --noconfirm --needed {aurprogram}"  # Pacman command to install the program
    subprocess.run(command.split(), check=True)  # Run the command and check for errors

# with open('/home/stefanom/prova.cfg', 'r') as f:
#     lines = f.readlines()

# with open('/home/stefanom/prova.cfg', 'w') as f:
#     for line in lines:
#         if 'GRUB_CMDLINE_LINUX_DEFAULT' in line:
#             line = line.replace('"', '"vfio"')
#         f.write(line)
