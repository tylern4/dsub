from logs import *
import os
from temp_dir import cd, tempdir

def batch(base):
    print(base)
    with tempdir() as dirpath:
        #shutil.copyfile(cwd+"/aao_rad.inp", dirpath+"/aao_rad.inp")
        #shutil.copyfile(cwd+"/gsim.inp", dirpath+"/gsim.inp")
        #shutil.copyfile(cwd+"/user_ana.tcl", dirpath+"/user_ana.tcl")
        #shutil.copyfile(cwd+"/batch.sh", dirpath+"/batch.sh")
        docker_cmd = "docker run --link clasdb:clasdb -v`pwd`:/root/code --rm -it tylern4/clas6:latest batch.sh"
        print_red(docker_cmd)
        #out = os.system("docker run --link clasdb:clasdb -v`pwd`:/root/code --rm -it tylern4/clas6:latest batch.sh")
        #if out == 0:
        #    shutil.copyfile(dirpath+"/cooked.root", base+".root")
        #else:
        #    print(out)

def make_list(args):
    from datetime import datetime
    time = datetime.now().strftime('%m_%d_%Y-%H%M_')
    l = []
    for i in range(0,args.num):
        l.append(args.output+"sim_"+time+str(i))
    return l
