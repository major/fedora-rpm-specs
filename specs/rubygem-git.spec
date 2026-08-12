# Generated from git-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name git

Name: rubygem-%{gem_name}
Version: 5.0.5
Release: %autorelease
Summary: Ruby/Git is a Ruby library that can be used to manipulate Git repositories
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
BuildRequires: git-core
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(rchardet)
BuildRequires: rubygem(process_executer) >= 4.0.0
BuildRequires: rubygem(addressable)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(rspec)
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
tar zxf %{SOURCE1} ruby-git-%{version}/spec --strip-components 1


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
# The TEST_ENV_NUMBER=1 is just to disable the Fuubar formatter
env TEST_ENV_NUMBER=1 COVERAGE=false rspec -Ilib spec


%files
%dir %{gem_instdir}
%{gem_instdir}/MAINTAINERS.md
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/README.md
%license LICENSE
%exclude %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.dockerignore
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.husky
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/.release-please-config.json
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.yard-lint.yml
%exclude %{gem_instdir}/
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/git.gemspec
%exclude %{gem_instdir}/.commitlintrc.yml
%exclude %{gem_instdir}/.husky/commit-msg
%exclude %{gem_instdir}/.release-please-manifest.json
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/redesign
%exclude %{gem_instdir}/tasks
%exclude %{gem_instdir}/docker



%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/UPGRADING.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/AI_POLICY.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/GOVERNANCE.md


%changelog
%autochangelog
