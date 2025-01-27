# Copyright 2022 99Cloud, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa: F401

from __future__ import annotations

from .algo_module import AlgoModule, AlgoModuleCreate, AlgoModuleUpdate
from .algo_name import (
    AlgoName,
    AlgoNameCreate,
    AlgoNameEdit,
    AlgoNames,
    AlgoNameUpdate,
    AlgoNameUpdateAll,
)
from .algo_version import (
    AlgoVersion,
    AlgoVersionCreate,
    AlgoVersionCreateAll,
    AlgoVersions,
    AlgoVersionUpdate,
)
from .area import Area, AreaCreate, AreaUpdate
from .camera import Camera, CameraCreate, Cameras, CameraUpdate
from .cgw import CGW, CGWCreate, CGWs, CGWUpdate
from .city import City, CityCreate, CityUpdate
from .cloud_home import OnlineRate, RouteInfo, RouteInfoCreate
from .country import Country, CountryCreate, CountryUpdate
from .edge_node import EdgeNode, EdgeNodeCreate, EdgeNodes, EdgeNodeUpdate
from .edge_node_rsu import (
    EdgeNodeRSU,
    EdgeNodeRSUCreate,
    EdgeNodeRSUs,
    EdgeNodeRSUUpdate,
    Location,
)
from .intersection import Intersection, IntersectionCreate, Intersections, IntersectionUpdate
from .lidar import Lidar, LidarCreate, Lidars, LidarUpdate
from .message import ErrorMessage, Message
from .mng import MNG, MNGCopy, MNGCreate, MNGs, MNGUpdate
from .osw import OSW, OSWCreate, OSWs, OSWUpdate
from .province import Province, ProvinceCreate, ProvinceUpdate
from .radar import Radar, RadarCreate, Radars, RadarUpdate
from .rdw import RDW, RDWCreate, RDWs, RDWUpdate
from .rsi_clc import RSICLCCreate, RSICLCs
from .rsi_cwm import RSICWMCreate, RSICWMs
from .rsi_dnp import RSIDNPCreate, RSIDNPs
from .rsi_event import RSIEvent, RSIEventCreate, RSIEvents, RSIEventUpdate
from .rsi_sds import RSISDSCreate, RSISDSs
from .rsm import RSM, RSMCreate, RSMs, RSMUpdate
from .rsm_participant import (
    RSMParticipant,
    RSMParticipantCreate,
    RSMParticipants,
    RSMParticipantUpdate,
)
from .rsu import (
    RSU,
    RSUCreate,
    RSUDetail,
    RSULocation,
    RSURunning,
    RSUs,
    RSUUpdate,
    RSUUpdateWithBaseInfo,
    RSUUpdateWithStatus,
    RSUUpdateWithVersion,
    RunningCPU,
    RunningDisk,
    RunningMEM,
    RunningNet,
)
from .rsu_config import RSUConfig, RSUConfigCreate, RSUConfigs, RSUConfigUpdate, RSUConfigWithRSUs
from .rsu_config_rsu import RSUConfigRSU, RSUConfigRSUCreate, RSUConfigRSUs, RSUConfigRSUUpdate
from .rsu_log import RSULog, RSULogCreate, RSULogs, RSULogUpdate
from .rsu_model import RSUModel, RSUModelCreate, RSUModels, RSUModelUpdate
from .rsu_query import RSUQueries, RSUQuery, RSUQueryCreate, RSUQueryDetail, RSUQueryUpdate
from .rsu_query_result import (
    RSUQueryResult,
    RSUQueryResultCreate,
    RSUQueryResults,
    RSUQueryResultUpdate,
)
from .rsu_query_result_data import RSUQueryResultData, RSUQueryResultDataCreate
from .rsu_tmp import RSUTMP, RSUTMPCreate, RSUTMPs, RSUTMPUpdate
from .spat import Spat, SpatCreate, Spats, SpatUpdate
from .ssw import SSW, SSWCreate, SSWs, SSWUpdate
from .system_config import MQTTConfig, SystemConfig, SystemConfigCreate
from .token import AccessToken, Token, TokenPayload
from .user import User, UserCreate, UserUpdate
