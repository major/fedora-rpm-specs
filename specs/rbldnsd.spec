# systemd-rpm-macros split out from systemd at Fedora 30
%if (0%{?fedora} && 0%{?fedora} <= 29) || 0%{?rhel}
%global systemd_rpm_macros systemd
%else
%global systemd_rpm_macros systemd-rpm-macros
%endif

# Build hardened (PIE) where possible
%global _hardened_build 1

Summary:	Small, fast daemon to serve DNSBLs
Name:		rbldnsd
Version:	0.998b
Release:	16%{?dist}
License:	GPL-2.0-or-later
URL:		https://rbldnsd.io/
Source0:	https://rbldnsd.io/dwl/rbldnsd-%{version}.tgz
Source2:	rbldnsd.conf
Source3:	rbldnsctl
Source4:	README.systemd
Patch0:		rbldnsd-configure-c99.patch
Patch1:		rbldnsd-0.998b-version.patch
BuildRequires:	coreutils
BuildRequires:	gawk
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	%{systemd_rpm_macros}
BuildRequires:	zlib-devel
Requires(pre):	shadow-utils
Requires:	gawk
%{?systemd_requires}

%description
Rbldnsd is a small, authoritative-only DNS nameserver designed to serve
DNS-based blocklists (DNSBLs). It may handle IP-based and name-based
blocklists.

%prep
%setup -q

# Port non-autoconf configure script to C99
%patch -P 0 -p1

# Fix version number reported by rbldnsd
%patch -P 1

sed -i	-e 's@/var/lib/rbldns\([/ ]\)@%{_localstatedir}/lib/rbldnsd\1@g' \
	-e 's@\(-r/[a-z/]*\) -b@\1 -q -b@g' contrib/debian/rbldnsd.default
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} ./

%build
# this is not an autotools-generated configure script, and does not support --libdir
CFLAGS="%{optflags}" \
LDFLAGS="%{?__global_ldflags}" \
./configure
make

%install
mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man8,%{_initrddir},%{_sysconfdir}/sysconfig}
mkdir -p %{buildroot}{/etc/systemd,%{_localstatedir}/lib/rbldnsd}
install -p -m 755 rbldnsd				%{buildroot}%{_sbindir}/
install -p -m 644 rbldnsd.8				%{buildroot}%{_mandir}/man8/
install -p -m 644 contrib/debian/rbldnsd.default	%{buildroot}%{_sysconfdir}/sysconfig/rbldnsd
install -p -m 644 rbldnsd.conf				%{buildroot}/etc/systemd/
install -p -m 755 rbldnsctl				%{buildroot}%{_sbindir}/

%pre
getent group rbldns >/dev/null || groupadd -r rbldns
getent passwd rbldns >/dev/null || \
	useradd -r -g rbldns -d %{_localstatedir}/lib/rbldnsd \
		-s /sbin/nologin -c "rbldns daemon" rbldns
exit 0

%post
systemctl daemon-reload &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
	# Package removal, not upgrade
	%{_sbindir}/rbldnsctl stop &>/dev/null || :
	%{_sbindir}/rbldnsctl disable &>/dev/null || :
fi

%postun
systemctl daemon-reload &>/dev/null || :
if [ $1 -ge 1 ]; then
	# Package upgrade, not uninstall
	%{_sbindir}/rbldnsctl try-restart &>/dev/null || :
fi

