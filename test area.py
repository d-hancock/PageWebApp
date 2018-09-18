trims = [{'title': '2018 Chevrolet Tahoe LS', 'content': 'Expect the unexpected with the Chevy Tahoe LS. This base model is packed with advanced technologies and premium amenities that you’re sure to use to your advantage.', 'trim list' : ['5.3L EcoTec3 V8 engine', 'Premium Smooth Ride suspension', '6-speed automatic transmission']}, {'title': '2018 Chevrolet Tahoe LT', 'content': 'Expect even more advanced features with the 2018 Chevy Tahoe LT, including an upgraded sound system and a driver-assist system. The Tahoe LT includes many Tahoe LS features, plus:', 'trim list' : ['Rear Vision Camera', 'Rear Vision Camera', '4.2-in. multi-color driver information center']}]

for trim in trims:
    print([trim['title']])

for trim in trims:
    print([trim['content']][0])

for trim in trims:
    for item in [trim['trim list']]:
        for l in item:
            print(l)


for trim in trims:
    for item in [trim['trim list']]:
       print(item)


for item in [trim['trim list']]:
    for l in item:
        print(l)