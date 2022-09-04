import argparse
import os
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="An postmodern news fetcher like teletext for the postmodern chads which are living in terminal."
    )
    parser.add_argument("-d", "--delimiter", help="Delimiter", default="\t")
    parser.add_argument("-c", "--column", help="Column", default=0)
    parser.add_argument("-s", "--separator", help="Separator", default=" ")
    parser.add_argument("-e", "--encoding", help="Encoding", default="utf-8")
    # test x
    parser.add_argument("-t", "--test", help="Test", default=False)

    args = parser.parse_args()

    if args.test:
        if args.test == "parser":
            from tests import test_parser
        if args.test == "comment":
            from tests import test_comment
        if args.test == "post":
            from tests import test_post
        if args.test == "story":
            from tests import test_story
        if args.test == "view":
            from tests import test_view
