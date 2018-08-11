<?php
function main(array $args) : array
{
    chdir('action/src/');
    $body = file_get_contents('header.html');

    $body .= 'Hello <b>World</b>!';
;
    $body .= file_get_contents('footer.html');
    return ['body' => $body];
}
?>
