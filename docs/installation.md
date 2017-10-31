# Installation

_Back to [Readme](/README.md)_


## Setup environment

1. Clone the repo

    ```bash
    $ git clone git@github.com:MichaelCurrin/trackMyLife.git
    $ cd trackMyLife
    ```

2. Create virtual enviroment

    - either create virtual environment in the repo

        ```bash
        $ virtualenv virtualenv
        ```

    - or create it in a central location with other environments and symlink to it
    
        ```bash
        $ mkdir ~/.local/virtualenvs
        $ virtualenv ~/.local/virtualenvs/trackMyLife
        $ ln -s ~/.local/virtualenvs/trackMyLife virtualenv
        ```

3. Install local packages

    ```bash
    $ source virtualenv/bin/activate
    $ pip install -r requirements.txt
    ```

4. Install global packages
    
    - SQLite must be installed at the global level, preferably with root access. It is not a python package. This repo was developed using version `3.16.2`.
        ```
        $ sudo apt-get install sqlite3
        ```


## Configure

TBC
