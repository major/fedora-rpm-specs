Name:           eiskaltdcpp
Version:        2.4.2
Release:        15%{?dist}
Summary:        Direct Connect client

# The entire source code is GPLv3+ except FlowLayout.cpp and .h which is LGPLv2+
# Automatically converted from old format: GPLv3+ and LGPLv2+ - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/eiskaltdcpp/eiskaltdcpp
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         https://github.com/eiskaltdcpp/eiskaltdcpp/commit/5ab5e1137a46864b6ecd1ca302756da8b833f754.patch

BuildRequires:  cmake >= 2.6.3
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  perl-generators

Requires:       %{name}-data = %{version}-%{release}


%description
EiskaltDC++ is a cross-platform program that uses the Direct Connect
(DC aka NMDC) and Advanced Direct Connect (ADC) protocols. It is compatible
with DC++, AirDC++, FlylinkDC++ and other DC clients. EiskaltDC++ also
interoperates with all common DC hub software.

%package xmlrpc
Summary:    CLI xmlrpc
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description xmlrpc
Subpackage with CLI xmlrpc for %{name}.

%package gtk
Summary:    GTK-based graphical interface
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-gui%{?_isa} = %{version}-%{release}

%description gtk
GTK+ 3 interface using GTK+ 3 library.


%package qt
Summary:    Qt-based graphical interface
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-gui%{?_isa} = %{version}-%{release}

%description qt
Qt-based graphical interface.

%package data
Summary:    Data files for eiskaltdcpp
Requires:   %{name} = %{version}-%{release}
Requires:   hicolor-icon-theme
BuildArch:  noarch

%description data
Necessary data files for %{name}.

%prep
%autosetup -p1

