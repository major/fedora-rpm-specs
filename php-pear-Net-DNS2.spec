# fedora/remirepo spec file for php-pear-Net-DNS2
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_with     tests

%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name Net_DNS2

Name:           php-pear-Net-DNS2
Version:        1.5.0
Release:        7%{?dist}
Summary:        PHP Resolver library used to communicate with a DNS server

License:        BSD
URL:            http://pear.php.net/package/Net_DNS2
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)
%if %{with tests}
%global phpunit %{_bindir}/phpunit
BuildRequires:  %{phpunit}
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)

# From phpcompatinfo report for version 1.5.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-shmop
Requires:       php-sockets
Requires:       php-spl
# Optional
Requires:       php-filter
Requires:       php-hash
Requires:       php-openssl

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_dns2) = %{version}


%description
Net_DNS2 - Native PHP5 DNS Resolver and Updater

The main features for this package include:
* Increased performance; most requests are 2-10x faster than Net_DNS
* Near drop-in replacement for Net_DNS
* Uses PHP5 style classes and exceptions
* Support for IPv4 and IPv6, TCP and UDP sockets.
* Includes a separate, more intuitive Updater class for handling dynamic update
* Support zone signing using TSIG and SIG(0) for updates and zone transfers
* Includes a local cache using shared memory or flat file to improve performance
* includes many more RR's, including DNSSEC RR's.


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%if %{with tests}
%check
cd %{pear_name}-%{version}/tests
if ! ping -c 1 google.com &>/dev/null
then
  : Internet needed for tests
  exit 0
fi

ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{phpunit} \
      --include-path=%{buildroot}/%{pear_phpdir}:%{_datadir}/php \
      --verbose Tests_Net_DNS2_AllTests.php || ret=1
  fi
done
exit $ret
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
%dir %{pear_phpdir}/Net
%{pear_phpdir}/Net/DNS2
%{pear_phpdir}/Net/DNS2.php
%{pear_testdir}/%{pear_name}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct  9 2020 Remi Collet <remi@remirepo.net> - 1.5.0-1
- Update to 1.5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.4.4-1
- Update to 1.4.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar  7 2017 Remi Collet <remi@remirepo.net> - 1.4.3-1
- Update to 1.4.3
- only run test suite when connected to internet

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-2
- use upstream patch for PHP 7

* Mon Nov 28 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 (stable)
- add patch for PHP 7
  open https://github.com/mikepultz/netdns2/pull/56

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1 (stable)

* Mon Dec 15 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (stable)
- provide php-composer(pear/net_dns2)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2 (stable)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
- hack for https://pear.php.net/bugs/19977 (bad role)

* Mon Apr 08 2013 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- hack for https://pear.php.net/bugs/19886 (shortag)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Remi Collet <remi@fedoraproject.org> - 1.2.5-1
- Version 1.2.5 (stable)

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 1.2.4-2
- php-mhash is optionnal and not available on RHEL-6

* Thu Sep 20 2012 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- Version 1.2.4 (stable)

* Sat Aug 18 2012 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- Version 1.2.3 (stable), API 1.2.3 (stable)
- upstream now provides LICENSE and tests
- run all tests if network available, else only parser

* Wed Aug 15 2012 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- rebuilt for new pear_testdir
- use php-pear(PEAR) in BR/R

* Sun Aug 12 2012 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Version 1.2.2 (stable), API 1.2.2 (stable)
- Initial package

