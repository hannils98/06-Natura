
This is the db url to connect postgres==>  postgresql://username:password@server/dbname

Just to have a backup I pasted it here ==> SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')


in .flaskenv ==> DATABASE_URL= postgresql://:password@server/dbname