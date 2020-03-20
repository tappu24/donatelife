"""creating blood stock and user table

Revision ID: f21f29a7d65e
Revises: 
Create Date: 2020-03-16 00:37:35.233857

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from constants.user_constants import *

# revision identifiers, used by Alembic.
revision = 'f21f29a7d65e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blood_stock',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('ab_positive', sa.BigInteger(), nullable=False),
    sa.Column('ab_negative', sa.BigInteger(), nullable=False),
    sa.Column('a_positive', sa.BigInteger(), nullable=False),
    sa.Column('a_negative', sa.BigInteger(), nullable=False),
    sa.Column('b_positive', sa.BigInteger(), nullable=False),
    sa.Column('b_negative', sa.BigInteger(), nullable=False),
    sa.Column('o_positive', sa.BigInteger(), nullable=False),
    sa.Column('o_negative', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blood_stock_a_negative'), 'blood_stock', ['a_negative'], unique=False)
    op.create_index(op.f('ix_blood_stock_a_positive'), 'blood_stock', ['a_positive'], unique=False)
    op.create_index(op.f('ix_blood_stock_ab_negative'), 'blood_stock', ['ab_negative'], unique=False)
    op.create_index(op.f('ix_blood_stock_ab_positive'), 'blood_stock', ['ab_positive'], unique=False)
    op.create_index(op.f('ix_blood_stock_b_negative'), 'blood_stock', ['b_negative'], unique=False)
    op.create_index(op.f('ix_blood_stock_b_positive'), 'blood_stock', ['b_positive'], unique=False)
    op.create_index(op.f('ix_blood_stock_o_negative'), 'blood_stock', ['o_negative'], unique=False)
    op.create_index(op.f('ix_blood_stock_o_positive'), 'blood_stock', ['o_positive'], unique=False)
    op.create_table('life_users',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=65), nullable=False),
    sa.Column('reset_password_code', sa.String(length=255), nullable=True),
    sa.Column('reset_password_expiry', sa.DateTime(), nullable=True),
    sa.Column('blood_group', sqlalchemy_utils.types.choice.ChoiceType(BloodGroup), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('sex', sqlalchemy_utils.types.choice.ChoiceType(UserSex), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('profile_picture_data', sa.JSON(), nullable=True),
    sa.Column('state', sqlalchemy_utils.types.choice.ChoiceType(IndianStates), nullable=False),
    sa.Column('country', sa.String(length=65), nullable=False),
    sa.Column('verification_status', sqlalchemy_utils.types.choice.ChoiceType(UserVerificationStatus), nullable=False),
    sa.Column('verification_code', sa.String(length=255), nullable=True),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(UserStatus), nullable=False),
    sa.Column('blood_requirement_status', sqlalchemy_utils.types.choice.ChoiceType(BloodRequirementStatus), nullable=False),
    sa.Column('required_blood_group', sqlalchemy_utils.types.choice.ChoiceType(BloodGroup), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_life_users_country'), 'life_users', ['country'], unique=False)
    op.create_index(op.f('ix_life_users_created_at'), 'life_users', ['created_at'], unique=False)
    op.create_index(op.f('ix_life_users_last_updated_at'), 'life_users', ['last_updated_at'], unique=False)
    op.create_index(op.f('ix_life_users_reset_password_code'), 'life_users', ['reset_password_code'], unique=False)
    op.create_index(op.f('ix_life_users_state'), 'life_users', ['state'], unique=False)
    op.create_index(op.f('ix_life_users_verification_code'), 'life_users', ['verification_code'], unique=False)
    op.create_table('blood_banks',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('state', sqlalchemy_utils.types.choice.ChoiceType(IndianStates), nullable=False),
    sa.Column('country', sa.String(length=65), nullable=False),
    sa.Column('blood_stock_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['blood_stock_id'], ['blood_stock.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_blood_banks_country'), 'blood_banks', ['country'], unique=False)
    op.create_index(op.f('ix_blood_banks_created_at'), 'blood_banks', ['created_at'], unique=False)
    op.create_index(op.f('ix_blood_banks_last_updated_at'), 'blood_banks', ['last_updated_at'], unique=False)
    op.create_index(op.f('ix_blood_banks_state'), 'blood_banks', ['state'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blood_banks_state'), table_name='blood_banks')
    op.drop_index(op.f('ix_blood_banks_last_updated_at'), table_name='blood_banks')
    op.drop_index(op.f('ix_blood_banks_created_at'), table_name='blood_banks')
    op.drop_index(op.f('ix_blood_banks_country'), table_name='blood_banks')
    op.drop_table('blood_banks')
    op.drop_index(op.f('ix_life_users_verification_code'), table_name='life_users')
    op.drop_index(op.f('ix_life_users_state'), table_name='life_users')
    op.drop_index(op.f('ix_life_users_reset_password_code'), table_name='life_users')
    op.drop_index(op.f('ix_life_users_last_updated_at'), table_name='life_users')
    op.drop_index(op.f('ix_life_users_created_at'), table_name='life_users')
    op.drop_index(op.f('ix_life_users_country'), table_name='life_users')
    op.drop_table('life_users')
    op.drop_index(op.f('ix_blood_stock_o_positive'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_o_negative'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_b_positive'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_b_negative'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_ab_positive'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_ab_negative'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_a_positive'), table_name='blood_stock')
    op.drop_index(op.f('ix_blood_stock_a_negative'), table_name='blood_stock')
    op.drop_table('blood_stock')
    # ### end Alembic commands ###
