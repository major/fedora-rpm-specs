Name:		splat
Version:	1.4.2
Release:	23%{?dist}
Summary:	Analyze point-to-point terrestrial RF communication links
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

URL:		http://www.qsl.net/kd2bd/%{name}.html
Source0:	http://www.qsl.net/kd2bd/%{name}-%{version}.tar.bz2

# Man pages for utilities, generated from utils README file
Source1:	citydecoder.man
Source2:	srtm2sdf.man
Source3:	usgs2sdf.man
Source4:	bearing.man
Source5:	postdownload.1
Source6:        splat.1

# Configuration parameters
Source7:        std-parms.h
Source8:        hd-parms.h

# Build flags patch
Patch0:		%{name}-%{version}-build_flags.patch

BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
BuildRequires:	groff
BuildRequires:	zlib-devel


%description
SPLAT! is a Surface Path Length And Terrain analysis application written for
Linux and Unix workstations. SPLAT! analyzes point-to-point terrestrial RF 
communication links, and provides information useful to communication system
designers and site engineers.

%prep
%setup -q
%patch -P0 -p1

install -p %{SOURCE7} .
%ifarch x86_64
install -p %{SOURCE8} .
%endif

# Fix end of line encoding
sed -i 's/\r//' utils/fips.txt


%build
# Uses custom build scripts
./build all


%install
# Build additional man pages
mkdir -p %{buildroot}%{_mandir}/man1/
groff -e -T ascii -man %{SOURCE1} > %{buildroot}%{_mandir}/man1/citydecoder.1
groff -e -T ascii -man %{SOURCE2} > %{buildroot}%{_mandir}/man1/srtm2sdf.1
groff -e -T ascii -man %{SOURCE3} > %{buildroot}%{_mandir}/man1/usgs2sdf.1
groff -e -T ascii -man %{SOURCE4} > %{buildroot}%{_mandir}/man1/bearing.1
install -pm 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/postdownload.1
install -pm 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/splat.1
install -D -pm 0644 docs/spanish/man/%{name}.1 %{buildroot}%{_mandir}/es/man1/splat.1

# Manual install, easier than patching upstream custom install script
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%ifarch x86_64
install -D -m 0755 %{name}-hd %{buildroot}%{_bindir}/%{name}-hd
%endif

# Install utils
install -D -m 0755 utils/citydecoder %{buildroot}%{_bindir}/citydecoder
install -D -m 0755 utils/bearing %{buildroot}%{_bindir}/bearing
install -D -m 0755 utils/postdownload %{buildroot}%{_bindir}/postdownload
install -D -m 0755 utils/usgs2sdf %{buildroot}%{_bindir}/usgs2sdf
install -D -m 0755 utils/srtm2sdf %{buildroot}%{_bindir}/srtm2sdf

# Rename this to avoid conflict with main readme
mv utils/README utils/README-utils


%files
%license COPYING
%doc CHANGES README utils/README-utils utils/fips.txt
%doc sample_data
%{_bindir}/*
%{_mandir}/es/man1/*
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.2-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-3
- Add fixed man pages to package, fixes BZ#1098421.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-1
- Update to latest upstream release, fixes BZ#1098419.
- Build splat-hd.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 1.4.0-1
- New upstream release. 1.4.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug  7 2010 Randall J. Berry <dp67@fedoraproject.org> - 1.3.0-3
- Added more macros to name and version.
- Cleanup spec
- Patch build file in utils with rpm_opt_flags
- Left rm -rf RPM_BUILD_ROOT for potential EPEL build

* Thu Aug  5 2010 Randall J. Berry <dp67@fedoraproject.org> - 1.3.0-2
- Build with $RPM_OPT_FLAGS bz #621371
- Remove unnecessary BuildRequires: desktop-file-utils
- Add additional man pages
- Added BuildRequires: zlib-devel for fontdata bz #621371
- Replace non-ascii characters in man pages

* Sun Aug  1 2010 Randall J. Berry <dp67@fedoraproject.org> - 1.3.0-1
- Upstream update 1.3.0
- Rebuild for F13/F14/Devel
- Clean up spec.
- Several files changed on newer version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Randall J. Berry <dp67@fedoraproject.org> - 1.2.3-6
- Update CVS
- Build with $RPM_OPT_FLAGS.
- Submit update fix bug #736499

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.2.3-5
- Build with $RPM_OPT_FLAGS.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 1.2.3-3
- fix broken obsoletes

* Sun Dec 22 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 1.2.3-2
- Merge main and -utils package, #475009

* Wed Jul 30 2008 Steve Conklin <fedora@conklinhouse.com> - 1.2.3-1
- New upstream
- added delivery of postdownload script and the new bearing utility
- added man pages for bearing and postdownload
* Thu Feb 28 2008 Steve Conklin <sconklin at redhat dot com> - 1.2.1-6
- Silly, there's no gui. Removed desktop and icon files.
* Thu Feb 28 2008 Steve Conklin <sconklin at redhat dot com> - 1.2.1-5
- installed desktop and icon files with main package, not utils

* Tue Feb 26 2008 Steve Conklin <sconklin at redhat dot com> - 1.2.1-4
- removed erroneous -march flag for ppc

* Mon Feb 25 2008 Steve Conklin <sconklin at redhat dot com> - 1.2.1-3
- Fixed declaration that the new gcc didn't like

* Tue Feb 19 2008 Steve Conklin <sconklin at redhat dot com> - 1.2.1-2
- Added desktop file and icon

* Sun Dec 09 2007 Sindre Pedersen Bjørdal - 1.2.1-1
- Initial Build
