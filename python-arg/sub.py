def add_subparser(subparsers):
    sub1 = subparsers.add_parser("sub1")
    sub1.add_argument("--env")
    subact = sub1.add_subparsers()
    sub2 = subact.add_parser("sub2")
    sub2.add_argument("--name")
