# remirepo/fedora spec file for php-phpspec-prophecy-phpunit
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    2d7a9df55f257d2cba9b1d0c0963a54960657177
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   prophecy-phpunit

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.0.1
Release:        6%{?dist}
Summary:        Integrating the Prophecy mocking library in PHPUnit test cases

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
%if %{with tests}
BuildRequires: (php-composer(phpspec/prophecy) >= 1.3   with php-composer(phpspec/prophecy) < 2)
BuildRequires:  phpunit9 >= 9.1
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# from composer.json, "requires": {
#        "php": "^7.3 || ^8",
#        "phpspec/prophecy": "^1.3",
#        "phpunit/phpunit":"^9.1"
Requires:       php(language) >= 7.3
Requires:      (php-composer(phpspec/prophecy) >= 1.3   with php-composer(phpspec/prophecy) < 2)
Requires:       phpunit9 >= 9.1
# From phpcompatinfo report for version 2.0.1
#none
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Prophecy PhpUnit integrates the Prophecy mocking library with PHPUnit
to provide an easier mocking in your testsuite.

Autoloader: %{_datadir}/php/Prophecy/PhpUnit/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Prophecy/autoload.php',
]);
EOF


%install
mkdir -p     %{buildroot}%{_datadir}/php/Prophecy/PhpUnit
cp -pr src/* %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/


%check
%if %{with tests}
: Dev autoloader
mkdir vendor
phpab --output vendor/autoload.php fixtures tests

cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php';
EOF

: check autoloader
php %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php


: upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/Prophecy/PhpUnit


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- initial package
