Name:           nmbscan
Version:        1.2.6
Release:        32%{?dist}
Summary:        NMB/SMB network scanner

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://nmbscan.g76r.eu/
Source0:        http://nmbscan.g76r.eu/down/%{name}-%{version}.tar.gz
Source1:        %{name}.1

# Remove dependency on deprecated arp tool, use ip neigh instead
Patch0:         %{name}-1.2.6-arp.patch

# rhbz#2279884 - Use grep -E instead of egrep to avoid using the grep alias
Patch1:         %{name}-1.2.6-egrep.patch


BuildArch:      noarch

Requires:       bind-utils
Requires:       iputils
Requires:       iproute
Requires:       samba-client

%description
Scans a SMB shares network, using NMB and SMB protocols. Useful to acquire
an information on a local area network (security audit, etc.)

Matches the information such as NMB/SMB/Windows host name, IP address,
IP host name, Ethernet MAC address, Windows user name,
NMB/SMB/Windows domain name and master browser.

Can discover all NMB/SMB/Windows hosts on a local area network thanks to 
hosts lists maintained by master browsers.

%prep
%autosetup -c %{name}-%{version}


%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 nmbscan %{buildroot}%{_bindir}/
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files
%doc Documentation/HOWTO_contribute.txt
%license Documentation/gplv2.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 21 2024 Michal Ambroz <rebus AT seznam.cz> - 1.2.6-31
- rhbz#2279884 - use grep -E instead of egrep

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.6-30
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-18
- Update spec file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Michal Ambroz <rebus AT seznam.cz> - 1.2.6-5
- patched tp use "ip neigh" rather than arp for ARP resolution 
- Patch from Jiri Popelka <jpopelka@redhat.com>

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 12 2010 Michal Ambroz <rebus AT seznam.cz> - 1.2.6-1
- rebuild for the version 1.2.6

* Wed Aug 04 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.2.5-5
- Fixed the project URL
- Added a man page (thx to Michal Ambroz)
- Cosmetic changes

* Sat Apr 17 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.2.5-4
- Fix the license and Source0

* Fri Mar 19 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.2.5-3
- Add Requires: bind-utils, iputils, net-tools

* Sat Mar 13 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.2.5-2
- Fix the license
- Fix the summary
- Replace generally useful macros by regular commands

* Thu Feb 04 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.2.5-1
- Initial package build

