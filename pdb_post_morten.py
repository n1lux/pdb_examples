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


def main():
    machine = json.loads(machine_info())
    try:
        print(machine['os'])
    except:
        import pdb, traceback, sys
        _, _, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)



if __name__ == "__main__":
    main()
