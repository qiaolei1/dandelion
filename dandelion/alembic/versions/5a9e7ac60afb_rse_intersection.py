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

# flake8: noqa
# fmt: off

"""rse_intersection

Revision ID: 5a9e7ac60afb
Revises: 8faa111d9e82
Create Date: 2022-12-05 16:22:40.397410

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5a9e7ac60afb"
down_revision = "8faa111d9e82"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("camera", sa.Column("intersection_code", sa.String(length=64), nullable=False))
    op.create_foreign_key(
        "camera_fk_intersection_code", "camera", "intersection", ["intersection_code"], ["code"],
        onupdate='CASCADE', ondelete='RESTRICT'
    )
    op.add_column("radar", sa.Column("intersection_code", sa.String(length=64), nullable=False))
    op.create_foreign_key(
        "radar_fk_intersection_code", "radar", "intersection", ["intersection_code"], ["code"],
        onupdate='CASCADE', ondelete='RESTRICT'
    )
    op.add_column("spat", sa.Column("intersection_code", sa.String(length=64), nullable=False))
    op.create_foreign_key(
        "spat_fk_intersection_code", "spat", "intersection", ["intersection_code"], ["code"],
        onupdate='CASCADE', ondelete='RESTRICT'
    )
    op.add_column("lidar", sa.Column("intersection_code", sa.String(length=64), nullable=False))
    op.create_foreign_key(
        "lidar_fk_intersection_code", "lidar", "intersection", ["intersection_code"], ["code"],
        onupdate='CASCADE', ondelete='RESTRICT'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("spat_fk_intersection_code", "spat", type_="foreignkey")
    op.drop_column("spat", "intersection_code")
    op.drop_constraint("radar_fk_intersection_code", "radar", type_="foreignkey")
    op.drop_column("radar", "intersection_code")
    op.drop_constraint("camera_fk_intersection_code", "camera", type_="foreignkey")
    op.drop_column("camera", "intersection_code")
    op.drop_constraint("lidar_fk_intersection_code", "lidar", type_="foreignkey")
    op.drop_column("lidar", "intersection_code")
    # ### end Alembic commands ###
