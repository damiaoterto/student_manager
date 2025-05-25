from app import Application

def main():
    app = Application()
    try:
        app.run()
    except KeyboardInterrupt:
        app.exit()

if __name__ == '__main__':
    main()