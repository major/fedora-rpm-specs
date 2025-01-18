# Force out of source build
%undefine __cmake_in_source_build

Name:		dnfdragora
Version:	2.99.0
Release:	2%{?dist}
Summary:	DNF package-manager based on libYui abstraction

License:	GPL-3.0-or-later
URL:		https://github.com/manatools/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	cmake			>= 3.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig
BuildRequires:	python3-devel		>= 3.4.0
BuildRequires:	python3-libdnf5		>= 5.2.7
BuildRequires:	python3-manatools	>= 0.0.3
BuildRequires:	python3-PyYAML
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
BuildRequires:	python3-yui
BuildRequires:	python3-pyxdg
BuildRequires:	python3-cairosvg
BuildRequires:	python3-pillow
BuildRequires:	python3-pystray		>= 0.16

Requires:	dnf5daemon-server	>= 5.2.7
Requires:	filesystem
Requires:	comps-extras
Requires:	hicolor-icon-theme
Requires:	libyui-mga-ncurses
Requires:	python3-libdnf5		>= 5.2.7
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-PyYAML
Requires:	python3-yui		>= 1.1.1-10

Provides:	%{name}-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)

%description
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.


%package updater
Summary:	Update notifier applet for %{name}

Requires:	%{name}			== %{version}-%{release}
Requires:	libnotify
Requires:	python3-pyxdg
Requires:	python3-cairosvg
Requires:	python3-pillow
Requires:	python3-pystray		>= 0.16

Obsoletes:	%{name}-gui		< 1.0.1-7

%description updater
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.

This package provides the update notifier applet for %{name}.


%prep
%autosetup -p 1


%build
%cmake \
  -DCHECK_RUNTIME_DEPENDENCIES=ON \
  -DENABLE_COMPS=ON               \
  %{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name}


