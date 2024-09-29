"# IoT Experimental para cultivo protegido. / Экспериментальная система IoT для защищенного земледелия." 

Texto en español y en ruso / Текст на испанском и русском языках 


Proyecto IoT experimental para agricultura inteligente utilizando una placa de desarrollo Raspberry Pi Pico, sensores y actuadores, bajo lenguaje de programación MicroPython.

Este realiza la función es la medición de la temperatura ambiente, humedad relativa, presión atmosférica, intensidad de la luz, además de la temperatura y la humedad del suelo. Estos seis datos son enviados a través de un pequeño servidor web configurado dentro del propio microcontrolador y enviados a una red Wifi utilizando el módulo ESP-01. Estos datos pueden visualizarse en un navegador web en cualquier dispositivo electrónico que cuente con un navegador y una conexión wifi. lo que permite el control de estas variables agroclimáticas para la toma oportuna de decisiones.

Además de la visualización de los datos en tiempo real, permite la activación de riego automático por medio de la activación de relés, que se activan tras recibir información del sensor de humedad del suelo. Otra de las funciones incorporadas son los sensores PIR para la detección de movimientos, permitiendo la activación de alarmas o luces. 

Este pequeño proyecto fue parte de la exposición de tesis de maestría, donde recibió un cálido recibimiento por parte del tribunal.

Экспериментальный IoT-проект для умного сельского хозяйства с использованием платы разработки Raspberry Pi Pico, датчиков и исполнительных устройств, под управлением языка программирования MicroPython.

Она выполняет функцию измерения температуры окружающей среды, относительной влажности, атмосферного давления, интенсивности освещения, а также температуры и влажности почвы. Эти шесть данных отправляются через небольшой веб-сервер, сконфигурированный в самом микроконтроллере, и передаются в сеть Wifi с помощью модуля ESP-01. Эти данные можно просматривать в веб-браузере на любом электронном устройстве, имеющем браузер и подключение к сети Wi-Fi, что позволяет отслеживать эти агроклиматические переменные для своевременного принятия решений.

Помимо визуализации данных в режиме реального времени, система позволяет активировать автоматический полив с помощью реле, которые срабатывают после получения информации от датчика влажности почвы. Еще одной функцией являются PIR-датчики для обнаружения движения, позволяющие активировать сигнализацию или освещение. 

Этот небольшой проект стал частью выставки магистерской диссертации, где был тепло принят трибуналом.
