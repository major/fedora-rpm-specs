Name:		cpmtools
Version:	2.23
Release:	9%{?dist}
Summary:	Programs for accessing CP/M disks

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.moria.de/~michael/cpmtools/
Source0:	http://www.moria.de/~michael/cpmtools/files/cpmtools-%{version}.tar.gz
Patch0:		cpmtools-2.23-nostrip.patch
Patch1: cpmtools-configure-c99.patch

BuildRequires:	gcc
BuildRequires:	ncurses-devel, libdsk-devel
BuildRequires:	make
#Requires:

%description
This package allows to access CP/M file systems similar to the well-known
mtools package, which accesses MSDOS file systems. I use it for file
exchange with a Z80-PC simulator, but it works on floppy devices as well.


%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .nostrip
%patch -P1 -p1
sed -i -e "s!@datarootdir@/diskdefs!\$\(DATADIR\)/diskdefs!" Makefile.in
#modify path contained in man files
sed -i -e "s!@DATADIR@!%{_datadir}/%{name}!" *.1.in


%build
%configure --datarootdir=%{_datadir}/%{name} --with-libdsk
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
make install BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir} DATADIR=$RPM_BUILD_ROOT%{_datadir}/%{name} INSTALL="install -p"



%files
%doc COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.23-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 2.23-2
- Port configure script to C99 (#2155164)

* Wed Dec 07 2022 Lucian Langa <lucilanga@gnome.eu.org> - 2.23-1
- update to latest upstream

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Lucian Langa <lucilanga@gnome.eu.org> - 2.22-1
- sync with latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Lucian Langa <lucilanga@gnome.eu.org> - 2.20-9
- rebuilt for newer libdsk

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Lucian Langa <lucilanga@gnome.eu.org> - 2.20-1
- sync with latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Lucian Langa <cooly@gnome.eu.org> - 2.19-1
- update to latest upstream

* Fri Jan 24 2014 Lucian Langa <cooly@gnome.eu.org> - 2.17-1
- sync with latest upstream release
- spec file cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Lucian Langa <cooly@gnome.eu.org> - 2.13-1
- build with libdsk support
- new upstream release

* Thu Mar 18 2010 Lucian Langa <cooly@gnome.eu.org> - 2.12-1
- drop patch1 (fixed upstream)
- new upstream release

* Tue Dec 01 2009 Lucian Langa <cooly@gnome.eu.org> - 2.11-2
- patch to fix crash in cpmcp

* Sun Nov 29 2009 Lucian Langa <cooly@gnome.eu.org> - 2.11-1
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Lucian Langa <cooly@gnome.eu.org> - 2.8-2
- place diskdefs under correct location

* Sat Jan 17 2009 Lucian Langa <cooly@gnome.eu.org> - 2.8-1
- initial package


