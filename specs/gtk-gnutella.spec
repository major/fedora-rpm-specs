Name: gtk-gnutella
Summary: GUI based Gnutella Client
Version: 1.2.3
Release: 2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gtk-gnutella.sourceforge.net
Source0: http://sourceforge.net/projects/gtk-gnutella/files/gtk-gnutella-%{version}.tar.xz
Source1: gtk-gnutella-recalculate-sha1.sh
Patch0: gtk-gnutella-configure-c99.patch

BuildRequires: gcc

%if 0%{!?_with_gtk1:1}
BuildRequires: gtk2-devel, libglade2-devel
%else
BuildRequires: gtk+-devel, libglade-devel
%endif
BuildRequires: libxml2-devel, byacc, groff, gettext

BuildRequires: gnutls-devel >= 1.0.16, dbus-devel >= 0.35.2

BuildRequires: desktop-file-utils >= 0.2.90
BuildRequires: make


%description
Gtk-Gnutella is a GUI based Gnutella p2p servent. It's a fully featured  
servent designed to share any type of file.  Gtk-gnutella implements 
compressed gnutella net connections, ultrapeer and leaf nodes and uses 
Passive/Active Remote Queuing (PARQ), and other modern gnutella network 
features.


%prep
%autosetup -p1


%build
./Configure -O -Dprefix=%{_prefix} -Dbindir=%{_bindir} \
	-Dglibpth="/%{_lib} %{_libdir}" \
	-Dprivlib=%{_datadir}/%{name} -Dsysman=%{_mandir}/man1 \
	-Dccflags="%{optflags}" -Dcc="%{__cc}" -Dyacc="byacc" \
	-Dgtkversion=%{?_with_gtk1:1}%{!?_with_gtk1:2} \
	-Dofficial=true -ders
make #%{?_smp_mflags}


%install

%global	__os_install_post	%__os_install_post\
	%{SOURCE1} %{buildroot}%{_bindir}/%{name} %{buildroot}/%{_datadir}/%{name}/*-linux/%{name}.nm\
%{nil}

make install INSTALL_PREFIX=$RPM_BUILD_ROOT
make install.man INSTALL_PREFIX=$RPM_BUILD_ROOT

chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*

rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/*.svg
install -D -m 644 extra_files/gtk-gnutella.16.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.32.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.svg \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/gtk-gnutella.svg

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/gtk-gnutella
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%doc README TODO AUTHORS LICENSE GEO_LICENSE doc/other/shell.txt


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-1
- update to 1.2.3
- use __os_install_post for recalculate_sha1 insertion

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Florian Weimer <fweimer@redhat.com> - 1.2.2-4
- Port non-autoconf Configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.2-1
- update to 1.2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.1-1
- update to 1.2.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Jeff Law <law@redhat.com> - 1.2.0-3
- Re-enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.0-1
- Upgrade to 1.2.0
- re-calculate sha1 of the stripped binary at the end of the install stage
  (when it is actually stripped in the distribution's specific way)
- provide appdata file
- drop obsoleted scriptlets

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.15-2
- fix startup crash (#1787421)

* Fri Aug 16 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.15-1
- update to 1.1.15

* Sat May 25 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.14-1
- update to 1.1.14

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.13-1
- update to 1.1.13

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct  9 2017 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.12-1
- update to 1.1.12

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.11-1
- update to 1.1.11

* Thu Sep 22 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.10-1
- update to 1.1.10

* Sun Mar  6 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.9-1
- update to 1.1.9

* Tue Feb  9 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.8-1
- update to 1.1.8 (#1300181)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 19 2014 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.1-1
- Upgrade to 1.1.1

* Mon Dec 30 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.0.0-1
- Upgrade to 1.0.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Jon Ciesla <limburgher@gmail.com> - 0.98.4-3
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.98.4-1
- Upgrade to 0.98.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  2 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.97.1-1
- Upgrade to 0.97.1
- add upstream patch for zero fileindex

* Tue Apr 12 2011 Dan Horák <dan[at]danny.cz> - 0.96.9-2
- s390(x) has IEEE 754 floats

* Thu Mar 24 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.9-1
- update to 0.96.9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 29 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.8-1
- update to 0.96.8

* Tue Mar 16 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.7-1
- update to 0.96.7

* Thu Nov  5 2009 Bill Nottingham <notting@redhat.com> - 0.96.6-3
- Rebuild against new glibc headers (#533063)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.6-1
- update to 0.96.6

* Fri Sep 26 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.5-3
- pass compiler correctly for Configure script

* Wed Jun 25 2008 Tomas Mraz <tmraz@redhat.com> - 0.96.5-2
- rebuild with new gnutls

* Tue Apr  8 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.5-1
- update to 0.96.5

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.96.4-4
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.4-3
- Update hostiles.txt file to the latest upstream SVN version

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.96.4-2
- Rebuild for selinux ppc32 issue.

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Tue Jul 10 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.4-1
- update to 0.96.4

* Tue Jun 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- drop X-Fedora category from desktop file

* Tue Nov 14 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.3-2
- switch GNU TLS support on

* Mon Nov 13 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.3-1
- update to 0.96.3
- specify libdirs explicitly for Configure script (needed for x86_64)

* Mon Oct 23 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.2-1
- update to 0.96.2

* Fri Feb 24 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96.1-1
- update to 0.96.1

* Tue Jan 31 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.96-1
- upgrade to 0.96

* Fri Oct 28 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.95.4-2
- patch0: don't pre-strip binary on makeinstall (#171922)

* Mon Oct  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.95.4-1
- accepted for Fedora Extra
  (review by Aurelien Bompard <gauret@free.fr>)

* Wed Sep 28 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.95.4-1
- Upgrade to 0.95.4
- spec file cleanups for Fedora Extras
- build with gtk2 by default, or specify "--with gtk1" for rpmbuild

* Mon Jul 12 2004 Simon Perreault <nomis80@nomis80.org> - 0.94-1.gtk2
- Update to 0.94

* Sun Jun 13 2004 Simon Perreault <nomis80@nomis80.org> - 0.93.4-1.gtk2
- Update to 0.93.4

* Mon Jan 26 2004 Simon Perreault <nomis80@nomis80.org> - 0.93.3-2.gtk2
- Replaced bison with byacc, needed for Fedora
- BuildPrereq: -> BuildRequires:
- Misc RPM cleanups

* Sun Jan 25 2004 Murphy <eqom14@users.sourceforge.net>
- 0.93.3
- Added -O option to Configure to override any symbols in config.sh from a previous config. Thanks to Aaron Sherman for pointing out the problem. 
- Removed INSTALLFLAGS option to make install since that bug was fixed (regular files don't get +x anymore.)

* Tue Jan 06 2004 Murphy <eqom14@users.sourceforge.net>
- 0.93.2
- First ChangeLog entry in a while.

* Tue Dec 11 2001 Sam Varshavchik <mrsam@courier-mta.com>
- Initial build.
