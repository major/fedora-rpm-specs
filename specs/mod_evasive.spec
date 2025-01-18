Name:           mod_evasive
Version:        2.3.0
Release:        2%{?dist}
Summary:        Denial of Service evasion module for Apache

License:        GPL-2.0-or-later
URL:            https://github.com/jvdmr/mod_evasive
Source0:        https://github.com/jvdmr/mod_evasive/archive/%{version}.tar.gz
Source1:        mod_evasive.conf

BuildRequires:  httpd-devel, gcc
Requires:       httpd
Requires:       httpd-mmn = %([ -a %{_includedir}/httpd/.mmn ] && cat %{_includedir}/httpd/.mmn || echo missing)

%description
mod_evasive is an evasive maneuvers module for Apache to provide evasive 
action in the event of an HTTP DoS or DDoS attack or brute force attack. It 
is also designed to be a detection and network management tool, and can be 
easily configured to talk to firewalls, routers, etc. mod_evasive presently 
reports abuses via email and syslog facilities. 


%prep
%setup -q -n %{name}-%{version}


%build
# create apache httpd-2.4 version and compile it
sed 's/connection->remote_ip/connection->client_ip/' \
  < mod_evasive20.c > mod_evasive24.c
apxs -Wc,"%{optflags}" -c mod_evasive24.c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -pm 755 \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -pm 755 .libs/mod_evasive24.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/



%files
%doc README.md LICENSE CHANGELOG
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%{_libdir}/httpd/modules/*


%changelog
* Thu Jan 16 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3.0-2
- fix apache httpd module loading

* Wed Jan 15 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3.0-1
- update to maintained fork

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.1-44
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-31
- Fix HTTP connection in test.pl script.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-29
- Added gcc to build requires.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-22
- revert evasive24_module to evasive20_module (bz#1232360)

* Tue May 26 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-21
- changed mod_evasive20 to mod_evasive24 (bz#1190556)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-18
- Rebuild for yum release changes. BZ#1072025

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-15
- fix configuration file for new version (#879269)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 31 2012 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-13
- adapt to httpd-2.4: changed remote_ip to client_ip

* Thu Mar 29 2012 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-12
- apxs moved to bindir, do not use sbindir macro

* Tue Mar 27 2012 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.1-11
- Rebuild for new httpd-mmn

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10.1-6
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.1-5.1
- Autorebuild for GCC 4.3

* Wed Sep 05 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-4.1
- Rebuild for APR changes

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.10.1-4
- Rebuild for selinux ppc32 issue.

* Tue Apr 10 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-3
- Modify the URL and finally import into extras.

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-2
- The source moved to another domain since last year.
- use _sbindir macro for apxs.

* Tue Dec 06 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-1
- Cleaning up description
- Cleaning up install
- Slight modification to default config (add DOSWhitelist entries)
- Disttagging
- Adding test.pl to docs

* Wed Nov 16 2005 Kosntantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-0.1
- Initial packaging.
