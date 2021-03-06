#!/usr/bin/env python
from flask.ext.script import Manager, prompt_bool
from openedx_webhooks import app
from openedx_webhooks.models import db

manager = Manager(app)


@manager.command
def dbcreate():
    "Creates database tables from SQLAlchemy models"
    db.create_all()
    db.session.commit()


@manager.command
def dbdrop():
    "Drops database tables"
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        db.session.commit()


if __name__ == "__main__":
    manager.run()
