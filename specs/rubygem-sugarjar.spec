# tests won't work until dependent packages are available
%bcond_without tests

%global app_root %{_datadir}/%{name}
%global gem_name sugarjar
%global version 2.0.1

%global common_description %{expand:
Sugarjar is a utility to help making working with git
and GitHub easier. In particular it has a lot of features
to make rebase-based and squash-based workflows simpler.}

Name: rubygem-%{gem_name}
Version: %{version}
Release: 2%{?dist}
Summary: A git/GitHub helper utility
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://www.github.com/jaymzh/sugarjar
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
# git clone https://github.com/jaymzh/sugarjar.git
# version='1.1.0'
# git checkout v${version?}
# tar -cf rubygem-sugarjar-${version?}-specs.tar spec/
Source1: %{name}-%{version}-specs.tar
BuildRequires: rubygems-devel
%if %{with tests}
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(deep_merge)
BuildRequires: rubygem(mixlib-log)
BuildRequires: rubygem(mixlib-shellout)
BuildRequires: gh
BuildRequires: git
%endif
BuildArch: noarch

%description
%{common_description}

%package -n sugarjar
Summary: A git/github helper utility
Requires: ruby(release) >= 3.2
Requires: gh
Requires: git
Requires: git-core
Requires: rubygem(deep_merge)
Requires: rubygem(mixlib-log)
Requires: rubygem(mixlib-shellout)
Requires: rubygem(pastel)
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
# These two specs require a git repo, so we exclude them. Filed a bug
# upstream: https://github.com/jaymzh/sugarjar/issues/194
rm spec/repoconfig_spec.rb
rm spec/commands/feature_spec.rb
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
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 12 2025 Phil Dibowitz <phil@ipom.com> - 2.0.1-1
- New upstream version

* Thu Feb 20 2025 Phil Dibowitz <phil@ipom.com> - 1.1.3-1
- New upstream version

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Phil Dibowitz <phil@ipom.com> - 1.1.2-1
- New upstream version

* Wed Feb 14 2024 Phil Dibowitz <phil@ipom.com> - 1.1.1-2
- Release bump to handle f40 branch snafu

* Mon Feb 12 2024 Phil Dibowitz <phil@ipom.com> - 1.1.1-1
- New upstream version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Phil Dibowitz <phil@ipom.com> - 1.1.0-1
- Update to upstream 1.1.0
- Prefer gh over hub

* Sun Oct 22 2023 Phil Dibowitz <phil@ipom.com> - 1.0.0-1
- Update to upstream 1.0.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Phil Dibowitz <phil@ipom.com> - 0.0.11-1
- Update to upstream 0.0.11

* Tue Aug 23 2022 Phil Dibowitz <phil@ipom.com> - 0.0.10-1
- Update to upstream 0.0.10

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Phil Dibowitz <phil@ipom.com> - 0.0.9-4
- Various specfile cleanups

* Mon Mar 08 2021 Phil Dibowitz <phil@ipom.com> - 0.0.9-3
- Add rspec BuildRequires for tests

* Mon Mar 01 2021 Phil Dibowitz <phil@ipom.com> - 0.0.9-2
- Use global instead of define
- Mark the license as a license
- Re-enable tests now that rubygem-mixlib-log exists

* Sun Feb 28 2021 Phil Dibowitz <phil@ipom.com> - 0.0.9-1
- Initial package
