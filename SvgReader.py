import os
from typing import List
import re

"""
define IconsData to store each icon's svg content.

example:
{
    "home": {
        "filled": `<svg content>`,
        "outline": `<svg content>`,
        "sharp": `<svg content>`
    },
    "back": {
        ...
    }
}

"""

class SvgReader:
    __icons_folder: str
    __projects_name: List[str]
    __classified_data: dict 

    def __init__(self):
        """define icons folder"""
        self.__icons_folder = 'svg-icons'
        self.__classified_data = {}

    def get_svg_data(self):
        self.__classify_icons_data()
        return self.__classified_data

    def __get_projects(self):
        """Get projects from the svg-icons directory"""
        dirs = os.listdir(self.__icons_folder)
        self.__remove_hidden_dirs(dirs)
        self.__projects_name = dirs

    def __remove_hidden_dirs(self, dirs: List[str]):
        """Remove hidden directories"""
        for item in dirs:
            if item.startswith('.'):
                dirs.remove(item)

    def __classify_icons_data(self):
        self.__get_projects()
        self.__init_classified_data()
        for project_name in self.__projects_name:
            types = self.__get_icon_types(project_name)
            for type in types:
                icons_file_path = self.__list_svg_files_path(project_name, type)
                type_name = self.__fix_type_name_for_data_construction(type)
                for icon_file_path in icons_file_path:
                    svg_content = self.__read_svg_file(icon_file_path)
                    icon_name = self.__get_icon_name(icon_file_path)
                    self.__classified_data.update
                    self.__classified_data[project_name].update({icon_name: {type_name: svg_content}})

    def __get_icon_types(self, project_name: str):
        types = os.listdir(os.path.join(self.__icons_folder, project_name))
        self.__remove_hidden_dirs(types)
        return types

    def __fix_type_name_for_data_construction(self, type:str):
        if type.find('fill') > -1:
            return 'filled'
        elif type.find('outline') > -1:
            return 'outline'
        elif type.find('sharp') > -1:
            return 'sharp'
        elif type.find('multicolor') > -1:
            return 'multicolor'

    def __get_icon_name(self, icon_path:str): 
        start = icon_path.rfind(os.sep) + 1
        end = icon_path.rfind('.svg')
        icon_name = icon_path[start:end]
        regex = re.compile("-outline|-sharp|-fill|-filled")
        icon_name = regex.sub('', icon_name)
        return icon_name
    
    def __list_svg_files_path(self, project_name, type):
        icons = os.listdir(os.path.join(self.__icons_folder, project_name, type))
        self.__remove_hidden_dirs(icons)
        return [
            os.path.join(self.__icons_folder, project_name, type, icon_name)
            for icon_name in icons
        ]

    def __read_svg_file(self, file_path:str):
        file = open(file_path)
        file_content = file.read()
        file.close()
        return file_content

    def __init_classified_data(self):
        for project in self.__projects_name:
            self.__classified_data[project] = {}