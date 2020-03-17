import os
from datetime import datetime


ROOT = os.environ.get('DATA_DIR', 'data/feeds')

def mkfilename(vendor_name, vendor_id, date=None):
    if date is None:
        date = datetime.now()

    directory = [ROOT, vendor_name,
        str(date.year), str(date.month), str(date.day)
    ]

    directory = "/".join(directory)
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

    return directory + "/" + str(vendor_id)
