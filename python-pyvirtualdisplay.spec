%global pypi_name PyVirtualDisplay
%global dist_name %{py_dist_name %{pypi_name}}

Name:           python-%{dist_name}
Version:        2.2
Release:        6%{?dist}
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc

License:        BSD
URL:            https://github.com/ponty/PyVirtualDisplay
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For Tests
BuildRequires:  %{py3_dist EasyProcess}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-server-Xvfb

%global _description %{expand:
pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc}

%description %_description

%package -n     python3-%{dist_name}
Summary:        %{summary}

Requires:       %{py3_dist py}
Requires:       xorg-x11-server-Xvfb
%description -n python3-%{dist_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{dist_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dist_name}/

%changelog
* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Scott Talbert <swt@techie.net> - 2.2-1
- Update to new upstream release 2.2 to fix FTBFS (#1987889)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 2.1-1
- Initial package
