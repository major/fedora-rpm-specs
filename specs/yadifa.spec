
%global _hardened_build	1

# version revision
%global revision	11259

Name:		yadifa
Version:	2.6.7
Release:	2%{?dist}
Summary:	Lightweight authoritative Name Server with DNSSEC capabilities

License:	BSD-3-Clause
URL:		http://www.yadifa.eu
Source0:	http://cdn.yadifa.eu/sites/default/files/releases/%{name}-%{version}-%{revision}.tar.gz
Source1:	yadifad.service
Source3:	yadifa.logrotate

BuildRequires:	gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	openssl-devel-engine
BuildRequires:	sed

Requires:	logrotate
Requires:	yadifa-libs = %{version}-%{release}

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd


%description
YADIFA is a name server implementation developed from scratch by .eu.
It is portable across multiple operating systems and supports DNSSEC,
TSIG, DNS notify, DNS update, IPv6.

%package libs
Summary:	Libraries used by the YADIFA packages

%description libs
Contains libraries used by YADIFA DNS server

%package tools
Summary:	Remote management client for YADIFA DNS server

%description tools
Contains utility for YADIFA DNS server remote management

%package devel
Summary:	Header files and libraries needed for YADIFA development
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The yadifa-devel package contains header files and libraries
required for development with YADIFA DNS server


%prep
%autosetup -n %{name}-%{version}-%{revision}

%build
export CPPFLAGS="%{optflags} -DNDEBUG -g"
export LDFLAGS="$LDFLAGS -lssl -lcrypto"

%configure \
    --with-tools \
    --enable-rrl \
    --enable-nsid \
    --enable-ctrl \
    --enable-systemd-resolved-avoidance \
    --enable-shared \
    --disable-static

# adjust build options
sed -i 's|-mtune=native||g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -fno-ident|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -ansi|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -pedantic|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YRCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -DCMR/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YPCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -pg -DCMP/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YDCFLAGS = -DDEBUG $(DEBUGFLAGS) -DCMD/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile

# adjust additional key options
sed -i 's|^include "keys.conf"|#include "keys.conf"|' etc/yadifad.conf.example
sed -i '/^<\/key>/a \ \n<key>\n \ name \ abroad-admin-key\n \ algorithm \ hmac-md5\n \ secret \ AbroadAdminTSIGKey==\n<\/key>' \
    etc/yadifad.conf.example

%make_build

%install
%make_install

# config
for conf in yadifad yakeyrolld; do
install -Dpm 0644 etc/${conf}.conf \
    %{buildroot}%{_sysconfdir}/${conf}.conf
done

mkdir -p %{buildroot}%{_localstatedir}/log/yadifa
mkdir -p %{buildroot}%{_localstatedir}/log/yakeyrolld
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/yadifa

# bash completion
for comp in yadifa yadifad; do
install -Dpm 0644 etc/${comp}.bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/${comp}
done

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/yadifad.service

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/yadifa


%post
%systemd_post yadifad.service
exit 0

%preun
%systemd_preun yadifad.service
exit 0

%postun
%systemd_postun_with_restart yadifad.service
exit 0

