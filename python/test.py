def getBoxesByProduct(product):
  products = {
    'IoT Box': {
        'BOX-06x02x02': 2.0,
        'BOX-20x20x12': 16.0,
        'BOX-16x16x16': 9.0,
        'BOX-08x08x08': 4.0,
    },
    'Scale-Up! The Business Game': {
        'BOX-16x16x16': 7.0,
        'BOX-10x08x08': 3.0,
        'BOX-23x17x12': 14.0,
    },
    'Basic Cash Drawer': {},
    'Shoes': {
        'BOX-06x02x02': 6.0,
    }
  }
  return list((box,products[product][box]) for box in products[product])

def getBoxesByProductInOrder(product_name,quantity):
  available_boxes=getBoxesByProduct(product_name)
  if len(available_boxes) == 0:
    return []
  products_to_insert_in_box=quantity
  
  taken_boxes=[]
  while products_to_insert_in_box > 0:
    compare_list=[]
    for box in available_boxes:
      compare_list.append((box[0],abs(products_to_insert_in_box - box[1])))
    
    taken_box_name= min(compare_list,key=lambda x:x[1])[0]
    if products_to_insert_in_box<box[1]:
      products_in_taken_box=products_to_insert_in_box
    else: 
      products_in_taken_box=products_to_insert_in_box-min(compare_list,key=lambda x:x[1])[1]
    products_to_insert_in_box=products_to_insert_in_box- products_in_taken_box
    taken_boxes.append((taken_box_name,products_in_taken_box))
    print(taken_boxes, compare_list)
  return taken_boxes

print(getBoxesByProductInOrder('IoT Box', 47.0))  

def processOrder(order):
  for product in order:
    boxes_by_product = getBoxesByProductInOrder(product,order[product])
    # packs = []
    # quantity = order[product]
    # boxes = getBoxesByProduct(product)
    # boxes.sort(reverse=True,key=lambda x:x[1])
    # print(boxes)
    # for box,size in boxes:
    #   if quantity/size > 0 and quantity%size > 0:
    #     packs.append((box, size))
    #     quantity = order[product]%size
    #     print(packs)
    #   else:
    #     packs.append((box, size))
    #     quantity = order[product]%size
    #     print(packs)
    #     break

processOrder({
       'Scale-Up! The Business Game': 15.0,
       'Basic Cash Drawer': 10.0,
       'IoT Box': 47.0,
       'Shoes': 5.0,
   })

def packingBoxes(orders):
  return {(order,orders[order]) for order in orders}

packingBoxes({
   'S0101': {
       'Scale-Up! The Business Game': 15.0,
       'Basic Cash Drawer': 10.0,
       'IoT Box': 47.0,
       'Shoes': 5.0,
   },
   'S0102': {
       'IoT Box': 2.0,
       'Scale-Up! The Business Game': 10.0,
   },
   'S0103': {
       'Shoes': 50.0,
       'IoT Box': 500.0,
       'Scale-Up! The Business Game': 32.0,
       'Basic Cash Drawer': 10.0,
   },
})

# - The following are the the Products and packaging boxes information
#   of Acme Inc.
# - Each product in given dictionary/hash contain possible packing boxes
#   that can be used to ship the product when ordered
# - Each packaging boxes gives you how many numbers of the given product
#   can be packed in the box.
# - Packing box names are just reference names, they are not dimension
#   of the packing box
# - Following are product details where data structure will be consistent
#   but number of product and boxes available for given product will be 
#   variable and you will not know their size before hand.
# - You can use  as many as boxes you like from the boxes list

products = {
   'IoT Box': {
       'BOX-06x02x02': 2.0,
       'BOX-20x20x12': 16.0,
       'BOX-16x16x16': 9.0,
       'BOX-08x08x08': 4.0,
   },
   'Scale-Up! The Business Game': {
       'BOX-16x16x16': 7.0,
       'BOX-10x08x08': 3.0,
       'BOX-23x17x12': 14.0,
   },
   'Basic Cash Drawer': {},
   'Shoes': {
       'BOX-06x02x02': 6.0,
   }
}

# -Following data contians order details with an order number, the ordered
#  products and their initial demand of product quantity by customer
# - Orders data structure will be consistent but data in orders will vary

# orders = {
#    'S0101': {
#        'Scale-Up! The Business Game': 15.0,
#        'Basic Cash Drawer': 10.0,
#        'IoT Box': 47.0,
#        'Shoes': 5.0,
#    },
#    'S0102': {
#        'IoT Box': 2.0,
#        'Scale-Up! The Business Game': 10.0,
#    },
#    'S0103': {
#        'Shoes': 50.0,
#        'IoT Box': 500.0,
#        'Scale-Up! The Business Game': 32.0,
#        'Basic Cash Drawer': 10.0,
#    },
# }

# - Write a program/script/solution to find and return the best and least
# possible packing boxes to be used for shipping the ordered products
# in an order.
# - Also, each box should give a count of product quantity to be packed
# in each selected boxe(s) from the given list.

# Expected return :

# packed_orders = {
#     'S0101': {
#         'Scale-Up! The Business Game': {
#             'packs': [('BOX-23x17x12', 14.0),
#                       ('BOX-10x08x08', 1.0)],
#             'quantity': 15.0
#         },
#         'IoT Box': {
#             'packs': [('BOX-20x20x12', 16.0),
#                       ('BOX-20x20x12', 16.0),
#                       ('BOX-16x16x16', 9.0),
#                       ('BOX-08x08x08', 4.0),
#                       ('BOX-06x02x02', 2.0)],
#             'quantity': 47.0
#         },
#         'Basic Cash Drawer': {
#             'packs': [],
#             'quantity': 10.0
#         },
#         'Shoes': {
#             'packs': [('BOX-06x02x02', 5.0)], 
#             'quantity': 5.0
#         }
#     },
#     'S0102': {...},
#     'S0103': {...},
# }