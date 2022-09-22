# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Created by pyp2rpm-3.3.2
%global pypi_name pystemd

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        6%{?dist}
Summary:        A thin Cython-based wrapper on top of libsystemd

License:        LGPLv2+
URL:            https://github.com/facebookincubator/pystemd
Source0:        %{url}/releases/download/v.%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(lxml)

%description
This library allows you to talk to systemd over D-Bus from Python,
without actually thinking that you are talking to systemd over D-Bus.

This allows you to programmatically start/stop/restart/kill and verify
service status from systemd point of view, avoiding subprocessing systemctl
and then parsing the output to know the result.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library allows you to talk to systemd over D-Bus from Python,
without actually thinking that you are talking to systemd over D-Bus.

This allows you to programmatically start/stop/restart/kill and verify
service status from systemd point of view, avoiding subprocessing systemctl
and then parsing the output to know the result.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py* %{pypi_name}/*/*.py*

# Remove pregenerated Cython bindings
find . -name \*.c -exec rm '{}' \;

%build
%py3_build

%install
%py3_install

%check
# This test fails in mock because systemd isn't running
rm -f tests/test_daemon.py

export PYTHONPATH=%{buildroot}%{python3_sitearch}
pushd tests
%{__python3} -m unittest discover
popd

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-4
- Drop unnecessary BuildRequires for deprecated package

* Thu Apr 07 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-3
- Add new upstream dependency to BuildRequires

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
- Ensure we always rebuild the Cython bindings (Resolves: rhbz#1900529)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 16:08:15 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.8.0-1
- Update to 0.8.0 (#1891609)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 19:09:25 EDT 2019 Neal Gompa <ngompa13@gmail.com> - 0.6.0-1
- Initial packaging
