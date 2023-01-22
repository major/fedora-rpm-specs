%bcond_without tests

%global pypi_name ratelimiter
%global extraver post0

%global _description %{expand:
This package provides the ratelimiter module, which ensures that an operation
will not be executed more than a given number of times on a given period. This
can prove useful when working with third parties APIs which require for example
a maximum of 10 requests per second.}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        10.%{extraver}%{?dist}
Summary:        Python module providing rate limiting

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name} %{version}.%{extraver}}
BuildArch:      noarch

# Fix warning that coroutine decorator is deprecated since Python 3.8
# https://github.com/RazerM/ratelimiter/issues/10
#
# async w/ python 3.8 compatibility sans warnings #11
# https://github.com/RazerM/ratelimiter/pull/11
# (only the fix, not the version number and metadata adjustments)
#
# Fixes Python 3.11 compatibility.
Patch0:         pr-11-minimal.patch
# Fix pytest 7.x compatibility
# https://github.com/RazerM/ratelimiter/pull/13
Patch1:         https://github.com/RazerM/ratelimiter/pull/13.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        Python module providing rate limiting
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}.%{extraver} -p1

rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH="%{buildroot}/%{python3_sitelib}/" pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}.%{extraver}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-8.post0
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.0-7.post0
- Fix pytest 7.x compatibility (fix RHBZ#2059969)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.0-5.post0
- Fix Python 3.11 compatibility (close RHBZ#2019853)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-3.post0
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2.post0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.2.0-1.post1
- Initial build
