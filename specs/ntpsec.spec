Name:           ntpsec
Version:        1.2.3
Release:        10%{?dist}
Summary:        NTP daemon and utilities

License:        NTP AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND ISC AND Apache-2.0 AND Beerware
URL:            https://www.ntpsec.org/
Source0:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz
Source1:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz.asc
Source2:        https://ftp.ntpsec.org/pub/releases/ntpsec.gpg.pub.asc
Source3:        ntp.conf

BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libbsd-devel
BuildRequires:  libcap-devel
BuildRequires:  m4
BuildRequires:  openssl-devel
BuildRequires:  pps-tools-devel
BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd
BuildRequires:  waf

# Use the bundled waf script instead of the system one until ntpsec supports
# the newer version
%global waf python3 waf

Requires(pre):  shadow-utils
%{?systemd_requires}

Conflicts:      ntp ntp-perl ntpdate
Obsoletes:      ntp < 4.2.10 ntp-perl < 4.2.10 ntp-doc < 4.2.10 ntpdate < 4.2.10 sntp < 4.2.10

# Set pool.ntp.org vendor zone for default configuration
%if 0%{!?vendorzone:1}
%global vendorzone %(source /etc/os-release && echo ${ID}.)
%endif

# Private library
%global __provides_exclude ^libntpc\\.so.*$
%global __requires_exclude ^libntpc\\.so.*$

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/ntpsec
Provides:       /usr/sbin/ntpq
Provides:       /usr/sbin/ntpdate
%endif

%description
NTPsec is a more secure and improved implementation of the Network Time
Protocol derived from the original NTP project.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1

# Fix egg info to use a shorter version which will work as an rpm provide
sed -i 's|NTPSEC_VERSION_EXTENDED|NTPSEC_VERSION|' pylib/ntp-in.egg-info

# Modify compiled-in statsdir
sed -i 's|/var/NTP|%{_localstatedir}/log/ntpstats|' \
        docs/includes/ntpd-body.adoc ntpd/ntp_util.c

%build
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

%{waf} configure \
        --enable-debug \
        --disable-doc \
        --refclock=all \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        ;

%{waf} build

%install
%{waf} --destdir=%{buildroot} install

install -p -m755 attic/ntpdate %{buildroot}%{_sbindir}/ntpdate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m644 etc/logrotate-config.ntpd \
        %{buildroot}%{_sysconfdir}/logrotate.d/ntpsec.conf

rm -rf %{buildroot}%{_docdir}

pushd %{buildroot}

sed -e 's|VENDORZONE\.|%{vendorzone}|' \
        -e 's|VARNTP|%{_localstatedir}/lib/ntp|' \
        < %{SOURCE3} > .%{_sysconfdir}/ntp.conf
touch -r %{SOURCE3} .%{_sysconfdir}/ntp.conf

