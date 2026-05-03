daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 13056, 952, 1100, 1025, 8574, 14014, 9987, 1238, 1458, 7803, 900, 13674, 14539, 13241, 10886, 7541, 8743, 1482, 11523, 977, 12181, 8903, 1008, 1530]
highest_sale = max(daily_sales)
highest_sale_day = daily_sales.index(highest_sale) + 1
lowest_sale = min(daily_sales)
lowest_sale_day = daily_sales.index(lowest_sale) + 1
average = sum(daily_sales) / len(daily_sales)
print(str(highest_sale_day) + " August has highest sales of $" + str(highest_sale))
print(str(lowest_sale_day) + " August has lowest sales of $" + str(lowest_sale))
print("Average daily sales for August is $" + str(average))