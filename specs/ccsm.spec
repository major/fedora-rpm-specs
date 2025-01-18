%global basever 0.8.16

Name:           ccsm
Version:        0.8.18
Release:        17%{?dist}
Epoch:          1
Summary:        Plugin and configuration tool - Compiz Reloaded Project

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gobject-introspection-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool

Requires:       compizconfig-python >= %{version}
Requires:       libcompizconfig >= %{basever}
Requires:       compiz >= %{basever}
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       gobject-introspection
Requires:       gdk-pixbuf2
Requires:       pango
Requires:       gtk3

%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.

This package contains a GUI configuration tool to configure Compiz
plugins and the composite window manager.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
python3 setup.py build --prefix=%{_prefix} --with-gtk=3.0

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/ccsm.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING VERSION
%{_bindir}/ccsm
%{_datadir}/appdata/ccsm.appdata.xml
%{_datadir}/applications/ccsm.desktop
%dir %{_datadir}/ccsm
%{_datadir}/ccsm/*
%{_datadir}/icons/hicolor/*/apps/ccsm.*
%{_datadir}/compiz/icons/hicolor/{22x22/{categories,devices,mimetypes},scalable/{apps,categories}}/*.{png,svg}
%dir %{python3_sitelib}/ccm
%{python3_sitelib}/ccm/*
%{python3_sitelib}/ccsm-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.8.18-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:0.8.18-14
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1:0.8.18-10
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-8
- Added setuptools build requirement
  Resolves: rhbz#2154828

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:0.8.18-6
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:0.8.18-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-1
- New version
  Related: rhbz#1891137

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.16-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.16-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.16-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-2
- Fixed popup
  Resolves: rhbz#1701693

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.14-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.8.14-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- Fixes for Python3.
- Introduce window state selector.
- Add an icon for the Earth plugin.
- Update translations.
- mv ccsm.appdata.xml to follow fedora package guide lines
- switch to python3
- modernize spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.12.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 27 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.4-1
- update to 0.8.12.4 release

* Mon Apr  4 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:0.8.12.3.0-2
- s390/ppc64 has libdrm now

* Tue Mar 29 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.3.0-1
- update to 0.8.12.3.0 release
- switch to gtk3
- use a fixed tarball from upstream

* Mon Mar 28 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.3-1
- update to 0.8.12.3 release
- switch to gtk3

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-1
- update to 0.8.12.1 release
- fix https://github.com/raveit65/ccsm/issues/1
- add more upstream patches

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-1
- update to 0.8.12 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-1
- update to 0.8.9
- new upstream is at https://github.com/raveit65/ccsm
- remove upstreamed patches
- remove sed commands
- fix rpmlint issue in description (gui --> GUI)
- modernize spec file for python

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-16
- rebuild for f22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 24 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-14
- fix no icons and text in main screen

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-12
- add ccsm_primary-is-control.patch
- fix (#910977)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-10
- remove commented out require
- drop gettext BR

* Sun Dec 02 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-9
- remove compizconfig-backend-mateconf require

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-8
- build for fedora
- rename patches
- fix invalid-lc-messages-dir
- add Epoch tag

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-7
- remove python sitelib stuff

* Wed Sep 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-6
- improve spec file

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-5
- build for mate
