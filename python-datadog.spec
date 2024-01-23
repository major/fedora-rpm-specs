%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:           python-datadog
Version:        0.44.0
Release:        8%{?dist}
Summary:        Python wrapper for the Datadog API
License:        BSD

URL:            https://github.com/DataDog/datadogpy
Source0:        %{url}/archive/v%{version}/datadogpy-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

BuildArch:      noarch

%description
Datadogpy is a collection of tools suitable for inclusion in existing Python
projects or for development of standalone scripts. It provides an abstraction on
top of Datadog's raw HTTP interface and the Agent's StatsD metrics aggregation
server, to interact with Datadog and efficiently report events and metrics.


%package -n python%{python3_pkgversion}-datadog
Summary:        Python wrapper for the Datadog API

%description -n python%{python3_pkgversion}-datadog
Datadogpy is a collection of tools suitable for inclusion in existing Python
projects or for development of standalone scripts. It provides an abstraction on
top of Datadog's raw HTTP interface and the Agent's StatsD metrics aggregation
server, to interact with Datadog and efficiently report events and metrics.

%generate_buildrequires
%pyproject_buildrequires -wt

%prep
%autosetup -n datadogpy-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files datadog

# Datadog has deprecated this binary name as it conflicts with the sheepdog
# package, but it still gets built right now.
rm %{buildroot}/%{_bindir}/dog{,wrap}

%check
%tox

%files -n python%{python3_pkgversion}-datadog -f %{pyproject_files}
%license LICENSE
%{_bindir}/dogshell
%{_bindir}/dogshellwrap

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.44.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.44.0-3
- Change to pyproject-rpm-macros and fix FTBFS with the latest setuptools
- Enable tests
Resolves: rhbz#2097110

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.44.0-2
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Dalton Miner <daltonminer@gmail.com> - 0.44.0-1
- Update to 0.44.0
- Remove python2/older distribution support

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.23.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Dalton Miner <daltonminer@gmail.com> - 0.23.0-2
- Added a patch to rename binaries that conflicted with sheepdog
* Thu Oct 25 2018 Dalton Miner <daltonminer@gmail.com> - 0.23.0-1
- Initial packaging
