


### Gör så:
		in  .flaskenv ==> DATABASE_URL= postgresql://user:password@server/dbname
		  remove all the files from /migrations/versions/ (leave the empty directory, do not remove it),
 			drop(or simply remove) the SQLite file (app.db)
    			then in terminal run:  flask db migrate
    			and then:  flask db upgrade<<<<<<<####

### install requirements:

		pip install -r requirements.txt