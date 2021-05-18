from termcolor import colored

import shutil
import os
import sys


ARCHIVATION = "1"
EXTRACTION = "2"
HELP = "3"
QUIT = "4"

argv = len(sys.argv)
if len(sys.argv) > 1:
    if sys.argv[1] == "-a":
        if sys.argv[2] == "--zip":
            path_to_new_zip_archive = sys.argv[3]
            archive_format = "zip"
            try:
                name_of_new_zip_archive = "/".join(path_to_new_zip_archive.split("/")[-1:])
                shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
                print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))

            except FileNotFoundError:
                print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
            except NotADirectoryError:
                print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

            print(colored('\n Program finished', 'blue'), '\n')
            sys.exit()
        elif sys.argv[2] == "--gztar":
            path_to_new_zip_archive = sys.argv[3]
            archive_format = "gztar"
            try:
                name_of_new_zip_archive = "/".join(path_to_new_zip_archive.split("/")[-1:])
                shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
                print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))

            except FileNotFoundError:
                print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
            except NotADirectoryError:
                print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

            print(colored('\n Program finished', 'blue'), '\n')
            sys.exit()
        elif sys.argv[2] == "--bztar":
            path_to_new_zip_archive = sys.argv[3]
            archive_format = "bztar"
            try:
                name_of_new_zip_archive = "/".join(path_to_new_zip_archive.split("/")[-1:])
                shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
                print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))

            except FileNotFoundError:
                print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
            except NotADirectoryError:
                print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

            print(colored('\n Program finished', 'blue'), '\n')
            sys.exit()
        elif sys.argv[2] == "--tar":
            path_to_new_zip_archive = sys.argv[3]
            archive_format = "tar"
            try:
                name_of_new_zip_archive = "/".join(path_to_new_zip_archive.split("/")[-1:])
                shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
                print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))

            except FileNotFoundError:
                print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
            except NotADirectoryError:
                print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

            print(colored('\n Program finished', 'blue'), '\n')
            sys.exit()
        elif sys.argv[2] == "--xztar":
            path_to_new_zip_archive = sys.argv[3]
            archive_format = "xztar"
            try:
                name_of_new_zip_archive = "/".join(path_to_new_zip_archive.split("/")[-1:])
                shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
                print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))

            except FileNotFoundError:
                print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
            except NotADirectoryError:
                print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

            print(colored('\n Program finished', 'blue'), '\n')
            sys.exit()
    if sys.argv[1] == "-e":
        try:
            zip_path = sys.argv[2]
            archive_format = ""
            extract_dir = ".".join(zip_path.split(".")[:-1])
            
            if ".".join(zip_path.split(".")[-2:]) == "tar.gz":
                archive_format = "gztar"
            elif ".".join(zip_path.split(".")[-1:]) == "zip":
                archive_format = "zip"
            elif ".".join(zip_path.split(".")[-2:]) == "tar.xz":
                archive_format = "xztar"
            elif ".".join(zip_path.split(".")[-2:]) == "tar.bz2":
                archive_format = "bztar"
            elif ".".join(zip_path.split(".")[-1:]) == "tar":
                archive_format = "tar"

            shutil.unpack_archive(zip_path, extract_dir, archive_format)

            print(colored('\n[!] >', 'white'), colored('Successfully.', 'blue'))
        except FileNotFoundError:
            print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
        except IsADirectoryError:
            print(colored('\n[!] >', 'white'), colored('It is a directory!', 'red'))
        finally:
            print(colored('\n Program finished.', 'blue'), '\n')

        sys.exit()
    if sys.argv[1] == "--help":
        print(f'''\nrun: {colored("python3 zipper.py -a --format folder", "green")},\n
        [ -a ] - archivation
        [ --format ] - (zip, gztar, xztar, bztar, tar)
        [ folder ] - a path to the archiving folder''')
        print(f'''\nrun: {colored("python3 zipper.py -e archive", 'green')}\n
        [ -e ] - extraction
        [ archive ] - a path to the archive (*.zip, *.tar., *.tar.gz, *.tar.xz, *.tar.bz2)\n''')
        print("Or if you run this utilite without arguments:")

        print(colored('\n\t[1] >', 'yellow'),
          'If you want to create archive, you have to to specify a path to your folder in the program.')
        print(colored('\t[2] >', 'yellow'),
            'If you want to extract zip-archive, you have to specify a path to your archive.')
        print(colored('\t[!] >', 'yellow'),
            'All archives extract to directory where the program is. If you archived folder or file so archive will be there, where the archive is.')

        sys.exit()

print(colored('Select action:', 'cyan'), '\n')
print('\t[1] -', colored('Create zip-archive...', 'green'))
print('\t[2] -', colored('Extract zip-archive...', 'yellow'))
print('\t[3] -', colored('Help...', 'magenta'))
print('\t[4] -', colored('Quit...', 'red'))

