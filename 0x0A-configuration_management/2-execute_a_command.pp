# Executes a bash command
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
