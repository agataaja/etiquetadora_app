from view.Register_Form import Register_Form
from connection.db import DB
from controller.services.log import Log

if __name__ == '__main__':
    Log().printLog("Iniciando a aplicação...Aguarde..")
    DB().create_conn()
    form = Register_Form()