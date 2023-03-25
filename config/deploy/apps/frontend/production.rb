server ENV['DEPLOY_HOST'], user: ENV['DEPLOY_USERNAME'], roles: %w{app db web}, port: ENV['DEPLOY_PORT']

set :repo_tree, "frontend/"
set :deploy_to, "/home/django/project/BlooBloop/frontend/"
set :branch, "deployment"

after 'deploy:updating', 'npm:build'

namespace :npm do
    desc 'Rebuild VueJS'
    task :build do
        on roles([:app, :web]) do |h|
            execute "cd #{release_path}; npm run build"
        end
    end
end

after 'deploy:publishing', 'nginx:restart'

namespace :nginx do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
            execute :sudo, 'service nginx restart'
        end
    end
end