Name:           rott
Version:        1.1.2
Release:        27%{?dist}
Summary:        Rise of the Triad
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://icculus.org/rott/
Source0:        http://icculus.org/rott/releases/rott-%{version}.tar.gz
Source1:        rott-shareware.sh
Source2:        rott-registered.sh
Source3:        rott.autodlrc
Source4:        rott-shareware.desktop
Source5:        rott-registered.desktop
Source6:        rott-shareware.appdata.xml
Source7:        rott-registered.metainfo.xml
# Notice this is made from an edited screenshot and thus derived from the non-
# free datafiles. I believe this constitutes fair-use. If anyone disagrees let
# me know and I'll remove it
Source8:        rott.png
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel desktop-file-utils libappstream-glib

%description
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad, which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.


%package        shareware
Summary:        Rise of the Triad shareware version
Requires:       hicolor-icon-theme autodownloader unzip

%description    shareware
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the shareware version of RotT. In order to
play the shareware version, you will need the shareware datafiles. Which can
be freely downloaded from Apogee/3DRealms, but cannot be distributed as a part
of Fedora. When you start RotT for the first time it will offer to download
the datafiles for you.


%package        registered
Summary:        Rise of the Triad registered version
Requires:       hicolor-icon-theme zenity

%description    registered
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the registered version of RotT. If you own
the registered version, this allows you to play the registered version under
Linux. Place the registered RotT datafiles in a dir and start rott-registered
from this dir.


%prep
%setup -q

cp -a doc/rott.6 rott-shareware.6
cp -a doc/rott.6 rott-registered.6
sed -i.orig 's/rott/rott-shareware/g' rott-shareware.6
sed -i.orig 's/rott/rott-registered/g' rott-registered.6
touch -r rott-shareware.6.orig rott-shareware.6
touch -r rott-registered.6.orig rott-registered.6


%build
pushd rott
make %{?_smp_mflags} \
  EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign" \
  ROTT=rott-shareware.bin
make tidy
make %{?_smp_mflags} \
  EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign" \
  ROTT=rott-registered.bin SHAREWARE=0 SUPERROTT=1
popd


%install
#no make install target, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 755 rott/rott-* $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-shareware
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}-registered
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{name}-shareware.6 $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{name}-registered.6 $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE5}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE6} %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE8} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/

%files shareware
%doc README doc/*.txt
%license COPYING
%{_bindir}/rott-shareware*
%{_mandir}/man6/%{name}-shareware.6*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}-shareware.appdata.xml
%{_datadir}/applications/%{name}-shareware.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%files registered
%doc README doc/*.txt
%license COPYING
%{_bindir}/rott-registered*
%{_mandir}/man6/%{name}-registered.6*
%{_datadir}/appdata/%{name}-registered.metainfo.xml
%{_datadir}/applications/%{name}-registered.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.2-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Hans de Goede <hdegoede@redhat.com> - 1.1.2-4
- Add support for game-data-packager provided assets (rhbz#1295511)
- Add appdata files
- Modernize spec a bit

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Hans de Goede <hdegoede@redhat.com> - 1.1.2-1
- New upstream release 1.1.2
- Fix FTBFS (rhbz#1037308)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-8
- Remove --vendor from desktop files for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-1
- New upstream release 1.1 (incorperating all our patches!)

* Thu Apr 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-6
- Many fixes (and a manpage) ported over from debian

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-5
- Autorebuild for GCC 4.3

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-4
- Update License tag for new Licensing Guidelines compliance
- Fix 2 calls of memset with the 2nd and 3th argument swaped,
  reported by Dave Jones

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-3
- Add missing autodownloader Requires to rott-shareware

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-2
- Add desktop entry and userfriendly launcher script for registered package
- Add a patch fixing crashes with "long" usernames

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-1
- Initial Fedora Extras package
