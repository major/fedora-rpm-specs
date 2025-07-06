# Generated from track_open_instances-0.1.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name track_open_instances

Name: rubygem-%{gem_name}
Version: 0.1.15
Release: %autorelease
Summary: A mix-in to ensure that all instances of a class are closed
License: MIT
URL: https://github.com/main-branch/track_open_instances
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Needed for the spec directory
Source1: https://github.com/main-branch/%{gem_name}/archive/v%{version}/%{gem_name}-%{version}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.1.0
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
A mix-in to track instances of Ruby classes that require explicit cleanup,
helping to identify potential resource leaks. It maintains a list of
created instances and allows checking for any that remain open.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} %{gem_name}-%{version}/spec --strip-components 1

# Skip coverage test formatter, not available and undesirable
sed -i '/# SimpleCov configuration/,/^end/s/.*//'  spec/spec_helper.rb
sed -i '/^SimpleCov::RSpec.start/,/^end/s/.*//' spec/spec_helper.rb

# Not surprising this is needed but odd its not needed when using
# rake.
sed -i '1a require '\''track_open_instances'\''' spec/spec_helper.rb


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
%exclude %{gem_instdir}/.commitlintrc.yml
%exclude %{gem_instdir}/.husky
%exclude %{gem_instdir}/.markdownlint.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.yamllint.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/pre-commit
%exclude %{gem_cache}
%{gem_spec}
%license LICENSE.txt


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.release-please-manifest.json
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/release-please-config.json


%changelog
%autochangelog
