import os
import commands
from webob.static import DirectoryApp

from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from ryu.base import app_manager



PATH = os.path.dirname(__file__)


# Serving static files
class GUIServerApp(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication,
    }

    def __init__(self, *args, **kwargs):
        super(GUIServerApp, self).__init__(*args, **kwargs)

        wsgi = kwargs['wsgi']
        wsgi.register(GUI_P4_ServerController)

class GUI_P4_ServerController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(GUI_P4_ServerController, self).__init__(req, link, data, **config)
        path = "%s/html/network_slice_web" % PATH
        self.static_app = DirectoryApp(path)

    @route('topology', '/{filename:.*}', methods=['GET'])
    def static_handler(self, req, **kwargs):
        if kwargs['filename']:
            if kwargs['filename'] == "ok":
                switches = req.GET['switches']
                hosts = req.GET['hosts']

                switches = req.GET['switches']
                switches = switches.encode('utf-8')
                switches = int(switches)

                hosts = req.GET['hosts']
                hosts = hosts.encode('utf-8')
                hosts = int(hosts)

                linksnum = req.GET['linksnum']
                linksnum = linksnum.encode('utf-8')
                linksnum = int(linksnum)

                links = []

                for i in range(linksnum):
                    links.append(req.GET['links' + (str(i+1))].encode('utf-8'))

                print links

                topo_file = open('topo.txt', 'w')
                topo_file.write('switches ' + str(switches) + '\n')
                topo_file.write('hosts ' + str(hosts) + '\n')
                for i in range(linksnum):
                    topo_file.write(links[i] + '\n')
                topo_file.close()

                print 'switches=%d' % switches
                print "hosts=%d" % hosts
                status, output = commands.getstatusoutput('pwd')
                print "wpq"
                return output
            req.path_info = kwargs['filename']
        return self.static_app(req)