for f in .%{_bindir}/*; do
        head -c 30 "$f" | grep -q python || continue
        %py3_shebang_fix "$f"
done

%if "%{_sbindir}" != "%{_bindir}"
# Move ntpq to sbin for better compatibility with ntp package
mv .%{_bindir}/ntpq .%{_sbindir}/ntpq
%endif

mkdir -p .%{_localstatedir}/{lib/ntp,log/ntpstats}
touch .%{_localstatedir}/lib/ntp/ntp.drift

mkdir -p .%{_prefix}/lib/systemd/ntp-units.d
echo 'ntpd.service' > .%{_prefix}/lib/systemd/ntp-units.d/60-ntpd.list

popd

%check
%{waf} check

%pre
# UID/GID inherited from the ntp package
/usr/sbin/groupadd -g 38 ntp 2> /dev/null || :
/usr/sbin/useradd -u 38 -g 38 -s /sbin/nologin -M -r \
        -d %{_localstatedir}/lib/ntp ntp 2>/dev/null || :

%post
%systemd_post ntpd.service ntp-wait.service
systemctl daemon-reload 2> /dev/null || :

%preun
%systemd_preun ntpd.service ntp-wait.service

%postun
%systemd_postun_with_restart ntpd.service

%global service_save_file /run/ntp-ntpsec.upgrade.services

%triggerprein -- ntp < 4.2.10
[ $1 = 0 ] || exit 0
# Save enabled ntp services and configuration (before our post)
for s in ntpd ntp-wait; do
        systemctl is-enabled -q "$s".service 2> /dev/null &&
                echo "$s" 2> /dev/null >> %{service_save_file}
done
rm -rf %{_sysconfdir}/ntp.ntpsec
cp -r --preserve=all %{_sysconfdir}/ntp %{_sysconfdir}/ntp.ntpsec 2> /dev/null
:

%triggerpostun -- ntp < 4.2.10
[ $2 = 0 ] || exit 0
# Restore the services and configuration from ntp (after its preun)
for s in ntpd ntp-wait; do
        grep -q "^$s$" %{service_save_file} 2> /dev/null &&
                systemctl enable -q "$s".service 2> /dev/null
done
rm -f %{service_save_file}
mv -f -T --backup=numbered %{_sysconfdir}/ntp.ntpsec %{_sysconfdir}/ntp
# Remove unsupported restrictions
sed -i.bak -E '/^restrict/s/no(e?peer|trap)//g' %{_sysconfdir}/ntp.conf
:

%files
%license LICENSES/*
%doc NEWS.adoc README.adoc
%config(noreplace) %{_sysconfdir}/ntp.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/ntpsec.conf
%{_bindir}/ntp*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/ntp*
%endif
%{_libdir}/libntpc.so*
%{_mandir}/man1/ntp*.1*
%{_mandir}/man5/ntp*.5*
%{_mandir}/man8/ntp*.8*
%{_unitdir}/ntp*.service
%{_unitdir}/ntp*.timer
%{_prefix}/lib/systemd/ntp-units.d/*ntpd.list
%dir %attr(-,ntp,ntp) %{_localstatedir}/lib/ntp
%ghost %attr(644,ntp,ntp) %{_localstatedir}/lib/ntp/ntp.drift
%dir %attr(-,ntp,ntp) %{_localstatedir}/log/ntpstats
%{python3_sitearch}/ntp-*.egg-info
%{python3_sitearch}/ntp

%changelog
* Thu Jan 16 2025 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-10
- Also add Provides:/usr/sbin/ntpdate (rhbz#2338300)

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-9
- Rebuilt for the bin-sbin merge (2nd attempt)

* Tue Dec 03 2024 Miroslav Lichvar <mlichvar@redhat.com> 1.2.3-8
- switch to building with bundled waf (#2329938)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-6
- Rebuilt for the bin-sbin merge

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.3-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.3-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Miroslav Lichvar <mlichvar@redhat.com> 1.2.3-1
- update to 1.2.3
- drop patch for detecting weak keys generated by 1.2.0
- convert license tag to SPDX

* Thu Aug 03 2023 Miroslav Lichvar <mlichvar@redhat.com> 1.2.2a-1
- update to 1.2.2a (CVE-2023-4012)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Miroslav Lichvar <mlichvar@redhat.com> 1.2.2-1
- update to 1.2.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-8
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-6
- fix building with OpenSSL-3.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.1-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-3
- detect weak keys generated by ntpkeygen (#1955859)

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.10

* Mon Jun 07 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-1
- update to 1.2.1 (CVE-2021-22212)
- enable refclock support (#1955859)
- add libbsd-devel to build requirements

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-8
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 01 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-6
- change ntpdate defaults to follow classic ntpdate (#1917884)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-4
- include associd in ntpq readvar output (#1914901)
- fix ntpq crash in raw mode (#1914901)

* Wed Jan 06 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-3
- switch to flat default configuration
- save enabled services and configuration when replacing ntp
- move ntpdate and ntpq to /usr/sbin for better compatibility
- extend ntp conflicts and obsoletes

* Tue Dec 01 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-2
- address issues found in package review (#1896368)

* Tue Nov 10 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-1
- package ntpsec
