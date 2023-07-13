import argparse

class Car:
    def __init__(self , door_num , brand , color ,rapid ):
        self.door_num = door_num
        self.brand = brand
        self.color = color
        self.rapid = rapid

    def __str__(self):
        return f'Car(name={self.door_num},brand={self.brand},color={self.color})' 
    
    def Sonata(self):
        print(f'문의 갯수는{self.door_num},브랜드는 {self.brand}이고 색상은 {self.color} 입니다! 시속 {self.rapid}로 주행중입니다. ')

def parsing_argument():
    parser = argparse.ArgumentParser(description="Car",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '-c',
        '--car',
        metavar="car",
        nargs='*',
        type=str,
        help="자동차의 문갯수,브랜드,색상",
        default=["4","쏘나타","블랙","50km"]
    )

    args = parser.parse_args()
    print(args)
    return args



def main():
    args = parsing_argument()
    car = Car(args.car[0],args.car[1],args.car[2],args.car[3])
    car.Sonata()
    
main()
    