import folium
import json
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from folium.plugins.treelayercontrol import TreeLayerControl
from .models import NeCountries, NeStatesProvinces


def index(request):
    countries = NeCountries.objects.all().order_by('name_long')
    return render(request, 'world/index.html', {'countries': countries})


def detail(request, iso_code):
    country = get_object_or_404(NeCountries, adm0_a3=iso_code)

    model_datas = NeStatesProvinces.objects.filter(adm0_a3=iso_code).order_by('name')

    centroid = country.geom.centroid

    m = folium.Map(location=(centroid.y, centroid.x), zoom_start=5)
    
    for model_data in model_datas:
        geojson_state = serialize(
            'geojson',
            [model_data],
            geometry_field="geom",
            fields=["name"],
        )
        geojson_state = json.loads(geojson_state)

        folium.GeoJson(
            geojson_state,
            name=model_data.name,
            tooltip=model_data.type + ' ' + model_data.name,
        ).add_to(m)

    folium.LayerControl().add_to(m)

    context = {}
    context['country'] = country
    context['map'] = m._repr_html_()

    return render(request, 'world/detail.html', context)
