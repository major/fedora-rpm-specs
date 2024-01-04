%global module_name erfa
%global pypi_name pyerfa
# tests need pytest-astropy, needs astropy, needs pyerfa
%bcond_without tests

Name:           python-pyerfa
Version:        2.0.1.1
Release:        1%{?dist}
Summary:        Python wrapper for the ERFA library
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
Source0:        %{pypi_source}

# Python BuildRequires
BuildRequires:  python3-devel
BuildRequires:  erfa-devel
BuildRequires:  gcc


%description
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
# Build using system liberfa, not bundled one
export PYERFA_USE_SYSTEM_LIBERFA=1 
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
%if %{with tests}
%{tox}
%else
%py3_check_import %{module_name}
%endif

%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.rst
%doc AUTHORS.rst CHANGES.rst README.rst


%changelog
* Tue Jan 02 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.1.1-1
- new version
- using SPDX license name

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.0.0.3-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0.3-2
- Bootstrap for Python 3.12

* Mon Mar 27 2023 Christian Dersch <lupinix@fedoraproject.org> - 2.0.0.3-1
- new version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.0.0.1-4
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.0.0.1-3
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Christian Dersch <lupinix@fedoraproject.org> - 2.0.0.1-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Christian Dersch <lupinix@mailbox.org> - 2.0.0-1
- new version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 11:37:40 CET 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.7.1.1-1
- initial package (Review: RHBZ #1898135)
