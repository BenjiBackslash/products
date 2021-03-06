import yaml


mongo_config = None
log_dict_config = None


def create(config_file):
    global consumer_config
    global mongo_config
    global log_dict_config
    with open(config_file, "r") as fdr:
        config = yaml.load(fdr)
    mongo_config = config["mongo"]
    log_dict_config = config["log"]
