%global srcname calcephpy

Name:           python-%{srcname}
Version:        3.5.1
Release:        4%{?dist}
Summary:        Astronomical library to access planetary ephemeris files

License:        CECILL-2.0 OR CECILL-B OR CECILL-C
URL:            https://pypi.python.org/pypi/calcephpy
Source0:        %{pypi_source}


%global _description %{expand:
This is the Python module of calceph.
Calceph is a library designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?rhel} == 7
BuildRequires:  python36-Cython
%else
BuildRequires:  python3-Cython
%endif

# Needed by EPEL7
%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove executable bit set on license files
chmod -x COPYING*

# Remove egg files from source
rm -r %{srcname}.egg-info


%build
%py3_build

# Remove hidden files from docdir
find doc -name .buildinfo -exec rm -f {} \;


%install
%py3_install


%files -n       python3-%{srcname}
%license COPYING_CECILL_V2.1.LIB COPYING_CECILL_B.LIB COPYING_CECILL_C.LIB
%{python3_sitearch}/*.so
%{python3_sitearch}/*egg-info/


%files      doc
%doc doc/calceph_python.pdf doc/html/python/


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.5.1-2
- Rebuilt for Python 3.11

* Wed Mar 02 2022 Mattia Verga <mattia.verga@protonmail.com> - 3.5.1-1
- Update to 3.5.1 (fedora#2059290)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Mattia Verga <mattia.verga@protonmail.com> - 3.5.0-1
- Update to 3.5.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.7-5
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-4
- Patch sources to fix build with Python 3.10a
- Fix rhbz#1948439

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-2
- Create a doc subpackage
- Remove executable bit set on license files
- Add py_provides macro for EPEL7

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-1
- Update to 3.4.7

* Tue Nov 3 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-1
- Initial packaging