%check
# Validate desktop-files.
desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/*.desktop

# Validate AppData-files.
appstream-util validate-relax --nonet		\
	%{buildroot}%{_datadir}/appdata/*.appdata.xml


%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%dir %{_sysconfdir}/%{name}
%doc README.md %{name}.yaml*.example
%exclude %{python3_sitelib}/%{name}/updater.py
%exclude %{python3_sitelib}/%{name}/__pycache__/updater.cpython*.py?
%license AUTHORS LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/applications/*%{name}-localinstall.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man5/%{name}*.5*
%{_mandir}/man8/%{name}*.8*
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*


%files updater
%{_bindir}/%{name}-updater
%{_datadir}/applications/*%{name}-updater.desktop
%{_sysconfdir}/xdg/autostart/*%{name}*.desktop
%{python3_sitelib}/%{name}/updater.py
%{python3_sitelib}/%{name}/__pycache__/updater.cpython*.py?



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 29 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.99.0-1
- Rebase to v2.99.0 (using dnf5daemon)

* Thu Sep 12 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.1.5-7
- Backport patch to drop dnf-makecache timer check

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.5-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.1.5-4
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Jonathan Wright <jonathan@almalinux.org> - 2.1.5-1
- Update to 2.1.5 rhbz#2251548

* Wed Aug 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.1.4-1
- Version 2.1.4

* Fri Aug 11 2023 Leigh Scott <leigh123linux@gmail.com> - 2.1.2-7
- Add build requires python3-setuptools

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 2.1.2-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.1.2-1
- Version 2.1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-2
- Backport fix from upstream to fix dnfdragora-updater (#1886178)

* Mon Oct 05 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-1
- Update to 2.1.0 (#1876299)

* Tue Aug 25 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.4-2
- Add missing dep on comps-extras for comps group icons (#1872359)

* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.4-1
- Update to 2.0.4 (#1823345)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.0-2
- Backport fix from upstream for crash on non-existing user prefs config file

* Sat Apr 04 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.0-1
- Rebase to 2.0.0 (#1703486)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Neal Gompa <ngompa13@gmail.com> - 1.1.1-1
- Rebase to 1.1.1
- Drop merged patches
- Add patch to fix metainfo file and drop unused import

* Mon Sep 17 2018 Adam Williamson <awilliam@redhat.com> - 1.0.1-13.git20180108.b0e8a66
- Backport PR#116 for RHBZ#1624652 (dnf callback-related crash)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12.git20180108.b0e8a66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-11.git20180108.b0e8a66
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10.git20180108.b0e8a66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.1-9.git20180108.b0e8a66
- Updated to snapshot fixing rhbz#1510632
- Fix rhbz#1531118
- Remove the obsolete scriptlets for updating icon-cache

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-8.git20171229.24e4647
- Add proper Obsoletes

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-7.git20171229.24e4647
- Updated to snapshot fixing several issues
- Rename dnfdragora-gui to dnfdragora-updater
- Add Provides for dnfdragora-gui to dnfdragora

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6.git20170505.2a3b056
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-5.git20170505.2a3b056
- Updated to snapshot adding new translations

* Thu May 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-4.git20170504.c525448
- Updated to snapshot containing all patches and improvements

* Thu May 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-3.git20170503.ca79256
- Updated to snapshot adding some stability improvements

* Wed May 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-2.git20170503.368ee94
- Updated to snapshot adding dnfdragora-updater

* Sat Apr 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-1
- New upstream release

* Wed Apr 12 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-19.git20170411.3662635
- Updated to new snapshot obsoleting patches
- Fixed dependency on libyui-mga-ncurses

* Tue Apr 11 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-18.git20170411.6098816
- Add fix from anaselli: `RecursionError: maximum recursion depth exceeded`
  (rhbz#1439247, #1436508, #1436451, #1440570, #1440565, #1440174)

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-17.git20170409.6138805
- Updated to snapshot fixing several translations
- Use rich-dependencies instead of requiring a virtual package

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-16.git20170407.769c37d
- Adjusted Obsoletes for Yumex-DNF

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-15.git20170407.769c37d
- Updated to snapshot fixing several translations

* Wed Apr 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-14.git20170405.cca9412
- Updated to snapshot fixing rhbz#1436451

* Wed Apr 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-13.git20170404.63fe191
- Updated to snapshot fixing several translations

* Sun Apr 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-12.git20170402.f3ca28b
- Updated to snapshot with improved icons and some fixed translations

* Sat Apr 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-11.git20170401.b97db68
- Updated to snapshot fixing some issues with the build-system

* Sat Apr 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-10.git20170401.d018d08
- Updated to snapshot adding manpages and fixing some translations

* Fri Mar 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-9.git20170330.f30c75c
- Replace and obsolete Yumex-DNF
  See:  https://pagure.io/fesco/issue/1690#comment-434558

* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-8.git20170330.f30c75c
- Updated to snapshot fixing a missing comma
- Pick up desktop-file for installing local rpms

* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-7.git20170330.6f50912
- Updated to snapshot fixing new dbus-signal with dnf >= 2.2.0

* Tue Mar 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-6.git20170325.b8545aa
- Updated to snapshot fixing several translations

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-5.git20170322.798975a
- Add gui-subpkg
- Prepare obsoletion of Yumex-DNF

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-4.git20170322.798975a
- Updated to snapshot fixing an issue with the ncurses interface

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 1.0.0-3.git20170226.ae5163e
- updated to snapshot fixing behaviour on start without network

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 1.0.0-2.git20170226.b0b2c9a
- updated to snapshot fixing some minor issues

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-1
- New upstream release (rhbz#1424827)

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.114.git20170218.58bd424
- New snapshot

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.0.0-0.113.git20170213.289d170
- Rebuild for brp-python-bytecompile

* Tue Feb 14 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.112.git20170213.289d170
- New snapshot

* Wed Feb 08 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.111.git20170207.783aede
- New snapshot

* Sun Feb 05 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.110.git20170205.d929620
- New snapshot

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.109.git20170204.2c34e52
- New snapshot
- Drop patch, upstreamed
- Run CMake with '-Wno-dev'-flag

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.108.git20170204.f2bb4da
- Swap date and commit-sha in release-tag

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.107.gitf2bb4da.20170204
- Add patch to build and install translations with CMake

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.106.gitf2bb4da.20170204
- New snapshot

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.105.git708a8a8.20170204
- Drop Requires: libyui-mga-ncurses, dnf should be smart enough
  to select the MGA-UI with the least deps during installation

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.104.git708a8a8.20170204
- New snapshot

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.103.gita3492da.20170204
- New snapshot

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.102.git4d872ab.20170202
- New snapshot

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.101.gitcc4e556.20170202
- Add Requires: libyui-mga-ncurses for functionality with low dependencies

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.100.gitcc4e556.20170202
- Initial import (rhbz#1418788)
- Bump to 0.100 to superseed builds from COPR

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.0-0.1.gitcc4e556.20170202
- Initial rpm-release (rhbz#1418788)
