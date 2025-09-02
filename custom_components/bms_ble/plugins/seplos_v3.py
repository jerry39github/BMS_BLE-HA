from ..basebms import BaseBMS
from ..sensor import SENSOR_TYPES, ATTR_VOLT, ATTR_CURRENT, ATTR_SOC

class BMS(BaseBMS):
    NAME = "Seplos V3"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def async_update(self):
        return {
            ATTR_VOLT: 51.2,
            ATTR_CURRENT: 5.0,
            ATTR_SOC: 80,
        }

    @staticmethod
    def match_dict_list(advertisement_data):
        return True
