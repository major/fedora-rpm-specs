Summary: Intrusion Detection System
Name: suricata
Version: 7.0.8
Release: 2%{?dist}
License: GPL-2.0-only
URL: https://suricata-ids.org/
Source0: https://www.openinfosecfoundation.org/download/%{name}-%{version}.tar.gz
Source1: suricata.sysconfig
Source2: fedora.notes
Source3: suricata-tmpfiles.conf

# Irrelevant docs are getting installed, drop them
Patch1: suricata-2.0.9-docs.patch
# Suricata service file needs some options supplied
Patch2: suricata-4.1.1-service.patch
# The default path needs to be fixed up to where Fedora keeps it
Patch3: suricata-5.0.4-geolite-path-fixup.patch
# The log path has an extra '/' at the end
Patch4: suricata-6.0.3-log-path-fixup.patch
# Build fails with ambiguous python shebang
Patch5: suricata-7.0.2-python.patch

BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: cargo rust >= 1.63
BuildRequires: rust-packaging
BuildRequires: libyaml-devel python3-pyyaml
BuildRequires: libnfnetlink-devel libnetfilter_queue-devel libnet-devel
BuildRequires: zlib-devel pcre2-devel libcap-ng-devel
BuildRequires: lz4-devel libpcap-devel
BuildRequires: nspr-devel nss-devel nss-softokn-devel file-devel
BuildRequires: jansson-devel libmaxminddb-devel python3-devel lua-devel
# Next line is for eBPF support
%if 0%{?fedora} >= 32
%ifarch x86_64
BuildRequires: clang llvm libbpf-devel
%endif
%endif
BuildRequires: autoconf automake libtool
BuildRequires: systemd-devel
BuildRequires: hiredis-devel
BuildRequires: libevent-devel
# Prelude is disabled pending resolution of bz 1908783
#BuildRequires: libprelude-devel
BuildRequires: pkgconfig(gnutls)

%if 0%{?fedora} >= 25 || 0%{?epel} >= 8
%ifarch x86_64
BuildRequires: hyperscan-devel
%endif
%endif

Requires: python3-pyyaml
Requires(pre): /usr/sbin/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# Rust is not working on ppc64le systems (bz 1757548)
# Or i686 (bz 2047425)
ExcludeArch: ppc64le i686


%description
The Suricata Engine is an Open Source Next Generation Intrusion
Detection and Prevention Engine. This engine is not intended to
just replace or emulate the existing tools in the industry, but
will bring new ideas and technologies to the field. This new Engine
supports Multi-threading, Automatic Protocol Detection (IP, TCP,
UDP, ICMP, HTTP, TLS, FTP and SMB! ), Gzip Decompression, Fast IP
Matching, and GeoIP identification.

%prep
%setup -q 
install -m 644 %{SOURCE2} doc/
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
sed -i 's/(datadir)/(sysconfdir)/' etc/Makefile.am
%ifarch x86_64
sed -i 's/-D__KERNEL__/-D__KERNEL__ -D__x86_64__/' ebpf/Makefile.am
%endif
find rust/ -name '*.rs' -type f -perm /111 -exec chmod -v -x '{}' '+'
autoreconf -fv --install

%build
#  ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"

%configure --enable-gccprotect --enable-pie --disable-gccmarch-native \
        --disable-coccinelle --enable-nfqueue --enable-af-packet \
        --with-libnspr-includes=/usr/include/nspr4 \
        --with-libnss-includes=/usr/include/nss3 \
        --enable-jansson --enable-geoip --enable-lua --enable-hiredis \
        --enable-rust  \
%if 0%{?fedora} >= 32
%ifarch x86_64
        --enable-ebpf-build --enable-ebpf \
%endif
%endif
        --enable-python

%make_build

%install
make DESTDIR="%{buildroot}" "bindir=%{_sbindir}" install

