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

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


# Shared properties
class SpatBase(BaseModel):
    """"""


# Properties to receive via API on creation
class SpatCreate(BaseModel):
    intersection_id: str = Field(..., alias="intersectionId", description="Spat intersection id")
    name: str = Field(..., alias="name", description="Spat Name")
    spat_ip: Optional[str] = Field(None, alias="spatIP", description="Spat IP")
    point: str = Field(..., alias="point", description="Point")
    phase_id: str = Field(..., alias="phaseId", description="PhaseId")
    light: str = Field(..., alias="light", description="Light")
    rsu_id: Optional[int] = Field(None, alias="rsuId", description="RSU ID")
    desc: Optional[str] = Field("", alias="desc", description="Description")
    intersection_code: str = Field(..., alias="intersectionCode", description="Intersection Code")


# Properties to receive via API on update
class SpatUpdate(SpatBase):
    intersection_id: Optional[str] = Field(
        None, alias="intersectionId", description="Spat intersection id"
    )
    name: Optional[str] = Field(None, alias="name", description="Spat Name")
    spat_ip: Optional[str] = Field(None, alias="spatIP", description="Spat IP")
    point: Optional[str] = Field(None, alias="point", description="Point")
    phase_id: Optional[str] = Field(None, alias="phaseId", description="PhaseId")
    light: Optional[str] = Field(None, alias="light", description="Light")
    rsu_id: Optional[int] = Field(None, alias="rsuId", description="RSU ID")
    desc: Optional[str] = Field("", alias="desc", description="Description")
    intersection_code: Optional[str] = Field(
        None, alias="intersectionCode", description="Intersection Code"
    )
    enabled: Optional[bool] = Field(None, alias="enabled", description="Enabled")


class SpatInDBBase(SpatBase):
    id: int = Field(..., alias="id", description="Spat ID")

    class Config:
        orm_mode = True


# Additional properties to return via API
class Spat(SpatInDBBase):
    intersection_id: str = Field(..., alias="intersectionId", description="Spat intersection id")
    name: str = Field(..., alias="name", description="Spat Name")
    spat_ip: Optional[str] = Field(None, alias="spatIP", description="Spat IP")
    point: str = Field(..., alias="point", description="Point")
    online_status: bool = Field(..., alias="onlineStatus", description="Online Status")
    enabled: bool = Field(..., alias="enabled", description="Enabled")
    phase_id: str = Field(..., alias="phaseId", description="PhaseId")
    light: str = Field(..., alias="light", description="Light")
    timing: datetime = Field(..., alias="timing", description="Timing")
    rsu_id: Optional[int] = Field(None, alias="rsuId", description="RSU ID")
    rsu_name: Optional[str] = Field(None, alias="rsuName", description="RSU Name")
    country_code: str = Field(..., alias="countryCode", description="Country Code")
    country_name: str = Field(..., alias="countryName", description="Country Name")
    province_code: str = Field(..., alias="provinceCode", description="Province Code")
    province_name: str = Field(..., alias="provinceName", description="Province Name")
    city_code: str = Field(..., alias="cityCode", description="City Code")
    city_name: str = Field(..., alias="cityName", description="City Name")
    area_code: str = Field(..., alias="areaCode", description="Area Code")
    area_name: str = Field(..., alias="areaName", description="Area Name")
    intersection_code: str = Field(..., alias="intersectionCode", description="Intersection Code")
    intersection_name: str = Field(..., alias="intersectionName", description="Intersection Name")
    desc: str = Field(..., alias="desc", description="Description")
    create_time: datetime = Field(..., alias="createTime", description="Create Time")


class Spats(BaseModel):
    total: int = Field(..., alias="total", description="Total")
    data: List[Spat] = Field(..., alias="data", description="Data")
