#===== Generic Info ======
%define apache_confdir %{_sysconfdir}/httpd/conf.d
%define lightsquid_confdir %{_sysconfdir}/lightsquid
%define lightsquid_reportdir %{_localstatedir}/lightsquid
%define srcname lightsquid-%{version}
%define ip2namepath %{_datadir}/%{name}/ip2name

Summary: Light, small, and fast log analyzer for squid proxy
Name: lightsquid
Version: 1.8
Release: 31%{?dist}
License: GPLv2+
Url: http://lightsquid.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0: shebang-and-thanks.patch
Requires: perl-GDGraph3d perl-GD perl-GDGraph
Requires: crontabs
BuildRequires: perl-generators
BuildRequires: sed
BuildArch: noarch
BuildRequires: util-linux-ng

%description
%{name} is a small and fast Squid log analyzer.

%prep
%setup -q -n %{srcname}
%patch0 -p1

%{__sed} -i 's|/var/www/html/lightsquid/lang|%{_datadir}/%{name}/lang|' lightsquid.cfg
%{__sed} -i 's|/var/www/html/lightsquid/tpl|%{_datadir}/%{name}/tpl|' lightsquid.cfg
%{__sed} -i 's|/var/www/html/lightsquid/ip2name|%{_datadir}/%{name}/ip2name|' lightsquid.cfg
%{__sed} -i 's|/var/www/html/lightsquid/report|%{lightsquid_reportdir}|' lightsquid.cfg
%{__sed} -i 's|/var/www/html/lightsquid|%{lightsquid_confdir}|' lightsquid.cfg
%{__sed} -i 's|require "ip2name|require "%{ip2namepath}|' lightparser.pl
%{__sed} -i 's|lightsquid.cfg|%{lightsquid_confdir}/lightsquid.cfg|' *.cgi *.pl
%{__sed} -i 's|common.pl|%{_datadir}/%{name}/common.pl|' *.cgi *.pl
%{__sed} -i 's|/etc/squid/users.txt|/etc/lightsquid/users.txt|' ip2name/ip2name.*list*
%{__sed} -i 's|"../lightsquid.cfg"|"%{lightsquid_confdir}/lightsquid.cfg"|' tools/fixreport.pl
%{__sed} -i 's|#/bin/perl|#!/usr/bin/perl|' tools/fixreport.pl
%{__sed} -i 's|#/bin/perl|#!/usr/bin/perl|' lang/check_tpl_lng.pl
col -bx <lang/check_tpl_lng.pl> lang/check_tpl_lng.pl.tmp
%{__mv} -f lang/check_tpl_lng.pl.tmp lang/check_tpl_lng.pl
col -bx <doc/thanks.txt> doc/thanks.txt.tmp
%{__mv} -f doc/thanks.txt.tmp doc/thanks.txt
%{__sed} -i 's|../../lightsquid.cfg|%{lightsquid_confdir}/lightsquid.cfg|' tools/SiteAggregator/ReportExplorer.pl
%{__sed} -i 's|../../lightsquid.cfg|%{lightsquid_confdir}/lightsquid.cfg|' tools/SiteAggregator/SiteAgregator.pl
iconv -f WINDOWS-1251 -t UTF8 lang/ru.lng > lang/ru-utf8.lng
%{__sed} -i 's|windows-1251|utf8|' lang/ru-utf8.lng

%install
%{__rm} -rf %{buildroot}

install -m 755 -d %{buildroot}%{_sbindir}
install -m 755 -d %{buildroot}%{_sysconfdir}/cron.daily
install -m 755 -d %{buildroot}%{apache_confdir}
install -m 755 -d %{buildroot}%{lightsquid_reportdir}
install -m 755 -d %{buildroot}%{_datadir}/%{name}/{tools,lang,ip2name,tpl,cgi}
install -m 755 -d %{buildroot}%{_datadir}/%{name}/tools/SiteAggregator
install -m 755 lightparser.pl %{buildroot}%{_sbindir}/
install -pD -m 644 lightsquid.cfg %{buildroot}%{lightsquid_confdir}/lightsquid.cfg
install -pD -m 644 group.cfg.src %{buildroot}%{lightsquid_confdir}/group.cfg
install -pD -m 644 realname.cfg %{buildroot}%{lightsquid_confdir}/realname.cfg

