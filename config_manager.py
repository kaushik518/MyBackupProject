import json

def load_config(path):
    with open(path, 'r') as file:
        config = json.load(file)
    return config

def display_config(config):
    print("Current Configuration:")
    for key, value in config.items():
        print(f" - {key}: {value}")

def main():
    config_path = "config.json"
    config = load_config(config_path)
    display_config(config)

if __name__ == "__main__":
    main()