%ldconfig_scriptlets libs


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc etc/*.conf.example
%config(noreplace) %{_sysconfdir}/yadifad.conf
%config(noreplace) %{_sysconfdir}/yakeyrolld.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifad
%{_unitdir}/yadifad.service
%{_localstatedir}/zones
%{_localstatedir}/log/yadifa
%{_localstatedir}/log/yakeyrolld
%{_sbindir}/yadifad
%{_sbindir}/yakeyrolld
%{_mandir}/man5/yadifa.*.5*
%{_mandir}/man5/yadifad.*.5*
%{_mandir}/man8/yadifad.8*
%{_mandir}/man5/yakeyrolld.*.5*
%{_mandir}/man8/yakeyrolld.8*

%files libs
%{_libdir}/libdnscore.so.7*
%{_libdir}/libdnsdb.so.7*
%{_libdir}/libdnslg.so.7*

%files tools
%license COPYING
%doc AUTHORS
%{_bindir}/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifa
%{_mandir}/man8/yadifa.8*

%files devel
%{_includedir}/dnscore
%{_includedir}/dnsdb
%{_includedir}/dnslg
%{_libdir}/libdnscore.so
%{_libdir}/libdnsdb.so
%{_libdir}/libdnslg.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 05 2024 Denis Fateyev <denis@fateyev.com> - 2.6.7-1
- Update to 2.6.7 release

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.6-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 01 2024 Denis Fateyev <denis@fateyev.com> - 2.6.6-1
- Update to 2.6.6 release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Denis Fateyev <denis@fateyev.com> - 2.6.5-1
- Update to 2.6.5 release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Denis Fateyev <denis@fateyev.com> - 2.6.4-1
- Update to 2.6.4 release

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Florian Weimer <fweimer@redhat.com> - 2.6.2-2
- Port configure script to C99 (#2161927)

* Fri Dec 09 2022 Denis Fateyev <denis@fateyev.com> - 2.6.2-1
- Update to 2.6.2 release

* Fri Oct 07 2022 Denis Fateyev <denis@fateyev.com> - 2.6.0-1
- Update to 2.6.0 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 04 2022 Denis Fateyev <denis@fateyev.com> - 2.5.4-1
- Update to 2.5.4 release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Denis Fateyev <denis@fateyev.com> - 2.5.3-1
- Update to 2.5.3 release

* Fri Oct 08 2021 Denis Fateyev <denis@fateyev.com> - 2.5.2-1
- Update to 2.5.2 release

* Mon Sep 27 2021 Denis Fateyev <denis@fateyev.com> - 2.5.1-1
- Update to 2.5.1 release

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.5.0-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 20 2021 Denis Fateyev <denis@fateyev.com> - 2.5.0-1
- Update to 2.5.0 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.11-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Denis Fateyev <denis@fateyev.com> - 2.3.11-1
- Update to 2.3.11 release

* Thu Sep 17 2020 Denis Fateyev <denis@fateyev.com> - 2.3.10-1
- Update to 2.3.10 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 2.3.9-4
- Add "legacy_common_support" build option

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Denis Fateyev <denis@fateyev.com> - 2.3.9-1
- Update to 2.3.9 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Denis Fateyev <denis@fateyev.com> - 2.3.8-1
- Update to 2.3.8 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 16 2017 Denis Fateyev <denis@fateyev.com> - 2.3.7-1
- Update to 2.3.7 release

* Fri Dec 01 2017 Denis Fateyev <denis@fateyev.com> - 2.2.6-2
- Unified service configuration across all branches

* Sat Sep 30 2017 Denis Fateyev <denis@fateyev.com> - 2.2.6-1
- Update to 2.2.6 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Denis Fateyev <denis@fateyev.com> - 2.2.5-1
- Update to 2.2.5 release

* Fri Apr 14 2017 Denis Fateyev <denis@fateyev.com> - 2.2.4-2
- Added aliased IPs support ("--enable-messages" option)

* Sat Apr 08 2017 Denis Fateyev <denis@fateyev.com> - 2.2.4-1
- Update to 2.2.4 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 2.2.3-1
- Update to 2.2.3 release

* Sat Sep 03 2016 Denis Fateyev <denis@fateyev.com> - 2.2.1-1
- Update to 2.2.1 release

* Sat Jul 16 2016 Denis Fateyev <denis@fateyev.com> - 2.2.0-1
- Update to 2.2.0 release

* Tue Feb 23 2016 Denis Fateyev <denis@fateyev.com> - 2.1.6-1
- Update to 2.1.6 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Denis Fateyev <denis@fateyev.com> - 2.1.5-1
- Update to 2.1.5 release

* Wed Sep 30 2015 Denis Fateyev <denis@fateyev.com> - 2.1.3-1
- Update to 2.1.3 release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Denis Fateyev <denis@fateyev.com> - 2.0.6-1
- Update to 2.0.6 release

* Sun Dec 21 2014 Denis Fateyev <denis@fateyev.com> - 2.0.4-1
- Update to 2.0.4 release

* Sat Oct 18 2014 Denis Fateyev <denis@fateyev.com> - 2.0.0-1
- Update to 2.0.0 release
- New program features added

* Thu Aug 28 2014 Denis Fateyev <denis@fateyev.com> - 1.0.3-2
- Build options clarification
- Minor specfile cleanup

* Sat Aug 16 2014 Denis Fateyev <denis@fateyev.com> - 1.0.3-1
- Initial Fedora RPM release
