from os.path import isfile
from sqlite3 import connect

from apscheduler.triggers.cron import CronTrigger

DB_PATH = "./data/db/database.db" #
BUILD_PATH = "./data/db/build.sql" # 

cxn = connect(DB_PATH, check_same_thread=False) # Sqlite3 connection
cur = cxn.cursor() # Sqlite3 cursor

def with_commit(func):
	"""
	Summary line
  
        Parameters: 
            fun ():

        TODO:
        	* Do the doctring
	"""
	def inner(*args, **kwargs):
		"""
		Summary line
	  
	        Parameters: 
		        *args: Variable length argument list.
		        **kwargs: Arbitrary keyword arguments.

	        TODO:
	        	* Do the doctring
		"""
		func(*args, **kwargs)
		commit()

	return inner


@with_commit
def build():
	"""
	Build a database with the path var (BUILD_PATH)
	"""
	if isfile(BUILD_PATH):
		scriptexec(BUILD_PATH)


def commit():
	"""
	Commit the database change
	"""
	cxn.commit()


def autosave(sched):
	"""
	Summary line
	  
        Parameters: 
	        sched (): 

        TODO:
        	* Do the doctring
	"""
	sched.add_job(commit, CronTrigger(second=0))

def close():
	"""
	Close the sqlite3 connection
	"""
	cxn.close()


def field(command, *values):
	"""
	Summary line
  
        Parameters: 
            command ():
            *values ():
          
        Returns: 
            fetchone()[0]:

        TODO:
        	* Do the doctring
	"""
	cur.execute(command, tuple(values))

	if (fetch := cur.fetchone()) is not None:
		return fetch[0]


def record(command, *values):
	"""
	Summary line
  
        Parameters: 
            command ():
            *values: Variable length values list.
          
        Returns: 
            fetchone():

        TODO:
        	* Do the doctring
        
	"""
	cur.execute(command, tuple(values))

	return cur.fetchone()

def records(command, *values):
	"""
	Summary line
  
        Parameters: 
            command ():
            *values: Variable length values list.
          
        Returns: 
            fetchall():

        TODO:
        	* Do the doctring
        
	"""
	cur.execute(command, tuple(values))

	return cur.fetchall()

def column(command, *values):
	"""
	Summary line
  
        Parameters: 
            command ():
            *values: Variable length values list.
          
        Returns: 

        TODO:
        	* Do the doctring
	"""
	cur.execute(command, tuple(values))

	return [item[0] for item in cur.fetchall()]


def execute(command, *values):
	"""
	Summary line 
  
        Parameters: 
            command ():
            *values: Variable length values list.

        TODO:
        	* Do the doctring
	"""
	cur.execute(command, tuple(values))


def multiexec(command, valueset):
	"""
	Summary line
  
        Parameters: 
   	        command  ():
	        valueset ():

        TODO:
        	* Do the doctring
	"""
	cur.executemany(command, valueset)


def scriptexec(path):
	"""
	Summary line
  
        Parameters: 
	        path ():

        TODO:
        	* Do the doctring
	"""
	with open(path, "r", encoding="utf-8") as script:
		cur.executescript(script.read())