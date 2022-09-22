%global		gittag0			2021-01-26-Release-2.8.0

%define			lang_subpkg() \
%package		langpack-%{1}\
Summary:		%{2} language data for %{name}\
BuildArch:	noarch\
Requires:		%{name} = %{version}-%{release}\
Supplements:	(%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description	langpack-%{1}\
%{2} language data for %{name}.\
\
%files			langpack-%{1}\
%{_datadir}/%{name}/translations/%{name}_%{1}.qm\
%{_datadir}/oracle/translations/oracle_%{1}.qm

Name:		cockatrice
Version:	2.8.0
Release:	6%{?dist}
Summary:	A cross-platform virtual tabletop software for multi-player card games

# * Public Domain (cockatrice/resources/countries/*.svg)
# * GPLv2+ (most of the code)
# * BSD (cockatrice/src/qt-json/, common/sfmt/, 
# * GPLv2 (oracle/src/zip/)
# * CPL or LGPLv2 (servatrice/src/smtp/)
# # Webclient code (not included?)
# * ASL 2.0 (webclient/js/protobuf.js, webclient/js/long.js,
# webclient/js/bytebuffer.js)
# * MIT (webclient/js/jquery-*.js)
License:	GPLv2 and Public Domain
URL:		https://%{name}.github.io
Source0:	https://github.com/%{name}/%{name}/archive/%{gittag0}.tar.gz
Source1:	cockatrice.appdata.xml
Patch0:		cockatrice-ea9e966330-fix-desktop-entry-files.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake >= 3.1
BuildRequires:	protobuf-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite-devel
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
Requires:		wget
Requires:		hicolor-icon-theme

%description
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.


%prep
%setup -q -n Cockatrice-%{gittag0}
%patch0 -p0
find . -iname "*.h" -exec chmod a-x "{}" \;
find . -iname "*.cpp" -exec chmod a-x "{}" \;


%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=OFF \
	-DWITH_SERVER=ON

%cmake_build


%check
appstream-util validate-relax --nonet %{SOURCE1}
desktop-file-validate cockatrice/%{name}.desktop
desktop-file-validate servatrice/servatrice.desktop
desktop-file-validate oracle/oracle.desktop


%install
%cmake_install

install -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
rm %{buildroot}%{_datadir}/cockatrice/themes/Default/.gitignore
rm %{buildroot}%{_datadir}/%{name}/translations/%{name}_en@pirate.qm
rm %{buildroot}%{_datadir}/oracle/translations/oracle_en@pirate.qm


%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/appdata/*
%{_datadir}/%{name}
%{_datadir}/servatrice
%{_datadir}/icons/hicolor/{48x48,scalable}/apps/*
%{_datadir}/oracle
%exclude %{_datadir}/%{name}/translations/%{name}_*.qm
%exclude %{_datadir}/oracle/translations/oracle_*.qm

%lang_subpkg cs Czech
%lang_subpkg de German
%lang_subpkg en English
%lang_subpkg es Spanish
%lang_subpkg et Estonian
%lang_subpkg fr French
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ru Russian
%lang_subpkg sr Serbian
%lang_subpkg sv Swedish
%lang_subpkg zh-Hans "Chinese (Simplified)"


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 2.8.0-4
- Rebuilt for protobuf 3.19.0

* Sun Oct 24 2021 Adrian Reber <adrian@lisas.de> - 2.8.0-3
- Rebuilt for protobuf 3.18.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 3 2021 Link Dupont <linkdupont@fedoraproject.org> - 2.8.0-1
- New upstream release

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.7.5-5
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 08:56:00 CET 2021 Adrian Reber <adrian@lisas.de> - 2.7.5-3
- Rebuilt for protobuf 3.14

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 2.7.5-2
- Rebuilt for protobuf 3.13

* Mon Sep 21 2020 Link Dupont <linkdupont@fedoraproject.org> - 2.7.5-1
- New upstream release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 2.7.4-2
- Rebuilt for protobuf 3.12

* Fri Mar 27 2020 Link Dupont <linkdupont@fedoraproject.org> - 2.7.4-1
- New upstream release

* Tue Jan 28 2020 Link Dupont <linkdupont@fedoraproject.org> - 2.7.2-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 2.7.1-3
- Rebuild for protobuf 3.11

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Link Dupont <linkdupont@fedoraproject.org> - 2.7.1-1
- New upstream release

* Thu Mar 07 2019 Link Dupont <linkdupont@fedoraproject.org> - 2.7.0-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.0-3
- Rebuild for protobuf 3.6

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Link Dupont <linkdupont@fedoraproject.org> - 2.6.0-1
- new upstream release

* Tue Apr 17 2018 Link Dupont <linkdupont@fedoraproject.org> - 2.5.1-1
- New upstream release

* Sat Mar 03 2018 Link Dupont <linkdupont@fedoraproject.org> - 2.5.0-1
- New upstream release

* Thu Feb 22 2018 Link Dupont <linkdupont@fedoraproject.org> - 2.4.0-5
- Add missing build dependency on g++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-3
- Remove obsolete scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.4.0-2
- Rebuild for protobuf 3.5

* Thu Nov 23 2017 Link Dupont <linkdupont@fedoraproject.org> - 2.4.0-1
- New upstream release

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.17-5
- Rebuild for protobuf 3.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Orion Poplawski <orion@cora.nwra.com> - 2.3.17-2
- Rebuild for protobuf 3.3.1

* Fri Jun 2 2017 Link Dupont <linkdupont@fedoraproject.org> - 2.3.17-1
- Initial package
