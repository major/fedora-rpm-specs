Name:       yourls
Version:    1.7.1
Release:    15%{?dist}
Summary:    Your Own URL Shortener
# License scenario:
#  * yourls files: GPL+
#  * GeoIP files: LGPLv2+
#  * JQuery files: MIT or GPLv2
License:    GPL+ and LGPLv2+ and (MIT or GPLv2)
URL:        http://yourls.org
Source0:    https://github.com/YOURLS/YOURLS/archive/%{version}.tar.gz
Source1:    yourls-httpd.conf
Patch0:     yourls.change-config-path.patch
Patch1:     yourls.add-fedora-readme.patch

Requires:   php >= 4.3.0
Requires:   mysql >= 4.1.0
Requires:   php-mysqlnd
Requires:   httpd
BuildArch:  noarch


%description
YOURLS is a small set of PHP scripts that will allow you to run your own URL 
shortening service (a la TinyURL). You can make it private or public, 
you can pick custom keyword URLs, it comes with its own API.


%prep
%setup -q -n YOURLS-%{version}
%patch0
%patch1


%build


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}
install -m 0644 -D -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/yourls.conf
cp -ad ./* ${RPM_BUILD_ROOT}%{_datadir}/%{name}
mv ./user/config-sample.php ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/config.php

# Remove docs from datadir, to be put in defaultdocdir later
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/%{name}/{README.fedora,README.md,CHANGELOG.md,CONTRIBUTING.md,LICENSE.md,readme.html,sample-*}

# Remove Flash files
rm -f ${RPM_BUILD_ROOT}%{_datadir}/%{name}/js/ZeroClipboard.swf


%files
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/yourls.conf
%doc README.md CHANGELOG.md CONTRIBUTING.md LICENSE.md
%doc readme.html sample-public-api.txt sample-public-front-page.txt
%doc sample-remote-api-call.txt sample-robots.txt
%doc README.fedora
%dir %{_sysconfdir}/%{name}/
%{_datadir}/%{name}/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Martin Krizek <mkrizek@redhat.com> - 1.7.1-3
- fix php-mysqlnd dep

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 7 2015 Martin Krizek <mkrizek@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4.20150410gitabc7d6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Martin Krizek <mkrizek@redhat.com> - 1.7-3.20150410gitabc7d6c
- Update to the latest master from git
- Fix bz #1157335

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Martin Krizek <mkrizek@redhat.com> - 1.7-1
- Update to 1.7
- Add upstream patch solving: Incorrect error message after installation

* Thu Aug 15 2013 Martin Krizek <mkrizek@redhat.com> - 1.6-1
- Update to 1.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Martin Krizek <mkrizek@redhat.com> - 1.5.1-3
- Add README.fedora

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Martin Krizek <mkrizek@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Martin Krizek <mkrizek@redhat.com> - 1.5-4
- Fixed license
- Fixed DOC line endings in the doc files

* Mon Aug 15 2011 Martin Krizek <mkrizek@redhat.com> - 1.5-3
- Editing source is now done with patch instead of sed

* Wed Aug 03 2011 Martin Krizek <mkrizek@redhat.com> - 1.5-2
- Fixed wrong version of license
- Made calling sed in prep section more readable

* Wed Jul 27 2011 Martin Krizek <mkrizek@redhat.com> - 1.5-1
- Initial packaging
