"""create-table-log_city_temp

Revision ID: 27adc71d4834
Revises: 
Create Date: 2020-06-24 21:05:05.223024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27adc71d4834'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('log_city_temp',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
                    sa.Column('city', sa.String(244)),
                    sa.Column('uf', sa.String(244)),
                    sa.Column('temp', sa.Float()),
                    sa.Column('music_gender', sa.String(244)),
                    sa.Column('provider', sa.String(244)),
                    sa.Column('status', sa.String(244)),
                    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.func.now()),
                    sa.Column('weather_response', sa.JSON()),
                    sa.Column('provider_response', sa.JSON())
                    )

def downgrade():
    op.drop_table('log_city_temp')
