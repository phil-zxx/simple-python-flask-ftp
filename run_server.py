from flask import Flask, request, send_from_directory

ROUTE_NAME     = 'file'
SERVER_CODE    = 'dkljdfs8923dfa1'
FOLDER_TO_FILE = 'C:\\Users\\some_user\\Downloads'
FILE_NAME      = 'some_file_name.txt'


def main():
    app = Flask(__name__)

    @app.route(f'/{ROUTE_NAME}')
    def route_function():
        code = request.args.get('code')
        if code != SERVER_CODE:
            return ''

        return send_from_directory(FOLDER_TO_FILE, FILE_NAME)

    app.run(debug=False, host='0.0.0.0', port=5023)


if __name__ == '__main__':
    main()
