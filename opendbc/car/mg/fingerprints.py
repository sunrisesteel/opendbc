from opendbc.car.structs import CarParams
from opendbc.car.mg.values import CAR  # Use your MG values, not Hyundai

Ecu = CarParams.Ecu

FW_VERSIONS = {
  CAR.MG_5EV_LR_2021: {
    (Ecu.adas, 0x730, None): [
      b'\xf1\x00\x02\x01\x00\x00]\x01\x02\x00\x00\xfbi',
    ],
  },
}