%files
%license LICENSE.txt
%doc CHANGES-0.81 NEWS README README.user TODO contrib/debian/changelog
%{_sbindir}/rbldnsd
%{_mandir}/man8/rbldnsd.8*
%dir %{_localstatedir}/lib/rbldnsd/
%config(noreplace) %{_sysconfdir}/sysconfig/rbldnsd
%doc README.systemd
%config(noreplace) %{_sysconfdir}/systemd/rbldnsd.conf
%{_sbindir}/rbldnsctl

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 23 2023 Paul Howarth <paul@city-fan.org> - 0.998b-11
- Avoid use of systemd ".include" directive (rhbz#2216790)
- Avoid use of deprecated patch syntax
- Fix version number reported by rbldnsd

* Mon Jan 30 2023 Paul Howarth <paul@city-fan.org> - 0.998b-10
- Use SPDX-format license tag

* Mon Jan 30 2023 Florian Weimer <fweimer@redhat.com> - 0.998b-9
- Port non-autoconf configure script to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Paul Howarth <paul@city-fan.org> - 0.998b-4
- Drop EL-6 support
  - Always assume systemd init
  - Drop support for sysv-to-systemd migration
  - Use %%license unconditionally
  - Use %%{?systemd_requires}

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.998b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Paul Howarth <paul@city-fan.org> - 0.998b-1
- Update to 0.998b
  - Minor fixes in copyright and documentation
  - Bugfix: Minor fix to prevent errors on newer compilers
  - Fix for memory errors on very large datasets
- Upstream is now at rbldnsd.io
- Package new LICENSE.txt and README files

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Paul Howarth <paul@city-fan.org> - 0.998-6
- Account for systemd-units being merged into systemd at Fedora 17
- Drop support for SysV-to-systemd migration from Fedora 18, RHEL 7
- Use forward-looking conditionals
- Use fewer full paths from commands in scriptlets, to aid readability
- Drop legacy BuildRoot: and Group: tags
- Drop explicit buildroot cleaning in %%clean and %%install

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.998-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Paul Howarth <paul@city-fan.org> - 0.998-1
- Update to 0.998
  - Correctly handle V4MAPPED (v4 in v6) addresses; the original v6 prefix was
    wrong
  - Sometimes IP4-based datasets gave false positives when an IP6 dataset was
    present, and it was also possible to have false positives in IP6 datasets;
    both have been fixed

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.997a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.997a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Paul Howarth <paul@city-fan.org> 0.997a-4
- fix return value from initscript, by using process substitution instead of
  a while loop at the end of a pipe (#1118013)
- drop %%defattr, redundant since rpm 4.4

* Sun Jun  8 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.997a-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 21 2013 Paul Howarth <paul@city-fan.org> 0.997a-2
- use format string in dslog() invocation

* Mon Jul 29 2013 Paul Howarth <paul@city-fan.org> 0.997a-1
- update to 0.997a
  - minor fixes/changes in packaging, no code changes
  - in particular, fixes a build failure on *BSD introduced in 0.997

* Sun Jun 30 2013 Paul Howarth <paul@city-fan.org> 0.997-1
- update to 0.997
  - main feature of this version is ipv6 support
  - feature: ip6trie - new dataset supports listing of arbitrary length ip6
    CIDRs, along with individual A/TXT values for each prefix
  - feature: ip6tset - new dataset supports listing of ip6 /64 subnets and the
    exclusion of /128 subnets; only supports a single A/TXT value for the
    entire dataset
  - optimization: ip4trie - using new trie implementation (developed for the
    ip6trie dataset) decreases memory consumption by roughly a factor of three
  - feature: acl dataset - ip6 addresses are now supported in ACLs
  - feature: added --enable-asserts configure option to enable compilation of
    debugging assertions; assertion checking is disabled by default
  - featurette: zero-length "wildcard" IP4 CIDR prefixes are now allowed in
    ip4trie and acl datasets

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.996b-10
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.996b-9
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Paul Howarth <paul@city-fan.org> 0.996b-8
- rename systemctl-rbldnsd to rbldnsctl (#807504)

* Tue Apr 17 2012 Paul Howarth <paul@city-fan.org> 0.996b-7
- use native systemd init from F-17 onwards (see README.systemd)

* Mon Apr 16 2012 Paul Howarth <paul@city-fan.org> 0.996b-6
- fix some initscript issues (#807504)
- do a hardened build (PIE) where possible

* Thu Jan  5 2012 Paul Howarth <paul@city-fan.org> 0.996b-5
- nobody else likes macros for commands

* Wed Feb  9 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.996b-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.996b-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.996b-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 0.996b-1
- update to 0.996b
- _GNU_SOURCE no longer needed

* Wed Feb 20 2008 Paul Howarth <paul@city-fan.org> 0.996a-6
- fix exit codes for reload, stop, and try-restart actions of initscript

* Wed Feb 13 2008 Paul Howarth <paul@city-fan.org> 0.996a-5
- define _GNU_SOURCE for NI_MAXHOST symbol visibility
- LSB-ize initscript (#247043)

* Thu Aug 23 2007 Paul Howarth <paul@city-fan.org> 0.996a-4
- add buildreq gawk

* Thu Aug 23 2007 Paul Howarth <paul@city-fan.org> 0.996a-3
- upstream released a new version without changing the version number (the
  only changes are in debian/control and debian/changelog, neither of which
  are used in the RPM package)
- unexpand tabs in spec
- use the standard scriptlet for user/group creation in %%pre
- drop scriptlet dependencies on /sbin/service by calling initscript directly
- clarify license as GPL version 2 or later

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 0.996a-2
- FE6 mass rebuild

* Fri Jul 28 2006 Paul Howarth <paul@city-fan.org> 0.996a-1
- update to 0.996a

* Tue Feb 21 2006 Paul Howarth <paul@city-fan.org> 0.996-1
- update to 0.996
- use /usr/sbin/useradd instead of %%{_sbindir}/useradd
- add buildreq zlib-devel to support gzipped zone files

* Wed Feb 15 2006 Paul Howarth <paul@city-fan.org> 0.995-5
- license text not included in upstream tarball, so don't include it

* Tue Jun 28 2005 Paul Howarth <paul@city-fan.org> 0.995-4
- include gpl.txt as %%doc

* Mon Jun 27 2005 Paul Howarth <paul@city-fan.org> 0.995-3
- fix /etc/sysconfig/rbldnsd references to /var/lib/rbldns to point to
  %%{_localstatedir}/lib/rbldnsd instead
- don't enable daemons in any runlevel by default
- add -q option to sample entries in /etc/sysconfig/rbldnsd

* Fri Jun 17 2005 Paul Howarth <paul@city-fan.org> 0.995-2
- first Fedora Extras build, largely based on upstream spec file
