Name:		classified-ads
Version:	0.16
Release:	12%{?dist}
Summary:	Classified ads is distributed, server-less messaging system

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
URL:		http://katiska.org/classified_ads/
Source0:	https://github.com/operatornormal/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/operatornormal/classified-ads/blob/graphics/preprocessed.tar.gz?raw=true#/%{name}-graphics-%{version}.tar.gz
Patch0:     %{name}-miniupnp228.patch
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	openssl-devel
BuildRequires:	libnatpmp-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	opus-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel

%description
Classified ads is an attempt to re-produce parts of the functionality
that went away when Usenet news ceased to exist. This attempt tries to
fix the problem of disappearing news-servers so that there is no servers
required and no service providers needed; data storage is implemented
inside client applications that users are running. Main feature is
public posting. Other features include private messages, group messages,
basic operator data, search, voice calls between nodes, UI extensions
with TCL language and general-purpose database shared between nodes of the 
application. 
%prep
%autosetup -p1 -a 1

%build
qmake-qt5 QMAKE_STRIP=echo
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/classified-ads.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/classified-ads.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc README.TXT
%{_bindir}/classified-ads
%{_datadir}/applications/classified-ads.desktop
%dir %{_datadir}/app-install
%dir %{_datadir}/app-install/icons
%{_datadir}/app-install/icons/turt-transparent-128x128.png
%{_mandir}/man1/classified-ads.1.*
%{_datadir}/metainfo/classified-ads.appdata.xml
%license LICENSE
%{_datadir}/doc/classified-ads/examples/sysinfo.tcl
%{_datadir}/doc/classified-ads/examples/luikero.tcl
%{_datadir}/doc/classified-ads/examples/calendar.tcl

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jun 19 2025 Simone Caronni <negativo17@gmail.com> - 0.16-11
- Rebuild for updated miniupnpc.

* Wed Apr 16 2025 Simone Caronni <negativo17@gmail.com> - 0.16-10
- Rebuild for updated miniupnpc.

* Tue Jan 28 2025 Simone Caronni <negativo17@gmail.com> - 0.16-9
- Rebuild for updated dependencies.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 0.16-7
- Rebuild for updated miniupnpc.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.16-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 12 2023 Antti Järvinen <antti.jarvinen@katiska.org> - 0.16-1
- New upstream release 0.16. Protocol connectivity fixes and translations.

* Sun Jun 12 2022 Antti Järvinen <antti.jarvinen@katiska.org> - 0.15-1
- New upstream release 0.15. Critical when used with OpenSSL 3.x.

* Mon Feb 28 2022 Antti Järvinen <antti.jarvinen@katiska.org> - 0.14-1
- New upstream release

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 0.13-4
- Rebuilt for miniupnpc soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.13-1
- New upstream version: refactoring due to qt5.11 changes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12-2
- Remove obsolete scriptlets

* Sun Nov 12 2017 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.12-1
- New upstream version: new features, many new translations
- Appdata moved to /usr/share/metainfo

* Sun Jul 3 2016 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.11-1
- New upstream version: bugfixes and support for OpenSSL 1.1 API

* Fri Apr 8 2016 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.10-1
- New upstream version: audio capabilities and translation additions

* Sat Oct 10 2015 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.09-1
- Fixes to serious networking bugs
- Translation additions

* Mon Sep 28 2015 Antti Jarvinen <antti.jarvinen@katiska.org> - 0.08-1
- Links against qt5 instead of qt4
- Translation system is gnu gettext instead of qm files of Qt.
- Better tracking of changing local network addresses
- Numerous small bugfixes, mostly in networking code

* Sun Apr 12 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.07-1
- Removed intermediate PNG files into separate tarball
- Included code to generate intermediate PNG files manually

* Mon Apr 6 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.06-1
- Included original high-res bitmaps in different format, conversion routines.
- Fixed potential SIGSEGV appearing in debug build
- Code indented + typos fixed

* Wed Mar 25 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.05-1
- spec-file changes due to review comments.
- tagged a new version to allow building of latest version.
- added copyright notice to FrontWidget.cpp.
- included LGPL_EXCEPTION.txt from Nokia alongside sources.

* Tue Mar 17 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.04-2
- Changed packaging to happen in more civilized way.
  Lot of changes into spec file. 
- Package name has changed classified_ads -> classified-ads.
- Added appdata, re-wrote the small manpage in less personal tone. 

* Sat Mar 14 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.04-1
- License change GPL->LGPL due to OpenSSL license incompatibility.
- Minor UI changes as some bitmaps removed due to licensing issues

* Tue Feb 24 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.03-1
- Rpm build fixes for fedora linux
- Slower connection attempts to unreachable nodes
- Better file extenstion handling
- UI tweaks for small vertical screen resolutions, affects at least 
   users of some mac models
- Classifications entered by user now actually work too 
- If no local search avail, still offer network search
- Possible crash case fix. Still having random crashes inside
  json serialize..
- Links between documents, still does not work with profile comments
- Try miniupnpc also in unix build
- Basic support for trust-tree based on trust lists
- Translations
* Sun Jan 04 2015 Antti Jarvinen <classified-ads.questions@katiska.org> - 0.02-1
- Libnatpmp is not used in windows build,
- Profile comment document width setting was missing
- Made main window slightly smaller vertically.
- Now compiles also under Qt5
- Fix for grave bug: only message sender (not recipient) can read binary attachments
- Error messages for some file operations
- Fix for situation where published private profile breaks every node in network
- Require c++ compiler for compilation of c++, when building rpm.

* Wed Dec 31 2014 Tuomas Haarala <tuoppi@hieno.net> - 0.01-1
- initial spec file scribbled together
