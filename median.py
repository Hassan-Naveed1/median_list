def median(median_list):

    new_list = []
    while median_list:
        smallest = median_list[0]
        for i in median_list:
            if i < smallest:
                smallest = i 
        print(median_list)
        new_list.append(smallest)
        median_list.remove(smallest)

    return new_list

print(median([1,2,3,55,6,2,1]))

