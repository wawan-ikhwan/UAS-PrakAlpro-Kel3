# insertion sort
order_id = [64,75,84,77,66]
order_date = ["2016-11-08","2016-06-12","2015-10-11","2014-06-09","2017-04-15"]
customer_id = ["CA-2016-152156","CA-2016-138688","CA-2016-108966","CA-2016-115812","CA-2016-114412"]

for i in range(1, len(order_id)):
    key = order_id[i]
    keya = customer_id[i]
    keyb = order_date[i]
    j = i-1
    while j >= 0 and key < order_id[j]:
        order_id[j+1] = order_id[j]
        customer_id[j+1] = customer_id[j]
        j -= 1
    order_id[j+1]=key
    customer_id[j+1]=keya
    order_date[j+1]=keyb
    print(order_id)
    
    print("\n")
print("Data sudah terurut")
print(order_id)
print(customer_id)
print(order_date)
