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

from logging import LoggerAdapter
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status
from oslo_log import log
from sqlalchemy.orm import Session

from dandelion import crud, models, schemas
from dandelion.api import deps

router = APIRouter()
LOG: LoggerAdapter = log.getLogger(__name__)


@router.get(
    "",
    response_model=List[schemas.Area],
    status_code=status.HTTP_200_OK,
    summary="List Areas",
    description="""
Search area by city.
""",
    responses={
        status.HTTP_200_OK: {"model": List[schemas.Area], "description": "OK"},
        status.HTTP_401_UNAUTHORIZED: {
            "model": schemas.ErrorMessage,
            "description": "Unauthorized",
        },
        status.HTTP_403_FORBIDDEN: {"model": schemas.ErrorMessage, "description": "Forbidden"},
        status.HTTP_404_NOT_FOUND: {"model": schemas.ErrorMessage, "description": "Not Found"},
    },
)
def get_all(
    city_code: Optional[str] = Query(None, description="Filter by cityCode", alias="cityCode"),
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> List[schemas.Area]:
    areas = crud.area.get_multi_by_city_code(db, city_code)
    return [area.to_all_dict(need_intersection=True) for area in areas if area.intersections]
