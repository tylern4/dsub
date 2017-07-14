from logs import *
import xmltodict
from multiprocessing import cpu_count

def into_list(xml_data):
    from datetime import datetime
    time = datetime.now().strftime('%m_%d_%Y_%H%M_')
    l = []
    for i in range(0,xml_data['count']):
        temp = xml_data.copy()
        temp['ID'] = time+str(i)
        temp['job_name_template'] = temp['job_name_template'].replace("$",temp['ID'])
        
        #TODO Get $ replace working for input/output files
        l.append(temp)
    return l

def get_list(temp):
    l = []
    try:
        for x in temp:
            l.append({'src': x['@src'], 'dest': x['@dest']})
    except:
        l.append({'src': temp['@src'], 'dest': temp['@dest']})
    else:
        pass
    return l


def xml_parse(xml_file):
    with open(xml_file) as fd:
        doc = xmltodict.parse(fd.read())['Request']

    try:
        docker_image = doc['Docker']['@name']
    except:
        print_red("Error no Docker image name given...Exiting")
        exit()

    try:
        memory_space = doc['Memory']['@space']
        memory_unit = doc['Memory']['@unit']
    except:
        memory_space = False
        memory_unit = False

    try:
        num_cores = int(doc['Cores']['@num'])
    except:
        num_cores = cpu_count()

    try:
        count = int(doc['NumOfJobs']['@num'])
    except:
        count = int(1)

    try:
        job_name_template = doc['Job']['Name']['@name']
    except:
        job_name_template = False

    input_list = get_list(doc['Job']['Input'])
    output_list = get_list(doc['Job']['Output'])
    scripts_list = get_list(doc['Job']['Script'])

    xml_data = {
        'docker_image': docker_image,
        'memory_space': memory_space,
        'memory_unit': memory_unit,
        'num_cores': num_cores,
        'count': count,
        'job_name_template': job_name_template,
        'input_list': input_list,
        'output_list': output_list,
        'scripts_list': scripts_list,
        'ID': False
    }

    xml_data = into_list(xml_data)
    return xml_data
