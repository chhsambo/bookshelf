import os
from datetime import datetime

cur_dir = os.getcwd()
print(cur_dir)

path = os.path.join(cur_dir, "assets")


def get_folders(parent_dir):
    items = os.listdir(parent_dir)
    # print(items)

    for item in items:
        item_path = os.path.join(parent_dir, item)
        if os.path.isdir(item_path):
            # yield item_path
            yield os.path.basename(item_path)


def get_files(parent_dir):
    items = os.listdir(parent_dir)
    # print(items)

    for item in items:
        item_path = os.path.join(parent_dir, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            last_access = os.path.getatime(item_path)

            yield {
                "basename": os.path.basename(item_path),
                "last_access": datetime.utcfromtimestamp(last_access).strftime(
                    "%Y-%m-%d %H:%M %p"
                ),
                "size": size,
                "size_mb": "{:.2f} MB".format(size / 1024 / 1024),
            }
            # yield item_path


# def walk_dir(parent_dir):
#     items = os.listdir(parent_dir)
#     # pprint(items)

#     for child in items:
#         child_path = os.path.join(parent_dir, child)
#         if os.path.isfile(child_path):
#             last_access = os.path.getatime(child_path)
#             size = os.path.getsize(child_path)
#             print(f"File: {child_path}")
#             print(f"\tLast access: {last_access}")
#             print(f"\tSize: {size}")
#         else:
#             print(child_path)
#             walk_dir(child_path)


# if __name__ == "__main__":
#     folders = get_folders(path)
#     print(folders)
#     for folder in folders:
#         folder_name = os.path.basename(folder)
#         print(folder_name)

#     # walk_dir(cur_dir)
