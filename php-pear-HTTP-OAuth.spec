# remirepo/fedora spec file for php-pear-HTTP-OAuth
#
# Copyright (c) 2009-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name HTTP_OAuth

Name:           php-pear-HTTP-OAuth
Version:        0.3.2
Release:        14%{?dist}
Summary:        Implementation of the OAuth spec

License:        BSD
URL:            http://pear.php.net/package/HTTP_OAuth
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  php-pear
# For test suite
BuildRequires:  php-pear(pear.phpunit.de/PHPUnit)
BuildRequires:  php-pear(Cache_Lite)
BuildRequires:  php-pear(HTTP_Request2) >= 0.5.1
BuildRequires:  php-pear(Log)

Requires(post): %{__pear}
Requires(postun): %{__pear}
# Mandatory, from package.xml
Requires:       php-date
Requires:       php-hash
Requires:       php-spl
Requires:       php-pear(HTTP_Request2) >= 0.5.1
Requires:       php-pear(PEAR)
# Optional, from package.xml
Requires:       php-pear(Log)
Requires:       php-pear(Cache_Lite)
# not yet available in Fedora Requires: php-pecl(pecl_http) >= 1.6.0

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/http_oauth) = %{version}


%description
Allows the use of the consumer and provider angles of the OAuth spec.


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# fix rpmlint warnings
sed -i -e 's/\r//' %{buildroot}%{pear_docdir}/%{pear_name}/examples/jquery.fade.js

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}



%check
cd %{pear_name}-%{version}/tests
# for 0.3.2 : OK (71 tests, 151 assertions)
%{_bindir}/phpunit \
    --include-path=%{buildroot}%{pear_phpdir} \
    AllTests.php

if which php70; then
  php70 %{_bindir}/phpunit \
    --include-path=%{buildroot}%{pear_phpdir} \
    AllTests.php
fi


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/HTTP/OAuth.php
%{pear_phpdir}/HTTP/OAuth
%{pear_testdir}/%{pear_name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 0.3.2-1
- update to 0.3.2 (alpha)
- add provide php-composer(pear/http_oauth)
- run test suite with both PHP 5 and 7 when available

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov  5 2013 Remi Collet <remi@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1 (alpha)
- License file is provided in tarball
- Drop patch merged upstream

* Sat Nov  2 2013 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- update to 0.3.0 (alpha)
- add explicit spec License
- open issues for missing License file and failed test

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 0.2.3-6
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.2.3-4
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Remi Collet <remi@fedoraproject.org> 0.2.3-1
- Version 0.2.3 (alpha) - API 0.2.0 (alpha)

* Sat Apr 16 2011 Remi Collet <Fedora@FamilleCollet.com> 0.2.2-3
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Remi Collet <Fedora@FamilleCollet.com> 0.2.2-1
- Version 0.2.2 (alpha) - API 0.2.0 (alpha)

* Wed Dec 29 2010 Remi Collet <Fedora@FamilleCollet.com> 0.2.1-1
- Version 0.2.1 (alpha) - API 0.2.0 (alpha)
- set timezone during build
- run phpunit in %%check

* Thu Jul 22 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.18-1
- Version 0.1.18 (alpha) - API 0.1.1 (alpha)

* Thu Jul 01 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.17-1
- Version 0.1.17 (alpha) - API 0.1.1 (alpha)

* Fri Jun 25 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.16-1
- Version 0.1.16 (alpha) - API 0.1.1 (alpha)

* Thu Jun 24 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.15-1
- Version 0.1.15 (alpha) - API 0.1.1 (alpha)

* Thu May 27 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.14-1
- Version 0.1.14 (alpha) - API 0.1.1 (alpha)

* Thu Apr 29 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.10-1
- new version 0.1.10 (alpha) - API 0.1.1 (alpha)
- add generated CHANGELOG
- add doc on howto run tests

* Sun Feb 21 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.9-1
- new version
- raise HTTP_Request2 to 0.5.1

* Thu Feb 18 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.8-1
- new version

* Fri Jan 29 2010 Remi Collet <Fedora@FamilleCollet.com> 0.1.7-1
- new version

* Tue Dec 01 2009 Remi Collet <Fedora@FamilleCollet.com> 0.1.6-1
- new version

* Fri Nov 20 2009 Remi Collet <Fedora@FamilleCollet.com> 0.1.5-1
- new version

* Wed Nov 11 2009 Remi Collet <Fedora@FamilleCollet.com> 0.1.4-1
- initial RPM

