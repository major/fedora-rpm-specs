%{!?_httpd_contentdir: %{expand: %%global _httpd_contentdir /var/www}}

Name:           php-adodb
Summary:        Database abstraction layer for PHP
Version:        5.22.7
Release:        5%{?dist}

License:        BSD-3-Clause or LGPL-2.0-or-later
URL:            http://adodb.org
BuildArch:      noarch
# for macros
BuildRequires:  httpd-devel

Source0:        http://downloads.sourceforge.net/adodb/adodb-%{version}.tar.gz

Requires:       php-common

%description
ADOdb is an object oriented library written in PHP that abstracts database 
operations for portability. It is modelled on Microsoft's ADO, but has many
improvements that make it unique (eg. pivot tables, Active Record support, 
generating HTML for paging recordsets with next and previous links, cached 
recordsets, HTML menu generation, etc).
ADOdb hides the differences between the different databases so you can easily
switch DBs without changing code.

# !! TODO !! MAKE A SUBPACKAGE FOR THE PEAR::AUTH DRIVER

%prep
%setup -q -n adodb5


%build
# fix dir perms
find . -type d | xargs chmod 755
# fix file perms
find . -type f | xargs chmod 644


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_httpd_contentdir}/icons
install -d $RPM_BUILD_ROOT%{_datadir}/php/adodb
cp -pr * $RPM_BUILD_ROOT%{_datadir}/php/adodb/

# cleanup
rm -rf $RPM_BUILD_ROOT%{_datadir}/php/adodb/docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/php/adodb/tests
rm -f $RPM_BUILD_ROOT%{_datadir}/adodb/*.txt


%files
%license LICENSE.md
%doc README.md docs/*
%{_datadir}/php/adodb


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.22.7-1
- 5.22.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.22.6-1
- 5.22.6

* Tue Apr 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.22.5-1
- 5.22.5

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.22.4-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.22.4-1
- 5.22.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Gianluca Sforna <giallu@gmail.com> - 5.20.6-2
- update to latest release
- fix for CVE-2016-7405 (#1376365)
- spec file clean up

* Tue Sep  6 2016 Gianluca Sforna <giallu@gmail.com> - 5.15-10
- fix for CVE-2016-4855 (#1373374)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jon Ciesla <limburgher@gmail.com> 5.15-6
- Date fixes to correct FTBFS.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 5.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Remi Collet <rcollet@redhat.com> - 5.15-3
- fix icons locations for httpd 2.4 (#876907)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Gianluca Sforna <giallu@gmail.com> - 5.15-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 05 2011 Gianluca Sforna <giallu@gmail.com> - 5.12-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 23 2010 Gianluca Sforna <giallu gmail com> - 5.11-1
- New upstream release

* Thu Nov 12 2009 Gianluca Sforna <giallu gmail com> - 5.10-1
- New upstream release

* Tue Aug 25 2009 Gianluca Sforna <giallu gmail com> - 5.09a-1
- Update to latest release
- Fix download URL
- Update summary and description
- Requires php-common

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.95-3.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.95-2.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 4.95-1.a
- version 4.95a
- fix license tag

* Fri Apr 06 2007 Aurelien Bompard <abompard@fedoraproject.org> 4.94-1
- version 4.94
- move install path to %%_datadir/php/adodb (#235461)

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 4.92-1
- version 4.92

* Fri Apr 14 2006 Aurelien Bompard <gauret[AT]free.fr> 4.80-1
- version 4.80

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 4.72-1
- version 4.72

* Fri Dec 23 2005 Aurelien Bompard <gauret[AT]free.fr> 4.68-1
- version 4.68

* Fri Nov 18 2005 Aurelien Bompard <gauret[AT]free.fr> 4.67-1
- version 4.67

* Sun May 08 2005 Aurelien Bompard <gauret[AT]free.fr> 4.62-1%{?dist}
- version 4.62
- use disttag

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Aug 11 2004 Aurelien Bompard <gauret[AT]free.fr> 0:4.52-0.fdr.1
- update to 4.52

* Sat Jul 31 2004 Aurelien Bompard <gauret[AT]free.fr> 0:4.51-0.fdr.1
- update to 4.51

* Sat Jul 03 2004 Aurelien Bompard <gauret[AT]free.fr> 0:4.23-0.fdr.2
- move to _datadir instead of _libdir
- use the _var macro

* Wed Jun 30 2004 Aurelien Bompard <gauret[AT]free.fr> 0:4.23-0.fdr.1
- Initial Fedora package (from Mandrake)

