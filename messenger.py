# -*- coding: utf-8 -*-
import click
import pybullet, contacts

term_width, term_height = click.get_terminal_size()
waiting = True


def setup():
    click.clear()
    click.echo(click.style('▔'*term_width, fg='green'))

def add_message(author, text):
    click.echo(click.style(author, fg='red') + "\t" + click.style(text, fg='blue'))

def loop_get_response():
    raw_send = click.prompt('>\t', prompt_suffix='')
    if raw_send is 'x':
        exit()
    to = raw_send.split()[0]
    if not contacts.get_number(to):
        click.echo(click.style("Not in your contacts!", bg='red', fg='black'))
        return
    else:
        pybullet.push_sms(contacts.get_number(to), ' '.join(raw_send.split()[1:]))

def exit():
    click.abort()
    click.close()
    click.exit(0)

