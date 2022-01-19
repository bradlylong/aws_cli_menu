#!/usr/bin/env python3

import os
import aws_command
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

menu_options = {
    1: 'ec2 info',
    2: 'subnet cidrs',
    3: 's3 buckets',
    4: 'cloud watch alarms',
    5: 'exit',
}

def print_menu():
    for key in menu_options.keys():
        console.print(key, '--', menu_options[key], style='black on green')

def ec2_info():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Region", style="bold blue")
    table.add_column("Instance ID", style="bold blue")
    table.add_column("Name", style="bold blue")
    table.add_column("Private IP", style="bold blue")
    table.add_column("Public IP", style="bold blue")
    table.add_column("State", style="bold blue")

    os.system(aws_command.ec2_info)

    with open('output.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split('\t')
            region = split_line[0]
            instance_id = split_line[1]
            name = split_line[2]
            private_ip = split_line[3]
            public_ip = split_line[4]
            state = split_line[5]
            table.add_row(
                region,
                instance_id,
                name,
                private_ip,
                public_ip,
                state, 
            )
    return console.print(table)

def subnet_info():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("CIDR", style="bold blue")
    table.add_column("Name", style="bold blue")

    os.system(aws_command.subnet_cidrs)

    with open('output.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split('\t')
            cidr = split_line[0]
            name = split_line[1]
            table.add_row(
                cidr,
                name, 
            )

    return console.print(table)

def s3_buckets():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="bold blue")

    os.system(aws_command.s3_buckets)

    with open('output.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            table.add_row(line.strip())

    return console.print(table)

def cloudwatch_alarms():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name Space", style="bold blue")
    table.add_column("Name", style="bold blue")
    table.add_column("Description", style="bold blue")
    table.add_column("State", style="bold blue")

    os.system(aws_command.cloudwatch_alarms)

    with open('output.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split('\t')
            name_space = split_line[0]
            name = split_line[1]
            description = split_line[2]
            state = split_line[3]

            table.add_row(
                name_space,
                name,
                description,
                state,
            )

    return console.print(table)

def file_clean_up():
    return os.remove('output.txt')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''

        try:
            option = int(input('Select an option from the menu: '))
        except:
            console.print('Error: Must select a # from the menu.', style='bold red')

        if option == 1:
            ec2_info()
            file_clean_up()
        elif option == 2:
            subnet_info()
            file_clean_up()
        elif option == 3:
            s3_buckets()
            file_clean_up()
        elif option == 4:
            cloudwatch_alarms()
            file_clean_up()
        elif option == 5:
            console.print('Exit', style='bold blue')
            exit()
        else:
            console.print('Invalid option.', style='bold red')