def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)
    except IsADirectoryError as err:
        print("Found config.txt but it is a directory, couldn't read it", err)
    except (BlockingIOError, TimeoutError) as err:
        print("Filesystem under heavy load, can't complete reading configuration file", err)

if __name__ == '__main__':
    main()