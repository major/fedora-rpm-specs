%global pypi_name PyQt-builder
%global srcname PyQt-builder

Name:           %{srcname}
Version:        1.14.1
Release:        1%{?dist}
Summary:        The PEP 517 compliant PyQt build system

License:        GPLv2 or GPLv3
URL:            https://www.riverbankcomputing.com/software/pyqt/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules.Projects that use
PyQt- builder provide an appropriate pyproject.toml file and an optional
project.py.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# These dll files are from openssl and microsoft visiual studio
# While we can redistribute them, we don't have source and it's 
# unlikely anyone will want to bundle a windows executable from linux.
rm -rf %{buildroot}/%{python3_sitelib}/pyqtbuild/bundle/dlls

%check
%py3_check_import pyqtbuild

%files
%license LICENSE-GPL2
%license LICENSE-GPL3
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel
%{python3_sitelib}/pyqtbuild
%{python3_sitelib}/PyQt_builder-%{version}.dist-info

%changelog
* Tue Jan 31 2023 Scott Talbert <swt@techie.net> - 1.14.1-1
- Update to new upstream release 1.14.1 (#2131649)
- Modernize python packaging

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Scott Talbert <swt@techie.net> - 1.13.0-1
- Update to new upstream release 1.13.0 (#2098289)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.12.2-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Scott Talbert <swt@techie.net> - 1.12.2-1
- Update to new upstream release 1.12.2 (#2018190)

* Tue Oct 12 2021 Scott Talbert <swt@techie.net> - 1.12.1-1
- Update to new upstream release 1.12.1 (#2013246)

* Mon Oct 04 2021 Scott Talbert <swt@techie.net> - 1.11.0-1
- Update to new upstream release (#2010060)

* Fri Sep 24 2021 Scott Talbert <swt@techie.net> - 1.10.3-2
- Fix license info (#2007385)

* Wed Jul 21 2021 Scott Talbert <swt@techie.net> - 1.10.3-1
- Update to new upstream release 1.10.3 (#1984602)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.10

* Mon May 24 2021 Scott Talbert <swt@techie.net> - 1.10.0-1
- Update to latest upstream release; remove hard-code on sip5

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Kevin Fenzi <kevin@scrye.com> - 1.6.0-2
- Remove shipped dlls.

* Tue Dec 15 2020 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Initial package.
