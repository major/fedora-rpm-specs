# tests won't work until dependent packages are available
%bcond_without tests

%global app_root %{_datadir}/%{name}
%global gem_name sugarjar
%global version 3.0.1

%global common_description %{expand:
Sugarjar is a utility to help making working with git and GitHub/GitLab easier.
In particular it has a lot of features to make rebase-based and squash-based
workflows simpler.}

Name: rubygem-%{gem_name}
Version: %{version}
Release: %autorelease
Summary: A git/GitHub helper utility
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://www.github.com/jaymzh/sugarjar
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
# git clone https://github.com/jaymzh/sugarjar.git
# version='1.1.0'
# git checkout v${version?}
# tar -cf ../rubygem-sugarjar/rubygem-sugarjar-${version?}-specs.tar spec/
Source1: %{name}-%{version}-specs.tar
BuildRequires: rubygems-devel
%if %{with tests}
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(deep_merge)
BuildRequires: rubygem(mixlib-log)
BuildRequires: rubygem(mixlib-shellout)
BuildRequires: gh
BuildRequires: git
BuildRequires: glab
%endif
BuildArch: noarch

%description
%{common_description}

%package -n sugarjar
Summary: A git/github helper utility
Requires: ruby(release) >= 3.2
Requires: rubygem(deep_merge)
Requires: rubygem(mixlib-log)
Requires: rubygem(mixlib-shellout)
Requires: rubygem(pastel)
Requires: git
Requires: git-core
Requires: gh
Requires: glab
%description -n sugarjar
%{common_description}

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{bash_completions_dir}
cp -a %{buildroot}%{gem_instdir}/extras/sugarjar_completion.bash %{buildroot}%{bash_completions_dir}/sugarjar_completion.bash

mkdir -p %{buildroot}%{_docdir}/sugarjar/examples
cp -a %{buildroot}/%{gem_instdir}/examples/* %{buildroot}%{_docdir}/sugarjar/examples/
cp -a %{buildroot}/%{gem_instdir}/{README.md,LICENSE,CONTRIBUTING.md,CHANGELOG.md} %{buildroot}%{_docdir}/sugarjar/

%if %{with tests}
%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec .
# https://github.com/jaymzh/sugarjar/issues/236
rm spec/commands/smartclone_spec.rb
rspec spec
%endif

%clean
rm -rf %{buildroot}

%files -n sugarjar
%dir %{gem_instdir}
%{_bindir}/sj
%{gem_instdir}/bin
%dir %{bash_completions_dir}
%{bash_completions_dir}/sugarjar_completion.bash
%license %{gem_instdir}/LICENSE
%doc %{_docdir}/sugarjar/{README.md,LICENSE,CONTRIBUTING.md,CHANGELOG.md}
%doc %{_docdir}/sugarjar/examples/*
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/{Gemfile,sugarjar.gemspec,CHANGELOG.md,README.md,LICENSE,CONTRIBUTING.md}
%exclude %{gem_instdir}/extras
%exclude %{gem_instdir}/examples
# We don't have ri/rdoc in our sources
%exclude %{gem_docdir}
%{gem_spec}

%changelog
%autochangelog
