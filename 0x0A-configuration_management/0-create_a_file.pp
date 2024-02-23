# This Puppet manifest creates a file named 'school' in the '/tmp' directory with specific permissions and content.
file { '/tmp/school':
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
