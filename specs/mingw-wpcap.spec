%{?mingw_package_header}

%global versionmajor 4
%global versionminor 1
%global versionsuffix 3

%global wpcapexamples %{_docdir}/%{name}/examples
%global wpcapdoc %{_docdir}/%{name}

Name:           mingw-wpcap
Version:        %{versionmajor}.%{versionminor}.final%{versionsuffix}
Release:        23%{?dist}
Summary:        MinGW user-level packet capture

# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            http://www.winpcap.org/
Source0:        http://www.winpcap.org/install/bin/WpcapSrc_%{versionmajor}_%{versionminor}_%{versionsuffix}.zip
Source1:        wpcap.pc
Source2:        wpcap64.pc
Patch0:         wpcap.patch
Patch1:         wpcap-w2k.patch
Patch2:         winpcap-mingw-w64-compatibility.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  doxygen
BuildRequires:  unzip
BuildRequires:  dos2unix
BuildRequires:  bison
BuildRequires:  flex

%description
MinGW Windows pcap library.

%package -n mingw32-wpcap
Summary:        MinGW user-level packet capture

%description -n mingw32-wpcap
MinGW Windows pcap library.

%package -n mingw32-wpcap-examples
Summary:        Example source code for MinGW pcap
Requires:       mingw32-wpcap = %{version}

%description -n mingw32-wpcap-examples
This package contains examples on the usage of the Windows pcap
library.

%package -n mingw32-wpcap-docs
Summary:        MinGW pcap documentation
Requires:       mingw32-wpcap = %{version}

%description -n mingw32-wpcap-docs
This package contains the Windows pcap library documentation.

%package -n mingw64-wpcap
Summary:        MinGW user-level packet capture

%description -n mingw64-wpcap
MinGW Windows pcap library.

%{?mingw_debug_package}

%prep
%setup -q -n winpcap

%patch -P0 -p0 -b .build
%patch -P2 -p0 -b .mingw-w64

find . -type f -print0 |xargs -0 dos2unix
pushd wpcap/libpcap/Win32/Include/
mv ip6_misc.h IP6_misc.h
popd

%patch -P1 -p0 -b .w2k

find . -name GNUmakefile |xargs perl -i -pe 's,-mno-cygwin,,'

# Prevent a conflict between getaddrinfo.c and ws2_32
sed -i s@../libpcap/Win32/Src/getaddrinfo.o@@ wpcap/PRJ/GNUmakefile

mkdir build64
cp -r packetNtx wpcap Common build64


%build
pushd packetNtx/Dll/Project
make -f GNUmakefile CC=i686-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd wpcap/PRJ
make -f GNUmakefile CC=i686-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd build64/packetNtx/Dll/Project
make -f GNUmakefile CC=x86_64-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd build64/wpcap/PRJ
make -f GNUmakefile CC=x86_64-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd dox/prj
doxygen winpcap_noc.dox
popd


