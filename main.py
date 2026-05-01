import argparse
from todo import add_task, list_tasks, remove_task, mark_done

parser = argparse.ArgumentParser(description="Todo CLI App")
subparsers = parser.add_subparsers(dest="command")

# add
add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")

# list
subparsers.add_parser("list")

# remove
remove_parser = subparsers.add_parser("remove")
remove_parser.add_argument("index", type=int)

# done
done_parser = subparsers.add_parser("done")
done_parser.add_argument("index", type=int)

args = parser.parse_args()

if args.command == "add":
    add_task(args.title)

elif args.command == "list":
    list_tasks()

elif args.command == "remove":
    remove_task(args.index)

elif args.command == "done":
    mark_done(args.index)

else:
    parser.print_help()
    