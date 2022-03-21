from pydantic import BaseModel, confloat, conint, conlist


class GeoPoint(BaseModel):
    # GeoJSON RFC says it must be in the order of [longitude, latitude] for a Position
    # https://github.com/samuelcolvin/pydantic/issues/2062
    longitude: confloat(ge=-180.0, le=180.0)
    latitude: confloat(ge=-90.0, le=90.0)

    def __init__(self, coordinates: conlist(float, max_items=2, min_items=2)):
        super().__init__(longitude=coordinates[0], latitude=coordinates[1])

    def dict(self, **kwargs):
        return [self.longitude, self.latitude]


class Zoom(BaseModel):
    value = conint(ge=1, le=18)

    def __init__(self, v: int):
        super().__init__(value=v)
