#trying to make dirbuster but for python I guesss?
import os
import click
import requests
#from http import HTTPStatus

#basic use: python3 busssted.py (flags) http://www.url.com/

@click.command()
@click.option('-f', '--file', default="small.txt", help="Filepath of wordlist you want to use")
@click.option('-r', '--recursive',  is_flag=True, help="Will have program search through directories recursively")
@click.option('-w', '--write', default="busssted.txt", help = "Saves output under a specified filename")
@click.option('-v', '--verbose', is_flag=True, help = "Will output the response code of every url it checks, not just ones with a 200")
#@click.argument('args')

#imma be honest, I can't figure out why it's not parsing the inputs or recogninzing defined variables so i'm just gonna leave this here for now

#hey, does anyone know if it's possible to thread recursive processes so it can finish the first layer check without getting hung up in the middle?
def urlCheck(url, file):
    with open(file) as keywords:
        for keyword in enumerate(keywords):
            test = url + keyword + "/"
            if (verbose): #verbose prints everything
                #write full URL to file + requests.get(test).status_code
                print(test + " Code: " + requests.get(test).status_code)
                if (recursive and (requests.get(test).status_code == 200)): #if you want it to be recursive and it gets a 200, go deeper
                    urlCheck(test, file)
            elif (requests.get(test).status_code == 200): #if it ain't verbose, just return the "200" responses
                #write full URL to file + requests.get(test).status_code
                print(test + " Code: " + requests.get(test).status_code)
                if (recursive): #if you wanted it to be rescusive, go deeper
                    urlCheck(test, file)

def main(url, file):
    urlCheck(url, file)
    #maybe something else


if __name__ == '__main__':
    main(url, file)
