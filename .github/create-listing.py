#!/usr/local/bin/python3
import os
import yaml

def main():
    for ipynb_dir in ['Lessons', 'Practices']:
        nb_dict = get_dict_list(f"{ipynb_dir}/_Keys/")
        with open(f'{ipynb_dir.lower()}.yml', 'w') as yml_file:
            yaml.dump(nb_dict, yml_file)

def get_dict_list(dirpath):
    return [{"title": f.strip('.ipynb').strip("KEY_"),
                    "path" : f"{dirpath}{f}"
                    } for f in os.listdir(lesson_dir) if f.endswith('.ipynb')]

main()