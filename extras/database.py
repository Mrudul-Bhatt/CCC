#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
sub=data.getvalue('submit')
n=data.getvalue('name')
sn=data.getvalue('studentno')
e=data.getvalue('email')
m=data.getvalue('mobileno')
b=data.getvalue('branch')
y=data.getvalue('year')
h=data.getvalue('a')
con=MySQLdb.connect("127.0.0.1","root","","ccccloud",3306)
query="INSERT INTO registration(name,studentno,email,mobileno,branch,year,hosteler) values('"+n+"','"+sn+"','"+e+"','"+m+"','"+b+"','"+y+"','"+h+"')"

cur=con.cursor()

			

if query and sub:
	print """
	<script> 
	    window.location.href='index.html'
		window.alert('YOU ARE SUCCESSFULLY REGISTERED')
		
	</script>
	"""
cur.execute(query)
con.commit()
con.close()
