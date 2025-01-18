%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# define icons directories...
%define _iconstheme    hicolor
%define _iconsbasedir  %{_datadir}/icons/%{_iconstheme}
%define _iconsscaldir  %{_iconsbasedir}/scalable/apps

Name:		byobu
Version:	6.12
Release:	6%{?dist}
Summary:	Light-weight, configurable window manager built upon GNU screen

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/dustinkirkland/byobu
Source0:	https://github.com/dustinkirkland/byobu/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# default windows
Source1:	fedoracommon

# prefer dnf when installed
# sent upstream: https://code.launchpad.net/~sanjay-ankur/byobu/byobu/+merge/415959
Patch:		0002-byobu-use-dnf.patch
# for F41+ where we have dnf5
Patch:		0002-byobu-use-dnf5.patch
Patch:  0001-byobu-autostart-with-fish-shell.patch 

BuildArch:	noarch
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  %{_bindir}/msgfmt
BuildRequires:  python3
Requires:       gettext-runtime
Requires:       newt
Requires:       python3-newt
Requires:       screen
Requires:       tmux

%Description
Byobu is a Japanese term for decorative, multi-panel screens that serve 
as folding room dividers. As an open source project, Byobu is an 
elegant enhancement of the otherwise functional, plain, 
practical GNU Screen. Byobu includes an enhanced profile 
and configuration utilities for the GNU screen window manager, 
such as toggle-able system status notifications.

%prep
%autosetup -N
%if 0%{?fedora} >= 41
%autopatch -p0 1
%else
%autopatch -p0 0
%endif

# remove swap file
if [ -e "usr/bin/.byobu-status-print.swp" ]; then rm usr/bin/.byobu-status-print.swp
fi
# fix path for lib directory in scripts
for i in `find . -type f -exec grep -l {BYOBU_PREFIX}/lib/ {} \;`; do
sed -i "s#{BYOBU_PREFIX}/lib/#{BYOBU_PREFIX}/libexec/#g" $i;
done
# fix path for lib directory #2
for i in `find . -type f -exec grep -l BYOBU_PREFIX/lib {} \;`; do
sed -i "s#BYOBU_PREFIX/lib/#BYOBU_PREFIX/libexec/#g" $i;
done

# fix path for correct directory in /usr/share
sed -i "s#DOC = BYOBU_PREFIX + '/share/doc/' + PKG#DOC='%{_pkgdocdir}'#g" usr/lib/byobu/include/config.py.in

# set default fedora windows
cp -p %{SOURCE1} usr/share/byobu/windows/common

# fix path from lib to libexec by modified Makefile.am and in
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/Makefile.am
#sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/Makefile.in
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/include/Makefile.am
#sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/include/Makefile.in

%build
export BYOBU_PYTHON=%{__python3}
sh ./autogen.sh
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_sysconfdir}/profile.d
# remove apport which is not available in fedora
rm %{buildroot}/%{_libexecdir}/%{name}/apport
sed -i 's#status\[\"apport\"\]=0##g' %{buildroot}%{_bindir}/byobu-config
cp -p COPYING %{buildroot}%{_pkgdocdir}

for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/%{name}.mo
done

#use the old xterm .desktop style for while
cp -a usr/share/%{name}/desktop/%{name}.desktop.old usr/share/%{name}/desktop/%{name}.desktop
desktop-file-install usr/share/%{name}/desktop/%{name}.desktop --dir %{buildroot}%{_datadir}/applications
# remove vigpg
rm %{buildroot}/usr/bin/vigpg
rm %{buildroot}/usr/share/man/man1/vigpg.1

# add icon into /usr/share/icons/hicolor/scalable/apps/ from /usr/share/byobu/pixmaps/byobu.svg
mkdir -p %{buildroot}%{_iconsscaldir}
cp -p usr/share/byobu/pixmaps/byobu.svg %{buildroot}%{_iconsscaldir}

%find_lang %{name}

