Name:		firetools
Version:	0.9.72
Release:	5%{?dist}
Summary:	Graphical user interface for the Firejail security sandbox
License:	GPL-2.0-only AND GPL-2.0-or-later AND CC-BY-SA-3.0 AND MPL-2.0 AND GPL-1.0-only AND LGPL-2.0-only AND CC0-1.0
Group:		Development/Tools
URL:		https://firejailtools.wordpress.com/
Source0:	https://downloads.sourceforge.net/project/firejail/%{name}/%{name}-%{version}.tar.xz
# Support installing in lib64 instead of hardcoded lib
# https://github.com/netblue30/firetools/issues/75
# https://github.com/netblue30/firetools/pull/76
Patch0:		firetools-libfix.patch
# https://github.com/netblue30/firetools/pull/77
Patch1:		firetools-desktopfix.patch
# https://github.com/netblue30/firetools/pull/78
Patch2:		firetools-appdata.patch
# https://github.com/netblue30/firetools/pull/80
Patch3:		firetools-licensefix.patch
Requires:	firejail
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	pkgconfig(Qt5)

%description
A Firejail sandbox launcher integrated with the system tray,
sandbox editing, management and statistics.

%prep
%autosetup -p 1

%build
%configure --with-qmake=/usr/bin/qmake-qt5
%make_build

%install
%make_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/firejail-ui.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/firetools.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/firejail-ui.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/firetools.metainfo.xml

# Remove redundant license file
rm %{buildroot}%{_docdir}/firetools/COPYING

%files
%license COPYING
%{_bindir}/firejail-ui
%{_bindir}/firetools
%dir %{_libdir}/firetools
%{_libdir}/firetools/fmgr
%{_libdir}/firetools/fstats
%{_libdir}/firetools/uiapps
%{_libdir}/firetools/uihelp
%{_libdir}/firetools/uimenus
%{_datadir}/applications/firejail-ui.desktop
%{_datadir}/applications/firetools.desktop
%{_docdir}/firetools
%{_mandir}/man1/firejail-ui.1.*
%{_mandir}/man1/firetools.1.*
%{_metainfodir}/firejail-ui.metainfo.xml
%{_metainfodir}/firetools.metainfo.xml
%{_datadir}/pixmaps/firejail-ui.png
%{_datadir}/pixmaps/firetools.png
%{_datadir}/pixmaps/firetools-minimal.png

%changelog
* Fri Apr 24 2026 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.72-5
- Update GPLv2 text

* Tue Dec 10 2024 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.72-4
- Correct URL
- Validate desktop file
- Add and validate appdata

* Tue Nov 5 2024 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.72-3
- Own firetools directory
- Correctly mark license file
- Correct license tag

* Fri Sep 15 2023 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.72-2
- Change to SPDX license identifier

* Mon Jan 30 2023 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.72-1
- Update to 0.9.72
- Add uiapps

* Fri Mar 19 2021 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.64-1
- Update to 0.9.64
- Explicitly require make

* Fri May 22 2020 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.62-2
- Use pkgconfig for BuildRequires

* Fri Jan 17 2020 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.62-1
- Update to 0.9.62
- Add missing %{?dist} tag
- Build with qt5

* Mon Mar 25 2019 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.58-1
- Update to 0.9.58
- Fix hardcoded prefix

* Thu Mar 29 2018 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.52-1
- Update to 0.9.52

* Fri Dec 22 2017 Brandon Nielsen <nielsenb@jetfuse.net> 0.9.50-1
- Initial specfile
