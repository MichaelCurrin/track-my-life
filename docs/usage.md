# Usage

_Back to [Readme](/README.md)_


## Run the app

Start the CherryPy server in order to serve HTML in the browser, allow REST API requests and interface with the databae.


### Embedded application

Steps for running on PythonAnywhere.com

TBC


### Local application


1. Tail your log files

    ```
    $ cd app/var/log/trackMyLife
    $ tail -F *.log
    ```

2. Start the app

    ```bash
    $ source virtualenv/bin/activate
    $ ./app/trackMyLife.py
    ```

Run with the `--drop` flag to delete all tables and their data, then start afresh.

3. Open in the browser
  
  - go to http://localhost:9000
