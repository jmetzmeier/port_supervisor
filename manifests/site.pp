class { 'apache': }
class { 'redis':
  redis_bind_address => '0.0.0.0',
}

