db.auth('admin', 'admin')

db = db.getSiblingDB('test-database')

db.createUser({
  user: 'user',
  pwd: 'user',
  roles: [
    {
      role: 'root',
      db: 'test-database',
    },
  ],
});
