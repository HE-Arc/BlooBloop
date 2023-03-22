#
# Put here shared configuration shared among all children
#
# Read more about configurations:
# https://github.com/railsware/capistrano-multiconfig/blob/master/README.md

# config valid for current version and patch releases of Capistrano
lock "~> 3.17.2"

set :application, "BlooBloop"
set :repo_url, "https://github.com/HE-Arc/BlooBloop.git"

append :linked_files, '.env'