# Remove bundled libs
rm -rf upnp
rm -rf data/examples/*.php eiskaltdcpp-qt/qtscripts/gnome/*.php
# Correct rpmlint W: crypto-policy-non-compliance-openssl
sed -i '/SSL_CTX_set_cipher_list/d' dcpp/CryptoManager.cpp

%build
%cmake \
    -DUSE_ASPELL=ON \
    -DFREE_SPACE_BAR_C=ON \
    -DUSE_MINIUPNP=ON \
    -DUSE_GTK3=ON \
    -DDBUS_NOTIFY=ON \
    -DUSE_JS=ON \
    -DPERL_REGEX=ON \
    -DUSE_CLI_XMLRPC=ON \
    -DWITH_SOUNDS=ON \
    -DLUA_SCRIPT=ON \
    -DWITH_LUASCRIPTS=ON
%cmake_build


%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}-gtk
%find_lang lib%{name}

%files -f lib%{name}.lang
%doc AUTHORS ChangeLog.txt README.md TODO
%license COPYING LICENSE
%{_bindir}/%{name}-daemon
%{_libdir}/libeiskaltdcpp.so.*
%{_mandir}/man?/%{name}-daemon.1.*

%files xmlrpc
%{_bindir}/%{name}-cli-xmlrpc
%{_mandir}/man?/%{name}-cli-xmlrpc.1.*

%files gtk -f %{name}-gtk.lang
%{_bindir}/*gtk
%{_mandir}/man?/*gtk*
%{_datadir}/%{name}/gtk
%{_datadir}/applications/*gtk*.desktop

%files qt
%{_bindir}/*qt
%{_mandir}/man?/*qt*
%{_datadir}/%{name}/qt
%{_datadir}/applications/*qt*.desktop

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cli
%{_datadir}/%{name}/luascripts
%{_datadir}/%{name}/emoticons
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/sounds
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/*.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 2.4.2-14
- Rebuild for updated miniupnpc.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.2-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.4.2-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.2-2
- Perl 5.34 rebuild

* Wed Mar 03 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Mon Jan 25 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.1-1
- Update to 2.4.1
- Update description and license

* Fri Dec 04 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.0-1
- Update to 2.4.0
- Remove Boost dependency

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-30.20200616git2ec27a2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-29.20200616git2ec27a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.11-28.20200616git2ec27a2
- Perl 5.32 re-rebuild updated packages

* Tue Jun 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-24.20200619git2ec27a2
- Update to latest git

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.11-27.20200414git89348ec
- Perl 5.32 rebuild

* Mon Apr 27 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-24.20200414git89348ec
- Update to latest git

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-25.20190922gita85c5d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-24.20190922gita85c5d8
- Update to latest git

* Wed Aug 14 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-23.20190603git1be7a44
- Update to latest git

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-23.20190527git09b9ffe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.11-22.20190527git09b9ffe
- Perl 5.30 rebuild

* Wed May 29 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-21.20190527git09b9ffe
- Move xmlrpc with perl deps to subpackage

* Tue May 28 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-20.20190527git09b9ffe
- Update to latest git

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 2.2.11-20.20181221gita1fdeb8
- Rebuilt for miniupnpc soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-19.20181221gita1fdeb8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 2.2.11-18.20181221gita1fdeb8
- Rebuilt for Boost 1.69

* Mon Jan 21 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.11-17.20181221gita1fdeb8
- Update to latest git

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-16.20180207git6ca065b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.11-15.20180207git6ca065b
- Perl 5.28 rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.11-14.20180207git6ca065b
- Perl 5.28 rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.2.11-13.20180207git6ca065b
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-12.20180207git6ca065b
- Build last version with Qt 5.10 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-11.20170207git3b9c502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.2.11-10.20170207git3b9c502
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.11-9.20170207git3b9c502
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-8.20170207git3b9c502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-7.20170207git3b9c502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.11-6.20170207git3b9c502
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.11-5.20170207git3b9c502
- Rebuilt for Boost 1.64

* Tue Jun 20 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-4.20170214git3b9c502
- Clean spec

* Tue Jun 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-3.20170214git3b9c502
- Disabled QT_QML

* Wed Apr 05 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-2.20170214git3b9c502
- Corrected some spec ussues

* Thu Mar 30 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-1.20170214git3b9c502
- Corrected some rpmlint errors and warnings

* Tue Mar 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-0.20170214git3b9c502
- Update to last git version

* Tue Feb 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-0.20161119git0fa9a73
- Update to last git version
- Add scriptlet for icons
- Add patch for openssl 1.1.0

* Tue Aug 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.11-0.20160510git52af555
- Clean spec
- Switch to git version

* Fri Jun 24 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.10-2
- Rebuild for new boost

* Mon Sep 28 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.10-1
- Update to 2.2.10

* Thu May 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-7
- Bump rebuild for Fedora 22
- Change URL to Sourceforge

* Wed Oct 08 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-6
- Bump rebuild for Fedora 21

* Mon Apr 28 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-5
- Rebuild
- Correct provides

* Mon Nov 25 2013 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-3
- Use multiple licenses
- Remove bundled libs

* Fri Nov 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-2
- Clean spec and descriptions
- Enable cli-xmlrpc
- License corrected

* Fri Aug 30 2013 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.9-1
- Update to 2.2.9

* Mon Jun 24 2013 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.8-1
- Update to 2.2.8

* Tue May 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.7-2
- Rebuild for F19

* Thu May 31 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.7-1
- Update to 2.2.7

* Sat May 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.6-5
- Added patch for non segfault in QT

* Fri Apr 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.6-4
- Added patch for compile with gcc 4.7

* Wed Mar 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.6-3
- Switch to GTK3 interface

* Tue Feb 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.6-2
- Back to GTK2 interface

* Tue Feb 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.6-1
- Update to 2.2.6

* Tue Dec 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.5-2
- Removed php

* Mon Dec 26 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.5-2
- Update to 2.2.5

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.4-2
- Added description in russian language

* Mon Oct 03 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Mon Jun 27 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.3-1
- update to 2.2.3

* Mon Apr 25 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.2-1
- update to 2.2.2
- added BR: libidn-devel

* Wed Mar  9 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.1-1
- update to 2.2.1

* Mon Jan 17 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 2.2.0-1
- update to 2.2.0

* Wed Dec  1 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.1-1
- update to 2.1.1

* Wed Nov 10 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.1.0-1
- update to 2.1.0
- added BR: gettext-devel gtk2-devel libnotify-devel lua-devel
  libglade2-devel
- build with gtk+
- make separate packages for gtk and qt gui

* Tue Oct 19 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.0.3-2
- remove php xamples

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.0.3-1
- update to 2.0.3

* Wed May 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.0.2-1
- update to new cpp version 2.0.2

* Thu Oct 29 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.0.30-1
- update to 1.0.30

* Mon Sep 28 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.0.2-1
- update to 1.0.2

* Wed Aug 26 2009 Dmitriy Pomerantsev (pda) <lrngate@yandex.ru> 1.0.0-1
- 1.0.0 from new upstream
- spec file is updated to Fedora standards

* Wed Jan 10 2007 Edward Sheldrake <ejs1920@yahoo.co.uk> 0.3.8-1
- replace antique .spec.in with one based on Fedora Extras .spec
- remove extra desktop file and icon sources

* Wed Jan 03 2007 Luke Macken <lmacken@redhat.com> 0.3.8-1
- 0.3.8 from new upstream
- Remove valknut-0.3.7-extra-qualification.patch

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 0.3.7-9
- Rebuild for FC6

* Sun Apr 30 2006 Luke Macken <lmacken@redhat.com> 0.3.7-8
- Execute with --disable-tray in desktop file, since it is horribly broken.

* Tue Feb 28 2006 Luke Macken <lmacken@redhat.com> 0.3.7-7
- Add patch to remove extra qualification build error

* Wed Feb 15 2006 Luke Macken <lmacken@redhat.com> 0.3.7-6
- Rebuild for FE5

* Wed Nov 09 2005 Luke Macken <lmacken@redhat.com> 0.3.7-5
- Rebuild for new openssl

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-4
- Add openssl-devel to BuildRequires

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-3
- Add bzip2-devel to BuildRequires

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-2
- Requires desktop-file-utils
- Use environment variables instead of hardcoding QTDIR
- Remove duplicate category from desktop file
- Use -p when calling 'install'

* Thu Sep 29 2005 Luke Macken <lmacken@redhat.com> 0.3.7-1
- Packaged for Fedora Extras
