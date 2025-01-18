Summary:        Tools for network auditing and penetration testing
Name:           dsniff
Version:        2.4
Release:        0.46.b1%{?dist}
# dsniff itself is BSD-3-Clause but uses other source codes, breakdown:
# BSD-4-Clause-UC: missing/{err.[ch],{memcmp,strsep}.c,sys/queue.h}
# ISC: base64.[ch]
# LicenseRef-Fedora-Public-Domain: missing/md5.[ch]
# MIT: remote.c
License:        BSD-3-Clause AND BSD-4-Clause-UC AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.monkey.org/~dugsong/%{name}/
Source0:        https://www.monkey.org/~dugsong/%{name}/beta/%{name}-%{version}b1.tar.gz
Patch0:         dsniff-2.4-time_h.patch
Patch1:         dsniff-2.4-mailsnarf_corrupt.patch
Patch2:         dsniff-2.4-pcap_read_dump.patch
Patch3:         dsniff-2.4-multiple_intf.patch
Patch4:         dsniff-2.4-amd64_fix.patch
Patch5:         dsniff-2.4-urlsnarf_zeropad.patch
Patch6:         dsniff-2.4-libnet_11.patch
Patch7:         dsniff-2.4-checksum.patch
Patch8:         dsniff-2.4-openssl_098.patch
Patch9:         dsniff-2.4-sshcrypto.patch
Patch10:        dsniff-2.4-sysconf_clocks.patch
Patch11:        dsniff-2.4-urlsnarf_escape.patch
Patch12:        dsniff-2.4-string_header.patch
Patch13:        dsniff-2.4-arpa_inet_header.patch
Patch14:        dsniff-2.4-pop_with_version.patch
Patch15:        dsniff-2.4-obsolete_time.patch
Patch16:        dsniff-2.4-checksum_libnids.patch
Patch17:        dsniff-2.4-fedora_dirs.patch
Patch18:        dsniff-2.4-glib2.patch
Patch19:        dsniff-2.4-link_layer_offset.patch
Patch20:        dsniff-2.4-tds_decoder.patch
Patch21:        dsniff-2.4-msgsnarf_segfault.patch
Patch22:        dsniff-2.4-urlsnarf_timestamp.patch
Patch23:        dsniff-2.4-arpspoof_reverse.patch
Patch24:        dsniff-2.4-arpspoof_multiple.patch
Patch25:        dsniff-2.4-arpspoof_hwaddr.patch
Patch26:        dsniff-2.4-modernize_pop.patch
Patch27:        dsniff-2.4-libnet_name2addr4.patch
Patch28:        dsniff-2.4-pntohl_shift.patch
Patch29:        dsniff-2.4-rpc_segfault.patch
Patch30:        dsniff-2.4-openssl_110.patch
Patch31:        dsniff-2.4-remote_typo.patch
Patch32:        dsniff-2.4-smp_mflags.patch
Patch33:        dsniff-2.4-libtirpc.patch
Patch34:        dsniff-2.4-pcap_init.patch
Patch35:        dsniff-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  libnet-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  libnids-devel
BuildRequires:  glib2-devel
BuildRequires:  libpcap-devel
BuildRequires:  libdb-devel
BuildRequires:  libXmu-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  rpcgen
BuildRequires:  libtirpc-devel
BuildRequires:  libnsl2-devel
%endif
BuildRequires:  make

%description
A collection of tools for network auditing and penetration testing. Dsniff,
filesnarf, mailsnarf, msgsnarf, urlsnarf and webspy allow to passively monitor
a network for interesting data (passwords, e-mail, files). Arpspoof, dnsspoof
and macof facilitate the interception of network traffic normally unavailable
to an attacker (e.g, due to layer-2 switching). Sshmitm and webmitm implement
active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions
by exploiting weak bindings in ad-hoc PKI.

%prep
%setup -q
%patch -P0 -p1 -b .time_h
%patch -P1 -p1 -b .mailsnarf
%patch -P2 -p1 -b .pcap_dump
%patch -P3 -p1 -b .multiple_intf
%patch -P4 -p1 -b .amd64_fix
%patch -P5 -p1 -b .urlsnarf_zeropad
%patch -P6 -p1 -b .libnet_11
%patch -P7 -p1 -b .checksum
%patch -P8 -p1 -b .openssl_098
%patch -P9 -p1 -b .sshcrypto
%patch -P10 -p1 -b .sysconf_clocks
%patch -P11 -p1 -b .urlsnarf_escape
%patch -P12 -p1 -b .string_header
%patch -P13 -p1 -b .arpa_inet_header
%patch -P14 -p1 -b .pop_with_version
%patch -P15 -p1 -b .obsolete_time
%patch -P16 -p1 -b .checksum_libnids
%patch -P17 -p1 -b .fedora_dirs
%patch -P18 -p1 -b .glib2
%patch -P19 -p1 -b .link_layer_offset
%patch -P20 -p1 -b .tds_decoder
%patch -P21 -p1 -b .msgsnarf_segfault
%patch -P22 -p1 -b .urlsnarf_timestamp
%patch -P23 -p1 -b .arpspoof_reverse
%patch -P24 -p1 -b .arpspoof_multiple
%patch -P25 -p1 -b .arpspoof_hwaddr
%patch -P26 -p1 -b .modernize_pop
%patch -P27 -p1 -b .libnet_name2addr4
%patch -P28 -p1 -b .pntohl_shift
%patch -P29 -p1 -b .rpc_segfault
%patch -P30 -p1 -b .openssl_110
%patch -P31 -p1 -b .remote_typo
%patch -P32 -p1 -b .smp_mflags
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch -P33 -p1 -b .libtirpc
%endif
%patch -P34 -p1 -b .pcap_init
%patch -P35 -p1

