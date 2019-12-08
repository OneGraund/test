class Processor:
    def __init__(self, cores_amount, frequency, cash_size):
        self.cores_amount = cores_amount
        self.frequency = frequency
        self.cash_size = cash_size

class Graph_processor:
    def __init__(self, frequency, video_memory_size):
        self.frequency = frequency
        self.video_memory_size = video_memory_size

class HDD:
    def __init__(self, motor_velocity, memory_size):
        self.motor_velocity = motor_velocity
        self.memory_size = memory_size

class Mother_board:
    def __init__(self, socket, chipset, front_side_bus):
        self.socket = socket
        self.chipset = chipset
        self.front_side_bus = front_side_bus

class Battery:
    def __init__(self, capacity, material_type, power):
        self.capacity = capacity
        self.material_type = material_type
        self.power = power

class Case:
    def __init__(self, colour, material, hightness, lenght_horizontal, lenght_vertical):
        self.colour = colour
        self.material = material
        self.hightness = hightness
        self.lenght_horizontal = lenght_horizontal
        self.lenght_vertical = lenght_vertical

class Display:
    def __init__(self, diagonal, matrix_type, density):
        self.diagonal = diagonal
        self.matrix_type = matrix_type
        self.density = density

class Keyboard:
    def __init__(self, key_travel, keyboard_type):
        self.key_travel = key_travel
        self.keyboard_type = keyboard_type

class Info:
    def __init__(self, firm, seller, serial_number, description):
        self.firm = firm
        self.seller = seller
        self.serial_number = serial_number
        self.description = description


#-----------------------------------------------------------------------------------

class Notebook:
    def __init__(self, processor, graph_processor, hdd, mother_board, battery, case, display, keyboard, info):
        self.processor = processor
        self.graph_processor = graph_processor
        self.hdd = hdd
        self.mother_board = mother_board
        self.battery = battery
        self.case = case
        self.display = display
        self.keyboard = keyboard
        self.info = info

asus = Notebook(processor = Processor(cores_amount=2, frequency=4.5, cash_size=50),
    graph_processor = Graph_processor(frequency=1.2, video_memory_size=2),
    hdd = HDD(motor_velocity=7600, memory_size=960),
    mother_board = Mother_board(socket="AM4", chipset="H110", front_side_bus=256),
    battery = Battery(capacity=2600, material_type="li-on", power=80),
    case = Case(colour="black", material="aluminium, plastic", hightness=3, lenght_horizontal=40, lenght_vertical=25),
    display = Display(diagonal=15.6, matrix_type="TS", density="1280x720"),
    keyboard = Keyboard(key_travel=0.4, keyboard_type="membran"),
    info = Info(firm="ASUS", seller="Rozetka", serial_number="C12353MN", description="Best notebook for 300 hohlo-baksiv"))