%install
# mingw32
install -d $RPM_BUILD_ROOT/%{mingw32_bindir}
install -d $RPM_BUILD_ROOT/%{mingw32_libdir}/pkgconfig
install -m0644 %{SOURCE1} $RPM_BUILD_ROOT/%{mingw32_libdir}/pkgconfig
install -m0644 packetNtx/Dll/Project/libpacket.a $RPM_BUILD_ROOT/%{mingw32_libdir}/libpacket.dll.a
install -m0644 packetNtx/Dll/Project/Packet.dll $RPM_BUILD_ROOT/%{mingw32_bindir}/packet.dll
install -m0644 wpcap/lib/libwpcap.a $RPM_BUILD_ROOT/%{mingw32_libdir}/libwpcap.dll.a
install -m0644 wpcap/PRJ/wpcap.dll $RPM_BUILD_ROOT/%{mingw32_bindir}
install -m0644 packetNtx/Dll/Packet.def $RPM_BUILD_ROOT/%{mingw32_libdir}/packet.def
install -m0644 wpcap/PRJ/WPCAP.DEF $RPM_BUILD_ROOT/%{mingw32_libdir}/wpcap.def
install -d $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap/*.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-int.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-bpf.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-namedb.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/remote-ext.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-stdinc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/Win32-Extensions/Win32-Extensions.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/bittypes.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/IP6_misc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/Gnuc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 Common/Packet32.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
# mingw64
install -d $RPM_BUILD_ROOT/%{mingw64_bindir}
install -d $RPM_BUILD_ROOT/%{mingw64_libdir}/pkgconfig
install -m0644 %{SOURCE2} $RPM_BUILD_ROOT/%{mingw64_libdir}/pkgconfig/wpcap.pc
install -m0644 build64/packetNtx/Dll/Project/libpacket.a $RPM_BUILD_ROOT/%{mingw64_libdir}/libpacket.dll.a
install -m0644 build64/packetNtx/Dll/Project/Packet.dll $RPM_BUILD_ROOT/%{mingw64_bindir}/packet.dll
install -m0644 build64/wpcap/lib/libwpcap.a $RPM_BUILD_ROOT/%{mingw64_libdir}/libwpcap.dll.a
install -m0644 build64/wpcap/PRJ/wpcap.dll $RPM_BUILD_ROOT/%{mingw64_bindir}
install -m0644 build64/packetNtx/Dll/Packet.def $RPM_BUILD_ROOT/%{mingw64_libdir}/packet.def
install -m0644 build64/wpcap/PRJ/WPCAP.DEF $RPM_BUILD_ROOT/%{mingw64_libdir}/wpcap.def
install -d $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/pcap
install -m0644 build64/wpcap/libpcap/pcap/*.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/pcap
install -m0644 build64/wpcap/libpcap/pcap.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-int.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-bpf.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-namedb.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/remote-ext.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-stdinc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/Win32-Extensions/Win32-Extensions.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/bittypes.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/IP6_misc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/Gnuc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/Common/Packet32.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
# doc
install -d $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/WinPcap_docs.html $RPM_BUILD_ROOT/%{wpcapdoc}/
install -m0644 dox/prj/docs/* $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/pics/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
# examples
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
cp -r Examples $RPM_BUILD_ROOT/%{wpcapexamples}/remote
cp -r Examples-pcap $RPM_BUILD_ROOT/%{wpcapexamples}/pcap
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/NetMeter
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/kdump
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/winpcap_stress
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/stats


%files -n mingw32-wpcap
%doc wpcap/libpcap/LICENSE
%{mingw32_libdir}/pkgconfig/wpcap.pc
%{mingw32_bindir}/packet.dll
%{mingw32_bindir}/wpcap.dll
%{mingw32_libdir}/libpacket.dll.a
%{mingw32_libdir}/libwpcap.dll.a
%{mingw32_libdir}/packet.def
%{mingw32_libdir}/wpcap.def
%{mingw32_includedir}/wpcap

%files -n mingw32-wpcap-docs
%{wpcapdoc}/WinPcap_docs.html
%{wpcapdoc}/html

%files -n mingw32-wpcap-examples
%{wpcapexamples}

%files -n mingw64-wpcap
%doc build64/wpcap/libpcap/LICENSE
%{mingw64_libdir}/pkgconfig/wpcap.pc
%{mingw64_bindir}/packet.dll
%{mingw64_bindir}/wpcap.dll
%{mingw64_libdir}/libpacket.dll.a
%{mingw64_libdir}/libwpcap.dll.a
%{mingw64_libdir}/packet.def
%{mingw64_libdir}/wpcap.def
%{mingw64_includedir}/wpcap

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.final3-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.1.final3-16
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 4.1.final3-10
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.final3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 04 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final3-1
- update to 4.1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final2-10
- avoid getaddrinfo (W2k does not provide it)

* Mon Nov 19 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final2-9
- avoid freeaddrinfo (W2k does not provide it)

* Fri Aug 17 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final2-8
- enable 64bit build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 4.1.final2-6
- Renamed the source package to mingw-wpcap (#801038)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.1.final2-5
- Rebuild against the mingw-w64 toolchain
- Added a patch to fix compatibility with the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final2-3
- fix build
- make wpcap.dll work again on Windows 2000

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.final2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final2-1
- update to 4.1.2
- examples and docs subpackages require base package for licensing reasons

* Tue Nov 10 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.final1-1
- update to 4.1.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.beta5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-8
- fix BR

* Wed Jul 15 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-7
- fix BR

* Tue Jun 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-6
- fix debuginfo package generation

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-5
- add debuginfo packages

* Fri Jun 12 2009 Richard W.M. Jones <rjones@redhat.com> - 4.1.beta5-4
- Doesn't work with byacc, needs bison.
- Some minor cleanups to the spec file.

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-3
- replace %%define with %%global

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-2
- fix BR
- add license file
- rename implibs

* Mon Feb 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.1.beta5-1
- initial package
