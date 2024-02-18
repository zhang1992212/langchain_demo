import os
import getopt
import sys
from demo.rag_search import RagSearch
from demo.base import Base, BaseDemo

usage = '''
usage: python main.py [options]

Options
-h, --help  帮助
-d, --demo  选择示例

-d value
base 基础示例
rag_search RAG搜索示例

'''


def init_demo(argv):
    i = ''
    try:
        opts, args = getopt.getopt(argv, "hd:", ["demo="])
    except getopt.GetoptError:
        print('python main.py -d <示例名称>')
        sys.exit(2)

    if len(opts) == 0:
        opts = [("-h", "")]

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-d", "--demo"):
            i = arg
    api_key = "sk-NXQlVDPLjVyMjRMmB8F89974E1Ff4dEeBd1060Cd9fD2073b"
    openai_api_base = "https://openkey.cloud/v1"
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_API_BASE"] = openai_api_base

    base_demo = Base()
    input_value = {}
    match i:
        case "demo":
            base_demo = BaseDemo()
            input_value = {"topic": "dog"}
        case "rag_search":
            base_demo = RagSearch()
        case _:
            print(usage)
            sys.exit(2)

    base_demo.run_demo(input=input_value)


if __name__ == "__main__":
    init_demo(sys.argv[1:])
