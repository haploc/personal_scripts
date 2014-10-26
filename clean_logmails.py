#!/usr/bin/env python3
# Clean up script for certain old mail folders

import mailbox
import os
import time

# Maildir main folder
mailpath = os.environ.get('HOME') + '/Mail/'

# List of tuples with (Maildir subfolder, number of days to keep)
cleanup_paths = [
    ('0_MAYBE_SPAM', 3),
    ('0_SPAM', 3),
    ('Trash', 3),
    ('Internet.CR-Net_Log', 7),
    ('CR-Net.Promotions', 31),
]

def main():
    now = time.time()
    print("Cleaning up old mails...")
    maildir = mailbox.Maildir(mailpath)
    for (cl_path, keep_days) in cleanup_paths:
        print("Processing {} discarding older than {} days".format(cl_path, keep_days))
        keep_time = now - keep_days * 86400
        cleanfolder = maildir.get_folder(cl_path)
        for filename, msg in cleanfolder.items():
            # If epoch timestamp of the msg is smaller than keep_time epoch timestamp
            if msg.get_date() < keep_time:
                print("Filename: {}\nSubject: {}\nDate: {}\n----------------------------------".format(filename, msg['subject'], msg['date']))
                cleanfolder.remove(filename)

    maildir.close()

if __name__ == '__main__':
    main()
