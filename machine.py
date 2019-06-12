def loop():
    print('press CTRL+C or CTLR+D to exit')

    while True:
        try:
            data = input('MACHINE> ')
            # do_it(data)
        except (KeyboardInterrupt, EOFError):
            print('goodbye!')
            break


if __name__ == "__main__":
    loop()

