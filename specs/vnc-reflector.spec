Name:       vnc-reflector
Version:    1.2.4 
Release:    41%{?dist}
Summary:    A specialized, multiplexing vnc proxy server
# LICENSE:  BSD-3-Clause
# region.c: MIT-open-group AND SMLNJ
License:    BSD-3-Clause AND MIT-open-group AND SMLNJ
URL:        http://sourceforge.net/projects/vnc-reflector
Source0:    http://dl.sf.net/vnc-reflector/vnc_reflector-%{version}.tar.gz
# Bug #569350, submitted to upstream
# <http://sourceforge.net/tracker/?func=detail&aid=2984246&group_id=38605&atid=422840>
Patch0:     %{name}-1.2.4-loggingfix.patch
# In upstream after 1.2.4 as commit r192
Patch1:     %{name}-1.2.4-rfb_format_buffer_overflow.patch
# Remove _LITTLE_ENDIAN identifier clash, bug #1125258, submitted to upstream
# <https://sourceforge.net/p/vnc-reflector/bugs/8/>
Patch2:     %{name}-1.2.4-unionfix.patch
# Respect compiler and linker flags, submitted to upstream
# <https://sourceforge.net/p/vnc-reflector/bugs/9/>
Patch3:     %{name}-1.2.4-Respect-external-CFLAGS-and-LDFLAGS.patch
# Adapt to GCC 15, bug #2341514, porposed upstream
# <>https://sourceforge.net/p/vnc-reflector/bugs/10/
Patch4:     %{name}-1.2.4-Port-to-ISO-C23.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  zlib-devel 

%description
Reflector is a specialized VNC server which acts as a proxy sitting between
real VNC server (a host) and a number of VNC clients. It was designed to work
efficiently with large number of clients.

%prep
%setup -q -n vnc_reflector
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1

%build
%{make_build} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS='%{__global_ldflags}'

%install
# No install target in the makefile.
install -D -t %{buildroot}%{_bindir} vncreflector

%files
%license LICENSE
%doc README ChangeLog
%{_bindir}/vncreflector

%changelog
* Fri Feb 14 2025 Petr Pisar <ppisar@redhat.com> - 1.2.4-41
- Adapt to GCC 15 (bug #2341514)
- Correct a license tag to "BSD-3-Clause AND MIT-open-group AND SMLNJ"

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-39
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 1.2.4-25
- Modernize spec file
- Respect compiler and linker flags

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Petr Pisar <ppisar@redhat.com> - 1.2.4-17
- Remove _LITTLE_ENDIAN identifier clashing on little-endian 64-bit PowerPC
  (bug #1125258)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.2.4-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2.4-12
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 Petr Pisar <ppisar@redhat.com> - 1.2.4-10
- Fix a crash when running on foreground (bug #569350)
- Fix a one-byte buffer overflow in formatting RFB version string
- Clean spec file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-5
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.2.4-4
- bump

* Fri Feb 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.2.4-3
- apply debuginfo fixes from BZ#225107

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.2.4-2
- bump for mass rebuild

* Wed Jun 14 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.2.4-1
- bump release to -1 for F-E builds
- change download source to a more generic sourceforgeish way

* Fri Jun 09 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.2.4-0
- Initial spec file for F-E
