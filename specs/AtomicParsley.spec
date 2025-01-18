Summary:   Command-line program to read and set MPEG-4 tags compatible with iPod/iTunes 
URL:       http://atomicparsley.sourceforge.net/
Name:      AtomicParsley
Version:   0.9.5
Release:   28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
Source0:   https://bitbucket.org/wez/atomicparsley/overview/%{name}-%{version}.tar.gz
#Patch0:    %{name}-fix_bad_math.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: perl-generators

# Need the following to not fail on Koji build on x86_64
BuildRequires: zlib-devel
BuildRequires: make



%description
AtomicParsley is a command line program for reading, parsing and setting
tags and meta-data into MPEG-4 files supporting these styles of meta-data:

* iTunes-style meta-data into .mp4, .m4a, .m4p, .m4v, .m4b files
* 3gp-style assets (3GPP TS 26.444 version 6.4.0 Release 6 specification
  conforming) in 3GPP, 3GPP2, MobileMP4 & derivatives
* ISO copyright notices at movie & track level for MPEG-4 & derivative files
* uuid private user extension text & file embedding for MPEG-4 & derivative
  files


%prep
%setup -q

%build
./autogen.sh
%configure --prefix=%{_prefix}
#OPTFLAGS="%{optflags} -Wall -Wno-parentheses -Wno-unused-result -Wno-write-strings -Wno-deprecated -fno-strict-aliasing" \
make %{?_smp_mflags}

%install
make install install DESTDIR=%{buildroot} BINDIR=%{_bindir}
#install -D -m0755 AtomicParsley "%{buildroot}%{_bindir}/AtomicParsley"


%files
%doc COPYING Changes.txt tools/iTunMOVI-1.1.pl
%{_bindir}/AtomicParsley

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.5-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Avi Alkalay <avi@unix.sh> 0.9.5-2
- Updated from new upstream on https://bitbucket.org/wez/atomicparsley
- Added BuildRequires for zlib-devel, for Koji

* Tue Jan 28 2014 Avi Alkalay <avi@unix.sh> 0.9.0-13
- Reduced warnings
- Adapted SPEC to build on Fedora 20

* Mon Oct 01 2012 Avi Alkalay <avi@unix.sh> 0.9.0-12
- Editing with comments from https://bugzilla.redhat.com/show_bug.cgi?id=800284#c7

* Mon Oct 01 2012 Avi Alkalay <avi@unix.sh> 0.9.0-11
- Editing with comments from https://bugzilla.redhat.com/show_bug.cgi?id=800284#c5

* Tue Sep 25 2012 Avi Alkalay <avi@unix.sh> 0.9.0-10
- Editing with comments from https://bugzilla.redhat.com/show_bug.cgi?id=800284#c3

* Fri Mar 02 2012 Avi Alkalay <avi@unix.sh> 0.9.0-9
- Editing with comments from https://bugzilla.rpmfusion.org/show_bug.cgi?id=2190#c1

* Wed Feb 22 2012 Avi Alkalay <avi@unix.sh> 0.9.0-7
- RPM and patches adapted and built for Fedora 16 based on Madriva SRPM

* Thu Jul 22 2010 pascal@links2linux.de
- initial package (0.9.0)

