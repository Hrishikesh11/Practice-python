class car:
    def __init__(self,speed=0):
        #This function initiates speed odometer and time
        self.speed=speed
        self.odometer=0
        self.time=0

    def say_state(self):
        # this function just returns your current speed
        print('Im going at {} kmp'.format(self.speed))

    def accelerate(self):
        #this function accelerates the speed by 5kmp
        self.speed+=5
    def brake(self):
        #this function decrese the speed by 5kmp
        self.speed-=5

    def step(self):
        self.odometer+=self.speed
        self.time+=1

    def averege_speed(self):
        if self.speed!=0:
            return self.odometer/self.time
        else:
            pass

if __name__=="__main__":
    my_car=car()
    action=""
    actionarr=[1,2,3,4,5]
    while action!=5:
        action=int(input("What should I do? [1] Accelerate, [2]Brake, [3] Show Odometer, [4] Show average speed? [5]Exit "))
        if action in actionarr:
            if action ==1:
                my_car.accelerate()
            elif action==2:
                my_car.brake()
            elif action==3:
                print("The car has driven {} kilometers".format(my_car.odometer))
            elif action==4:
                print("The cars average speed was {} kph".format(my_car.averege_speed()))
        my_car.step()
        my_car.say_state()