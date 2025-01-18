%bcond_with	dvdrom

Summary: Additional error protection for CD/DVD media
Name: dvdisaster
Version: 0.79.5
Release: 22%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://dvdisaster.net
Source0: http://dvdisaster.net/downloads/dvdisaster-%{version}.tar.bz2

# Nothing illegal, just a scratch wiping from the media
# (legally bought) with a probably copyrighted content,
# but see http://bugzilla.redhat.com/231574 why it is
# not enabled by default...
Patch1: dvdisaster-0.79.5-dvdrom.patch

Patch0: dvdisaster-configure-c99.patch

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: gtk2-devel >= 2.6.0
BuildRequires: gettext, desktop-file-utils
BuildRequires: bzip2-devel, libpng-devel
BuildRequires: make
Requires: xdg-utils


%description
%{name} provides a margin of safety against data loss on CD and DVD media
caused by scratches or aging. It creates error correction data,
which is used to recover unreadable sectors if the disc becomes damaged
at a later time.


%description -l de
%{name} erzeugt einen Sicherheitspuffer gegen Datenverluste, die auf
CD- und DVD-Datenträgern durch Alterung oder Kratzer entstehen. Es erzeugt
Fehlerkorrekturdaten, um bei nachfolgenden Datenträger-Problemen unlesbare
Sektoren zu rekonstruieren.


%description -l it
%{name} offre un margine di sicurezza contro la perdita di dati dei supporti
CD e DVD causata dall'invecchiamento e dai graffi. Crea dei dati di correzione
degli errori che saranno poi utilizzati per recuperare i settori illeggibili
se il supporto dovesse danneggiarsi col tempo.


%description -l cs
%{name} poskytuje dodatečnou ochranu proti ztrátě dat na médiích CD a DVD
způsobených poškrábáním nebo stárnutím. Vytváří data oprav chyb, která
jsou použita pro obnovu nečitelných sektorů, pokud se disk později
poškodí.


%prep
%setup -q
%{?_with_dvdrom:%patch1 -p1 -b .dvdrom}
%patch -P0 -p1

%build

export CFLAGS="$RPM_OPT_FLAGS -fcommon"

%configure	\
	--docdir=%{_docdir} \
	--docsubdir=%{name} \
	--localedir=%{_datadir}/locale

# can not build locales with %{?_smp_mflags}
make


%install

make install BUILDROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/*-uninstall.sh

install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m644 -D contrib/dvdisaster48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/dvdisaster48.png

for NN in 16 24 32 48 64
do
    install -p -m644 -D contrib/dvdisaster${NN}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${NN}x${NN}/apps/dvdisaster${NN}.png
done

desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications	\
	--add-category=AudioVideo \
	--add-category=DiscBurning \
	contrib/%{name}.desktop
	
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%{_docdir}/%{name}
%lang(de) %{_docdir}/%{name}/CREDITS.de

%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.79.5-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Florian Weimer <fweimer@redhat.com> - 0.79.5-15
- Port configure script to C99 (#2159453)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Use gcc -fcommon flag to build

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.79.5-1
- Upgrade to 0.79.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.72.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.5-1
- update to 0.72.5
- fix format-security issue (#1037046)

* Thu Aug  8 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.4-3
- Use unversioned docdir (#993736)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar  5 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.4-1
- update to 0.72.4

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.72.3-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix bogus date in changelog

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.3-1
- Update to 0.72.3
- Fix build with glib2 >= 2.31

* Fri Mar 25 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.2-1
- Update to 0.72.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 19 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72.1-1
- Update to 0.72.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.72-1
- Upgrade to 0.72

* Tue Apr  8 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.6-1
- Update to 0.70.6

* Tue Mar  4 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.5-1
- Update to 0.70.5

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70.4-4
- Autorebuild for GCC 4.3

* Tue Nov  6 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.4-3
- Add xdg-open patch (by Ville Skytta, #365401)

* Tue Aug 28 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Correct Source0 url

* Thu Aug 16 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Tue Jun 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- drop X-Fedora category from desktop file

* Mon Mar 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.4-2
- own root docdir too (#233832)

* Fri Feb 16 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.4-1
- update to 0.70.4

* Fri Dec 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.3-1
- update to 0.70.3

* Mon Oct 23 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.2-1
- update to 0.70.2

* Mon Sep 11 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70.1-1
- update to 0.70.1
- add two upstream's pre-0.70.2 patches.

* Mon Jul 24 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.70-1
- upgrade to 0.70

* Fri Mar 31 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.66-2
- fix pixmap icon name

* Thu Mar 30 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.66-1
- upgrade to 0.66
- spec file changes/cleanups, merged from a skeleton now included upstream
- still specify dirs explicitly on install due to typo in GNUmakefile
- remove unneeded uninstall.sh script after install

* Tue Jan 31 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.65-1
- upgrade to 0.65
- drop browser patch (no more needed)
- drop manual convertations to utf8 -- already in good encodings.
- handle new locale (czech)

* Thu Nov  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.64.2-2
- use user preferred browser to view manuals online (patch0)
- Accepted for Fedora Extra (review by Ville Skytta <ville.skytta@iki.fi>)

* Wed Nov  2 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.64.2-1
- update to 0.64.2
- drop the patches (no more needed).

* Thu Oct 27 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.64-3
- add 0.64-pl1 patch, generated by upstream "0.64-1" version
  (do not include new version tarball itself due to bad versioning scheme).
- remove StartupNotify from .desktop file at all.
- add patch1 -- do not create files with executable bit set.

* Sat Oct 22 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.64-2
- spec file cleanups
- build and install stages correct

* Fri Oct 21 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.64-1
- initial release
- convert locale manuals to utf8
- add desktop file

