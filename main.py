#!/bin/env python
# -*- coding: utf-8 -*-
from io import BytesIO
import multiprocessing
import click
import zipfile


THREADS = 8

def crack_zip(wordlist, zip_file, index):
    with open(zip_file, mode="rb",) as file_obj:
        buf = BytesIO(file_obj.read())
        with zipfile.ZipFile(buf, 'r') as zip_ref:
            info = zip_ref.infolist()
            for word in wordlist:
                try:
                    x = zip_ref.read(info[0], pwd=word.strip())
                except Exception as e:
                    continue
                else:
                    print("[+] Password found:", word.decode().strip())
                    exit(0)


def multiprocessing_func(x):
    print("work init")
    for i in range(200000000):
        y = x*x


def chunker_list(seq, size):
    return (seq[i::size] for i in range(size))


@click.command()
@click.option('-d', type=click.Path(), help='wordlist file.')
@click.option('-f', type=click.Path(), help='zip file')
def hello(d, f):
    wordlist = d
    n_words = len(list(open(wordlist, "rb")))
    zip_file = f

    with open(wordlist, "rb") as wordlist:
        x = list(chunker_list(list(wordlist), THREADS))
        count = 1
        print(f'palabras totales: {n_words}')
        for wordli in x:
            p = multiprocessing.Process(
                target=crack_zip, args=(wordli, zip_file, count))
            count += 1
            processes.append(p)
            p.start()


if __name__ == '__main__':
    processes = []
    hello()

    for process in processes:
        process.join()

    print("[!] Password not found, try other wordlist.")
