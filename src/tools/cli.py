# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 18/05/2019 23:45

# https://click.palletsprojects.com/en/7.x/

import click


@click.command()
def cmd_without_args():
    print("hello")



@click.command()
@click.argument('name')
@click.argument('greeting')
# def main(name):
# @click.option('--greeting', '-g')
def main(name, greeting):
    click.echo("{}, {}".format(greeting, name))
    # click.echo("{}".format( name))

if __name__ == "__main__":
    main()