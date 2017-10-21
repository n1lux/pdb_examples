import platform
import json


def machine_info():
        p = platform.uname()
        info = {'machine': p.machine,
                'node': p.node,
                'processor': p.processor,
                'release': p.release,
                'system': p.system,
                'version': p.version
              }

        return json.dumps(info)


def load_machine_conf():

    machine = json.loads(machine_info())
    
    data = dict()
    
    data['version'] = machine['version']
    data['os_version'] = machine['os']
    
    return data

def main():

    try:
        load_machine_conf()
    except:
        import pdb, traceback, sys
        _, _, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)


if __name__ == "__main__":
    main()
