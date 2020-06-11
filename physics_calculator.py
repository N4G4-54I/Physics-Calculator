# Physics Calculator


def speed(distance, time = None):
    distance, time = values.values()
    print(round(distance/time, 3), "m/s")

def acceleration(speed, time = None):
    speed, time = values.values()
    print(round(speed/time, 3), "m/s^2")

def density(mass, volume = None):
    mass, volume = values.values()
    print(round(mass/volume, 2), "kg/m^3")

def moments(force, perpendicular_distance = None):
    force, perpendicular_distance = values.values()
    print(round(force*perpendicular_distance, 2), "Nm")

def pressure(force, surface_area = None):
    force, surface_area = values.values()
    print(round(force/surface_area, 2), "Pa")

def newton_2(mass, acceleration = None):
    mass, acceleration = values.values()
    print(round(mass*acceleration, 2), "N")

def power(work_done, time = None):
    work_done, time = values.values()
    print(round(work_done/time, 2), "W")

def weight(mass, gravitational_field_strength = None):
    mass, gravitational_field_strength = values.values()
    print(round(mass*gravitational_field_strength, 2), "N")

def kinetic_energy(mass, velocity = None):
    mass, velocity = values.values()
    print(round(0.5*mass*(velocity**2), 2), "J")

def voltage(current, resistance = None):
    current, resistance = values.values()
    print(round(current*resistance, 2), "V")

def current(voltage, resistance = None):
    voltage, resistance = values.values()
    print(round(voltage/resistance, 2), "A")

def resistance(current, voltage = None):
    current, voltage = values.values()
    print(round(voltage/current, 2), "Ω")

def frequency(wave_speed, wavelength = None):
    wave_speed, wavelength = values.values()
    print(round(wave_speed/wavelength, 2), "Ω")

def fluid_pressure(fluid_density, depth = None, gravitational_field_strength = None):
    fluid_density, depth, gravitational_field_strength = values.values()
    print(round(fluid_density*depth*gravitational_field_strength, 2), "Pa")

def gravitational_potential_energy(mass, gravitational_field_strength = None, height_from_ground = None):
    mass, gravitational_field_strength, height_from_ground = values.values()
    print(round(mass*gravitational_field_strength*height_from_ground, 2), "J")

import inspect

functions = {"speed": speed, "acceleration": acceleration, "density": density, 
"moments": moments, "pressure": pressure, "newton_2nd_law": newton_2, "power": power,
 "weight": weight, "kinetic_energy": kinetic_energy, "current": current, "voltage": voltage,
  "resistance": resistance, "fluid_pressure": fluid_pressure, "gravitational_potential_energy": gravitational_potential_energy}

functions_num = {"1": speed, "2": acceleration, "3": density, "4": moments, "5": pressure, "6": newton_2, "7": power, 
"8": weight, "9": kinetic_energy, "10": current, "11": voltage, "12": resistance, "13": fluid_pressure, 
"14": gravitational_potential_energy}

parameter_symbols = {"mass": "(kg)", "gravitational_field_strength": "(N/kg)", "height_from_ground": "(m)", "fluid_density": "(kg/m^3)", "depth": "(m)",
"wave_speed": "(m/s)", "wavelength": "(m)", "current": "(A)", "voltage": "(V)", "resistance": "(Ω)", "velocity": "(m/s)", "work_done": "(J)",
"time": "(s)", "acceleration": "(m/s^2)", "force": "(N)", "perpendicular_distance": "(m)", "distance": "(m)", "volume": "m^3", "surface_area": "(m^2)"}

print("Type \"list\" for list of functions")
print("Type \"quit\" to quit program")
while True:
    print()
    mode = input("Select a mode: ").strip().replace(" ", "_").lower()
    
    if mode == "stop":
        break
    elif mode == "list":
        x = 1
        for i in functions.keys():
            print(str(x) + ". " + i.replace("_", " "))
            x += 1
        x = 1
    elif mode in functions:
        try:
            mode = functions[mode]
            function = inspect.getfullargspec(mode)
            print()

            values = {}

            for parameter in function[0]:
                message = "Please enter " + str(parameter).replace("_", " ") + " " +parameter_symbols[str(parameter)]+ ": "
                value = float(input(message))
                values[parameter] = value
            print("\n Final Answer:")
            mode(values)
        except ValueError:
            print("\nPlease enter a numerical value")
        except ZeroDivisionError:
            print("\nSorry, 0 is not a valid input")
    elif mode in functions_num:
        try:
            mode = functions_num[mode]
            function = inspect.getfullargspec(mode)
            print()

            values = {}

            for parameter in function[0]:
                message = "Please enter " + str(parameter).replace("_", " ") + " " +parameter_symbols[str(parameter)]+ ": "
                value = float(input(message))
                values[parameter] = value
            print()
            print("Final Answer:")
            mode(values)
        except ValueError:
            print("\nPlease enter a numerical value")
        except ZeroDivisionError:
            print("\nSorry, 0 is not a valid input")
    else:
        print("\nMode Not Found")