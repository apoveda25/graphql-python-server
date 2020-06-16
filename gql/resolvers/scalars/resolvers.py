from datetime import datetime as dt
from ariadne import ScalarType

datetime_scalar = ScalarType("DateTime")


@datetime_scalar.serializer
def serialize_datetime(value):
    return dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f").isoformat()
