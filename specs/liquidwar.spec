%define _hardened_build 1
Name:           liquidwar
Version:        5.6.5
Release:        18%{?dist}
Summary:        Multiplayer wargame with liquid armies
License:        GPL-2.0-or-later
URL:            http://www.ufoot.org/liquidwar/v5
Source0:        http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source2:        liquidwar.sysconfig
Source3:        liquidwar.logrotate
Source4:        liquidwar-server.service
Patch0:         liquidwar-5.6.5-python3.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel allegro-tools python3-devel
BuildRequires:	systemd
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Liquid War is a unique multiplayer wargame. You control an army of liquid
and have to try and eat your opponents. A single player mode is available,
but the game is definitely designed to be multiplayer, and has network
support.


%package doc
Summary:        Documentation for the LiquidWar game in additional formats
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains the documentation of LiquidWar in html, pdf, ps and txt
format.


%package server
Summary:        Network game server for the LiquidWar game
Requires:       %{name} = %{version}-%{release}
Requires(pre):  /usr/sbin/useradd

%description server
This package contains the server for hosting network LiquidWar games.


%prep
%setup -q

%patch -P0 -p0

# don't strip the binaries please
sed -i 's/install\(\s\+-c\)\?\s\+-s/install/g' Makefile.in
# fix README.* encoding
for i in de dk fr; do
  iconv -f ISO-8859-1 -t UTF8 README.$i > $i
  mv $i README.$i
done


%build
%configure --disable-target-opt \
  --disable-doc-pdf \
  --disable-doc-ps \
  --disable-doc-info \
%ifnarch %{ix86}
  --disable-asm \
%endif
LDFLAGS="%{__global_ldflags}"
CFLAGS="$RPM_OPT_FLAGS -fcommon -std=gnu17"
LDFLAGS="$LDFLAGS -lm"
PYTHON="%{__python3}"

MAKE_FLAGS="DEBUG_FLAGS= GAMEDIR=%{_bindir} DATADIR=%{_datadir}/%{name}"
# to show to compile flags with out MAKE_FLAGS
make config $MAKE_FLAGS LDFLAGS="$LDFLAGS" CFLAGS="$CFLAGS"
make %{?_smp_mflags} $MAKE_FLAGS LDFLAGS="$LDFLAGS" CFLAGS="$CFLAGS"

# make docs utf-8
iconv -f ISO-8859-1 -t UTF8 doc/man/%{name}.6 | gzip > doc/man/%{name}.6.gz
gzip -cd doc/info/%{name}.info.gz | \
  iconv -f ISO-8859-1 -t UTF8 > doc/info/%{name}.info
gzip -f doc/info/%{name}.info


%install
make install_nolink DESTDIR=$RPM_BUILD_ROOT GAMEDIR=%{_bindir} \
  DATADIR=%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} liquidwardocs
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm

# below is the desktop file and icon stuff.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications        \
  --add-category StrategyGame                          \
  --remove-category Application                        \
  --remove-category ArcadeGame                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{32x32,48x48}/apps
install -p -m 644 misc/%{name}_32x32.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -p -m 644 misc/%{name}.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm

install -p -D -m 755 %{SOURCE4} \
        $RPM_BUILD_ROOT/%{_unitdir}/%{name}-server.service
install -p -D -m 644 %{SOURCE2} \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}-server
install -p -D -m 644 %{SOURCE3} \
        $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}-server

%pre server
user_uid=`id -u %{name} 2>/dev/null`
if [ x"$user_uid" = x ] ; then
    /usr/sbin/useradd -r -s /sbin/nologin -d %{_datadir}/%{name} -M \
            -c 'LiquidWar Server' \
            %{name} >/dev/null || :
fi

%post server
%systemd_post liquidwar-server.service

%preun server
%systemd_post liquidwar-server.service

%postun server
%systemd_postun_with_restart liquidwar-server.service

%files
%license COPYING
%doc README*
%{_bindir}/%{name}
%{_bindir}/%{name}-mapgen
%{_datadir}/%{name}
%{_infodir}/%{name}.*
%{_mandir}/man6/%{name}.6.gz
%{_mandir}/man6/%{name}-mapgen.6.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.xpm

%files doc
%doc liquidwardocs/*

%files server
%{_bindir}/%{name}-server
%{_mandir}/man6/%{name}-server.6.gz
%{_unitdir}/liquidwar-server.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-server
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.6.5-13
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.6.5-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 5.6.5-5
- Fix FTBFS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.6.5-3
- Fix FTBTS.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.6.5-1
- 5.6.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.6.4-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 5.6.4-24
- systemd cleanup
- Patch for printf error.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Jon Ciesla <limburgher@gmail.com> - 5.6.4-18
- Fix reference to docdir, BZ 993858.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Jon Ciesla <limburgher@gmail.com> - 5.6.4-16
- Add PIE, BZ 955271.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 5.6.4-15
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 5.6.4-13
- Add hardened build.

* Mon Apr 09 2012 Jon Ciesla <limburgher@gmail.com> - 5.6.4-12
- Patch for server buffer overflow, BZ 810607.
- Changed unit file to simple.

* Mon Feb 13 2012 Jon Ciesla <limburgher@gmail.com> - 5.6.4-11
- Migrated to systemd, BZ 789757.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Jon Ciesla <limb@jcomserv.net> - 5.6.4-9
- Bump and rebuild for new Allegro.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 5.6.4-7
- FTBFS fix, BZ 599842.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.4-4
- Add missing BuildRequires:  desktop-file-utils

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.6.4-3
- Autorebuild for GCC 4.3

* Wed Dec 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.4-2
- Fix generation of debuginfo package (bz 413081)
- Fix encoding of README.* files

* Mon Oct 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.4-1
- New upstream release 5.6.4

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.3-4
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.3-3
- Fixup .desktop file categories for games-menus usage

* Thu Nov 23 2006 Wart <wart@kobold.org> 5.6.3-2
- Added init.d startup and logrotate scripts for the game server
- Put the game server in its own subpackage

* Sun Nov 19 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 5.6.3-1
- Initial Fedora Extras package