%{__cat} << EOF > %{buildroot}%{_sysconfdir}/cron.daily/lightsquid
#!/bin/bash
%{_sbindir}/lightparser.pl yesterday
EOF
%__chmod 0755 %{buildroot}%{_sysconfdir}/cron.daily/lightsquid

%{__cat} << EOF > %{buildroot}%{apache_confdir}/lightsquid.conf
Alias /lightsquid %{_datadir}/%{name}/cgi

<Directory %{_datadir}/%{name}/cgi>
    DirectoryIndex index.cgi
    Options ExecCGI
    AddHandler cgi-script .cgi
    AllowOverride None
</Directory>
EOF
%__chmod 0644 %{buildroot}%{apache_confdir}/lightsquid.conf

# install lib
install -p -m 755 {common.pl,check-setup.pl} %{buildroot}%{_datadir}/%{name}/
install -p -m 755 {lang/check_tpl_lng.pl,lang/check_lng.pl} %{buildroot}%{_datadir}/%{name}/lang
install -p -m 644 lang/*.lng %{buildroot}%{_datadir}/%{name}/lang/
install -p -m 644 ip2name/* %{buildroot}%{_datadir}/%{name}/ip2name/
install -p -m 755 tools/*.pl %{buildroot}%{_datadir}/%{name}/tools/
install -p -m 755 tools/SiteAggregator/* %{buildroot}%{_datadir}/%{name}/tools/SiteAggregator/

%{__cp} -aRf tpl/* %{buildroot}%{_datadir}/%{name}/tpl/

install -p -m 755 [^A-Z]*.cgi %{buildroot}%{_datadir}/%{name}/cgi/

%files
%doc doc/*
%_sbindir/*
%_datadir/%name/ip2name/*
%_datadir/%name/lang/*
%_datadir/%name/tools/*
%_datadir/%name/tpl/*
%_datadir/%name/check-setup.pl
%_datadir/%name/common.pl
%dir %{lightsquid_confdir}
%dir %{lightsquid_reportdir}
%config(noreplace) %{lightsquid_confdir}/*.cfg
%config(noreplace) %{_sysconfdir}/cron.daily/lightsquid

%package apache
Summary: Web Controls for %{name}
Requires: %{name} = %{version}-%{release}
Requires: httpd
%description apache
%{name} configuration files and scripts for Apache.


%files apache
%config(noreplace) %{apache_confdir}/lightsquid.conf
%_datadir/%name/cgi/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.8-16
- Add missing requires on crontabs
- Mark cron job as config(noreplace)
- Fix RHBZ#989072

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.8-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 18 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-9
- Some fixed littles bugs wich Ruediger Landmann <r.landmann@redhat.com>.

* Wed Nov 17 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-8
- Fixed of grammatics errors wich Ruediger Landmann <r.landmann@redhat.com>.
- Some fixed littles bugs wich Ruediger Landmann <r.landmann@redhat.com>.

* Thu Jul 22 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-7
- Moved *.cgi file back to lightsquid-apache package.

* Thu Jul 20 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-6
- Some fixed by Andrey Lavrinenko lxlight@gmail.com.

* Thu Jul 20 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-5
- Some fixed littles bugs.
- Deleted SOURCE.redhat file.
- Deleted post directive with reports files.
- Moved *.cgi file from the lightsquid-apache package.
- Some cosmetics by Andrey Lavrinenko lxlight@gmail.com.

* Thu Jul 19 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-4
- Added of Requires: httpd wich Manuel Wolfshant <wolfy@nobugconsulting.ro>.
- Returned self package of lightsquid-apache.
- Some cosmetics edition wich Peter Lemenkov <lemenkov@gmail.com>.

* Thu Jul 16 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-3
- Fixed some the littles errors with Manuel Wolfshant <wolfy@nobugconsulting.ro>.

* Thu Jul 16 2010 Popkov Aleksey <aleksey@psniip.ru> 1.8-2
- lightsquid.conf - moved from self package.
- Fixed some the littles bugs.
- Some cosmetics edition.

* Thu Jul 9 2009 Popkov Aleksey <aleksey@psniip.ru> 1.8-1
- Build version lightsquid 1.8
- Added patch for fixed some the littles bugs.

* Wed Jun 17 2009 Popkov Aleksey <aleksey@psniip.ru> 1.7.1-1
- Some removed sed's
- Added BuildRoot directive
- lightsquid.conf - moved from main package to self package.

* Tue Jun 16 2009 Popkov Aleksey <aleksey@psniip.ru> 1.7.1-1
- Adapted for Fedora Group
