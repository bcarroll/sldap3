import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import logging
from multiprocessing import Process
from sys import exit, path

logging.basicConfig(
    filename='c:\\Temp\\sldap3.log',
    level=logging.DEBUG,
    format='[sldap3-service] %(levelname)-7.7s %(message)s'
)

logging.info('start log')
try:
    path.append('C:\\Python\\OpenSource\\sldap3')
    from sldap3 import JsonUserBackend, Dsa, Instance
except ImportError:
    logging.error('PATH: ' + str(path))
    logging.error('sldap3 package missing')
    exit(1)


class Sldap3Service (win32serviceutil.ServiceFramework):
    _svc_name_ = 'sldap3'
    _svc_display_name_ = 'sldap3 - LDAP Server'

    def __init__(self,args):
        logging.info('Initializing class...')

        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False
        self.instances = list()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        logging.info('Stopping service...')
        for instance in self.instances:
            instance.stop()

    def SvcDoRun(self):
        logging.info('Starting service...')
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        logging.info('Executing service...')

        user_backend = JsonUserBackend('localhost-users.json')
        user_backend.add_user('giovanni', 'admin', 'password')
        user_backend.add_user('beatrice', 'user', 'password')
        user_backend.store()

        dsa1 = Instance(Dsa('DSA1', 'localhost', cert_file='server-cert.pem', key_file='server-key.pem', user_backend=user_backend))
        dsa2 = Instance(Dsa('DSA2', 'localhost', port=1389, user_backend=user_backend))

        self.instances.append(dsa1)
        self.instances.append(dsa2)

        if len(self.instances) > 1:  # start each process in a new thread
            for instance in self.instances:
                instance.process = Process(target=instance.dsa.start)
                instance.process.start()
        elif len(self.instances) == 1:  # use the same thread
            self.instances[0].dsa.start()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Sldap3Service)