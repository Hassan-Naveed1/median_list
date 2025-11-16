def median(median_list):

  if len(median_list) == 1:
    return median_list[0]
  new_list = []
  while median_list:
    smallest = median_list[0]
    for i in median_list:
      if i < smallest:
        smallest = i
    new_list.append(smallest)
    median_list.remove(smallest)

  if len(new_list) % 2 != 0:
    mid_item = len(new_list) // 2
    return new_list[mid_item]

  elif len(new_list) % 2 == 0:
    mid_item1 = len(new_list) // 2
    mid_item2 = mid_item1 - 1
    avrg_mid_items = (new_list[mid_item1] + new_list[mid_item2]) / 2

    return avrg_mid_items


print(median([4,5,5,4]))
