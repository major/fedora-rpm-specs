%define _legacy_common_support 1
Name:		simh
Version:	3.11.0
Release:	27%{?dist}
Summary:	A highly portable, multi-system emulator

#The licensing is mostly MIT, but there is also some GPL+ (literally, v1+) code
#in there, notably in AltairZ80/.
#(each target is compiled into its own binary, so only AltairZ80 is GPL+)
# Automatically converted from old format: MIT and GPL+ - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND GPL-1.0-or-later

URL:		http://simh.trailing-edge.com/
Source0:	simh-%{version}-noroms.tar.gz
# we use
# this script to remove the roms binary and patented code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./simh-generate-tarball.sh 3.8.1
Source1:	simh-generate-tarball.sh
Patch0:		simh-3.11.0-crl.patch


BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libpcap-devel, dos2unix
#Requires:

%description
SIMH is a historical computer simulation system. It consists of simulators
for many different computers, all written around a common user
interface package and set of supporting libraries.
SIMH can be used to simulate any computer system for which sufficient detail
is available, but the focus to date has been on simulating computer systems
of historic interest.

SIMH implements simulators for:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9, PDP-10,
  PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

%prep
%setup -qn %{name}-%{version}/sim
%patch -P0 -p2


%build
mkdir -p BIN
CC="$CC -I . -fPIE -g"
LDFLAGS="$LDFLAGS -lm"
make %{?_smp_mflags} -e ROMS_OPT="%{optflags}" USE_NETWORK=1


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in `ls BIN/`; do
	install -p -m 755 BIN/$i $RPM_BUILD_ROOT%{_bindir}/simh-$i
done
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
for i in `find -iname "*.txt"`; do dos2unix -k $i; done


%files
%{_bindir}/*
%doc ALTAIR/altair.txt NOVA/eclipse.txt 0readme_311.txt 0readme_ethernet.txt
%doc I7094/i7094_bug_history.txt Interdata/id_diag.txt
%doc PDP1/pdp1_diag.txt PDP10/pdp10_bug_history.txt PDP18B/pdp18b_diag.txt
%doc S3/haltguide.txt S3/readme_s3.txt S3/system3.txt SDS/sds_diag.txt
%doc VAX/vax780_bug_history.txt


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.11.0-26
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Lucian Langa <lucilanga@gnome.eu.org> - 3.11.0-22
- forgot the patch file in previous commit

* Tue Jan 24 2023 Lucian Langa <lucilanga@gnome.eu.org> - 3.11.0-21
- add patch from Joshua Cogliati <jrincayc@yahoo.com> to fix FTBFS
- update build flags

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Lucian Langa <lucilanga@gnome.eu.org> - 3.9.0-14
- update generation script
- apply temporary gcc10 fix
- update to latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Lucian Langa <cooly@gnome.eu.org> - 3.9.0-1
- sync with latest upstream stable
- drop all patches - fixed upstream
- fix bogus dates

* Tue Aug 06 2013 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-11
- don't create versioned docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 19 2010 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-6
- bump rel to fix NVR higher than previous version

* Sat Jan 09 2010 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-5
- fix altair segfault

* Tue Nov 17 2009 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-4
- add correct source

* Fri Nov 13 2009 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-3
- update description

* Sun Nov 08 2009 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-2
- add correct generate script

* Thu Oct 08 2009 Lucian Langa <cooly@gnome.eu.org> - 3.8.1-1
- remove separate docs
- misc cleanups
- new upstream release

* Wed Dec 24 2008 Lucian Langa <cooly@gnome.eu.org> - 3.8.0-1
- initial spec file


