import yaml


class backup_system:
    def __init__(self):
        with open('config.yml', 'r') as stream:
            try:
                self.status = True
                self.sucess = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                self.status = False
                self.error = exc
