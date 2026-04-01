"""setup postgres triggers

Revision ID: 81e40f002800
Revises: 
Create Date: 2026-04-01 23:14:27.845677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81e40f002800'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(current_dir, '../triggers.sql')
    
    with open(sql_file_path, 'r') as file:
        sql_commands = file.read()
        
    op.execute(sql_commands)


def downgrade():
    op.execute('DROP TRIGGER IF EXISTS reset_and_check_leaves ON "leave";')
    op.execute('DROP TRIGGER IF EXISTS increment_leave_counts ON "leave";')
    op.execute('DROP TRIGGER IF EXISTS cleanup_old_leaves ON "leave";')
    
    op.execute('DROP FUNCTION IF EXISTS reset_and_check_leaves_fn();')
    op.execute('DROP FUNCTION IF EXISTS increment_leave_counts_fn();')
    op.execute('DROP FUNCTION IF EXISTS cleanup_old_leaves_fn();')
