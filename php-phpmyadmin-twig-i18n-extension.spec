# remirepo/fedora spec file for php-phpmyadmin-twig-i18n-extension
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    1f509fa3c3f66551e1f4a346e4477c6c0dc76f9e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
#global gh_date      20150820
%global gh_project   twig-i18n-extension
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    PhpMyAdmin
%global ns_project   Twig
%global ns_sub       Extensions
%global major        %nil

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        3.0.0
Release:        7%{?dist}
Summary:        Internationalization support for Twig via the gettext library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires: (php-composer(twig/twig) >= 2 with php-composer(twig/twig) < 4)
# For tests, from composer.json "require-dev": {
#        "phpmyadmin/coding-standard": "^2.0",
#        "phpunit/phpunit": "^7 || ^8 || ^9"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%endif
%endif
# For autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.1",
#        "twig/twig": "^2.0|^3.0"
Requires:       php(language) >= 7.1
Requires:      (php-composer(twig/twig) >= 2 with php-composer(twig/twig) < 4)
# From phpcompatinfo report for 3.0.0
# Only Core and standard
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
The i18n extension adds gettext support to Twig.
It defines one tag, trans.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
phpab --template fedora -o src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    [
        '%{_datadir}/php/Twig3/autoload.php',
        '%{_datadir}/php/Twig2/autoload.php',
    ],
));
AUTOLOAD


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\Tests\\%{ns_project}\\%{ns_sub}\\', dirname(__DIR__).'/tests');
EOF

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit9} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.rst
%dir %{_datadir}/php/%{ns_vendor}
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct  9 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.1
- raise dependency on twig v2 and allow v3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- initial package
