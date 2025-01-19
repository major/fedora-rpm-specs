%global _hardened_build 1

Name:           hostapd
Version:        2.11
Release:        2%{?dist}
Summary:        IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator
License:        BSD-3-Clause
URL:            http://w1.fi/hostapd

Source0:        http://w1.fi/releases/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.conf.5
Source4:        %{name}.sysconfig
Source5:        %{name}.init


BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  gcc

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:      systemd
BuildRequires: make
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%endif

%if 0%{?rhel} == 6
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(postun):   /sbin/service
%endif

%description
%{name} is a user space daemon for access point and authentication servers. It
implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP
Authenticators and RADIUS authentication server.

%{name} is designed to be a "daemon" program that runs in the back-ground and
acts as the backend component controlling authentication. %{name} supports
separate frontend programs and an example text-based frontend, hostapd_cli, is
included with %{name}.

%package logwatch
Summary:        Logwatch scripts for hostapd
Requires:       %{name} = %{version}-%{release}
Requires:       logwatch
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
Requires:       perl
%else
Requires:       perl-interpreter
%endif

%description logwatch
Logwatch scripts for hostapd.

%prep
%setup -q
sed \
    -e '$ a CONFIG_SAE=y' \
    -e '$ a CONFIG_SUITEB192=y' \
    -e '$ a CONFIG_P2P=y' \
    -e '$ a CONFIG_P2P_MANAGER=y' \
    -e '/^#CONFIG_DRIVER_NL80211=y/s/^#//' \
    -e '/^#CONFIG_RADIUS_SERVER=y/s/^#//' \
    -e '/^#CONFIG_DRIVER_WIRED=y/s/^#//' \
    -e '/^#CONFIG_DRIVER_NONE=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211N=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211R=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211AC=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211AX=y/s/^#//' \
    -e '/^#CONFIG_FULL_DYNAMIC_VLAN=y/s/^#//' \
    -e '/^#CONFIG_LIBNL32=y/s/^#//' \
    -e '/^#CONFIG_ACS=y/s/^#//' \
    -e '/^#CONFIG_OCV=y/s/^#//' \
    -e '/^#CONFIG_OWE=y/s/^#//' \
    -e '/^#CONFIG_WPS=y/s/^#//' \
    -e '/^#CONFIG_WPA_CLI_EDIT=y/s/^#//' \
    < hostapd/defconfig \
    > hostapd/.config
echo "CFLAGS += -I%{_includedir}/libnl3 -DOPENSSL_NO_ENGINE" >> hostapd/.config
echo "LIBS += -L%{_libdir}" >> hostapd/.config


%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS -DOPENSSL_NO_ENGINE" -C hostapd


%install
%if 0%{?fedora} || 0%{?rhel} >= 7

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%else

# Initscripts
install -p -m 755 -D %{SOURCE5} %{buildroot}%{_initrddir}/%{name}

%endif

# logwatch files
install -d %{buildroot}/%{_sysconfdir}/logwatch/conf/services
install -pm 0644 %{name}/logwatch/%{name}.conf  \
        %{buildroot}/%{_sysconfdir}/logwatch/conf/services/%{name}.conf
install -d %{buildroot}/%{_sysconfdir}/logwatch/scripts/services
install -pm 0755 %{name}/logwatch/%{name} \
        %{buildroot}/%{_sysconfdir}/logwatch/scripts/services/%{name}

# config files
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -pm 0600 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}

install -d %{buildroot}/%{_sysconfdir}/sysconfig
install -pm 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

# binaries
install -d %{buildroot}/%{_sbindir}
install -pm 0755 %{name}/%{name} %{buildroot}%{_sbindir}/%{name}
install -pm 0755 %{name}/%{name}_cli %{buildroot}%{_sbindir}/%{name}_cli

# man pages
install -d %{buildroot}%{_mandir}/man{1,5,8}
install -pm 0644 %{name}/%{name}_cli.1 %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE3} %{buildroot}%{_mandir}/man5
install -pm 0644 %{name}/%{name}.8 %{buildroot}%{_mandir}/man8

# prepare docs
cp %{name}/README ./README.%{name}
cp %{name}/README-WPS ./README-WPS.%{name}
cp %{name}/logwatch/README ./README.logwatch

%if 0%{?fedora} || 0%{?rhel} >= 7

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%endif

%if 0%{?rhel} == 6

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%endif

