
import costyl.misc as misc

if __name__ == "__main__":

    source_folder_path = "/Users/Jbernardis/costyl/tests/source_folder"
    target_folder_path = "/Users/Jbernardis/costyl/tests/target_folder"

    print(misc.get_authors_files_paths(source_folder_path))

    print(misc.get_target_files_paths(target_folder_path))
