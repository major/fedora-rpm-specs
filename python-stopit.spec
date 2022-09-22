%bcond_without tests

%global pypi_name stopit

%global _description %{expand:
Raise asynchronous exceptions in other threads, control the timeout of
blocks or callables with two context managers and two decorators.

This module provides:

* a function that raises an exception in another thread, including the main
thread.
* two context managers that may stop its inner block activity on timeout.
* two decorators that may stop its decorated callables on timeout.}

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        5%{?dist}
Summary:        Timeout control decorator and context managers

License:        MIT
URL:            https://github.com/glenfant/stopit
Source0:        https://github.com/glenfant/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}

Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# License changed from GPLv3 to MIT
# https://github.com/glenfant/stopit/pull/23
sed -i "s/license='GPLv3',/license='MIT',/g" setup.py

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{__python3} tests.py
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 1.1.2-1
- Initial build
