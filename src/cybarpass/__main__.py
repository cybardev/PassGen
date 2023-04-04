#!/usr/bin/env python3

import argparse
import cybarpass

if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser(
        description="Generate a secure passphrase",
        epilog="Launch without arguments for GUI mode\n"
        + "or use -g | --gui with /path/to/word/list to preload the file\n"
        + "\nPS: -n | --len has no effect in GUI mode",
        allow_abbrev=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "filename",
        help="Path to dictionary file",
        metavar="WORD_LIST",
        type=str,
        nargs="?",
        default=None,
    )
    parser.add_argument(
        "-n",
        "--len",
        help="Minimum length of passphrase",
        dest="char_limit",
        metavar="NUM",
        type=int,
        default=16,
    )
    parser.add_argument(
        "-g",
        "--gui",
        help="Run the program in GUI mode",
        action="store_true",
        dest="gui_mode",
    )
    args = parser.parse_args()

    # main program logic
    cybarpass.run(args.filename, args.char_limit, args.gui_mode)
