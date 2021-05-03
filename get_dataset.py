import os
import easygui

def get_folder():
    return "C:\!mywork\datasets\dataset_instanses"

def get_path_to_json_7_healthy():
    filename = '7_pacients_ideally_healthy_and_normal_axis.json'
    return os.path.join(get_folder(), filename)

def get_path_to_st_depression6():
    filename = "st_depression6.json"
    return os.path.join(get_folder(), filename)

def get_path_to_no_qrs1():
    filename= "t_without_qrs_1.json"
    return os.path.join(get_folder(), filename)

def get_path_to_200():
    folder= "C:\!mywork\datasets\BWR_ecg_200_delineation"
    filename ="ecg_data_200.json"
    return os.path.join(folder, filename)

def get_path():
    return easygui.fileopenbox("Select json dataset")

def get_part_path(num):
    folder = "C:\!mywork\datasets\BWR_data_schiller"
    filename = "data_part_"+str(num)+".json"
    return os.path.join(folder, filename)