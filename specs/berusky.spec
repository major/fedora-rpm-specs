%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global version_data 1.7

Summary:        Sokoban clone
Name:           berusky
Version:        1.7.1
Release:        31%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source:         http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
Source1:        berusky.desktop
Source2:        berusky.png
Source3:        berusky.appdata.xml
Source4:        http://www.anakreon.cz/download/%{name}-data-%{version_data}.tar.gz
Source5:        berusky.ini.in
Patch1:         berusky-1.7.1-sdl-build.patch
Patch2:         berusky-1.7.1-data-dir.patch
Patch3:         berusky-1.7.1-events-num.patch
Patch4:         berusky-gcc11-build.patch
URL:            http://www.anakreon.cz/?q=node/1
Requires:       SDL SDL_image
Obsoletes:      berusky-data
Conflicts:      berusky-data
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_image-devel desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  autoconf
BuildRequires: make

%description
Berusky is a 2D logic game based on an ancient puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

%prep
%setup -q -n %{name}-%{version} -b 4
%patch -P1 -p1 -b .sdl-build
%patch -P2 -p1 -b .data-dir
%patch -P3 -p1 -b .events-num
%patch -P4 -p1 -b .build

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoconf
%configure

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/doc/berusky/* %{buildroot}%{_pkgdocdir}

rm -rf %{buildroot}/%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata/

# Game data install
cd ../%{name}-data-%{version_data}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -r GameData %{buildroot}%{_datadir}/%{name}
cp -r Graphics %{buildroot}%{_datadir}/%{name}
cp -r Levels   %{buildroot}%{_datadir}/%{name}
cp README   %{buildroot}%{_datadir}/%{name}
cp COPYING  %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}
%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE5} > %{buildroot}%{_datadir}/%{name}/%{name}.ini

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/INSTALL
%exclude %{_pkgdocdir}/NEWS
%{_bindir}/berusky
%{_datadir}/applications/berusky.desktop
%{_datadir}/icons/hicolor/128x128/apps/berusky.png
%{_datadir}/appdata/berusky.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-30
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 4 2021 Martin Stransky <stransky@redhat.com> 1.7.1-22
- Added gcc11 build fix

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.7.1-19
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Martin Stransky <stransky@redhat.com> 1.7.1-17
- Fixed crash https://github.com/stransky/berusky/issues/11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 6 2019 Martin Stransky <stransky@redhat.com> 1.7.1-14
- Moved /var/games/berusky to /usr/share/berusky

* Sun May 5 2019 Martin Stransky <stransky@redhat.com> 1.7.1-13
- Bundle berusky-data

* Thu Apr 25 2019 Martin Stransky <stransky@redhat.com> 1.7.1-12
- Fixed missing SDL.h headers in flatpak build.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-8
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 17 2014 Martin Stransky <stransky@redhat.com> 1.7.1-1
- New upstream version (1.7.1)

* Thu Sep 25 2014 Martin Stransky <stransky@redhat.com> 1.7-4
- Added appdata file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 8 2014 Martin Stransky <stransky@redhat.com> 1.7-1
- New upstream version (1.7)

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6-4
- Install docs to %%{_pkgdocdir} where available (#993683).
- Fix bogus dates in %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-2
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix url and sourceurl
- fix desktop file to follow specification

* Sun Dec 9 2012 Martin Stransky <stransky@redhat.com> 1.6-1
- New upstream version (1.6)

* Sat Sep 15 2012 Martin Stransky <stransky@redhat.com> 1.5-2
- Fixed player profile save

* Sat Sep 1 2012 Martin Stransky <stransky@redhat.com> 1.5-1
- New upstream version (1.5)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Martin Stransky <stransky@redhat.com> 1.4-1
- New upstream version (1.4)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2-3
- Rebuild for new libpng

* Wed Jun 22 2011 Martin Stransky <stransky@redhat.com> 1.2-2
- Fixed rhbz#689106 - seg. fault after start

* Sun Mar 6 2011 Martin Stransky <stransky@redhat.com> 1.2-1
- updated to 1.2

* Thu Nov 19 2009 Martin Stransky <stransky@redhat.com> 1.1-13
- fixed dirs (#473628)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 2 2008 Martin Stransky <stransky@redhat.com> 1.1-10
- added patch from #458477 - Berusky aborts at end
  of intermediate level 18

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1-9
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-8
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Martin Stransky <stransky@redhat.com> 1.1-7
- rebuild

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.1-6
- Rebuild for selinux ppc32 issue.

* Tue Jun 26 2007 Martin Stransky <stransky@redhat.com> 1.1-5
- added a menu entry and an icon

* Wed May 23 2007 Martin Stransky <stransky@redhat.com> 1.1-4
- removed spec files from binary rpm package

* Tue May 8 2007 Martin Stransky <stransky@redhat.com> 1.1-3
- moved documentation from doc/berusky-1.1/berusky to doc/berusky-1.1

* Tue May 8 2007 Martin Stransky <stransky@redhat.com> 1.1-2
- fixed build in mock

* Mon Apr 23 2007 Martin Stransky <stransky@redhat.com> 1.1-1
- fixes from #237416

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build
