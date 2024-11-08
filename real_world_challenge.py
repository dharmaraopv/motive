# Processing methods (utils.py)
import requests

"""
Data format: 
{
"Count": 121,
"Message": "Results returned successfully",
"SearchCriteria": "Make:honda | ModelYear:2016",
"Results": [
{
"Make_ID": 474,
"Make_Name": "HONDA",
"Model_ID": 1861,
"Model_Name": "Accord"
},

"""


def get_car_data(year):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/honda/modelyear/{year}?format=json"
    data = requests.get(url).json()
    if not "Results" in data:
        return []

    return {car["Model_Name"]: {"id": car["Model_ID"]} for car in data["Results"]}


def get_discontinued_models_for_last_10_years(curr_year):
    all_models = {}
    for year in range(curr_year - 9, curr_year + 1):
        models = get_car_data(year)
        for model in models:
            all_models[model] = models[model]
            all_models[model]['latest_year'] = year
    discountinued_models = {model: all_models[model] for model in
                            all_models if all_models[model]['latest_year'] != curr_year and all_models[model][
                                'latest_year'] != curr_year - 1}
    return discountinued_models


# API views (views.py)
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def car_data_for_year(request, year):
    data = get_car_data(year)
    return Response(data)


@api_view(['GET'])
def get_discontinued_models(request, year):
    data = get_discontinued_models_for_last_10_years(year)
    return Response(data)


# URL configuration (urls.py)
from django.urls import path, include
from .views import car_data_for_year, get_discontinued_models

urlpatterns = [
    path('car_data/<int:year>/', car_data_for_year),
    path('discontinued_models/<int:year>/', get_discontinued_models),
]
