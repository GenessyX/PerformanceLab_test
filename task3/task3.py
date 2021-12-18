import argparse
import os
import json
from typing import List

def get_value(id: str, values: List[dict]) -> str:
    for value in values:
        if value['id'] == id:
            return value['value']

def rec_parse(tests: List[dict], values: List[dict]) -> List[dict]:
    for index, test in enumerate(tests):
        if 'value' in test.keys():
            tests[index]['value'] = get_value(test['id'], values)
        if 'values' in test.keys():
            rec_parse(test['values'], values)
    return tests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tests_file', type=str)
    parser.add_argument('values_file', type=str)
    args = parser.parse_args()

    values_file, tests_file = args.values_file, args.tests_file

    if (not os.path.exists(values_file) or not os.path.exists(tests_file)):
        raise Exception("File not found")

    with open(values_file, 'r') as v_f:
        values = json.loads(v_f.read())
    
    with open(tests_file, 'r') as t_f:
        tests = json.loads(t_f.read())

    res = rec_parse(tests['tests'], values['values'])
    with open('report.json', 'w') as r:
        r.write(json.dumps(res, indent=2))
    

if __name__ == "__main__":
    main()