#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-FILESTORE > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-FILESTORE/blob/master/LICENSE >
#
# All rights reserved.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ERASTORE'


if __name__ == "__main__":
    app.run()

