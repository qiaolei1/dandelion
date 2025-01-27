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

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from dandelion import crud, models, schemas
from dandelion.api import deps

router = APIRouter()


@router.get(
    "",
    response_model=schemas.EdgeNodeRSUs,
    status_code=status.HTTP_200_OK,
    summary="List Edge Node RSUs",
    description="""
Get all Edge Node RSUs.
""",
    responses={
        status.HTTP_200_OK: {"model": schemas.EdgeNodeRSUs, "description": "OK"},
        status.HTTP_401_UNAUTHORIZED: {
            "model": schemas.ErrorMessage,
            "description": "Unauthorized",
        },
        status.HTTP_403_FORBIDDEN: {"model": schemas.ErrorMessage, "description": "Forbidden"},
        status.HTTP_404_NOT_FOUND: {"model": schemas.ErrorMessage, "description": "Not Found"},
    },
)
def get_all(
    node_id: int = Query(None, alias="nodeId", description=""),
    intersection_code: str = Query(None, alias="intersectionCode", description=""),
    page_num: int = Query(1, alias="pageNum", ge=1, description="Page number"),
    page_size: int = Query(10, alias="pageSize", ge=-1, description="Page size"),
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> schemas.EdgeNodeRSUs:
    skip = page_size * (page_num - 1)
    total, data = crud.edge_node_rsu.get_multi_with_total(
        db,
        skip=skip,
        limit=page_size,
        node_id=node_id,
        intersection_code=intersection_code,
    )
    return schemas.EdgeNodeRSUs(total=total, data=[rsu.to_all_dict() for rsu in data])


@router.put(
    "/{edge_node_id}",
    response_model=schemas.EdgeNodeRSU,
    status_code=status.HTTP_200_OK,
    description="""
Update a RSU.
""",
    responses={
        status.HTTP_200_OK: {"model": schemas.EdgeNodeRSU, "description": "OK"},
        status.HTTP_401_UNAUTHORIZED: {
            "model": schemas.ErrorMessage,
            "description": "Unauthorized",
        },
        status.HTTP_403_FORBIDDEN: {"model": schemas.ErrorMessage, "description": "Forbidden"},
        status.HTTP_404_NOT_FOUND: {"model": schemas.ErrorMessage, "description": "Not Found"},
    },
)
def update(
    edge_node_id: int,
    edge_rsu_in: schemas.EdgeNodeRSUCreate,
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> schemas.EdgeNodeRSU:
    edge_rsu_in_db = crud.edge_node_rsu.get_by_node_id_rsu(
        db=db, edge_node_id=edge_node_id, edge_rsu_id=edge_rsu_in.edge_rsu_id
    )
    edge_rsu_in.edge_node_id = edge_node_id
    location = edge_rsu_in.location
    if location is not None:
        edge_rsu_in.location = schemas.Location()
        edge_rsu_in.location.lon = location.lon
        edge_rsu_in.location.lat = location.lat
    if edge_rsu_in_db:
        edge_rsu_in_db = crud.edge_node_rsu.update(
            db=db, db_obj=edge_rsu_in_db, obj_in=edge_rsu_in.dict()
        )
    else:
        edge_rsu_in_db = crud.edge_node_rsu.create(db=db, obj_in=edge_rsu_in)
    return edge_rsu_in_db.to_all_dict()
