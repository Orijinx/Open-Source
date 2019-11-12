<?php
$them="Them:".$_GET['them'];
$to='&to='.$_GET['gr'].$them;
$txt='&text='.$_GET['msg'];
$body='http://sms.ru/sms/send?api_id=9FF5D0FE-F09E-87BF-026F-DBA8E892B27C';
$sms=file_get_contents($body.$to.$txt);
echo $body.$to.$txt;
?>