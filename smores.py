smoreingredients = ['INGREDIENTS:','9 HONEY MAID Honey Grahams, broken crosswise in half (18 squares)',
'36 JET-PUFFED Marshmallows, cut crosswise in half',
'4 HERSHEYS Milk Chocolate Bars, (1.55 oz. each), chopped']

smoreinstructions = ['INSTRUCTIONS:','HEAT  oven to 350°F.',
'PLACE  9 graham squares in single layer on bottom of 8-inch square pan; top with 36 marshmallow halves. Sprinkle with chopped chocolate. Cover with remaining graham squares.',
'TOP  with remaining marshmallow halves, cut sides down.',
'BAKE  9 to 11 min. or until marshmallows are puffed and golden brown. Let stand 5 min. before serving.']

smore = [smoreingredients, smoreinstructions]




my_dict = {'smores' : smore}
response = input("What are you looking for?")
print (my_dict[response])
