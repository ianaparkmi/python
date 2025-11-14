import numpy as np

def trip():
    
    print("Enter the lengths of all sections of the road separated by spaces:")
    lengths_input=input('length: '.strip())
    print("\nEnter the average speeds in the sections separated by spaces:")
    speeds_input = input("Speed: ").strip()
    lengths_list = lengths_input.split()
    speeds_list = speeds_input.split()
    if len(lengths_list) != len(speeds_list):
        print("Error: the number of lengths and speeds does not match")
        return

    lengths = np.array([float(x) for x in lengths_list])  
    speeds = np.array([float(x) for x in speeds_list])
    print("\nEnter the section number where the car entered the road:")
    k = int(input("k = "))
    print("Enter the section number where the car left the road:")
    p = int(input("p = "))

    start_idx = k - 1
    end_idx = p - 1

    selected_lengths = lengths[start_idx:end_idx + 1]
    selected_speeds = speeds[start_idx:end_idx + 1]

    print(f"location {k}-{p}:")
    for i in range(len(selected_lengths)):
        print(f"location {i}: {selected_lengths[i]} km, {selected_speeds[i]} km/h")

    total_length=np.sum(selected_lengths)
    print(f'total length: {total_length}')
    times = selected_lengths / selected_speeds
    total_time = np.sum(times)
    print(f'total time: {total_time}')
    average_speed = total_length / total_time
    print(f'average speed: {average_speed}')

trip()
