# Generated from process_executer-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name process_executer

Name: rubygem-%{gem_name}
Version: 1.2.0
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
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)

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

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} %{gem_name}-%{version}/spec --strip-components 1

# Skip coverage test formatter, not available
sed -i "s/require 'simplecov-lcov'//" spec/spec_helper.rb
sed -i "s/require 'simplecov-rspec'//" spec/spec_helper.rb
sed -i "s/, SimpleCov::Formatter::LcovFormatter//" spec/spec_helper.rb
sed -i "s/\s*SimpleCov::.*$//" spec/spec_helper.rb


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
%exclude %{gem_instdir}/.tool-versions
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.commitlintrc.yml
%exclude %{gem_instdir}/.husky/commit-msg
%exclude %{gem_instdir}/package.json

%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/process_executer.gemspec


%changelog
%autochangelog
