# Load DSL and Setup multiple configurations
# https://github.com/railsware/capistrano-multiconfig
require 'capistrano/multiconfig'

# Includes default deployment tasks
require 'capistrano/deploy'

# Load the SCM plugin appropriate to your project:
#
# require "capistrano/scm/hg"
# install_plugin Capistrano::SCM::Hg
# or
# require "capistrano/scm/svn"
# install_plugin Capistrano::SCM::Svn
# or
require "capistrano/scm/git"
install_plugin Capistrano::SCM::Git

require 'dotenv/load'

# Includes tasks from other gems included in your Gemfile
#
# For documentation on these, see for example:
#
#   https://github.com/capistrano/rvm
#   https://github.com/capistrano/rbenv
#   https://github.com/capistrano/chruby
#   https://github.com/capistrano/bundler
#   https://github.com/capistrano/rails/tree/master/assets
#   https://github.com/capistrano/rails/tree/master/migrations
#   https://github.com/railsware/capistrano-uptodate
#   https://github.com/railsware/capistrano-patch
#   https://github.com/railsware/capistrano-calendar
#
# require 'capistrano/rvm'
# require 'capistrano/rbenv'
# require 'capistrano/chruby'
# require 'capistrano/bundler'
# require 'capistrano/rails/assets'
# require 'capistrano/rails/migrations'
# require 'capistrano/uptodate'
# require 'capistrano/patch'
# require 'capistrano/calendar'

# Loads custom tasks
# Dir.glob('tasks/*.cap').each { |r| import r }

# Load custom tasks from lib/capistrano/tasks if you have any defined
Dir.glob("lib/capistrano/tasks/*.rake").each { |r| import r }

# vim syntax=ruby
