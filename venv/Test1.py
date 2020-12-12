#esta libreria es para correr el archivo como unit test
#sin embargo en este ejemplo no lo utlizo
import unittest

#Esto importa la libreria webdriver que se encarga de manejar los elementos de la automatizacion
from appium import webdriver

#variable/diccionario que tendra las desired capibilities
#estos valores tendran la informacion de la plataforma o entorno donde se estara
#ejecutando la prueba, puede ser un emulador o un dispositivo fisico
desired_caps= dict(
    platformName='Android',
    platformVersion='9',
    automationName='uiautomator2',
    deviceName='159cd09e',
    app='c:\\debug.apk'
)


#Instanciando el controlador
#se hace uso del paquete webdriver para iniciar la conexion con el servidor
#que iniciara la aplicacion en el dispositivo o emulador
#como otro parametro se pasan las desired capibilities
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#Elementos de la Activity Login
campoNombre = driver.find_element_by_id("com.example.firsttest:id/nameField")
campoPassword = driver.find_element_by_id("com.example.firsttest:id/passwordField")
botonLogin = driver.find_element_by_class_name("android.widget.Button")

#Enviando Valores
campoNombre.send_keys("Angel")
campoPassword.send_keys("Jocelyne")
botonLogin.click()