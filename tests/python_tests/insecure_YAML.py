import yaml

testConfig = yaml.load(open('config.yml') , Loader=yaml.Loader)
testConfig = yaml.load(open('config.yml') , Loader=yaml.FullLoader)
testConfig = yaml.load(open('config.yml'))

testConfig = yaml.load(open('config.yml') , Loader=yaml.SafeLoader)