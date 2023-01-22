# remirepo/fedora spec file for php-phpunit-selenium
#
# Copyright (c) 2010-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    41711edd4dfcc5a0db2f8a22da6d2ddc908da741
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     giorgiosironi
%global gh_project   phpunit-selenium
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global php_home     %{_datadir}/php/PHPUnit9
# No test, as test suite requires a Selenium server

Name:           php-%{pk_project}
Version:        9.0.1
Release:        3%{?dist}
Summary:        Selenium RC integration for PHPUnit 9

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
#        "php": ">=7.3",
#        "ext-curl": "*"
#        "phpunit/phpunit": ">=9.0,<10.0",
Requires:       php(language) >= 7.3
Requires:       php-curl
Requires:       phpunit9
# From phpcompatinfo report for version 9.0.0
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-reflection
Requires:       php-spl
Requires:       php-zip
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This package contains a Selenium2TestCase class that can be used to run
end-to-end tests against Selenium 2.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

rm PHPUnit/Extensions/SeleniumCommon/Autoload.php*


%build
# Regenerate Autoloader as upstream one is outdated
%{_bindir}/phpab \
  --template fedora \
  --output   PHPUnit/Extensions/SeleniumCommon/autoload.php \
  PHPUnit


%install
mkdir -p         %{buildroot}%{php_home}
cp -pr PHPUnit/* %{buildroot}%{php_home}


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog.markdown README.md
%doc composer.json
%{php_home}/Extensions/Selenium*


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Remi Collet <remi@remirepo.net> - 9.0.1-1
- update to 9.0.1 (no change)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Remi Collet <remi@remirepo.net> - 9.0.0-1
- update to 9.0.0
- raise dependency on PHP 7.3
- switch from PHPUnit 8 to 9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Remi Collet <remi@remirepo.net> - 8.0.0-1
- update to 8.0.0
- raise dependency on PHP 7.2
- switch from PHPUnit 7 to 8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul  4 2019 Remi Collet <remi@remirepo.net> - 7.0.0-1
- update to 7.0.0
- raise dependency on PHP 7.1
- switch from PHPUnit 6 to 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep  6 2017 Remi Collet <remi@remirepo.net> - 4.1.0-2
- fix dir ownsership, from review #1485924

* Mon Aug 28 2017 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0

* Mon Aug 21 2017 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0 for phpunit6
- rename to php-phpunit-selenium
- raise dependency on PHP 7.0

* Tue Jan 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3
- switch to fedora/autoloader

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1

* Sun Feb 28 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHPUnit >= 5
- raise dependency on PHP >= 5.6

* Sun Feb 28 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- only support PHP 5

* Fri Jan 29 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- fix autoloader

* Mon Jan  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHPUnit >=4.8,<=6.0

* Sun Nov  2 2014 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2
- fix license handling

* Tue Aug 19 2014 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- add dependency on sebastian/comparator

* Mon Aug  4 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-2
- sources from github

* Fri Nov 22 2013 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3 (stable)
- improve description

* Mon Aug 26 2013 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Mon Jun 03 2013 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Mon May 06 2013 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Mon Feb 04 2013 Remi Collet <remi@fedoraproject.org> - 1.2.12-1
- Version 1.2.12 (stable) - API 1.2.1 (stable)

* Mon Dec 10 2012 Remi Collet <remi@fedoraproject.org> - 1.2.11-1
- Version 1.2.11 (stable) - API 1.2.1 (stable)

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.10-1
- Version 1.2.10 (stable) - API 1.2.1 (stable)

* Sat Sep 29 2012 Remi Collet <remi@fedoraproject.org> - 1.2.9-1
- Version 1.2.9 (stable) - API 1.2.1 (stable)
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

