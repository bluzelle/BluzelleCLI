from PyInstaller.utils.hooks import collect_submodules, collect_data_files
hiddenimports = collect_submodules('faker')
datas = collect_data_files('faker.providers', include_py_files=True)

#command to create binary distribution
#pyinstaller --clean --distpath dist --name console --additional-hooks-dir pyinstaller/ --onefile console.py