%build
%if 0%{?rhel} == 7
sed \
  -e 's|include/openssl/|include/openssl11/openssl/|g' \
  -e 's|\(SSLINC="\)-I${prefix}/include|\1$(pkg-config --cflags openssl11)|g' \
  -e 's|\(SSLLIB="\)-L${prefix}/lib -lssl -lcrypto|\1$(pkg-config --libs openssl11)|g' \
  -i configure
%endif

%configure
%make_build

%install
%make_install install_prefix=$RPM_BUILD_ROOT

%files
%license LICENSE
%doc CHANGES README TODO
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/arpspoof
%{_sbindir}/dnsspoof
%{_sbindir}/%{name}
%{_sbindir}/filesnarf
%{_sbindir}/macof
%{_sbindir}/mailsnarf
%{_sbindir}/msgsnarf
%{_sbindir}/sshmitm
%{_sbindir}/sshow
%{_sbindir}/tcpkill
%{_sbindir}/tcpnice
%{_sbindir}/urlsnarf
%{_sbindir}/webmitm
%{_sbindir}/webspy
%{_mandir}/man8/arpspoof.8*
%{_mandir}/man8/dnsspoof.8*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/filesnarf.8*
%{_mandir}/man8/macof.8*
%{_mandir}/man8/mailsnarf.8*
%{_mandir}/man8/msgsnarf.8*
%{_mandir}/man8/sshmitm.8*
%{_mandir}/man8/sshow.8*
%{_mandir}/man8/tcpkill.8*
%{_mandir}/man8/tcpnice.8*
%{_mandir}/man8/urlsnarf.8*
%{_mandir}/man8/webmitm.8*
%{_mandir}/man8/webspy.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.46.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.45.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.44.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.43.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.42.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.41.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 2.4-0.40.b1
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.39.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.38.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.4-0.37.b1
- Rebuilt with OpenSSL 3.0.0

* Sun Jul 25 2021 Robert Scheck <robert@fedoraproject.org> 2.4-0.36.b1
- Added patch to work around pcap_init() API change in libpcap

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.35.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.34.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.33.b1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.32.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.31.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.30.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.29.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.28.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Robert Scheck <robert@fedoraproject.org> 2.4-0.27.b1
- Added patch to allow building dsniff against libtirpc (#1582770)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.26.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.25.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.24.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Robert Scheck <robert@fedoraproject.org> 2.4-0.23.b1
- Added patch to allow building dsniff with OpenSSL >= 1.1.0
- Added patch to correct a typo related to the -remote option

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.22.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.21.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.20.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.19.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.18.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 20 2013 Robert Scheck <robert@fedoraproject.org> 2.4-0.17.b1
- Corrected patch which touches tabular data stream protocol handler
- Added a patch to add both communication partners in arpspoof
- Added patch to allow multiple targets to be imitated simultaniously
- Added patch to allow the selection of source hw address in arpspoof
- Added a patch which fixes and modernizes the POP decoder
- Fixed segmentation faults related to libnet_name2addr4() (#1009879)
- Added a patch to fix bit-shift in pntohl() macro (#714958, #850496)
- Avoid xdrs being used without being initialised (#715042, #850494)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.16.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.15.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 30 2012 Robert Scheck <robert@fedoraproject.org> 2.4-0.14.b1
- Added a patch which adds further link layer offsets
- Avoid opportunity for DoS in tabular data stream protocol handler
- Added a memset in msgsnarf to correctly 0 out the C struct
- Patched urlsnarf to use timestamps from pcap file if available

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.13.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 2.4-0.12.b1
- libnet rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.11.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.10.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 29 2010 Robert Scheck <robert@fedoraproject.org> 2.4-0.9.b1
- Rebuild against libnids 1.24

* Fri Jan 08 2010 Robert Scheck <robert@fedoraproject.org> 2.4-0.8.b1
- Added build requirement to libXmu-devel for webspy (#553230)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.4-0.7.b1
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.6.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.4-0.5.b1
- Rebuild against gcc 4.4 and rpm 4.6

* Sat Aug 30 2008 Robert Scheck <robert@fedoraproject.org> 2.4-0.4.b1
- Re-diffed dsniff url log escaping patch for no fuzz

* Thu May 29 2008 Robert Scheck <robert@fedoraproject.org> 2.4-0.3.b1
- Rebuild against libnids 1.23

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 2.4-0.2.b1
- Rebuild against gcc 4.3

* Thu Nov 29 2007 Robert Scheck <robert@fedoraproject.org> 2.4-0.1.b1
- Upgrade to 2.4b1 and added many patches from Debian
- Initial spec file for Fedora and Red Hat Enterprise Linux