%files -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_libexecdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_pkgdocdir}
%{_iconsscaldir}/%{name}.svg
%{_pkgdocdir}/*
%{_bindir}/%{name}*
%{_bindir}/col1
%{_bindir}/ctail
%{_bindir}/manifest
%{_bindir}/purge-old-kernels
%{_bindir}/wifi-status
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/us.kirkland.terminals.byobu.service
%{_mandir}/man1/%{name}*.1.gz
%{_mandir}/man1/col1.1.gz
%{_mandir}/man1/ctail.1.gz
%{_mandir}/man1/manifest.1.gz
%{_mandir}/man1/purge-old-kernels.1.gz
%{_mandir}/man1/wifi-status.1.gz
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild


* Sun Jan 05 2025 Priscila Gutierres <prgutier AT REDHAT DOT com> - 6.12-5
- Fix BZ 2277627

* Tue Nov 26 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 6.12-4
- Update patch for dnf5

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 6.12-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 6.12-1
- Update byobu to 6.12

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Filipe Rosset <rosset.filipe@gmail.com> - 5.133-8
- Add patch to use dnf when installed (thanks to Ankur Sinha ankursinha)

* Wed Sep 07 2022 Filipe Rosset <rosset.filipe@gmail.com> - 5.133-7
- spec cleanup and reorganization of Requires and BuildRequires

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.133-1
- Update to 5.133 fixes rhbz#1803380

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.132-1
- Update to 5.132 fixes rhbz#1803380

* Tue Feb 11 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.131-1
- Update to 5.131 fixes rhbz#1800974

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.130-1
- Update to 5.130 fixes rhbz#1778324

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Filipe Rosset <rosset.filipe@gmail.com> - 5.129-1
- new upstream release 5.129, fixes rhbz #1719515

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 5.127-3
- Switch to Python 3 (#1532565)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.127-1
- Rebuilt for new upstream release 5.127, fixes rhbz #1615175

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.125-1
- Rebuilt for new upstream release 5.125, fixes rhbz #1480023

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.119-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.119-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.119-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Filipe Rosset <rosset.filipe@gmail.com> - 5.119-1
- Rebuilt for new upstream release 5.119, fixes rhbz #1458069

* Sun Apr 30 2017 Filipe Rosset <rosset.filipe@gmail.com> - 5.117-1
- Rebuilt for new upstream release 5.117, fixes rhbz #1446592

* Fri Apr 14 2017 Filipe Rosset <rosset.filipe@gmail.com> - 5.116-2
- Added newt python deps (thanks to Daniele Viganò), fixes rhbz #1441067

* Mon Mar 20 2017 Filipe Rosset <rosset.filipe@gmail.com> - 5.116-1
- Rebuilt for new upstream release 5.116, fixes rhbz #1433633

* Tue Feb 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 5.115-1
- Rebuilt for new upstream release 5.115, fixes rhbz #1417321

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.113-2
- Fixed issue with .desktop file (thanks to mastaiza for all tests/bug reports)

* Fri Dec 09 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.113-1
- Rebuilt for new upstream release 5.113, fixes rhbz #1276014

* Fri Dec 09 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.97-3
- Spec clean up

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Jan Klepek <jan.klepek at, gmail.com> - 5.97-1
- update to 5.97

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Jan Klepek <jan.klepek at, gmail.com> - 5.92-1
- update to 5.92, fix for #1196950

* Tue Nov 11 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.87-1
- update to 5.87

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.73-4
- patch for issue with missing ~/.byobu/status leading to crash in byobu-config

* Thu Feb 27 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.73-3
- various upstream patches

* Wed Feb 26 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.73-2
- various upstream patches

* Tue Feb 18 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.73-1
- Update to latest release 

* Thu Jan 9 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.69-2
- added icon (#1013240)

* Wed Jan 8 2014 Jan Klepek <jan.klepek at, gmail.com> - 5.69-1
- update to latest version (#873560)
- added tmux dependency (#907267)

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 5.21-7
- Install docs to %%{_pkgdocdir} where available (#993689).
- Fix bogus dates in %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Jan Klepek <jan.klepek at, gmail.com> - 5.21-4 
- desktop file handling fixed

* Sat Aug 25 2012 Jan Klepek <jan.klepek at, gmail.com> - 5.21-3
- another fix into documentation

* Sun Aug 19 2012 Jan Klepek <jan.klepek at, gmail.com> - 5.21-2
- fixed documentation

* Sun Aug 19 2012 Jan Klepek <jan.klepek at, gmail.com> - 5.21-1
- new minor release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Jan Klepek <jan.klepek at, gmail.com> - 5.17-1
- update to latest version

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 15 2011 Jan Klepek <jan.klepek at, gmail.com> - 4.41-1
- update to 4.41

* Mon Aug 1 2011 Jan Klepek <jan.klepek at, gmail.com> - 4.23-1
- update to 4.23

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 4.22-2
- updated to 4.22 + various bugfixes

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 4.20-1
- new major release

* Sat Jan 8 2011 Jan Klepek <jan.klepek at, gmail.com> - 3.21-1
- new release

* Sat Dec 18 2010 Jan Klepek <jan.klepek at, gmail.com> - 3.20-2
- upgrade to 3.20 + some patches

* Fri Sep 3 2010 Jan Klepek <jan.klepek at, gmail.com> - 3.4-1
- upgraded to 3.4

* Thu Jun 17 2010 Jan Klepek - 2.80-1
- bugfix for BZ#595087, changed default windows selection, removed apport from toggle status notification
- upgraded to 2.80 version

* Sun May 2 2010 Jan Klepek <jan.klepek at, gmail.com> - 2.73-1
- new version released

* Wed Apr 21 2010 Jan Klepek <jan.klepek at, gmail.com> - 2.67-3
- adjusted SHARE path

* Tue Apr 20 2010 Jan Klepek <jan.klepek at, gmail.com> - 2.67-2
- adjusted path for looking for po files and removed duplicate file entry

* Fri Apr 2 2010 Jan Klepek <jan.klepek at, gmail.com> - 2.67-1
- Initial fedora RPM release
