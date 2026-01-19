# Generated from process_executer-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name process_executer

Name: rubygem-%{gem_name}
Version: 4.0.2
Release: %autorelease
Summary: An API for executing commands in a sub process
License: MIT
URL: https://github.com/main-branch/process_executer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# SOURCE1 contains the upstream tag of the project from github
# in particular this includes the spec directory which was not
# included in the gemfile.
Source1: https://github.com/main-branch/%{gem_name}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.0.0
BuildRequires: rubygem(logger)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(track_open_instances)

BuildArch:     noarch

%description
An API for executing commands in a sub process.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
An API for executing commands in a sub process


%prep
%setup -q -n %{gem_name}-%{version}
# From lib/process_executer.rb
%gemspec_add_dep -g logger

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} %{gem_name}-%{version}/spec --strip-components 1

# Skip coverage test formatter, not available and undesirable
sed -i '/# SimpleCov configuration/,/^end/s/.*//'  spec/spec_helper.rb
sed -i '/^SimpleCov::RSpec.start/,/^end/s/.*//' spec/spec_helper.rb


%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
rspec spec


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.markdownlint.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/README.md
%exclude %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.commitlintrc.yml
%exclude %{gem_instdir}/.husky/commit-msg
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/.release-please-manifest.json
%exclude %{gem_instdir}/release-please-config.json
%exclude %{gem_instdir}/process_spawn_test
%{gem_instdir}/process_executer.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc README.md
%doc CHANGELOG.md
%license LICENSE.txt

%files doc
%doc %{gem_docdir}



%changelog
%autochangelog
