"""
创建 奥迪 汽车 类
"""
import time


def create_component(comp_name, spend_time=0.5):
    print(f"开始创建汽车{comp_name}")
    print("正在创建")
    time.sleep(spend_time)
    print(f"{comp_name}创建好了")


class VehicleComponent:
    def __init__(self):
        self.name = None
        self.vehicle_brand = None
        self.motor_type = None
        self.price = None

    def create_motor(self):
        create_component("发动机", 1.2)
        return self

    def create_direction(self):
        create_component("方向盘", 0.6)
        return self

    def create_bottom(self):
        create_component("底盘", 1.0)
        return self

    def create_iron(self):
        for i in range(4):
            create_component(f"轮子{i + 1}", 0.3)
        return self

    def create_appearance(self):
        create_component("外壳", 2.6)
        return self

    def __repr__(self):
        return f"name={self.name}, vehicle_brand={self.vehicle_brand}, " \
               f"motor_type={self.motor_type}, price={self.price}"


def create_vehicle():
    vehicle_audio = VehicleComponent()
    vehicle_audio.name = "奥迪A6"
    vehicle_audio.vehicle_brand = "奥迪"
    vehicle_audio.motor_type = "小轿车"
    vehicle_audio.price = '100'  # 万
    vehicle_audio.create_motor().create_bottom().create_iron().create_appearance().create_direction()
    return vehicle_audio


if __name__ == "__main__":
    vehicle_audio = create_vehicle()
    print(vehicle_audio)
