# Created by pyp2rpm-3.3.10
%global pypi_name timelib
%global pypi_version 0.3.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        7%{?dist}
Summary:        Parse english textual date descriptions

License:        Zlib AND PHP-3.01
# Code in ext-date-lib is from PHP, the rest is Zlib.

URL:            https://github.com/pediapress/timelib/
Source0:        %{pypi_source %pypi_name}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildREquires:  python3dist(cython)

%description
timelib is a short wrapper around php's internal timelib module. It currently
only provides a few functions:timelib.strtodatetime:>>>
timelib.strtodatetime("today") datetime.datetime(2009, 6, 23, 0, 0) >>>
timelib.strtodatetime("today") datetime.datetime(2009, 6, 23, 0, 0) >>>
timelib.strtodatetime("next friday") datetime.datetime(2009, 6, 26, 0, 0) >>>
timelib.strtodatetime("29 feb 2008 -108...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
timelib is a short wrapper around php's internal timelib module. It currently
only provides a few functions:timelib.strtodatetime:>>>
timelib.strtodatetime("today") datetime.datetime(2009, 6, 23, 0, 0) >>>
timelib.strtodatetime("today") datetime.datetime(2009, 6, 23, 0, 0) >>>
timelib.strtodatetime("next friday") datetime.datetime(2009, 6, 26, 0, 0) >>>
timelib.strtodatetime("29 feb 2008 -108...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %pypi_name

%check
%pyproject_check_import

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/timelib.cpython*so
%{python3_sitearch}/timelib-%{version}.dist-info

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.0-2
- Review fixes.

* Tue Jan 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.0-1
- Initial package.
