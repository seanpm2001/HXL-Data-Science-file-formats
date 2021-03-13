"""hxlm.core.model.hdp contains HDP class

This is used by the HDP Declarative Programming Command Line Interface


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from typing import (
    Union
)

import json
import yaml


__all__ = ['HDP']


class HDP:
    """Class used by HDP Declarative Programming Command Line Interface
    """

    _hdp: dict = None
    # TODO: what name to use? Maybe Knowledge base?
    #       https://en.wikipedia.org/wiki/Knowledge_base
    #       (Emerson Rocha, 2021-03-13 00:59 UTC)

    _hdp_raw: Union[str, dict] = None

    _online_unrestricted_init: bool = False
    """For requests that implicitly ask for not-only localhost data, should
    we implicitly initiate HDP?

    Defaults to False (for security reasons)
    """

    _safer_zone_hosts: list = [
        'localhost'
    ]
    """List of hostnames that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised
    """

    _safer_zone_list: list = [
        '127.0.0.1',
        '::1'
    ]
    """List of IPv4 or IPv6 that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised.
    """

    def __init__(self, hdp_entry_point: str = None,
                 yml_string: str = None,
                 json_string: str = None,
                 online_unrestricted_init: bool = False,
                 safer_zone_hosts: list = None,
                 safer_zone_list: list = None
                 ):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """

        self._online_unrestricted_init = online_unrestricted_init

        if safer_zone_hosts:
            self._safer_zone_hosts = safer_zone_hosts
        if safer_zone_list:
            self._safer_zone_list = safer_zone_list

        if hdp_entry_point:
            self._prepare_from_entry_point(hdp_entry_point)
        if json_string:
            self._prepare_from_json_string(json_string)
        if yml_string:
            self._prepare_from_entry_point(yml_string)

    def _prepare_from_entry_point(self, hdp_entry_point):
        pass

    def _prepare_from_json_string(self, json_string):
        self._hdp_raw = json_string
        self._hdp = json.loads(json_string)

    def _prepare_from_yml_string(self, hdp_yml_string):
        self._hdp_raw = hdp_yml_string
        self._hdp = yaml.safe_load(hdp_yml_string)

    def export_schema_json(self) -> str:
        """Export the current HDP internal metadata in an YAML format

        Returns:
            str: The entire HDP internal metadata
        """
        # TODO: check potential privacy issues with objects that could contain
        #       access credentials. Or maybe we should put such things
        #       in an place outside HDP internal metadata?
        #       (Emerson Rocha, 2021-03-13 01:00 UTC)

        return json.dumps(self._hdp)

    def export_yml(self) -> str:
        """Export the current HDP internal metadata in an YAML format

        Returns:
            str: The entire HDP internal metadata
        """
        # TODO: check potential privacy issues with objects that could contain
        #       access credentials. Or maybe we should put such things
        #       in an place outside HDP internal metadata?
        #       (Emerson Rocha, 2021-03-13 01:00 UTC)

        return yaml.dump(self._hdp, Dumper=Dumper)


class Dumper(yaml.Dumper):
    """Force identation on pylint, https://github.com/yaml/pyyaml/issues/234
    TODO: check on future if this still need
          (Emerson Rocha, 2021-02-28 10:56 UTC)
    """

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
