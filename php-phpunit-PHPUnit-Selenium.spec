# remirepo/fedora spec file for php-phpunit-PHPUnit-Selenium
#
# Copyright (c) 2010-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    343ba4e389ad97046c78fb2c7111e199795e7a80
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     giorgiosironi
%global gh_project   phpunit-selenium
%global php_home     %{_datadir}/php
%global pear_name    PHPUnit_Selenium
%global pear_channel pear.phpunit.de
# No test, as test suite requires a Selenium server

Name:           php-phpunit-PHPUnit-Selenium
Version:        3.0.3
Release:        15%{?dist}
Summary:        Selenium RC integration for PHPUnit

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
#        "php": ">=5.6",
#        "phpunit/phpunit": "~5.0",
#        "sebastian/comparator": "~1.0",
#        "ext-curl": "*",
#        "ext-dom": "*"
Requires:       php(language) >= 5.6
%if 0%{?fedora} >= 27
Requires:       (php-composer(phpunit/phpunit)      >= 5   with php-composer(phpunit/phpunit)      <  6)
Requires:       (php-composer(sebastian/comparator) >= 1.0 with php-composer(sebastian/comparator) <  2)
%else
Requires:       php-phpunit-PHPUnit >= 5
Requires:       php-phpunit-comparator
%endif
Requires:       php-curl
Requires:       php-dom
# From phpcompatinfo report for version 1.3.3
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-zip
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/phpunit-selenium) = %{version}

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
Selenium RC integration for PHPUnit.

This package contains a base Testcase Class that can be used to run end-to-end
tests against Selenium 2 (using its Selenium 1 backward compatible Api).

Optional dependency: XDebug (php-pecl-xdebug)


%prep
%setup -q -n %{gh_project}-%{gh_commit}

rm PHPUnit/Extensions/SeleniumCommon/Autoload.php.in


%build
# Regenerate Autoloader as upstream one is outdated
%{_bindir}/phpab \
  --template fedora \
  --output   PHPUnit/Extensions/SeleniumCommon/Autoload.php \
  PHPUnit

cat << 'EOF' >>PHPUnit/Extensions/SeleniumCommon/Autoload.php
// Dependency
require_once 'File/Iterator/Autoload.php';
EOF


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr PHPUnit %{buildroot}%{php_home}/PHPUnit


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog.markdown README.md
%doc composer.json
%{php_home}/PHPUnit/Extensions/Selenium*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@fedoraproject.org> - 3.0.3-4
- use range dependencies on F27+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3
- switch to fedora/autoloader

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHPUnit >= 5
- raise dependency on PHP >= 5.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHPUnit >=4.8,<=6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov  2 2014 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2
- fix license handling

* Tue Aug 19 2014 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- add dependency on sebastian/comparator

* Mon Aug  4 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-2
- sources from github

* Fri Nov 22 2013 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3 (stable)
- improve description

* Mon Aug 26 2013 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Mon May 06 2013 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Version 1.3.0 (stable) - API 1.3.0 (stable)

* Mon Feb 04 2013 Remi Collet <remi@fedoraproject.org> - 1.2.12-1
- Version 1.2.12 (stable) - API 1.2.1 (stable)

* Mon Dec 10 2012 Remi Collet <remi@fedoraproject.org> - 1.2.11-1
- Version 1.2.11 (stable) - API 1.2.1 (stable)

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.10-1
- Version 1.2.10 (stable) - API 1.2.1 (stable)
- raise dependencies: php 5.3.3, PHPUnit 3.7.0

* Thu Aug  9 2012 Remi Collet <remi@fedoraproject.org> - 1.2.8-1
- Version 1.2.8 (stable) - API 1.2.1 (stable)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Remi Collet <remi@fedoraproject.org> - 1.2.7-1
- Version 1.2.7 (stable) - API 1.2.1 (stable)

* Sun Apr 01 2012 Remi Collet <remi@fedoraproject.org> - 1.2.6-1
- Version 1.2.6 (stable) - API 1.2.1 (stable)

* Sat Mar 17 2012 Remi Collet <remi@fedoraproject.org> - 1.2.5-1
- Version 1.2.5 (stable) - API 1.2.1 (stable)

* Mon Mar 12 2012 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- Version 1.2.4 (stable) - API 1.2.1 (stable)

* Fri Feb 17 2012 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- Version 1.2.3 (stable) - API 1.2.1 (stable)

* Mon Jan 23 2012 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Version 1.2.1 (stable) - API 1.2.1 (stable)
- add Selenium2TestCase extension

* Mon Jan 16 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 (stable) - API 1.2.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Version 1.1.3 (stable) - API 1.1.0 (stable)

* Mon Dec 12 2011 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Version 1.1.2 (stable) - API 1.1.0 (stable)

* Wed Nov 30 2011 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Version 1.1.1 (stable) - API 1.1.0 (stable)

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.3-1
- Version 1.0.3 (stable) - API 1.0.0 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.2-3
- rebuild for doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.2-1
- Version 1.0.2 (stable) - API 1.0.0 (stable)
- CHANGELOG and LICENSE are now in the tarball

* Wed Nov 17 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.1-1
- Version 1.0.1 (stable) - API 1.0.0 (stable)

* Fri Nov 05 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-2
- lower PEAR dependency to allow el6 build
- fix URL

* Sun Sep 26 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1
- initial generated spec + clean