action = input(colored('>>> ', 'yellow'))

while action != ARCHIVATION and action != EXTRACTION and action != HELP and action != QUIT:
    print(colored('Select action:', 'cyan'), '\n')
    print('\t[1] -', colored('Create zip-archive...', 'green'))
    print('\t[2] -', colored('Extract zip-archive...', 'yellow'))
    print('\t[3] -', colored('Help...', 'magenta'))
    print('\t[4] -', colored('Quit...', 'red'))

    action = input(colored('>>> ', 'yellow'))

if action == ARCHIVATION:
    print(colored('\nEnter path to your folder for archivation:', 'cyan'))
    path_to_new_zip_archive = input(colored('>>> ', 'yellow'))

    try:
        print(colored('\nSelect a format of your archive:', 'cyan'))
        print(colored('\t[1] .zip', 'yellow'))
        print(colored('\t[2] .tar', 'yellow'))
        print(colored('\t[3] .tar.bz2', 'yellow'))
        print(colored('\t[4] .tar.gz', 'yellow'))
        print(colored('\t[5] .tar.xz', 'yellow'))

        archive_format = input(colored('>>> ', 'yellow'))
        if archive_format == "1":
            archive_format = "zip"
        elif archive_format == "2":
            archive_format = "tar"
        elif archive_format == "3":
            archive_format = "bztar"
        elif archive_format == "4":
            archive_format = "gztar"
        elif archive_format == "4":
            archive_format = "xztar"

        print(colored('\nWhat\'s the name for your achive ?:', 'cyan'))
        name_of_new_zip_archive = input(colored('>>> ', 'yellow'))

        shutil.make_archive(name_of_new_zip_archive, archive_format, path_to_new_zip_archive)
        print(colored('\n[!] >', 'white'), colored('Successfully', 'blue'))
    except FileNotFoundError:
        print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
    except NotADirectoryError:
        print(colored('\n[!] >', 'white'), colored('Not a directory!', 'red'))

    print(colored('\n Program finished', 'blue'), '\n')

elif action == EXTRACTION:
    try:
        print(colored('\nEnter a path to your archive:', 'cyan'))
        zip_path = input(colored('>>> ', 'yellow'))
        archive_format = ""
        extract_dir = ".".join(zip_path.split(".")[:-1])
        
        if ".".join(zip_path.split(".")[-2:]) == "tar.gz":
            archive_format = "gztar"
        elif ".".join(zip_path.split(".")[-1:]) == "zip":
            archive_format = "zip"
        elif ".".join(zip_path.split(".")[-2:]) == "tar.xz":
            archive_format = "xztar"
        elif ".".join(zip_path.split(".")[-2:]) == "tar.bz2":
            archive_format = "bztar"
        elif ".".join(zip_path.split(".")[-1:]) == "tar":
            archive_format = "tar"

        shutil.unpack_archive(zip_path, extract_dir, archive_format)
        # os.system(f"rm {zip_path}")

        print(colored('\n[!] >', 'white'), colored('Successfully.', 'blue'))
    except FileNotFoundError:
        print(colored('\n[!] >', 'white'), colored('File does not exist!', 'red'))
    except IsADirectoryError:
        print(colored('\n[!] >', 'white'), colored('It is a directory!', 'red'))
    finally:
        print(colored('\n Program finished.', 'blue'), '\n')

elif action == HELP:
        print("Conditions of use:")
        print(colored('\n\t[1] >', 'yellow'),
            'If you want to create a new archive, you have to specify a path to your folder in the program.')
        print(colored('\t[2] >', 'yellow'),
            'If you want to extract your zip-archive, you have to specify a path to your archive.')
        print(colored('\t[!] >', 'yellow'),
            'All archives extract to directory where the program is. If you archived folder or file, it will be shown where the archive is.')

        print("\nOr you can use the utilite like that:")
        print(f'''\n\trun: {colored("python3 zipper.py -a --format folder", "green")},\n
            [ -a ] - archivation
            [ --format ] - (zip, gztar, xztar, bztar, tar)
            [ folder ] - a path to the archiving folder''')
        print(f'''\n\trun: {colored("python3 zipper.py -e archive", 'green')}\n
            [ -e ] - extraction
            [ archive ] - a path to the archive (*.zip, *.tar., *.tar.gz, *.tar.xz, *.tar.bz2)\n''')

elif action == QUIT:
    print(colored('\n Program finished.', 'blue'), '\n')
    exit()

else:
    print(colored('\n[!] >', 'white'), colored('You selected wrong option!', 'red'))
    print(colored('\n Program finished.', 'blue'), '\n')

# Clenup the namespace
del shutil, os, sys

