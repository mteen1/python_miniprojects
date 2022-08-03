def formatted_print(a):
   
    
    sort_orders = sorted(a.items(), key=lambda x: x[0],reverse=True)

    for i in sort_orders:
        print("{:10s} {:6.2f}".format(i[0], i[1]))

dict = {"ali":24.146,"matin":23.900}
formatted_print(dict)
