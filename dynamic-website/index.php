<?php
function connect_database()
{
    $db = new PDO('sqlite:database.sqlite');
    $result = $db->query('SELECT * FROM pages');
    return $db;
}

function get_page($db, $page)
{
    $query = $db->prepare('SELECT title,content FROM pages WHERE title LIKE :title LIMIT 1;');
    $query->bindParam(':title', $page);
    $query->execute();
    return $query->fetch();
}


function main(array $args) : array
{
    chdir('action/src/');

    $db = connect_database();

    $body = file_get_contents('header.html');

    $page = $args['page'] ?? 'Homepage';
    $result = get_page($db, $page);
    $body .= '<h2>' . $result['title'] . '</h2>' . $result['content'];

    $body .= file_get_contents('footer.html');

    $db = null;

    return ['body' => $body];
}
?>
