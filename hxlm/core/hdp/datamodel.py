"""hxlm.core.hdp.datamodel is focused on data model strictly related to HDP

See also:
  - hxlm/core/types.py
  - hxlm/core/htype/

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass, InitVar

from typing import (
    List,
    Tuple,
    Union
)

from hxlm.core.types import (
    EntryPointType,
    ResourceWrapper
)

from hxlm.core.constant import (
    HONTOLOGIA_LKG,
    HONTOLOGIA_VKG
)


@dataclass(init=True, eq=True)
class HDPIndex:
    """An HDP Index object

    Different from most HDP files (that most of the time can reference
    data sets, files, data transformation tasks, etc), HDP index files are
    mostly to be used by people 'building' colletion of HDP files that may be
    in several different places.

    They have a very minimalistic syntax.

    An HDP index file have syntax similar to this:

        # .hdp.yml
        #### Vocabulary Knowledge Graph
        # Notation: ∫, ∬, ∭
        ∫:
          - hxlm/data/core.vkg.yml

        #### Localization Knowledge Graph
        # Notation: ∮, ∯, ∰
        ∮:
          - hxlm/data/core.lkg.yml

        #### HDP Declarative Programming entry points
        # Notation: ∂
        ∂:
          - hxlm/data/hxl/hxl.eng.hdp.yml
          - hxlm/data/udhr/udhr.lat.hdp.yml
    """
    # pylint: disable=invalid-name,non-ascii-name

    resource: ResourceWrapper
    """The ResourceWrapper from this item"""

    hsilos: List['HSiloWrapper']

    # ∂
    hdp: InitVar[list] = []
    """List of HDP indexes files"""

    # ∫
    vkg: InitVar[list] = [
        'file://' + HONTOLOGIA_VKG
    ]
    """List of Vocabulary Knowledge Graph"""

    # ∮, ∯, ∰
    lkg: InitVar[list] = [
        'file://' + HONTOLOGIA_LKG
    ]
    """List of Localization Knowledge Graph"""

    log: InitVar[list] = []
    """Log of messages. Can be used when failed = True or for verbose output"""

    failed: bool = False
    """If something failed"""


@dataclass
class HDPLoadRecursion:
    """Abstraction to internals of hxlm.core.hdp.hazmat hdprecursion_resource
    """
    log: InitVar[list] = []
    """Log of messages (if any)"""


@dataclass
class HDPPolicyLoad:
    """Policies about how resources (like HDP rules or data) are allowed

    Used by hxlm.core.hdp.hazmat to abstract not just what already is cached
    but also what should not be loaded without user request
    """

    # TODO: move the rest of the hxlm.core.model.hdp rules to here and to
    #       hxlm.core.hdp.hazmat (Emerson Rocha, 2021-03-30 17:57 UTC)

    allowed_entrypoint_type: InitVar[Tuple] = [
        EntryPointType.FTP,
        EntryPointType.GIT,
        EntryPointType.HTTP,
        EntryPointType.LOCAL_DIR,  # air-gapped compliant
        EntryPointType.LOCAL_FILE,  # air-gapped compliant
        EntryPointType.NETWORK_DIR,  # air-gapped compliant
        EntryPointType.NETWORK_FILE,  # air-gapped compliant
        EntryPointType.PYDICT,  # air-gapped compliant
        EntryPointType.PYLIST,  # air-gapped compliant
        EntryPointType.SSH,
        EntryPointType.STREAM,
        EntryPointType.STRING,  # air-gapped compliant
        # EntryPointType.UNKNOW,
        EntryPointType.URN  # air-gapped compliant (it's an resolver)
    ]
    """Tuple of EntryPointType"""

    debug_no_restrictions: bool = False
    """Debug Mode. This ask policy checkers to not enforce any other rule"""

    enforce_startup_generic_tests: bool = False
    """If, and only if, implementations could do generic check EVERY time
    an library start, this variable is the way to give a hint.

    The use case is, even if an HDP implementation like this python library
    would try to comply, actually do generic tests like if no network access
    is allowed, try to test if is possible to do HTTP requests and then refuse
    to run until this is fixed.
    """

    custom_allowed_domains: InitVar[Tuple] = ()
    """Allow list of strings that, if an suffix of an domain, are allowed"""

    log: InitVar[list] = []
    """Log of messages (if any)"""

    safer_zones_hosts: InitVar[Tuple] = (
        'localhost'
    )
    """Tuple of hostnames that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised
    """

    safer_zone_list: InitVar[Tuple] = (
        '127.0.0.1',
        '::1'
    )
    """Tuple of IPv4 or IPv6 that even if under restrictions are considered safe
    The name 'safer' does not mean that is 100% safe if an resource on the
    listed item already is compromised.
    """


@dataclass(init=True, eq=True)
class HDPRaw:
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.

    """

    resource: ResourceWrapper
    """The ResourceWrapper from this item"""

    # hsilos: List[dict]
    hsilos: InitVar[List[dict]] = []
    """The list of hsilos"""

    log: InitVar[list] = []
    """Log of messages. Can be used when failed = True or for verbose output"""

    failed: bool = False
    """If something failed"""

    # def about(self, key: str = None):
    #     """Export values"""
    #     about = {
    #         'raw': self.raw,
    #         'hsilos': self.hsilos,
    #     }
    #     if key:
    #         if key in about:
    #             return about[key]
    #         return None
    #     return about


@dataclass
class AttrAdm0:
    """Country/territory"""
    value: str


@dataclass
class AttrDescriptionem:
    """Description with localized key, examples
      descriptionem:
        ARA: "الإعلان العالمي لحقوق الإنسان"
        ENG: Universal Declaration of Human Rights
        FRA: Déclaration universelle des droits de l’homme
    """
    values: dict


@dataclass
class HDatumItem:
    """A Data set group"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]


@dataclass
class HFilumItem:
    """A File"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]


@dataclass
class HTransformareItem:
    """Data transformation"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]
    grupum:  List[str]


@dataclass
class HMetaItem:
    """An individual item in an metadata header reference.
    Like the 'salve mundi!' in the:

    - ([Lingua Latina]):
      - salve mundi!
      - (CRC32 'α "3839021470")
    """

    _type: str  # CRC, raw string, etc

    value_raw: str
    """The raw value"""


@dataclass
class HMetaWrapper:
    """The metadata header reference.

    Like the entire group:

    - ([Lingua Latina]):
      - salve mundi!
      - (CRC32 'α "3839021470")

    Note: the last item of an HMetaWrapper can be another HMetaWrapper!
    """

    values: List[Union[HMetaItem, 'HMetaWrapper']]
    """Ordered list of values"""


@dataclass
class HSiloItem:
    """Individual HSilo (one physical file could have multiple"""


@dataclass
class HSiloWrapper:
    """Individual HSilo (one physical file could have multiple)"""

    hdatum: List[HDatumItem]
    """A list of HDatum (data sets)"""

    hfilum: List[HFilumItem]
    """A list of Hfilum (files)"""

    hsilo: HSiloItem
    """The HSilo representation"""

    htransformare: List[HTransformareItem]
    """Data transformation"""

    source_raw: dict
    """The original source, without any changes"""
