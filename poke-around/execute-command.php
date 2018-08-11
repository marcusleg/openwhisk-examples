<?php
function main(array $args) : array
{
    $output = shell_exec($args['cmd']);
    return ['output' => $output];
}
?>
