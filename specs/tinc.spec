Name:           tinc
Version:        1.0.36
Release:        15%{?dist}
Summary:        A virtual private network daemon

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  lzo-devel
BuildRequires:  systemd
BuildRequires:  systemd-units

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%autosetup

%build
%configure --with-systemd=%{_unitdir}
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service

%files
%doc AUTHORS COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.*
%{_sbindir}/%{name}d
%{_unitdir}/%{name}*.service

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.36-14
- Fix FTBFS (closes rhbz#2301329)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.36-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.36-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.36-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.36-1
- Update to new upstream version 1.0.36

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.35-3
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.35-1
- Fix for CVE-2018-16737, CVE-2018-16738 and CVE-2018-16758 
- Update to new upstream version 1.0.35

* Fri Oct 26 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.34-1
- Update to new upstream version 1.0.34

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.33-3
- Fix BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.33-1
- Update to new upstream version 1.0.33

* Sat Sep 30 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.32-1
- Update to new upstream version 1.0.32

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.31-1
- Update to new upstream version 1.0.31

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.30-1
- Update to new upstream version 1.0.30

* Sat Apr 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.28-1
- Use upstream service units
- Update to new upstream version 1.0.28

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.26-1
- Update to new upstream version 1.0.26

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-6
- Fix service file (rhbz#1155666)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-3
- Update systemd

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-2
- Migration to systemd (rhbz#1078237)

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-1
- Update to new upstream version 1.0.24

* Tue Oct 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.23-1
- Update to new upstream version 1.0.23

* Mon Aug 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.22-1
- Update to new upstream version 1.0.22

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.21-1
- Update to new upstream version 1.0.21

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.19-1
- Update to new upstream version 1.0.16

* Sat Mar 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.18-1
- Update to new upstream version 1.0.18

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-1
- Update to new upstream version 1.0.16

* Wed Apr 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.13-1
- Update to new upstream version 1.0.13

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.12-1
- Update to new upstream version 1.0.12

* Mon Dec 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.11-1
- Update to new upstream version 1.0.11

* Thu Oct 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.10-1
- Removed translation stuff
- Update to new upstream version 1.0.10

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.9-1
- Initial package for Fedora
