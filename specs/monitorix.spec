%global __requires_exclude perl\\(Monitorix\\)|perl\\(HTTPServer\\)
%global __provides_exclude perl\\(

Name:              monitorix
Version:           3.16.0
Release:           2%{?dist}
Summary:           A free, open source, lightweight system monitoring tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:           GPL-2.0-or-later
URL:               http://www.monitorix.org
Source0:           http://www.monitorix.org/%{name}-%{version}.tar.gz
BuildArch:         noarch
BuildRequires:     perl-interpreter
BuildRequires:     perl-generators
BuildRequires:     systemd
Requires:          logrotate
Requires:          perl(DBD::mysql)
Requires:          perl(DBD::Pg)
Requires:          perl(IO::Socket::SSL)
Requires:          perl(Time::HiRes)
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Monitorix is a free, open source and lightweight system monitoring tool
designed to monitor as many services and system resources as possible. It has
been created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well.

%prep
%setup -q
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}.cgi

%build
# Nothing to build.

%install
install -pDm644 docs/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -pDm644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
install -pDm644 lib/*.pm %{buildroot}%{_prefix}/lib/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 logo_top.png %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 logo_bot.png %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 %{name}ico.png %{buildroot}%{_sharedstatedir}/%{name}/www
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/imgs
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/cgi
install -pDm755 %{name}.cgi %{buildroot}%{_sharedstatedir}/%{name}/www/cgi
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/css
install -pDm644 css/*.css %{buildroot}%{_sharedstatedir}/%{name}/www/css
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/reports
install -pDm644 reports/*.html %{buildroot}%{_sharedstatedir}/%{name}/reports
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/usage
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
install -pDm644 man/man5/%{name}.conf.5 %{buildroot}%{_mandir}/man5
install -pDm644 man/man8/%{name}.8 %{buildroot}%{_mandir}/man8
install -pDm644 docs/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pDm644 docs/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc Changes README README.nginx
%doc docs/%{name}-alert.sh docs/%{name}-apache.conf docs/%{name}-lighttpd.conf
%doc docs/htpasswd.pl
%license COPYING
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%dir %{_sysconfdir}/%{name}/conf.d
%dir %{_sharedstatedir}/%{name}/
%dir %{_sharedstatedir}/%{name}/www
%dir %{_sharedstatedir}/%{name}/www/cgi
%dir %{_sharedstatedir}/%{name}/www/css
%dir %{_sharedstatedir}/%{name}/reports
%{_sharedstatedir}/%{name}/www/css/*.css
%{_sharedstatedir}/%{name}/reports/*.html
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_sharedstatedir}/%{name}/www/logo_top.png
%{_sharedstatedir}/%{name}/www/logo_bot.png
%{_sharedstatedir}/%{name}/www/%{name}ico.png
%{_sharedstatedir}/%{name}/www/cgi/%{name}.cgi
%attr(755,nobody,nobody) %{_sharedstatedir}/%{name}/www/imgs
%attr(755,root,root) %{_sharedstatedir}/%{name}/usage

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Jordi Sanfeliu <jordi@fibranet.cat> - 3.16.0-1
- Updated to 3.16.0.

* Tue Nov 26 2024 Jordi Sanfeliu <jordi@fibranet.cat> - 3.15.90-1
- Updated to 3.15.90.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.15.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Jordi Sanfeliu <jordi@fibranet.cat> - 3.15.0-1
- Updated to 3.15.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.14.0-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Jordi Sanfeliu <jordi@fibranet.cat> - 3.14.0-1
- Updated to 3.14.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.13.1-3
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.13.1-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Jordi Sanfeliu <jordi@fibranet.cat> - 3.13.1-1
- Updated to 3.13.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jordi Sanfeliu <jordi@fibranet.cat> - 3.13.0-1
- Updated to 3.13.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.12.0-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.12.0-2
- Perl 5.32 rebuild

* Fri Feb 21 2020 Jordi Sanfeliu <jordi@fibranet.cat> - 3.12.0-1
- Updated to 3.12.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.11.0-2
- Perl 5.30 rebuild

* Thu Mar 14 2019 Jordi Sanfeliu <jordi@fibranet.cat> - 3.11.0-1
- Updated to 3.11.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.10.1-2
- Perl 5.28 rebuild

* Thu Mar 15 2018 Jordi Sanfeliu <jordi@fibranet.cat> - 3.10.1-1
- Updated to 3.10.1.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jordi Sanfeliu <jordi@fibranet.cat> - 3.10.0-1
- Updated to 3.10.0.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.9.0-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Jordi Sanfeliu <jordi@fibranet.cat> - 3.9.0-1
- Updated to 3.9.0.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.8.1-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Jordi Sanfeliu <jordi@fibranet.cat> - 3.8.1-1
- Updated to 3.8.1.

* Thu Sep 17 2015 Jordi Sanfeliu <jordi@fibranet.cat> - 3.8.0-1
- Updated to 3.8.0.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.7.0-2
- Perl 5.22 rebuild

* Thu Mar 12 2015 Jordi Sanfeliu <jordi@fibranet.cat> - 3.7.0-1
- Updated to 3.7.0.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.6.0-2
- Perl 5.20 rebuild

* Wed Aug 20 2014 Jordi Sanfeliu <jordi@fibranet.cat> - 3.6.0-1
- Updated to 3.6.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Jordi Sanfeliu <jordi@fibranet.cat> - 3.5.1-1
- Updated to 3.5.1.

* Mon Mar 31 2014 Jordi Sanfeliu <jordi@fibranet.cat> - 3.5.0-1
- Updated to 3.5.0.

* Tue Dec 03 2013 Christopher Meng <rpm@cicku.me> - 3.4.0-1
- Update to 3.4.0

* Sat Nov 23 2013 Christopher Meng <rpm@cicku.me> - 3.3.1-1
- Urgent security update.

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 3.3.0-1
- New release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.2.1-2
- Perl 5.18 rebuild

* Wed Jun 05 2013 Christopher Meng <rpm@cicku.me> - 3.2.1-1
- New release.

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 3.2.0-2
- Fixes.

* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 3.2.0-1
- New release.

* Tue Apr 30 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-4
- libdir fixed.

* Sat Apr 06 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-3
- Errors fixed.

* Tue Apr 02 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-2
- Fixed review bugs(BZ#947071)

* Mon Apr 01 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-1
- Initial Package.