%files
%license COPYING
%doc README README.hostapd README-WPS.hostapd
%doc %{name}/%{name}.conf %{name}/wired.conf
%doc %{name}/%{name}.accept %{name}/%{name}.deny
%doc %{name}/%{name}.eap_user %{name}/%{name}.radius_clients
%doc %{name}/%{name}.vlan %{name}/%{name}.wpa_psk
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/%{name}
%{_sbindir}/%{name}_cli
%dir %{_sysconfdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif

%files logwatch
%doc %{name}/logwatch/README
%config(noreplace) %{_sysconfdir}/logwatch/conf/services/%{name}.conf
%{_sysconfdir}/logwatch/scripts/services/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Davide Caratti <dcaratti@redhat.com> - 1:2.11-1
- Update to version 2.11 (#2299039)
- Disable OpenSSL ENGINE API

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 05 2024 Lubomir Rintel <lkundrak@v3.sk> - 2.10-11
- Enable hostapd_cli(1) command line editing
- Enable Wi-Fi Protected Setup
- Enable Wi-Fi P2P

* Fri Mar 22 2024 Davide Caratti <dcaratti@redhat.com> - 2.10-10
- Enable Suite B 192 cipher suite

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 John W. Linville <linville@redhat.com> - 2.10-6
- Correct path for example hostapd.conf cited in hostapd.conf.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 John W. Linville <linville@redhat.com> - 2.10-2
- Enable CONFIG_OCV build option to fight multi-channel MITM attacks

* Mon Jan 17 2022 John W. Linville <linville@redhat.com> - 2.10-1
- Update to version 2.10 from upstream
- Enable support for IEEE802.11ax

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.9-13
- Rebuilt with OpenSSL 3.0.0

* Fri Sep 10 2021 Davide Caratti <dcaratti@redhat.com> - 2.9-12
- backport fix for NetworkManager-ci failures with openssl-3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 11 2021 John W. Linville <linville@redhat.com> - 2.9-10
- Enable CONFIG_OWE build option in order to provide WPA3 capability

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.9-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 10 2021 John W. Linville <linville@redhat.com> - 2.9-8
- Add hostapd.conf.5 man file, with content borrowed from NetBSD

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 John W. Linville <linville@redhat.com> - 2.9-6
- Enable environment file in hostapd service definition

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 John W. Linville <linville@redhat.com> - 2.9-4
- Fix CVE-2020-12695 (UPnP SUBSCRIBE misbehavior in hostapd WPS AP)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 John W. Linville <linville@redhat.com> - 2.9-2
- Fix CVE-2019-16275 (AP mode PMF disconnection protection bypass)

* Fri Aug 09 2019 John W. Linville <linville@redhat.com> - 2.9-1
- Update to version 2.9 from upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.8-2
- Enable SAE

* Wed May 15 2019 John W. Linville <linville@redhat.com> - 2.8-1
- Update to version 2.8 from upstream
- Drop obsoleted patches

* Fri Apr 12 2019 John W. Linville <linville@redhat.com> - 2.7-2
- Bump N-V-R for rebuild

* Fri Apr 12 2019 John W. Linville <linville@redhat.com> - 2.7-1
- Update to version 2.7 from upstream
- Remove obsolete patches for NL80211_ATTR_SMPS_MODE encoding and KRACK
- Fix CVE-2019-9494 (cache attack against SAE)
- Fix CVE-2019-9495 (cache attack against EAP-pwd)
- Fix CVE-2019-9496 (SAE confirm missing state validation in hostapd/AP)
- Fix CVE-2019-9497 (EAP-pwd server not checking for reflection attack)
- Fix CVE-2019-9498 (EAP-pwd server missing commit validation for scalar/element)
- Fix CVE-2019-9499 (EAP-pwd peer missing commit validation for scalar/element)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 John W. Linville <linville@redhat.com> - 2.6-11
- Add previously unnecessary BuildRequires for gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Davide Caratti <dcaratti@redhat.com> - 2.6-9
- backport fix for Fix NL80211_ATTR_SMPS_MODE encoding (rh #1582839)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Simone Caronni <negativo17@gmail.com> - 2.6-7
- Fix dependencies on the logwatch package for RHEL/CentOS.

* Fri Nov 03 2017 Xavier Bachelot <xavier@bachelot.org> - 2.6-6
- Add patches for KRACK : CVE-2017-13077, CVE-2017-13078, CVE-2017-13079,
  CVE-2017-13080, CVE-2017-13081, CVE-2017-13082, CVE-2017-13086,
  CVE-2017-13087, CVE-2017-13088 (RHBZ#1502588).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.6-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 John W. Linville <linville@redhat.com> - 2.6-1
- Update to version 2.6 from upstream
- Remove patch for CVE-2016-4476, now included in base tarball

* Fri Jul 15 2016 John W. Linville <linville@redhat.com> - 2.5-5
- Bump NVR and rebuild to resolve GLIBC_2.24 symbol issue

* Mon Jun 06 2016 John W. Linville <linville@redhat.com> - 2.5-4
- Add WPS patch for CVE-2016-4476

* Tue Apr 19 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5-3
- Enable ACS feature (automatic channel switching)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 John W. Linville <linville@redhat.com> - 2.5-1
- Update to version 2.5 from upstream
- Remove patches made redundant by version update

* Fri Jul 10 2015 John W. Linville <linville@redhat.com> - 2.4-3
- apply fix for NDEF record payload length checking

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 John W. Linville <linville@redhat.com> - 2.4-2
- apply fix for underflow in WMM action frame parser

* Tue Apr 21 2015 John W. Linville <linville@redhat.com> - 2.4-1
- Update to version 2.4 from upstream
- Enable support for IEEE802.11r and IEEE802.11ac

* Wed Feb  4 2015 John W. Linville <linville@redhat.com> - 2.3-4
- Use %%license instead of %%doc for file containing license information

* Sun Nov 02 2014 poma <poma@gmail.com> - 2.3-3
- Further simplify hostapd.conf installation
- Rebase "EAP-TLS server" patch to 2.3

* Tue Oct 28 2014 John W. Linville <linville@redhat.com> - 2.3-2
- Remove version info from /usr/share/doc/hostapd/hostapd.conf

* Thu Oct 23 2014 John W. Linville <linville@redhat.com> - 2.3-1
- Update to version 2.3 from upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 John W. Linville <linville@redhat.com> - 2.2-1
- Update to version 2.2 from upstream

* Sat Feb 22 2014 Simone Caronni <negativo17@gmail.com> - 2.1-2
- Re-enable drivers (#1068849).

* Fri Feb 14 2014 John W. Linville <linville@redhat.com> - 2.1-1
- Update to version 2.1 from upstream
- Remove obsolete patch for libnl build documentation

* Mon Feb 03 2014 Simone Caronni <negativo17@gmail.com> - 2.0-6
- Add libnl build documentation and switch libnl-devel to libnl3-devel build
  dependency (#1041471).

* Fri Nov 22 2013 John W. Linville <linville@redhat.com> - 2.0-5
- Enable CONFIG_FULL_DYNAMIC_VLAN build option

* Wed Aug 07 2013 Simone Caronni <negativo17@gmail.com> - 2.0-4
- Add EPEL 6 support.
- Remove obsolete EPEL 5 tags.
- Little spec file formatting.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0-2
- Perl 5.18 rebuild

* Thu May 30 2013 John W. Linville <linville@redhat.com> - 2.0-1
- Update to version 2.0 from upstream
- Convert to use of systemd-rpm macros
- Build with PIE flags

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  8 2012 John W. Linville <linville@redhat.com> - 1.0-3
- EAP-TLS: Add extra validation for TLS Message Length

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 John W. Linville <linville@redhat.com> - 1.0-1
- Update to version 1.0 from upstream

* Fri Jun  8 2012 John W. Linville <linville@redhat.com> - 0.7.3-9
- Remove hostapd-specific runtime state directory

* Wed Jun  6 2012 John W. Linville <linville@redhat.com> - 0.7.3-8
- Fixup typo in pid file path in hostapd.service

* Wed May 30 2012 John W. Linville <linville@redhat.com> - 0.7.3-7
- Add BuildRequires for systemd-units

* Fri May 25 2012 John W. Linville <linville@redhat.com> - 0.7.3-6
- Fixup typo in configuration file path in hostapd.service
- Tighten-up default permissions for hostapd.conf

* Tue Feb 28 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.3-5
- Migrate to systemd, BZ 770310.

* Wed Jan 18 2012 John W. Linville <linville@redhat.com> - 0.7.3-4
- Add reference to sample hostapd.conf in the default installed version
- Include README-WPS from the hostapd distribution as part of the docs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 John W. Linville <linville@redhat.com> - 0.7.3-1
- Update to version 0.7.3

* Wed Nov 24 2010 John W. Linville <linville@redhat.com> - 0.6.10-3
- Use ghost directive for /var/run/hostapd
- Remove some rpmlint warnings

* Thu May 27 2010 John W. Linville <linville@redhat.com> - 0.6.10-2
- Move DTIM period configuration into Beacon set operation

* Mon May 10 2010 John W. Linville <linville@redhat.com> - 0.6.10-1
- Update to version 0.6.10

* Tue Jan 19 2010 John W. Linville <linville@redhat.com> - 0.6.9-8
- Do not compress man pages manually in spec file
- Correct date of previous changelog entry

* Thu Jan 14 2010 John W. Linville <linville@redhat.com> - 0.6.9-7
- Enable 802.11n support

* Thu Dec 17 2009 John W. Linville <linville@redhat.com> - 0.6.9-6
- Enable RADIUS server
- Enable "wired" and "none" drivers
- Use BSD license option

* Wed Dec 16 2009 John W. Linville <linville@redhat.com> - 0.6.9-5
- Use openssl instead of gnutls (broken)

* Wed Dec 16 2009 John W. Linville <linville@redhat.com> - 0.6.9-4
- Remove wired.conf from doc (not in chosen configuration)
- Use $RPM_OPT_FLAGS
- Add dist tag

* Wed Dec 16 2009 John W. Linville <linville@redhat.com> - 0.6.9-3
- Use gnutls instead of openssl
- Turn-off internal EAP server (broken w/ gnutls)
- Remove doc files not applicable to chosen configuration
- Un-mangle README filename for logwatch sub-package

* Wed Dec 16 2009 John W. Linville <linville@redhat.com> - 0.6.9-2
- Initial build
- Start release at 2 to avoid conflicts w/ previous attempts by others
