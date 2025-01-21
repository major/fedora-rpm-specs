%bcond_without  use_qt6
%bcond_with     bundle_lxqtwallet
%bcond_without  bundle_tcplay
%global srcname zuluCrypt

Name:           zulucrypt
Version:        7.1.0
Release:        2%{?dist}
Summary:        Qt GUI front end to cryptsetup

# More details available in the copyright file in the source tarball.
# Major license is GPLv2+ (but GPLv3+ for some files)
# BSD for zuluwallet and dependencies lxqt_wallet and tcplay (at least tcplay is always bundled)
# CRC32 for a file in tcplay
# generic-xts for a part of tcplay
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-2-clause AND BSD-3-clause AND generic-xts AND LicenseRef-Fedora-UltraPermissive
URL:            https://mhogomchungu.github.io/zuluCrypt
Source0:        https://github.com/mhogomchungu/zuluCrypt/archive/%{version}/%{name}-%{version}.tar.gz

# polkit policy stolen from Debian, https://github.com/marciosouza20/zulucrypt
Source10:      zulucrypt-gui.policy
Source11:      zulumount-gui.policy

BuildRequires:  gcc gcc-c++

BuildRequires:  kf5-rpm-macros

# These are only needed for building the lxqt-wallet bundled library
%if %{with bundle_lxqtwallet}
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Notifications)
%endif

