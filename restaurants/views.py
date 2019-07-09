from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list" : [

    {
    "restaurant_name": "San Marco", "food_type": "Pizza"
    }, 

    {
    "restaurant_name": "Babel", "food_type": "Lebanese"
    },

    {
    "restaurant_name": "IHOP", "food_type": "Breakfast"
    	},
    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object": {
    "restaurant_name": "San Marco",
    "food_type": "Pizza",
    },

    }
    return render(request, 'detail.html', context)
