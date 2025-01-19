Summary:	High-level API (toolkit) to construct and inject network packets
Name:		libnet10
Version:	1.0.2a
Release:	47%{?dist}
License:	BSD-2-Clause AND BSD-4-Clause-UC
URL:		http://www.packetfactory.net/libnet/
Source0:	http://www.packetfactory.net/libnet/dist/deprecated/libnet-%{version}.tar.gz
Source1:	libnet10-config.1
Patch0:		libnet10-1.0.2a-fedora.patch
Patch1:		libnet10-1.0.2a-gcc33.patch
Patch2:		libnet10-1.0.2a-c99.patch
BuildRequires:	gcc, libpcap-devel, make, libtool, autoconf, automake

%description
Libnet is a high-level API (toolkit) allowing the application programmer to
construct and inject network packets. It provides a portable and simplified
interface for low-level network packet shaping, handling and injection. Libnet
hides much of the tedium of packet creation from the application programmer
such as multiplexing, buffer management, arcane packet header information,
byte-ordering, OS-dependent issues and much more. Libnet features portable
packet creation interfaces at the IP layer and link layer, as well as a host
of supplementary and complementary functionality.

This package contains an old and deprecated version of libnet. You need it
only if the software you are using hasn't been updated to work with the newer
version and the newer API.

%package devel
Summary:	Development files for the libnet library
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libnet10-devel package includes header files and libraries necessary for
developing programs which use the libnet library. Using libnet, quick and
simple packet assembly applications can be whipped up with little effort.
With a bit more time, more complex programs can be written (traceroute and
ping were easily rewritten using libnet and libpcap).

This package contains an old and deprecated version of libnet. You need it
only if the software you are using hasn't been updated to work with the newer
version and the newer API.

%prep
%setup -q -n Libnet-%{version}
%patch -P0 -p1 -b .fedora
%patch -P1 -p1 -b .gcc33
%patch -P2 -p1 -b .c99

# Required to apply changes from Patch0
autoreconf -i -f

%build
%configure --with-pf_packet=yes
%make_build

%install
%make_install

# Complete the package renaming at missing places
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}/
mv -f $RPM_BUILD_ROOT%{_includedir}/{libnet{,.h},%{name}}
mv -f $RPM_BUILD_ROOT%{_bindir}/libnet{,10}-config

# Install all man pages to their appropriate place
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,3}/
install -p -m 644 doc/libnet.3 $RPM_BUILD_ROOT%{_mandir}/man3/%{name}.3
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}-config.1

# Don't install any static .a and libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.{a,la}

%ldconfig_scriptlets

%files
%license doc/COPYING
%doc README doc/CHANGELOG
%{_libdir}/%{name}.so.*
%{_mandir}/man3/%{name}.3*

%files devel
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_mandir}/man1/%{name}-config.1*
%{_includedir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Arjun Shankar <arjun@redhat.com> - 1.0.2a-42
- Port to C99 (#2190051)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Robert Scheck <robert@fedoraproject.org> 1.0.2a-17
- Enabled a shared library and made lots of spec file cleanups

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.0.2a-16
- Rebuild against gcc 4.4 and rpm 4.6

* Sun Jun 15 2008 Patrice Dumas <pertusus@free.fr> - 1.0.2a-15
- copy config.* from rpm directory, those shpped with libnet10 are too old

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2a-14
- Autorebuild for GCC 4.3

* Mon May  7 2007 Patrice Dumas <pertusus@free.fr> - 1.0.2a-13
- add a libnet-1.0 directory with a libnet.a link to the library

* Tue Aug 29 2006 Patrice Dumas <pertusus@free.fr> - 1.0.2a-12
- rename gcc33.patch to libnet10-gcc33.patch
- patch to have a version parallel installable with libnet (#229297),
  correct perms and keep timestamps
- remove Obsoletes and Provides for libnet and libnet-devel (#229297)

* Tue Aug 29 2006 Patrice Dumas <pertusus@free.fr> - 1.0.2a-11
- rebuild for FC6

* Fri Feb 17 2006 Patrice Dumas <pertusus@free.fr> - 1.0.2a-10
- rebuild for fc5

* Wed Feb  1 2006 Patrice Dumas <pertusus@free.fr> - 1.0.2a-9
- rebuild

* Sun Aug 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2a-8
- add versioned Obsoletes/Provides for libnet and libnet-devel
  so libnet/libnet-devel >= 1.1.0 upgrade this and don't just conflict
- pass CFLAGS to make explicitly

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.2a-7
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Sep 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.5
- Fixed last header file permission.

* Mon Sep 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.4
- Spec patch from Michael Schwendt (header file permissions)

* Sun Sep 07 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.3
- Fixed file permissions.

* Wed Jul 30 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.2
- gcc33 patch from Enrico Scholz.
- no longer need gcc32.
- spec same for shrike and severn.
- renamed spec to libnet10.spec.

* Fri Jul 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.1
- shrke vs severn differentiation
- buildroot -> RPM_BUILD_ROOT.
- Renamed to libnet10.
- Provides libnet
- Obsoletes libnet < 1.1.0.
- BuildReq gcc32 for severn.

* Mon Apr 07 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2a-0.fdr.1
- Initial Release.