# Setup etc directory
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/rules
install -m 640 rules/*.rules %{buildroot}%{_sysconfdir}/%{name}/rules
install -m 600 etc/*.config %{buildroot}%{_sysconfdir}/%{name}
install -m 600 threshold.config %{buildroot}%{_sysconfdir}/%{name}
install -m 600 suricata.yaml %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 etc/%{name}.service %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# Set up logging
mkdir -p %{buildroot}/%{_var}/log/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 etc/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Remove a couple things so they don't get picked up
rm -rf %{buildroot}%{_includedir}
rm -f %{buildroot}%{_libdir}/libhtp.la
rm -f %{buildroot}%{_libdir}/libhtp.a
rm -f %{buildroot}%{_libdir}/libhtp.so
rm -rf %{buildroot}%{_libdir}/pkgconfig

# Setup suricata-update data directory
mkdir -p %{buildroot}/%{_var}/lib/%{name}

# Setup tmpdirs
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

cp suricata-update/README.rst doc/suricata-update-README.rst

%check
make check

%pre
getent passwd suricata >/dev/null || useradd -r -M -s /sbin/nologin suricata

%post
%systemd_post suricata.service
if [ -d %{_var}/log/%{name} ] ; then
	file=$(ls %{_var}/log/%{name}/* 2> /dev/null | wc -l)
	if [ -n "$files" ] && [ "$files" != "0" ] ; then
		chown -R suricata:suricata %{_var}/log/%{name}/ 2> /dev/null || :
	fi
fi

%preun
%systemd_preun suricata.service

%postun
%systemd_postun_with_restart suricata.service

%files
%doc doc/Basic_Setup.txt doc/suricata-update-README.rst
%doc doc/Setting_up_IPSinline_for_Linux.txt doc/fedora.notes
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(644,root,root) %{_mandir}/man1/*
%{_sbindir}/suricata
%{_sbindir}/suricatasc
%{_sbindir}/suricatactl
%{_sbindir}/suricata-update
%{_libdir}/libhtp*
/usr/lib/suricata/python/suricata/*
/usr//lib/suricata/python/suricatasc
%config(noreplace) %attr(0640,suricata,suricata) %{_sysconfdir}/%{name}/suricata.yaml
%config(noreplace) %attr(0640,suricata,suricata) %{_sysconfdir}/%{name}/*.config
%config(noreplace) %attr(0640,suricata,suricata) %{_sysconfdir}/%{name}/rules/*.rules
%config(noreplace) %attr(0600,suricata,root) %{_sysconfdir}/sysconfig/%{name}
%attr(644,root,root) %{_unitdir}/suricata.service
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/%{name}
%attr(750,suricata,suricata) %dir %{_var}/log/%{name}
%attr(750,suricata,suricata) %dir %{_sysconfdir}/%{name}
%attr(750,suricata,suricata) %dir %{_sysconfdir}/%{name}/rules
%attr(2770,suricata,suricata) %dir %{_var}/lib/%{name}
%attr(2770,suricata,suricata) %dir /run/%{name}/
%{_tmpfilesdir}/%{name}.conf
%{_datadir}/%{name}/rules

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Steve Grubb <sgrubb@redhat.com> 7.0.8-1
- New security and bugfix release

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 7.0.7-2
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Mon Oct 14 2024 Steve Grubb <sgrubb@redhat.com> 7.0.7-1
- New security and bugfix release

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Steve Grubb <sgrubb@redhat.com> 7.0.6-1
- New security and bugfix release

* Fri Jun 07 2024 Steve Grubb <sgrubb@redhat.com> 7.0.5-3
- Don't fail install if log doesn't exist

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 7.0.5-2
- rebuild for hiredis soname bump

* Tue May 07 2024 Steve Grubb <sgrubb@redhat.com> 7.0.5-1
- New security and bugfix release

* Wed Mar 20 2024 Steve Grubb <sgrubb@redhat.com> 7.0.4-1
- New security and bugfix release

* Mon Feb 26 2024 Steve Grubb <sgrubb@redhat.com> 7.0.3-1
- New security and bugfix release

* Wed Jan 31 2024 Steve Grubb <sgrubb@redhat.com> 7.0.2-1
- New major release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Steve Grubb <sgrubb@redhat.com> 6.0.15-1
- New security and bugfix release

* Tue Sep 19 2023 Steve Grubb <sgrubb@redhat.com> 6.0.14-1
- New security and bugfix release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Steve Grubb <sgrubb@redhat.com> 6.0.13-1
- New security and bugfix release

* Wed May 10 2023 Steve Grubb <sgrubb@redhat.com> 6.0.12-1
- New bugfix release

* Thu Apr 13 2023 Steve Grubb <sgrubb@redhat.com> 6.0.11-1
- New security and bugfix release

* Mon Mar 13 2023 Steve Grubb <sgrubb@redhat.com> 6.0.10-1
- New security and bugfix release

* Mon Feb 06 2023 Fabio Valentini <decathorpe@gmail.com> - 6.0.9-3
- Ensure standard Rust compiler flags are set.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Steve Grubb <sgrubb@redhat.com> 6.0.9-1
- New security and bugfix release
- SPDX migration

* Thu Nov 03 2022 Jiri Olsa <jolsa@kernel.org> - 6.0.6-3
- libbpf 1.0.0 build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Steve Grubb <sgrubb@redhat.com> 6.0.6-1
- New security and bugfix release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.0.5-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Steve Grubb <sgrubb@redhat.com> 6.0.5-1
- New security and bugfix release

* Thu Mar 17 2022 Steve Grubb <sgrubb@redhat.com> 6.0.4-5
- ExcludeArch i686

* Thu Jan 27 2022 Steve Grubb <sgrubb@redhat.com> 6.0.4-4
- Updated post install script to chown only if files exist

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Kevin Fenzi <kevin@scrye.com> - 6.0.4-2
- Rebuild for hiredis 1.0.2

* Thu Nov 18 2021 Jason Taylor <jtfas90@gmail.com> 6.0.4-1
- New security and bugfix release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Steve Grubb <sgrubb@redhat.com> 6.0.3-1
- New security and bugfix release
- Fix logrotation location (#1966955)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.0.2-2
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Steve Grubb <sgrubb@redhat.com> 6.0.2-1
- New security and bugfix release

* Sat Feb 13 2021 Miro Hrončok <mhroncok@redhat.com> - 6.0.1-4
- Enable hyperscan on EPEL 8+

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Steve Grubb <sgrubb@redhat.com> 6.0.1-2
- New major feature release
- Dropped prelude support due to (#1908783).

* Tue Dec 15 2020 Steve Grubb <sgrubb@redhat.com> 5.0.5-1
- New bugfix release

* Thu Oct 15 2020 Steve Grubb <sgrubb@redhat.com> 5.0.4-1
- New security and bugfix release
- File ownership and location cleanups (#1861144)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.3-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Jason Taylor <jtfas90@gmail.com> 5.0.3-1
- Upstream security/bugfix release
- Updated reference, classification, threshold config file installs

* Fri Apr 03 2020 Jason Taylor <jtfas90@gmail.com> 5.0.2-2
- Add python3-pyyaml to resolve (#1818935)

* Thu Feb 13 2020 Steve Grubb <sgrubb@redhat.com> 5.0.2-1
- New bugfix release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Steve Grubb <sgrubb@redhat.com> 5.0.1-1
- New bugfix release

* Fri Oct 18 2019 Steve Grubb <sgrubb@redhat.com> 5.0.0-2
- New feature release (which also fixes a security issue)
- Enable ebpf on x86_64 only
- Disable building on ppc64le due to rust problems

* Thu Aug 01 2019 Steve Grubb <sgrubb@redhat.com> 4.1.4-4
- Fix FTBFS bz 1736727

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Steve Grubb <sgrubb@redhat.com> 4.1.4-2
- Rebuild for libprelude so bump

* Tue Apr 30 2019 Jason Taylor <jtfas90@gmail.com> 4.1.4-1
- Upstream bugfix release

* Thu Mar 07 2019 Steve Grubb <sgrubb@redhat.com> 4.1.3-1
- Upstream bugfix release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Jason Taylor <jtfas90@gmail.com> 4.1.2-1
- Upstream bugfix release
- Updated source to use official download site

* Thu Dec 20 2018 Steve Grubb <sgrubb@redhat.com> 4.1.1-4
- Adjust permissions on /run/suricata and /var/lib/suricata to group writable

* Mon Dec 17 2018 Steve Grubb <sgrubb@redhat.com> 4.1.1-2
- Remove ragel requirement

* Mon Dec 17 2018 Steve Grubb <sgrubb@redhat.com> 4.1.1-1
- Make log directory group readable
- Allow users of the suricata group to run suricata-update
- Add lz4-devel BuildRequires to support pcap compression
- Update service file for systemd security protections
- Upstream bugfix update

* Tue Nov 20 2018 Steve Grubb <sgrubb@redhat.com> 4.1.0-3
- Use the upstream service and logrote files (#1330331)
- Make the log directory readable by members of the suricata group (#1651394)

* Wed Nov 07 2018 Steve Grubb <sgrubb@redhat.com> 4.1.0-2
- Add cargo BuildRequires

* Tue Nov 06 2018 Steve Grubb <sgrubb@redhat.com> 4.1.0-1
- Latest upstream major release
- Fixes CVE-2018-18956 Segmentation fault in the ProcessMimeEntity function

* Mon Aug 13 2018 Steve Grubb <sgrubb@redhat.com> - 4.0.5-3
- Consolidate branches so that everything is in sync (#1614935)

* Fri Aug 10 2018 Jason Taylor <jtfas90@gmail.com> 4.0.5-2
- fixes bz#1614935

* Wed Jul 18 2018 Jason Taylor <jtfas90@gmail.com> - 4.0.5-1
- upstream security fix release
- addresses CVE-2018-10242, CVE-2018-10243, CVE-2018-10244

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Jason Taylor <jtfas90@gmail.com> - 4.0.4-2
- bumped release for build against hyperscan 5.0.0

* Mon Jul 09 2018 Jason Taylor <jtfas90@gmail.com> - 4.0.4-1
- added gcc-c++ buildrequires

* Thu Feb 15 2018 Jason Taylor <jtfas90@gmail.com> - 4.0.4-1
- fixes bz#1543250 and bz#1543251
- multiple upstream bugfixes

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Jason Taylor <jtfas90@gmail.com> 4.0.3-2
- Added prelude support

* Fri Dec 08 2017 Jason Taylor <jtfas90@gmail.com> 4.0.3-1
- Upstream bugfix release

* Wed Oct 18 2017 Steve Grubb <sgrubb@redhat.com> 4.0.1-1
- Upstream bugfix update

* Tue Sep 26 2017 Steve Grubb <sgrubb@redhat.com> 4.0.0-2
- Make suricata user own /run/suricata (#1396150)

* Mon Jul 31 2017 Jason Taylor <jtfas90@gmail.com> 4.0.0-1
- Latest upstream major release
- Build now has hyperscan and redis support

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Jason Taylor <jtfas90@gmail.com> 3.2.3-1
- Upstream bugfix update

* Wed Jun 07 2017 Steve Grubb <sgrubb@redhat.com> 3.2.2-1
- Upstream bugfix update

* Wed Feb 15 2017 Steve Grubb <sgrubb@redhat.com> 3.2.1-1
- Upstream security update

* Mon Feb 13 2017 Steve Grubb <sgrubb@redhat.com> 3.2-1
- New upstream feature release
- Rotate /var/log/suricata/eve.json (#1396151)
- Fix ownership of /run/suricata (#1396150)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Steve Grubb <sgrubb@redhat.com> 3.1.3-1
- New upstream bug fix release

* Wed Sep 07 2016 Steve Grubb <sgrubb@redhat.com> 3.1.2-1
- New upstream bug fix release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Steve Grubb <sgrubb@redhat.com> 3.1.1-1
- New upstream bug fix release

* Wed Jun 22 2016 Steve Grubb <sgrubb@redhat.com> 3.1-1
- New upstream bug fix release

* Mon Apr 04 2016 Steve Grubb <sgrubb@redhat.com> 3.0.1-1
- New upstream bug fix release

* Wed Mar 16 2016 Steve Grubb <sgrubb@redhat.com> 3.0-2
- Fixed Bug 1227085 - Have Suricata start after the network is online

* Mon Mar 07 2016 Steve Grubb <sgrubb@redhat.com> 3.0-1
- New upstream bug fix release

* Wed Feb 10 2016 Peter Schiffer <pschiffe@redhat.com> 2.0.11-3
- Run suricata under suricata user

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Steve Grubb <sgrubb@redhat.com> 2.0.11-1
- New upstream bug fix release

* Wed Nov 25 2015 Steve Grubb <sgrubb@redhat.com> 2.0.10-1
- New upstream bug fix release

* Sat Oct 03 2015 Steve Grubb <sgrubb@redhat.com> 2.0.9-1
- New upstream bug fix release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Steve Grubb <sgrubb@redhat.com> 2.0.8-1
- New upstream security bug fix release

* Thu Feb 26 2015 Steve Grubb <sgrubb@redhat.com> 2.0.7-1
- New upstream security bug fix release for CVE-2015-0928

* Thu Jan 15 2015 Steve Grubb <sgrubb@redhat.com> 2.0.6-1
- New upstream bug fix release
- Don't use the system libhtp library

* Fri Dec 12 2014 Steve Grubb <sgrubb@redhat.com> 2.0.5-1
- New upstream bug fix release
- Use the system libhtp library

* Wed Sep 24 2014 Steve Grubb <sgrubb@redhat.com> 2.0.4-1
- New upstream bug fix release
- Fixes CVE-2014-6603 out-of-bounds access in SSH parser

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Steve Grubb <sgrubb@redhat.com> 2.0.3-1
- New upstream bug fix release

* Sat Jun 28 2014 Steve Grubb <sgrubb@redhat.com> 2.0.2-2
- Specfile cleanups (#1113413)

* Wed Jun 25 2014 Steve Grubb <sgrubb@redhat.com> 2.0.2-1
- New upstream bug fix release
- Enable liblua support

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Steve Grubb <sgrubb@redhat.com> 2.0.1-1
- New upstream bug fix release

* Wed Mar 26 2014 Steve Grubb <sgrubb@redhat.com> 2.0-1
- Major new upstream release with new features

* Tue Jan 21 2014 Dan Horák <dan[at]danny.cz> 1.4.7-3
- luajit available only on selected arches

* Sat Jan 11 2014 Steve Grubb <sgrubb@redhat.com> 1.4.7-2
- Enable luajit support

* Wed Dec 18 2013 Steve Grubb <sgrubb@redhat.com> 1.4.7-1
- New upstream bug fix release

* Fri Oct 04 2013 Steve Grubb <sgrubb@redhat.com> 1.4.6-1
- New upstream bug fix release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Steve Grubb <sgrubb@redhat.com> 1.4.3-2
- Drop prelude support

* Fri Jun 21 2013 Steve Grubb <sgrubb@redhat.com> 1.4.3-1
- New upstream bug fix release

* Mon Jun 03 2013 Steve Grubb <sgrubb@redhat.com> 1.4.2-1
- New upstream bug fix release

* Sun Mar 10 2013 Steve Grubb <sgrubb@redhat.com> 1.4.1-1
- New upstream bugfix release
- Enable libgeoip support
- Switch to stack-protector-all

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Steve Grubb <sgrubb@redhat.com> 1.4-1
- New upstream feature enhancement release

* Thu Dec 06 2012 Steve Grubb <sgrubb@redhat.com> 1.3.5-1
- New upstream bugfix release

* Tue Nov 27 2012 Steve Grubb <sgrubb@redhat.com> 1.3.4-1
- New upstream release

* Mon Nov 05 2012 Steve Grubb <sgrubb@redhat.com> 1.3.3-1
- New upstream release

* Tue Oct 09 2012 Steve Grubb <sgrubb@redhat.com> 1.3.2-2
- Add nss-devel build require and systemd macros

* Mon Oct 08 2012 Steve Grubb <sgrubb@redhat.com> 1.3.2-1
- New upstream release

* Sat Aug 25 2012 Steve Grubb <sgrubb@redhat.com> 1.3.1-1
- New upstream release
- Switch startup to use systemd

* Fri Jul 06 2012 Steve Grubb <sgrubb@redhat.com> 1.3-1
- New upstream release

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.1-3
- Rebuild for updated libnet.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.2.1-2
- Rebuild against PCRE 8.30

* Thu Feb 02 2012 Steve Grubb <sgrubb@redhat.com> 1.2.1-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Steve Grubb <sgrubb@redhat.com> 1.1.1-2
- Enable AF_PACKET support

* Wed Dec 07 2011 Steve Grubb <sgrubb@redhat.com> 1.1.1-1
- New upstream release

* Mon Jul 25 2011 Steve Grubb <sgrubb@redhat.com> 1.0.5-1
- New upstream release

* Fri Jun 24 2011 Steve Grubb <sgrubb@redhat.com> 1.0.4-1
- New upstream release

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> 1.0.3-2
- don't override -march set by the buildsystem (fixes build on non-x86)

* Sat Apr 23 2011 Steve Grubb <sgrubb@redhat.com> 1.0.3-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 10 2010 Steve Grubb <sgrubb@redhat.com> 1.0.2-1
- New upstream release (#651978)

* Thu Jul 01 2010 Steve Grubb <sgrubb@redhat.com> 1.0.0-1
- New upstream release

* Fri May 07 2010 Steve Grubb <sgrubb@redhat.com> 0.9.0-1
- New upstream release

* Tue Apr 20 2010 Steve Grubb <sgrubb@redhat.com> 0.8.2-1
- New upstream release

* Sat Feb 27 2010 Steve Grubb <sgrubb@redhat.com> 0.8.1-1
- Initial packaging

