# remirepo/fedora spec file for php-mock-integration2
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    ec6a00a8129d50ed0f07907c91e3274ca4ade877
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2024-02-10
%global gh_owner     php-mock
%global gh_project   php-mock-integration
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock-integration%{major}
Version:        2.3.0
Release:        3%{?dist}
Summary:        Integration package for PHP-Mock

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# 7.4 because of phpunit9
BuildRequires:  php(language) >= 7.4
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7.27 || ^6 || ^7 || ^8 || ^9 || ^10 || ^11"
BuildRequires: (php-composer(php-mock/php-mock)         >= 2.5 with php-composer(php-mock/php-mock)         < 3)
BuildRequires: phpunit8
BuildRequires: phpunit9
BuildRequires: phpunit10
# TODO phpunit11 but requires php 8.2
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)

# from composer.json, "require": {
#        "php": ">=5.6",
#        "php-mock/php-mock": "^2.5",
#        "phpunit/php-text-template": "^1 || ^2|| ^3 || ^4"
Requires:       php(language) >= 5.6
Requires:      (php-composer(php-mock/php-mock)         >= 2.5 with php-composer(php-mock/php-mock)         < 3)
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 5)
# From phpcompatinfo report from version 2.0.0
# only core and standard

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
This is a support package for PHP-Mock integration into other frameworks.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Same namespace than php-mock, not specific autoloader needed


%build
# Nothing


%install
mkdir -p       %{buildroot}%{_datadir}/php/
mkdir -p       %{buildroot}%{_datadir}/php/phpmock%{major}
cp -pr classes %{buildroot}%{_datadir}/php/phpmock%{major}/integration


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', '%{buildroot}%{_datadir}/php/phpmock%{major}');
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\integration\\', dirname(__DIR__) . '/tests');
require_once '%{_datadir}/php/phpmock%{major}/autoload.php';
require_once dirname(__DIR__) . '/tests/autoload.php';
EOF

ret=0
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php80 php81 php82;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --verbose || ret=1
    fi
  done
fi

if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php80 php81 php82 php83;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
    fi
  done
fi

if [ -x %{_bindir}/phpunit10 ]; then
  for cmd in php php81 php82php83;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi

if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php php82 php83;do
    if which $cmd; then
      $cmd %{_bindir}/phpunit10 || ret=1
    fi
  done
fi
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock%{major}/integration


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0 (no change)
- raise dependency on php-mock 2.5
- allow phpunit11

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 13 2023 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1
- allow phpunit10

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- raise dependency on php-mock 2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.0.0-5
- use php-mock2 2.1 single autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 2.0.0-2
- use range dependencies on F27+

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.0.0-1
- rename to php-mock-integration2
- Update to 2.0.0
- raise dependency on PHP 5.6
- raise dependency on php-mock 2

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- switch to fedora/autoloader

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- Fix: license is WTFPL

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
