from logs import *
import os
from temp_dir import cd, tempdir

def _docker_command(files_xml):
    for x in files_xml['input_list']:
        x['src'] = x['src'].replace("$",files_xml['ID'])
        x['dest'] = x['dest'].replace("$",files_xml['ID'])
    for x in files_xml['output_list']:
        x['src'] = x['src'].replace("$",files_xml['ID'])
        x['dest'] = x['dest'].replace("$",files_xml['ID'])

    docker_cmd = "docker run "
    #TODO get extras from xml as well
    docker_extras = "--link clasdb:clasdb -v`pwd`:/root/code --rm -it "
    if files_xml['memory_space'] and files_xml['memory_unit']:
        docker_cmd = docker_cmd + "-m " + str(files_xml['memory_space']) + str(files_xml['memory_unit']) + " "

    cmd = docker_cmd + docker_extras + str(files_xml['docker_image']) + " " + str(files_xml['script']['dest'])
    inputs = files_xml['input_list']
    outputs = files_xml['output_list']
    return cmd,inputs,outputs

def batch(files):
    with tempdir() as dirpath:
        docker_cmd,ins,outs = _docker_command(files)
        shutil.copyfile(files['script']['src'], dirpath+"/"+files['script']['dest'])

        for i in ins:
            shutil.copyfile(i['src'], dirpath+"/"+i['dest'])

        out = os.system(docker_cmd)
        if out == 0:
            for o in outs:
                shutil.copyfile(dirpath+"/"+o['src'],o['dest'])
        else:
            print(out)
