Name:           pyhoca-gui
Version:        0.6.1.1
Release:        23%{?dist}
Summary:        Graphical X2Go client written in (wx)Python

License:        AGPL-3.0-or-later
URL:            https://www.x2go.org/
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distutils-extra
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
# Requires are in /usr/bin/pyhoca and not found by dependency generator
Requires:       python%{python3_pkgversion}-cups
Requires:       python%{python3_pkgversion}-setproctitle
Requires:       python%{python3_pkgversion}-x2go >= 0.5.0.0
Requires:       libnotify
Requires:       python%{python3_pkgversion}-gobject-base
Requires:       python%{python3_pkgversion}-wxpython4

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-GUI is a slim X2Go client that docks to the desktop's
notification area and allows multiple X2Go session handling.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
# Fix shebang of pyhoca-gui executable.
%py3_shebang_fix %{name}
%{__python3} setup.py build_i18n
%pyproject_wheel


%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}%{_datadir}/locale
mv %{buildroot}%{python3_sitelib}%{_datadir}/* %{buildroot}%{_datadir}/
%pyproject_save_files -l pyhoca
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang PyHoca-GUI


%files -f PyHoca-GUI.lang -f %{pyproject_files}
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/PyHoca/
%{_datadir}/pixmaps/pyhoca_x2go-logo-ubuntu.svg
%{_datadir}/pyhoca
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/PyHoca_GUI-*-nspkg.pth


%changelog
* Sun Jul 27 2025 Orion Poplawski <orion@nwra.com> - 0.6.1.1-23
- Use pyproject macros (rhbz#2377392)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.6.1.1-21
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.1.1-18
- Rebuilt for Python 3.13

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1.1-17
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.1.1-13
- Rebuilt for Python 3.12

* Sun May 28 2023 Orion Poplawski <orion@nwra.com> - 0.6.1.1-12
- Use %%py3_shebang_fix for Python 3.12 support (bz#2155192)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.1.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.1.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Orion Poplawski <orion@nwra.com> - 0.6.1.1-1
- Update to 0.6.1.1

* Sun Nov 24 2019 Orion Poplawski <orion@nwra.com> - 0.5.1.0-1
- Update to 0.5.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.8-1
- Update to 0.5.0.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.7-5
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.5.0.7-4
- Fix shebangs to avoid depending on Python 2 for Fedora 28+

* Sat Apr 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.7-3
- Require python3-wxpython4

* Sat Apr 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.7-2
- Switch to python 3 for Fedora 28+

* Sat Apr 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.7-1
- Update to 0.5.0.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0.6-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 24 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.6-1
- Update to 0.5.0.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.5-1
- Update to 0.5.0.5
- Drop notify patch fixed upstream

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.4-2
- Use pygobject3 libnotify bindings with wxPython/wxGTK 3

* Mon Jan 26 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.4-1
- Update to 0.5.0.4

* Mon Dec 1 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.3-1
- Update to 0.5.0.3

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.2-1
- Update to 0.5.0.2

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.0-1
- Update to 0.5.0.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.9-2
- No python-cups, use system-config-printer-libs on EL6 (bug #1056434)

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.9-1
- Update to 0.4.0.9
- Add Requires python-cups

* Thu Aug 29 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.8-1
- Update to 0.4.0.8
- Add BR on desktop-file-utils, validate the desktop file
- Add gtk-update-icon-cache scriptlets
- Own /usr/share/pyhoca
- Change tabs to spaces

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.6-1
- Update to 0.4.0.6

* Wed Feb 13 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.1-1
- Update to 0.4.0.1

* Tue Feb 12 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.0-1
- Update to 0.4.0.0

* Tue Dec 18 2012 Orion Poplawski <orion@cora.nwra.com> - 0.2.1.1-1
- Initial Fedora release
