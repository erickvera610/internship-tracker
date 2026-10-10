import sqlite3
from datetime import date

STATUSES=('Saved','Applied','Interview','Offer','Closed')
def connect(path='applications.db'):
    db=sqlite3.connect(path)
    db.row_factory=sqlite3.Row
    db.execute('CREATE TABLE IF NOT EXISTS applications (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, deadline TEXT)')
    return db
def add(db, company, role, status='Saved', deadline=''):
    if not isinstance(company,str) or not isinstance(role,str) or not company.strip() or not role.strip():
        raise ValueError('Company and role are required')
    if status not in STATUSES: raise ValueError('Invalid status')
    if deadline: date.fromisoformat(deadline)
    with db:
        cursor=db.execute('INSERT INTO applications(company,role,status,deadline) VALUES(?,?,?,?)',(company.strip(),role.strip(),status,deadline))
    return cursor.lastrowid
def run(payload):
    with connect() as db:
        if payload.get('company') is not None:
            add(db,payload.get('company'),payload.get('role'),payload.get('status','Saved'),payload.get('deadline',''))
        rows=[dict(r) for r in db.execute('SELECT * FROM applications ORDER BY id DESC')]
    return {'applications':rows,'counts':{s:sum(r['status']==s for r in rows) for s in STATUSES}}
