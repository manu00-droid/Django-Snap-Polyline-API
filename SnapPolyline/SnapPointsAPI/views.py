from rest_framework.decorators import api_view
from rest_framework.response import Response
import googlemaps as gm

key = "AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ"
gmc = gm.Client(key=key)


@api_view(['POST'])
def snapPoly(request):
    points = request.POST["point"]
    points = points.replace("(", "")
    point = points.split("),")
    combPoint = point
    combPoint[-1] = combPoint[-1].replace(")", "")
    print(combPoint[-1])
    points_snapped = []
    prev = 0
    for i in range(100, len(combPoint), 100):
        points_snapped += gmc.snap_to_roads(path=combPoint[prev:i], interpolate=True)
        prev = i
    points_snapped += gmc.snap_to_roads(path=combPoint[prev:len(combPoint)], interpolate=True)
    print(points_snapped[0])
    return Response(points_snapped)
