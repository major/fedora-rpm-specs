%global __cmake_in_source_build 1

Summary: Python Integration with Gamerzilla Library
Name: pylibgamerzilla
Version: 0.0.1
Release: 10%{?dist}
License: MIT
URL: https://github.com/dulsi/pylibgamerzilla
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: cmake
BuildRequires: libgamerzilla-devel
BuildRequires: python3-devel

%description
Python interface to the Gamerzilla trophy/achievement system for games.
It allows you display achievements from python games online.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}/%{python3_sitearch}
mkdir -p %{buildroot}/%{python3_sitelib}
cp %{_builddir}/%{name}-%{version}/_gamerzilla.so %{buildroot}/%{python3_sitearch}/
cp %{_builddir}/%{name}-%{version}/gamerzilla.py %{buildroot}/%{python3_sitelib}/

%files
%license LICENSE
%{python3_sitearch}/_gamerzilla.so
%{python3_sitelib}/gamerzilla.py
%{python3_sitelib}/__pycache__/gamerzilla.cpython-%{python3_version_nodots}{,.opt-?}.pyc

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Andy Mender <andymenderunix@gmail.com> - 0.0.1-4
- Enable in-source builds
- Switch RPM_BUILD_ROOT to buildroot macro

* Sat Oct 03 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-3
- Add another missing build requires

* Sat Oct 03 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-2
- Add missing build requires

* Tue Sep 22 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-1
- Initial spec
