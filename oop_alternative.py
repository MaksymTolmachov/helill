import uuid
from dataclasses import dataclass, field
# class Parcel:
#     parcel_id: str
#     recipient_name: str
#
# p = Parcel()
# p.parcel_id = "fghjkl;"
# p.recipient_name = "fdghjkl;"
#
# print(p.__dict__)

@dataclass(frozen=True)
class Parcel:
    parcel_id: str = field(default="sdfghjkl;'#")
    # recipient_name: str = field(default="sdfghjklkjuytr")
    recipient_name:uuid.UUID = field(default_factory=uuid.u)

p = Parcel(parcel_id="dfghjk", recipient_name="dfghjkl;")
# p.parcel_id = "fghjkl;"
# p.recipient_name = "fdghjkl;"

print(p.__dict__)



