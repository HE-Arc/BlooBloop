server ENV['DEPLOY_HOST'], user: ENV['DEPLOY_USERNAME'], roles: %w{app db web}, port: ENV['DEPLOY_PORT']

set :repo_tree, "api/"
set :deploy_to, "/home/django/project/BlooBloop/api/"
set :branch, "main"

after 'deploy:updating', 'pip:install'

namespace :pip do
    desc 'Install Django'
    task :install do
        on roles([:app, :web]) do |h|
            execute "pip install -r #{release_path}/requirements.txt"
        end
    end
end

after 'pip:install', 'python:migrate'

namespace :python do
    desc "Migrate database"
    task :migrate do
        on roles([:app, :web]) do |h|
            execute "cd #{release_path}; python manage.py migrate"
        end
    end
end

after 'deploy:publishing', 'gunicorn:restart'

namespace :gunicorn do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
            execute :sudo, 'systemctl restart gunicorn'
        end
    end
end

after 'gunicorn:restart', 'gunicorn:websocket'

namespace :gunicorn do
    desc 'Launch asgi server for websocket'
    task :websocket do
        on roles(:web) do |h|
            execute :sudo, 'systemctl restart daphne.service'
        end
    end
end