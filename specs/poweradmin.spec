Name:         poweradmin
Version:      2.1.7
Release:      21%{?dist}
Summary:      A friendly web-based DNS administration tool for Bert Hubert's PowerDNS server

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:      GPL-3.0-or-later
URL:          http://www.poweradmin.org
Source0:      https://www.poweradmin.org/download/%{name}-%{version}.tgz
Source1:      %{name}.conf
Source2:      %{name}-config.inc.php
Source3:      README.Fedora
BuildArch:    noarch

Requires:     httpd
Requires:     php
Requires:     php-pear(MDB2_Driver_mysqli)
Requires:     php-pear(MDB2_Driver_pgsql)
Requires:     php-mcrypt

%description
Poweradmin is a friendly web-based DNS administration tool for Bert Hubert's
PowerDNS server. The interface has full support for most of the features of
PowerDNS. It has full support for all zone types (master, native and slave),
for supermasters for automatic provisioning of slave zones, full support
for IPv6 and comes with multi-language support.

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{__mkdir} -pv %{buildroot}/%{_datadir}/%{name}
%{__mkdir} -pv %{buildroot}/%{_sysconfdir}/httpd/conf.d/
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/%{name}

%{__cp} -adpv ./* %{buildroot}/%{_datadir}/%{name}
%{__cp} -pv %{SOURCE1} %{buildroot}/%{_sysconfdir}/httpd/conf.d/%{name}.conf

%{__cp} %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/config.inc.php
%{__cp} %{SOURCE3} .
ln -s %{_sysconfdir}/%{name}/config.inc.php %{buildroot}/%{_datadir}/%{name}/inc/config.inc.php

%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/install
%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/README.md
%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/LICENSE

%files
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
%doc LICENSE README.md README.Fedora

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.7-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Sven Lankes <sven@lank.es> - 2.1.7-2
- replace pear-MDB2-mysql driver with mysqli variant

* Mon Feb 22 2016 Sven Lankes <sven@lank.es> - 2.1.7-1
- new upstream release
- Add README.Fedora listing manual steps required to upgrade from 2.1.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Sven Lankes <sven@lank.es> - 2.1.6-3
- fix httpd config file to work with apache 2.2 and 2.4 
- fixes rhbz #871373

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Sven Lankes <sven@lank.es> - 2.1.6-1
- new upstream release
- remove upstreamed templatefix

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Sven Lankes <sven@lank.es> 2.1.5-1
- new upstream release (includes template fix from svn r512)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Sven Lankes <sven@lank.es> 2.1.5-0.2.rc1
- Add new runtime-dependency php-mcrypt

* Sun Dec 12 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.1.5-0.1.rc1
- Upstream released new version

* Thu Nov 05 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.1.3-3
- Symlink config.inc.php to right directory

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.1.3-1
- Upstream released new version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 2.1.2-2
- Review fixes (#480552)

* Sun Jan 18 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 2.1.2-1
- Initial import

