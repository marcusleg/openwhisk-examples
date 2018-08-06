<?php
function main(array $params) : array
{
    $params["absolute_product"] = abs($params["product"]);
    return $params;
}
