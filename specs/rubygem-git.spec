# Generated from git-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name git

Name: rubygem-%{gem_name}
Version: 2.3.3
Release: %autorelease
Summary: Ruby/Git is a Ruby library that can be used to create, read and manipulate Git repositories by wrapping system calls to the git binary
License: MIT
URL: http://github.com/schacon/ruby-git
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# SOURCE1 contains the upstream tag of the project from github
# in particular this includes the tests and bin directory which was not
# included in the gemfile.
Source1: https://github.com/ruby-git/ruby-git/archive/v%{version}/ruby-git-%{version}.tar.gz


BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9
BuildRequires: rubygem(test-unit)
BuildRequires: git-core
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(rchardet)
BuildRequires: rubygem(process_executer)
BuildRequires: rubygem(addressable)
BuildArch: noarch
Requires:  git-core
%description
Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# unpack only the test files from SOURCE1.
tar zxf %{SOURCE1} ruby-git-%{version}/tests --strip-components 1
tar zxf %{SOURCE1} ruby-git-%{version}/bin --strip-components 1

# Some tests require rubygem-minitar - skip them.
# https://bugzilla.redhat.com/show_bug.cgi?id=2181580
rm -f tests/units/test_archive.rb
sed -i 's/^.*minitar.*//' tests/test_helper.rb
# Requires writing to home directory with a generated gpg key ignore
rm -f tests/units/test_signed_commits.rb


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
# The following polutes home directoy so need to find a better way
# git fails fatally if it cannot guess an email adress
# as is the case inside mock.
git config --global init.defaultBranch main
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
ruby  -Ilib -I. -Itests -e 'Dir.glob "tests/**/*.rb", &method(:require)'


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MAINTAINERS.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/RELEASING.md
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/git.gemspec


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md


%changelog
%autochangelog
