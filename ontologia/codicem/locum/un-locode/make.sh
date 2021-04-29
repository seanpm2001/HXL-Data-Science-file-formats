#!/bin/sh
#===============================================================================
#
#          FILE:  ontologia/codicem/locum/un-locode/make.sh
#
#         USAGE:  ./ontologia/codicem/locum/un-locode/make.sh
#
#   DESCRIPTION:  Download files from ontologia/codicem/locum/un-locode/
#                 Script based on work from @sabas, from
#  https://github.com/datasets/un-locode/blob/master/scripts/prepare_edition.sh
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - sh
#                 - wget
#                 - unzip
#                 - mdbtools (https://github.com/mdbtools/mdbtools)
#                 - csvkit (https://github.com/wireservice/csvkit)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#                 (Based @sabas Stefano work, github.com/datasets/un-locode)
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2021-04-28 23:18 UTC v1.0 started
#      REVISION:  ---
#===============================================================================

ROOTDIR="$(pwd)"

UNLOCODE_DATE="2020-12"  # https://unece.org/sites/default/files/2020-12/loc202mdb.zip
UNLOCODE_UID="loc202"    # "loc202" on loc202mdb.zip
UNLOCODE_PREFIX="2020-2" # "2020-2" on "2020-2 UNLOCODE CodeList.mdb"

FONTEM_UNLOCODE_MDB_URL="https://unece.org/sites/default/files/${UNLOCODE_DATE}/${UNLOCODE_UID}mdb.zip"
# FONTEM_UNLOCODE_MDB_URL="https://unece.org/sites/default/files/2020-12/loc202mdb.zip"


# @see https://data.humdata.org/dataset/hxl-core-schemas
ONTOLOGIA_CODICEM_LOCUM_UN_LOCODE="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI%2Fpub%3Fgid%3D319251406%26single%3Dtrue%26output%3Dcsv"
# ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_ATTRIBUTE="https://proxy.hxlstandard.org/data.csv?dest=data_view&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI%2Fpub%3Fgid%3D1810309357%26single%3Dtrue%26output%3Dcsv&strip-headers=on"

# # @see https://data.humdata.org/dataset/hxl-master-vocabulary-list
# ONTOLOGIA_CODICEM_HXL_STANDARD_MASTER_VOCABULARY="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1dGPthewm3Dm5_IWBU4buJ370qJBnrVYPL3XbxZ0O-BY%2Fedit%3Fts%3D5a201f69%23gid%3D0"
# # @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/2
# # @see https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=245471857

# ONTOLOGIA_CODICEM_HXL_CPLP_HXL2TAB="https://proxy.hxlstandard.org/data.csv?dest=data_edit&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY%2Fedit%23gid%3D245471857"


# # Download terminologia-anatomica.hxl.csv (ignored by .gitignore)
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_HASHTAG" > "${ROOTDIR}/ontologia/codicem/hxl/standard/core/hashtag.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_CORE_ATTRIBUTE" > "${ROOTDIR}/ontologia/codicem/hxl/standard/core/attribute.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_STANDARD_MASTER_VOCABULARY" > "${ROOTDIR}/ontologia/codicem/hxl/standard/master-vocabulary.hxl.csv"
# wget -qO- "$ONTOLOGIA_CODICEM_HXL_CPLP_HXL2TAB" > "${ROOTDIR}/ontologia/codicem/hxl/cplp/hxl2tab.hxl.csv"


#### Ignore after here ________________________________________________________
# https://github.com/mdbtools/mdbtools
# sudo apt install mdbtools

if [ ! -f "${ROOTDIR}/ontologia/codicem/locum/un-locode/temp/${UNLOCODE_UID}mdb.zip" ]; then
    wget -qO- "$FONTEM_UNLOCODE_MDB_URL" > "${ROOTDIR}/ontologia/codicem/locum/un-locode/temp/${UNLOCODE_UID}mdb.zip"
    unzip "${ROOTDIR}/ontologia/codicem/locum/un-locode/temp/${UNLOCODE_UID}mdb.zip" -d "${ROOTDIR}/ontologia/codicem/locum/un-locode/temp/"
fi
