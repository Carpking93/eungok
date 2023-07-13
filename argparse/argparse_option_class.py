import argparse

class Cat:
    def __init__(self , name , color ,sound ):
        self.name = name
        self.color = color
        self.sound = sound

    def __str__(self):
        return f'Cat(name={self.name},color={self.color},sound={self.sound})' 
    
    def lotto(self):
        print(f'내이름은{self.name},색은 {self.color}인 고양이가 {self.sound} 라고 웁니다!')

def parsing_argument():
    parser = argparse.ArgumentParser(description="Cat Cat",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '-n',
        '--name',
        metavar="name",
        nargs='*',
        type=str,
        help="고양이의 이름을 적어줘",
        default=["나비"]
    )
    parser.add_argument(
        '-c',
        '--color',
        metavar="색깔",
        nargs='*',
        type=str,
        help="고양이의 이름을 적어줘",
        default=["흰색","냐옹"]
    )
    

    args = parser.parse_args()
    print(args)
    return args



def main():
    args = parsing_argument()
    cat = Cat(args.name[0],args.color[0],args.color[1])
    cat.lotto()
    
main()

# nabi = Cat("나비","흰색")
# nabi.lotto()
# nero = Cat("네로","검은색")

# print(nabi)
# print(nero)