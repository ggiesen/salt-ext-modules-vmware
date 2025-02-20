# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import os
import uuid
from unittest.mock import MagicMock

import pytest
import salt.exceptions
import saltext.vmware.modules.vsphere as vsphere
import saltext.vmware.utils.common as utils_common


def test_system_info(service_instance):
    ret = vsphere.system_info(
        service_instance=service_instance,
    )
    assert ret
    assert isinstance(ret["apiType"], str)
    assert isinstance(ret["fullName"], str)


def test_list_resourcepools(service_instance):
    ret = vsphere.list_resourcepools(
        service_instance=service_instance,
    )
    assert ret


def test_list_networks(service_instance):
    ret = vsphere.list_networks(
        service_instance=service_instance,
    )
    assert ret
    for network in ret:
        assert isinstance(network, str)
