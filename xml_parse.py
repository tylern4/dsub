from logs import *
import xmltodict
from multiprocessing import cpu_count

def into_list(xml_data):
    from datetime import datetime
    time = datetime.now().strftime('%m_%d_%Y_%H%M_')
    l = []
    for i in range(0,int(xml_data['count'])):
        xml_data['execute'] = time+str(i)
        l.append(xml_data)
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
        count = doc['NumOfJobs']['@num']
    except:
        count = int(1)

    try:
        job_name_template = doc['Job']['Name']['@name']
    except:
        job_name_template = False

    input_list = []
    output_list = []
    scripts_list = []

    temp = doc['Job']['Input']
    try:
        for x in temp:
            input_list.append({'src': x['@src'], 'dest': x['@dest']})
    except:
        input_list.append({'src': temp['@src'], 'dest': temp['@dest']})
    else:
        pass

    temp = doc['Job']['Output']
    try:
        for x in temp:
            output_list.append({'src': x['@src'], 'dest': x['@dest']})
    except:
        output_list.append({'src': temp['@src'], 'dest': temp['@dest']})
    else:
        pass

    temp = doc['Job']['Script']
    try:
        for x in temp:
            scripts_list.append({'src': x['@src'], 'dest': x['@dest']})
    except:
        scripts_list.append({'src': temp['@src'], 'dest': temp['@dest']})
    else:
        pass

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
    'execute': False
    }

    xml_data = into_list(xml_data)
    return xml_data
