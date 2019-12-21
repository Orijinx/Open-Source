navigator.geolocation.getCurrentPosition(

    // Функция обратного вызова при успешном извлечении локации
    function(position) {

        /*
        В объекте position изложена подробная информация
        о позиции устройства:

        position = {
            coords: {
                latitude - Широта.
                longitude - Долгота.
                altitude - Высота в метрах над уровнем моря.
                accuracy - Погрешность в метрах.
                altitudeAccuracy - Погрешность высоты над уровнем моря в метрах.
                heading - Направление устройства по отношению к северу.
                speed - Скорость в метрах в секунду.
            }
            timestamp - Время извлечения информации.
        }
        */

    },

    // Функция обратного вызова при неуспешном извлечении локации
    function(error){

        /*
        При неудаче, будет доступен объект error:

        error = {
            code - Тип ошибки
                    1 - PERMISSION_DENIED
                    2 - POSITION_UNAVAILABLE
                    3 - TIMEOUT

            message - Детальная информация.
        }
        */

    }
);