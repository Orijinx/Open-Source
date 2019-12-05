
function WindowOnLoad() {
    var iWidth = 800, iHeight = 500; // Размер окна

    // Изменение размера окна и его центрирование
    var iLeft = (screen.availWidth - iWidth) / 2;
    var iTop = (screen.availHeight - iHeight) / 2;
    focus();
    resizeTo(iWidth, iHeight);
    moveTo(iLeft, iTop);
    // Вывод версии приложения на форму
    Version_Div.innerHTML = "Версия: " + oHTA.Version;
}

var attributes = ["id", "",
    "applicationName", "",
    "border", "Thick",
    "borderStyle", "Normal",
    "caption", "Yes",
    "commandLine", "Yes",
    "contextMenu", "",
    "icon", "",
    "innerBorder", "Yes",
    "maximizeButton", "Yes",
    "minimizeButton", "Yes",
    "navigable", "No",
    "scroll", "Yes",
    "scrollFlat", "No",
    "selection", "Yes",
    "showInTaskBar", "Yes",
    "singleInstance", "No",
    "sysMenu", "Yes",
    "version", "",
    "windowState", "Normal"];


function RunApplication(sApplication) {
    var sCommandLine = "";
    var oShell = new ActiveXObject("WScript.Shell");
    switch (sApplication) {
        case "CommandPrompt":
            sCommandLine = "%ComSpec%";
            DynamicContent_Div.innerHTML = "Командная строка открыта";
            break;
        case "TestScript":
            if (CheckFile(oShell.CurrentDirectory + "\\MyHTA_files\\Test.js")) {
                sCommandLine = 'WScript "' + oShell.CurrentDirectory + '\\MyHTA_files\\Test.js"';
                DynamicContent_Div.innerHTML = "Скрипт " + oShell.CurrentDirectory +
                    "\MyHTA_files\Test.js" + " выполнен";
            }
            else DynamicContent_Div.innerHTML = "Файл не найден";
            break;
        case "TextFile":
            if (CheckFile(oShell.CurrentDirectory + "\\MyHTA_files\\Test.txt")) {
            DynamicContent_Div.innerHTML = "<div>Выберите режим отображения содержимого файла:<ul>" +
                '<li class="NormalLink" id="TextFile_Notepad" onclick="RunApplication(this.id)">Открыть файл в блокноте</li>' +
                '<li class="NormalLink" id="TextFile_Form" onclick="RunApplication(this.id)">Отобразить здесь<~¡R0¡~div>';
            }
            else DynamicContent_Div.innerHTML = "Файл не найден";
            break;
        case "TextFile_Form":
            DynamicContent_Div.innerHTML = '<div style="float: left; font-size: 10pt;">Текстовый файл: ' +
                oShell.CurrentDirectory + '\\MyHTA_files\\Test.txt</div>' +
                '<div class="NormalLink" style="float: right;" id="TextFile_Close" onclick="RunApplication(this.id)">Закрыть</div>' +
                '<pre class="TextFile">' +
                ReadFile(oShell.CurrentDirectory + "\\MyHTA_files\\Test.txt") +
                "</pre>";
            break;
        case "TextFile_Notepad":
            sCommandLine = 'Notepad "' + oShell.CurrentDirectory + '\\MyHTA_files\\Test.txt"';
            DynamicContent_Div.innerHTML = "Файл " + oShell.CurrentDirectory + "\\MyHTA_files\\Test.txt" + " открыт в блокноте";
            break;
        case "TextFile_Close":
            DynamicContent_Div.innerHTML = "Добро пожаловать";
            break;
        case "TempDir":
            sCommandLine = "Explorer " + oShell.ExpandEnvironmentStrings("%Temp%");
            DynamicContent_Div.innerHTML = "Папка временных файлов открыта";
            break;
        case "Attributes":
            var s = '<b>Атрибуты ( Свойства )</b><div class="attr">';
            for (var i = 0; i < attributes.length; i += 2)
                s += '<i>' + attributes[i] + '</i> = <span>' +
                    (oHTA[attributes[i]] || attributes[i + 1]) + '<~¡R1¡~>';
            DynamicContent_Div.innerHTML = s + '</div>';
            break;
        case "default":
            sCommandLine = "";
            break;
    }
    if (sCommandLine.length > 0) oShell.Run(sCommandLine, 1, 0);
}

function ReadFile(sFileName) {
    var oFSO = new ActiveXObject("Scripting.FileSystemObject");
    var oInFile = oFSO.OpenTextFile(sFileName, 1, false, 0)
    var sFileContent = oInFile.ReadAll();
    oInFile.Close();
    return sFileContent;
}

function CheckFile(sFilePath) {
    var oFSO = new ActiveXObject("Scripting.FileSystemObject")
    return oFSO.FileExists(sFilePath) ? true : false;
}