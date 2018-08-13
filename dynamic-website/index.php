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

function build_navigation($db) : string
{
    $result = $db->query('SELECT title FROM pages;');
    $html = '| ';
    foreach ($result as $row)
    {
        $html .= '<a href="?page=' . $row['title'] . '">' . $row['title'] . '</a> | ';
    }
    return $html . '<hr>';
}


function main(array $args) : array
{
    chdir('action/src/');

    $db = connect_database();

    $body = file_get_contents('header.html');

    // navigation bar
    $body .= build_navigation($db);

    // page specific content
    $page = $args['page'] ?? 'Homepage';
    $result = get_page($db, $page);
    $body .= '<h2>' . $result['title'] . '</h2>' . $result['content'];

    $body .= file_get_contents('footer.html');

    $db = null;

    return [
        'headers' => ['Content-Type' => 'text/html'],
        'body' => $body
    ];
}
?>
