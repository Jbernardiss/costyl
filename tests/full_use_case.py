
import costyl as cstyl

costyl = cstyl.Costyl()

costyl.import_authors_files("/Users/Jbernardis/costyl/tests/source_folder")
costyl.import_target_files("/Users/Jbernardis/costyl/tests/target_folder")

costyl.generate_model()
print(costyl.predict_authors())
