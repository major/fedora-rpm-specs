Name:		pam_shield
Version:	0.9.5
Release:	32%{?dist}
Summary:	Pam Shield - A pam module to counter brute force attacks

License:	GPLv2
URL:		http://www.heiho.net/pam_shield/index.html
Source0:	http://www.heiho.net/pam_shield/pam_shield-0.9.5.tar.gz
Source1:	shield-trigger.8.gz
Source2:	shield-purge.8.gz
Source3:	shield-trigger-iptables.8.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	pam-devel, gdbm-devel
%if 0%{?rhel} <= 5
Requires:	policycoreutils
%else
Requires:	policycoreutils-python
%endif
Patch0:		shield_purge_segfault.patch
Patch1:		shield-trigger-iptables.patch

%description
This is a pam module that supports brute force blocking against pam
authentication mechanisms.

%prep
%setup -q -n pam_shield-%{version}
mv GPL LICENSE
%patch0 -p0 -b .shield_purge_segfault
%patch1 -p0 -b .shield_trigger_iptables
#disable debug by default
sed -i -e 's/debug on/debug off/' shield.conf
#change to block all users for failed attempts
sed -i -e 's/block unknown-users/block all-users/' shield.conf
#reduce connections before block from 10 to 3
sed -i -e 's/max_conns 10/max_conns 3/' shield.conf
#reduce retention time from 1 week to 1 hour
sed -i -e 's/retention 1w/retention 1h/' shield.conf
#change the default behavior from shield-trigger to shield-trigger-iptables
#this uses iptables instead of route to block brute force attack
sed -i -e 's/shield\-trigger/shield-trigger-iptables/' shield.conf

%build
#software required -fPIC flag to build
make CFLAGS="%{optflags} -fPIC"

%check

%install
rm -rf %{buildroot}
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/security
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/cron.daily
mkdir -p -m 755 %{buildroot}%{_sbindir}
mkdir -p -m 755 %{buildroot}/%{_lib}/security
mkdir -p -m 755 %{buildroot}%{_mandir}/man8
install -m 755 pam_shield.so %{buildroot}/%{_lib}/security/
install -m 755 -T pam_shield.cron %{buildroot}%{_sysconfdir}/cron.daily/pam_shield
install -m 755 shield-trigger %{buildroot}%{_sbindir}/
install -m 755 shield-trigger-iptables %{buildroot}%{_sbindir}/
install -m 755 shield-purge %{buildroot}%{_sbindir}/
install -m 644 shield.conf %{buildroot}%{_sysconfdir}/security/
mkdir -p -m 700 %{buildroot}/var/lib/pam_shield
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man8/

%post
semanage fcontext -a -t var_auth_t '/var/lib/pam_shield' 2>/dev/null || :
restorecon -R /var/lib/pam_shield || :

%postun
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t var_auth_t '/var/lib/pam_shield' 2>/dev/null || :
if [ -e "/var/lib/pam_shield/db" ]
then
rm -f /var/lib/pam_shield/db
fi
fi

%files
/%{_lib}/security/pam_shield.so
%doc INSTALL README LICENSE CREDITS Changelog
%doc %{_mandir}/man8/shield-trigger.8.gz
%doc %{_mandir}/man8/shield-purge.8.gz
%doc %{_mandir}/man8/shield-trigger-iptables.8.gz
%config(noreplace) %{_sysconfdir}/security/shield.conf
%dir /var/lib/pam_shield
%{_sysconfdir}/cron.daily/pam_shield
%{_sbindir}/shield-trigger
%{_sbindir}/shield-purge
%{_sbindir}/shield-trigger-iptables

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.5-14
- Install docs with special %%doc (#994019).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-9
- fixed selinux conflict by adding context definition
- added some additional cleanup on uninstall
* Sat Apr 30 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-8
- patches shield-trigger-iptables to insert rules instead of add
- and added checks for chain existance and creation if necessary
- before adding rules to iptables/ip6tables and dropped the
- destination port so it can be used for any service
* Sun Apr 10 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-7
- restored /var/lib/pam_shield to 700
* Sat Apr 9 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-6
- fixed the permissions duplications
- changed permissions on /var/lib/pam_shield to 755
- changed permissions on pam_shield.so to 755
- removed -s flag from install command to preserve
- debuginfo data
* Fri Apr 8 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-5
- fixed issues with my implementation of %%{optflags}
- this in turn fixed the empty -debug package
* Thu Apr 7 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-4
- fixed a typo in previous release in %%build section
* Thu Apr 7 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-3
- updated %%build section with %%{optflags}
* Mon Mar 28 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-2
- included shield-trigger-iptables
- changed default blocking method from route to iptables
- modified default retention policy from 1 week to 1 hour
- added man page for shield-trigger-iptables
- fixed typos in man page for shield-purge
* Sat Mar 26 2011 Carl Thompson <fedora@red-dragon.com> 0.9.5-1
- Initial package
