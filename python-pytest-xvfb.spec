%global pypi_name pytest-xvfb

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        10%{?dist}
Summary:        A pytest plugin to run Xvfb for tests

License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For tests
BuildRequires:  %{py3_dist pytest} >= 2.8.1
BuildRequires:  %{py3_dist pyvirtualdisplay} >= 1.3
BuildRequires:  xorg-x11-xauth

%global _description %{expand:
With Xvfb and the plugin installed, your testsuite automatically runs with
Xvfb. This allows tests to be run without windows popping up during GUI tests
or on systems without a display (like a CI).

If Xvfb is not installed, the plugin does not run and your tests will still
work as normal. However, a warning message will print to standard output
letting you know that Xvfb is not installed.

If you're currently using xvfb-run in something like .travis.yml, simply remove
it and install this plugin instead - then you'll also have the benefits of Xvfb
locally.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_dist py}
%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm tests/test_xvfb_windows.py

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{pypi_name}
%doc CHANGELOG.rst README.rst
%pycached %{python3_sitelib}/pytest_xvfb.py
%{python3_sitelib}/pytest_xvfb-*.egg-info/

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 2.0.0-1
- Initial package
