# spec file for php-pear-Net-URL2
#
# Copyright (c) 2009-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name   Net_URL2
%global with_tests  0%{?_with_tests:1}

Name:           php-pear-Net-URL2
Version:        2.2.1
Release:        13%{?dist}
Summary:        Class for parsing and handling URL

License:        BSD
URL:            http://pear.php.net/package/Net_URL2
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
%if %{with_tests}
BuildRequires:  php-phpunit-PHPUnit
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
# From phpcompatinfo report for 2.1.1
Requires:       php-pcre

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_url2) = %{version}


%description
Provides parsing of URLs into their constituent parts (scheme, host, path
etc.), URL generation, and resolving of relative URLs.


%prep
%setup -q -c

cd %{pear_name}-%{version}
# Package is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
%if %{with_tests}
# test suite cannot run in mock (use network)
# Version 2.2.0 : OK (113 tests, 270 assertions)
cd %{buildroot}%{pear_testdir}/%{pear_name}/tests
phpunit \
   --include-path=%{buildroot}%{pear_phpdir} \
   AllTests.php
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
%{pear_phpdir}/Net
%{pear_testdir}/%{pear_name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (no change)

* Sun Dec 28 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Mon Oct 27 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (no change, for semver)

* Sat Oct 18 2014 Remi Collet <remi@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11

* Fri Oct 10 2014 Remi Collet <remi@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10 (stable) - no change
- provide php-composer(pear/net_url2)

* Thu Oct  9 2014 Remi Collet <remi@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9 (stable)

* Wed Oct  8 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8 (stable)

* Mon Sep  8 2014 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7 (stable)

* Mon Jun 23 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6 (stable)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  2 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5 (stable)

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (stable)

* Mon Dec 30 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 (stable)

* Sat Dec 28 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (stable)

* Wed Dec 25 2013 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (stable)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-6
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-4
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Version 2.0.0 (stable) - API 2.0.0 (stable)
- add tests option to run tests during rpmbuild

* Mon Apr 18 2011 Remi Collet <Fedora@FamilleCollet.com> 0.3.1-4
- doc in /usr/share/doc/pear
- set date.timezone during build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 22 2010 Remi Collet <Fedora@FamilleCollet.com> 0.3.1-2
- spec cleanup

* Sun Jan 24 2010 Remi Collet <Fedora@FamilleCollet.com> 0.3.1-1
- update to 0.3.1

* Wed Nov 11 2009 Remi Collet <Fedora@FamilleCollet.com> 0.3.0-1
- initial RPM

