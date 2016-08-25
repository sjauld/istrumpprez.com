# Gemfile
ruby '2.3.1'

source 'https://rubygems.org' do

  # For faster file watcher updates on Windows:
  gem 'wdm', '~> 0.1.0', platforms: [:mswin, :mingw]

  # Windows does not come with time zone data
  gem 'tzinfo-data', platforms: [:mswin, :mingw, :jruby]

  # Middleman Gems
  gem 'middleman', '>= 4.0.0'
  gem 'middleman-livereload'

  # # Extra stuff for AWS Support
  # gem 'middleman-aws'
  # gem 'middleman-s3_sync'
  #
  # # waiting for the next release to support middleman 4 ftw
  # gem 'middleman-cloudfront',
  #   git: 'https://github.com/andrusha/middleman-cloudfront.git',
  #   branch: 'master'

  gem 's3_website'

  gem 'mime-types'
end
