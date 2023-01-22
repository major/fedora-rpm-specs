# remirepo/fedora spec file for php-pear-HTTP-Request2
#
# Copyright (c) 2009-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_with tests

%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name   HTTP_Request2

Name:           php-pear-HTTP-Request2
Version:        2.5.1
Release:        4%{?dist}
Summary:        Provides an easy way to perform HTTP requests

License:        BSD
URL:            http://pear.php.net/package/HTTP_Request2
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  php(language) >= 5.6
BuildRequires:  php-pear(PEAR) >= 1.9.2
# For test suite
%if %{with tests}
BuildRequires:  phpunit9
BuildRequires:  php-pear(Net_URL2) >= 2.2.0
BuildRequires:  php-yoast-phpunit-polyfills
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.6
# From package.xml
Requires:       php-pear(Net_URL2) >= 2.2.0
Requires:       php-pear(PEAR) >= 1.9.2
# From package.xml, optional
Requires:       php-curl
Requires:       php-fileinfo
Requires:       php-openssl
Requires:       php-zlib
# From phpcompatinfo report for version 2.2.0
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/http_request2) = %{version}


%description
PHP5 rewrite of HTTP_Request package. Provides cleaner API and pluggable
Adapters. Currently available are:
  * Socket adapter, based on old HTTP_Request code,
  * Curl adapter, wraps around PHP's cURL extension,
  * Mock adapter, to use for testing packages dependent on HTTP_Request2.
Supports POST requests with data and file uploads, basic and digest 
authentication, cookies, proxies, gzip and deflate encodings, monitoring 
the request progress with Observers...


%prep
%setup -q -c

cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}

cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# for rpmlint
sed -i -e 's/\r//' %{buildroot}%{pear_docdir}/%{pear_name}/examples/upload-rapidshare.php

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
%if %{with tests}
cd %{pear_name}-%{version}/tests
# Tests: 178, Assertions: 180, Skipped: 76.

sed -e "s:'HTTP/Request2.php':'HTTP/Request2.php'; require_once 'Yoast/PHPUnitPolyfills/autoload.php':" \
    -i TestHelper.php

phpunit9 --do-not-cache-result --verbose .
%else
echo 'Test suite disabled (missing "--with tests" option)'
%endif



%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/HTTP
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan  7 2022 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1 (stable)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0 (stable)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2 (stable)

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1 (stable)
- raise dependency on PHP 5.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0 (stable)
- raise dependency on Net_URL2 >= 2.2.0
- provide php-composer(pear/http_request2)
- drop generated Changelog

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1 (stable)

* Mon Jan 13 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0 (stable)
- https://pear.php.net/bugs/20176 - corrupted archive
- https://pear.php.net/bugs/20175 - license

* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-8
- xml2change need simplexml

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Remi Collet <remi@fedoraproject.org> - 2.1.1-5
- add requires on all extensions

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 2.1.1-4
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 2.1.1-3
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Version 2.1.1 (stable) - API 2.1.0 (stable)
- requires PEAR 1.9.2
- (re)enable test during build

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Version 2.0.0 (stable) - API 2.0.0 (stable)
- add "tests" option

* Sun Apr 17 2011 Remi Collet <Fedora@FamilleCollet.com> 0.6.0-2
- doc in /usr/share/doc/pear

* Wed Feb 16 2011 Remi Collet <Fedora@FamilleCollet.com> 0.6.0-1
- Version 0.6.0 (alpha) - API 0.6.0 (alpha)
- set date.timezone during build
- run phpunit test suite during %%check

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 22 2010 Remi Collet <Fedora@FamilleCollet.com> 0.5.2-2
- spec cleanup

* Wed Apr 21 2010 Remi Collet <Fedora@FamilleCollet.com> 0.5.2-1
- new upstream version 0.5.2 (bugfix) - API 0.5.0
- add generated Changelog

* Sun Nov 22 2009 Remi Collet <Fedora@FamilleCollet.com> 0.5.1-1
- new version

* Fri Nov 20 2009 Remi Collet <Fedora@FamilleCollet.com> 0.5.0-1
- new version

* Wed Nov 11 2009 Remi Collet <Fedora@FamilleCollet.com> 0.4.1-1
- initial RPM
