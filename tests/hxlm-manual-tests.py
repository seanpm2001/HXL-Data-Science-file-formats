#!/usr/bin/env python3

# ./tests/hxlm-manual-tests.py

import hxlm.core.util
import hxlm.core
import hxlm.routing

hxlm.routing.routing_info()
print(hxlm.routing.get_external_ip())

print(hxlm.routing.request_cache_resource(
    url='https://example.org/dataset/data.csv', hpeer='192.0.2.0'))

# from hxlm.core.htype.encryption import EncryptionHtype
# from hxlm.core.htype.sensitive import SensitiveHtype

hdata = hxlm.core.base.HConteiner()

print(hdata)
# mdataset.encryption = "abc"
hdata.sensitive = hxlm.core.constant.HDSL1
print(hdata.describe())

hxlm.core.util.debug()
