<?php
error_reporting  (E_ALL);
ini_set('display_errors', true);
?>
<!doctype html>
<html>
<head><title>hello world</title></head>
<body>
<h1><?php echo 'Hello World!'; ?></h1>
<hr/>
<?php
    $conn = pg_connect("host=localhost dbname=appdb user=dbuser");
    $result = pg_query("SELECT * FROM things");
    $rows = pg_fetch_all($result);
    if($rows) {
        echo '<ul>';
        foreach($rows as $item) {
            echo '<li>' . $item['name'] . '</li>';
        }
        echo '</ul>';
    }
?>
</body>
</html>
