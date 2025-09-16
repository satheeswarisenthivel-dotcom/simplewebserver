from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title> TABLE</title>
    </head>
    <body>
        <table border="3" cellpadding="30" cellspacing ="10">
            <tr >
                <th bgcolor="red"><h1>s.no</h1></th>        
                <th bgcolor="purple"><h1>Drive specifications(satheeswari)</h1></th>
                <th bgcolor="purple"><h1>Type</h1></th>
            </tr> 
            <tr>
                <td>1.</td>
                <td>device name</td>
                <td>12th Gen Intel(R) Core(TM) i5-1235U (1.30 GHz)</td>
            </tr>
            <tr>
                    <td>2.</td>
                    <td>installed RAM</td>
                    <td>8.00 GB (7.69 GB usable)</td>
                
            </tr>
            <tr>
                <td>3.</td>
                <td>device ID</td>
                <td>F63C9C87-93AD-49E2-B84D-49EC936F89B6</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>product ID</td>
                <td>00356-24616-85662-AAOEM</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>syatem type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
        </table>    
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()