Summary: A syslog data viewer for the web
Name: phplogcon
Version: 2.1.6
Release: 27.beta%{?dist}
License: GPLv3+
URL: http://www.phplogcon.com/
Source0: http://download.adiscon.com/phplogcon/%{name}-%{version}.tar.gz
Source1: README.fedora
Source2: phplogcon-httpd.conf
Requires: php php-gd webserver
BuildArch: noarch

%description
phpLogCon is a web interface to syslog and other network event data. It
provides easy browsing and some basic analysis of realtime network events.
Depending on the applications feeding the database, it can process syslog
messages, Windows event log entries and even SNMP trap data - just to name a
few.

%prep

%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -aRf src/*     %{buildroot}/%{_datadir}/%{name}/

touch             %{buildroot}%{_sysconfdir}/%{name}/config.php
ln -s ../../../%{_sysconfdir}/%{name}/config.php %{buildroot}/%{_datadir}/%{name}/config.php

install -d -m 755  %{buildroot}%{_sysconfdir}/httpd/conf.d
cp      %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
cp      %{SOURCE1} ./

%files
%doc COPYING INSTALL ChangeLog README.fedora
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0755,root,apache) %dir %{_sysconfdir}/%{name}
%attr(0664,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/config.php
%{_datadir}/%{name}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-27.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-26.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-25.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-24.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-23.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-22.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-21.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-20.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Remi Collet <rcollet@redhat.com> - 2.1.6-9.beta
- fix configuration file for httpd 2.4, #871461

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 23 2008 Peter Vrabec <pvrabec@redhat.com> 2.1.6-3.beta
- package improvements (#444722)

* Thu May 22 2008 Peter Vrabec <pvrabec@redhat.com> 2.1.6-2.beta
- package improvements (#444722)

* Mon May 19 2008 Peter Vrabec <pvrabec@redhat.com> 2.1.6-1.beta
- package improvements (#444722)

* Mon May 05 2008 Peter Vrabec <pvrabec@redhat.com> 2.3.1-1
- package improvements (#444722)

* Mon Apr 21 2008 Peter Vrabec <pvrabec@redhat.com> 2.1.3-1
- initial fedora package

