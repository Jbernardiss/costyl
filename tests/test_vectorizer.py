from costyl import vectorizer as vec
from costyl import misc

source_folder_path = "/Users/Jbernardis/costyl/tests/source_folder"
target_folder_path = "/Users/Jbernardis/costyl/tests/target_folder"

source_files_paths, source_files_labels = misc.get_authors_files_paths(source_folder_path)
target_files_paths, target_files_labels = misc.get_target_files_paths(target_folder_path)


vectorized_source_files_whole, vectorized_source_files_lines = vec.vectorize_source_files(source_files_paths)
vectorized_targets_files_whole, vectorized_source_files_lines = vec.vectorize_target_files(target_files_paths)

print(vectorized_source_files_whole)
print(vectorized_source_files_lines)
print(vectorized_targets_files_whole)
print(vectorized_targets_files_whole)

vectorized_source_files_whole = vec.vectorize_source_files(source_files_paths, type="whole")
vectorized_source_files_lines = vec.vectorize_source_files(source_files_paths, type="lines")

print()
print()
print(vectorized_source_files_whole)
print(vectorized_source_files_lines)
