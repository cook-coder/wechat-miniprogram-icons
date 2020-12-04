import os
import shutil
import json
from pathlib import Path
class Export:
    __target_dir = "dist"
    __project_name = ''
    def __init__(self, project_name: str):
        """
        Create dist if not exists
        """
        self.__project_name = project_name
        self.__target_dir = os.path.join(self.__target_dir, project_name)
        dir = Path(self.__target_dir)
        if dir.exists():
            shutil.rmtree(self.__target_dir)
        os.makedirs(self.__target_dir)

    def __clear_export_dir(self):
        """Clear dist directory."""
        pass

    def export(self, data:dict):
        """Export components to dist directory."""
        self.__clear_export_dir()
        self.__copy_and_rename_files()
        self.__write_wxml()
        self.__write_wxss()
        self.__write_icons_data(data)

    def __copy_and_rename_files(self):
        shutil.copyfile('icons-component-template/base64.js', os.path.join(self.__target_dir, "base64.js"))
        shutil.copyfile('icons-component-template/template-icons.js', os.path.join(self.__target_dir, self.__project_name + ".js"))
        shutil.copyfile('icons-component-template/template-icons.json', os.path.join(self.__target_dir, self.__project_name + ".json"))

    def __write_wxss(self):
        wxss_file = open('icons-component-template/template-icons.wxss')
        lines = wxss_file.readlines()
        wxss_file.close()
        lines[0] = lines[0].replace("%%project_name%%", self.__project_name) 
        target_file = open(os.path.join(self.__target_dir, self.__project_name + ".wxss"), 'w')
        target_file.writelines(lines)
        target_file.close()

    def __write_wxml(self):
        wxml_file = open('icons-component-template/template-icons.wxml')
        lines = wxml_file.readlines()
        wxml_file.close()
        size = len(lines)
        lines[size-1] = lines[size-1].replace("%%project_name%%", self.__project_name) 
        target_file = open(os.path.join(self.__target_dir, self.__project_name + ".wxml"), 'w')
        target_file.writelines(lines)
        target_file.close()

    def __write_icons_data(self, data: dict):
        data_file = open(os.path.join(self.__target_dir, 'icons-data.js'), 'w')
        data_str = "export default " + json.dumps(data)
        data_file.write(data_str)
        data_file.close()