%if %{with use_qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(libcryptsetup)

BuildRequires:  libgcrypt-devel

BuildRequires:  desktop-file-utils

# upstream: 'extended the "personal" copy of the library in incompatible ways'
%if %{with bundle_tcplay}
Provides:       bundled(tcplay) = 2.0
%else
#BuildRequires:  tcplay-devel >= 2.0
%endif

# NB: LXQT version 4.0.0 is only built with QT6
%if %{with bundle_lxqtwallet}
# Version 6.2.0 bundles lxqt-wallet 3.2.2
Provides:       bundled(lxqt-wallet) = 3.2.0
%else
BuildRequires:  pkgconfig(lxqt-wallet) >= 4.0.0
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-console%{?_isa} = %{version}-%{release}

# ownership of top folders we place files in
Requires:       polkit
Requires:       hicolor-icon-theme
Requires:       shared-mime-info

# optional support for ecryptfs
%if %{?fedora}
Suggests:       ecryptfs-simple
%endif

%description
zuluCrypt is a front end to cryptsetup. It makes it easier to use cryptsetup
by providing a Qt-based GUI and a simpler to use CLI frontend to cryptsetup.
It does the same thing truecrypt does but without licensing problems or
requiring a user to setup sudo for it or presenting root's password.
This package contains the applications.

%package console
Summary:        Console tools of %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description console
This package contains the console (CLI) frontends of zuluCrypt. Those got
split into an own subpackage to provide possible independence from Qt as some
minimum.

%package libs
Summary:        Library for %{name}

%description libs
This package contains libraries that provide higher level access to
cryptsetup API and provide mounting/unmounting API to easy opening and
closing of volume.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files and libraries
necessary to build programs around zuluCrypt.

%package doc
Summary:        Additional documentation files for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Documentation later with %%doc
mv 'ABOUT ME' AUTHORS
sed -i /docs/d CMakeLists.txt
# Drop rpath, https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
# better use CMAKE_SKIP_INSTALL_RPATH=ON, https://fedorahosted.org/fpc/ticket/641
#find . -name CMakeLists.txt |xargs sed -i /INSTALL_RPATH/d
# Handle zuluSafe as a GUI application, binary needs Qt
sed -i -r 's:(zuluSafe)-cli:\1:g' CMakeLists.txt zuluSafe/CMakeLists.txt zuluSafe-cli.1
mv zuluSafe-cli.1 zuluSafe.1

%if %{without bundle_lxqtwallet}
rm -rf %{srcname}-gui/lxqt_wallet
%endif
%if %{without bundle_tcplay}
rm -rf external_libraries/tc-play
#sed -i -r 's:(STATIC_TCPLAY ").*":\1false":' CMakeLists.txt
%endif


%build
%{cmake_kf5} \
 -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
 -DCMAKE_SKIP_INSTALL_RPATH=ON \
 -DREUSEMOUNTPOINT=false \
 -DUDEVSUPPORT=true \
 -DNOGUI=false \
%if %{with use_qt6}
 -DBUILD_WITH_QT6=true \
%else
 -DQT5=true \
%endif
 -DHOMEMOUNTPREFIX=false \
 -DNOGNOME=false \
 -DNOKDE=false \
 -DUSE_POLKIT=true \
 %{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt --all-name
%if 0%{?rhel}
# Explicitly create folders in epel, install does not know target option
#mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
%endif
install -p -m0644 -t %{buildroot}%{_datadir}/polkit-1/actions -D %{SOURCE10} %{SOURCE11}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/zulu*.desktop

%ldconfig_scriptlets libs

%files -f %{name}.lang
%{_bindir}/zuluCrypt-gui
%{_bindir}/zuluMount-gui
%{_bindir}/zuluPolkit
%{_bindir}/zuluSafe
# Specific GUI plugins stored to libdir, need Qt
%{_libdir}/%{srcname}/
%{_datadir}/applications/zulu*.desktop
%{_datadir}/icons/hicolor/*/apps/zulu*.png
%{_datadir}/icons/zulu*.png
%{_datadir}/pixmaps/zulu*.png
%{_mandir}/man1/zulu*-gui.1*
%{_mandir}/man1/zuluSafe.1*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/mime/packages/*.xml
# find_lang does not care about subfolders
%dir %{_datadir}/%{srcname}
%dir %{_datadir}/%{srcname}/translations
%dir %{_datadir}/%{srcname}/translations/zulu*-gui

%files console
%{_bindir}/zuluCrypt-cli
%{_bindir}/zuluMount-cli
%{_mandir}/man1/zulu*-cli.1*

%files libs
%license COPYING GPLv* LICENSE
%doc AUTHORS *README* TODO changelog
%{_libdir}/lib%{srcname}*.so.*

%files devel
%{_includedir}/%{srcname}/
%{_libdir}/lib%{srcname}*.so
%{_libdir}/pkgconfig/libzulu*.pc

%files doc
%license COPYING GPLv* LICENSE
%doc docs/*.pdf
%doc docs/README docs/*.jpg

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Ian McInerney <ian.s.mcinerney@ieee.org> - 7.1.0-1
- Update to upstream 7.1.0 (fixes rhbz#2330000, rhbz#2331292)
- Update license string with final SPDX expression

* Wed Nov 06 2024 Ian McInerney <ian.s.mcinerney@ieee.org> - 7.0.0-2
- Switch to QT6 for new lxqt-wallet version 4.0.0 update
- Spec file cleanup

* Sun Sep 01 2024 Ian McInerney <ian.s.mcinerney@ieee.org> - 7.0.0-1
- Update to upstream 7.0.0 (fixes rhbz#2307507)
- License audit and update to SPDX license expressions (fixes rhbz#2118200)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Ian McInerney <ian.s.mcinerney@ieee.org> - 6.2.0-1
- Update to version 6.2.0 (fixes rhbz#2088941)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 12 2021 Ian McInerney <Ian.S.McInerney@ieee.org> - 6.0.0-3
- Rebuild due to lxqt-wallet soname bump (fixes rhbz#1948408)

* Tue Mar 30 2021 Ian McInerney <Ian.S.McInerney@ieee.org> - 6.0.0-2
- Bump minimum version of lxqt-wallet required and bundled

* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.0.0-1
- Update to latest upstream release 6.0.0 (#1922201)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.7.1-1
- Update to latest upstream release 5.7.1 (rhbz#1798062)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 5.7.0-1
- Update to latest upstream release 5.7.0

* Fri Sep 13 2019 Raphael Groner <projects.rg@smart.ms> - 5.6.0-1
- new version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Raphael Groner <projects.rg@smart.ms> - 5.5.0-1
- new version

* Tue May 07 2019 Raphael Groner <projects.rg@smart.ms> - 5.4.0-6
- add explicit BR: pkgconfig(uuid) as needed with util-linux 2.34

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.0-2
- Remove obsolete scriptlets

* Tue Jan 09 2018 Raphael Groner <projects.rg@smart.ms> - 5.4.0-1
- new version
- add support for mime

* Wed Nov 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.0-4
- Rebuild for cryptsetup-2.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Raphael Groner <projects.rg@smart.ms> - 5.2.0-1
- new version

* Mon Jun 12 2017 Builder <projects.rg@smart.ms> - 5.1.0-4
- rebuilt for soname bump of lxqt-wallet 3.1.0

* Wed Mar 01 2017 Raphael Groner <projects.rg@smart.ms> - 5.1.0-3
- add Suggests: encryptfs-simple

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Raphael Groner <projects.rg@smart.ms> - 5.1.0-1
- rhbz#1409373

* Fri Dec 16 2016 Raphael Groner <projects.rg@smart.ms> - 5.0.2-2
- rebuilt for latest Qt5

* Tue Dec 06 2016 Builder <projects.rg@smart.ms> - 5.0.2-1
- new version

* Tue Sep 27 2016 Raphael Groner <projects.rg@smart.ms> - 5.0.1-1
- new version

* Sat Aug 27 2016 Raphael Groner <projects.rg@smart.ms> - 5.0.0-3.20160802git064e9db
- drop obsolete Provides: bundled(md5-openssl)
- add userid to desktop files

* Fri Jul 22 2016 Raphael Groner <projects.rg@smart.ms> - 5.0.0-2.20160802git064e9db
- switch to git snapshot to include all latest upstream patches
- unbundle lxqt-wallet
- prepare to unbundle tcplay
- drop hack for desktop-file-validate, upstream issue#42
- add polkit
- split cli into console subpackage
- move licenses and general documentation into libs subpackage
- fix incorrect desktop files
- use BR: pkgconfig() where applicable
- drop default dependencies
- add scriptlets for MimeType key
- drop scriptlets option -p to not confuse rpmlint
- note Public Domain for bundled md5-openssl
- note GPLv3+ and GPLv2+ partly in source files
- fix find_lang
- drop chrpath (previously commented)

* Thu Jul 14 2016 Raphael Groner <projects.rg@smart.ms> - 5.0.0-1
- adjust for Fedora, based on upstream spec file
- unbundle tcplay
- try to unbundle lxqtwallet (unfinished)

* Thu May  1 2014 Francis Banyikwa <mhogomchungu@gmail.com> - 5.0.0-0
- version 5.0.0

* Fri Mar 15 2013 Francis Banyikwa <mhogomchungu@gmail.com> - 4.6.2-0
- upate to version 4.6.2

* Sat Jan 14 2012 Francis Banyikwa <mhogomchungu@gmail.com> - 4.6.0-0
- update to version 4.6.0

