# Usage

_Back to [Readme](/README.md)_


## Run the app

Start the CherryPy server, to serve HTML and allow REST API requests

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
