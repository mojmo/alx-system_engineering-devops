# Replaces problematic 'phpp' extensions with 'php' in the WordPress file 'wp-settings.php'.

exec { 'fix-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}

