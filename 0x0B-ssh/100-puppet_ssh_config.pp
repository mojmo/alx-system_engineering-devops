# Puppet manifest to configure SSH client settings

file_line { 'Turn off passwd auth':
    ensure  => 'present',
    path    => '~/.ssh/config',
    line    => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
    ensure  => 'present',
    path    => '~/.ssh/config',
    line    => '    IdentityFile ~/.ssh/school',
}
