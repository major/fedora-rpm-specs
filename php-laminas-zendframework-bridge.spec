# remirepo/Fedora spec file for php-laminas-zendframework-bridge
#
# Copyright (c) 2020-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5ef52e26392777a26dbb8f20fe24f91b406459f6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-zendframework-bridge
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ZendFrameworkBridge
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Alias legacy ZF class names to Laminas Project equivalents

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Adapt for Fedora autoloader and RPM layout
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "squizlabs/php_codesniffer": "^3.7.1",
#        "vimeo/psalm": "^4.29.0"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.26
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.1
%endif

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0"
Requires:       php(language) >= 8.0
# From phpcompatinfo report for version 1.0.0
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader) >= 1.0.1

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
# no replacement (for now)
Obsoletes:      php-zendframework                                  < 3.0.1
Obsoletes:      php-zendframework-zend-debug                       < 3
Obsoletes:      php-zendframework-zend-expressive                  < 2
Obsoletes:      php-zendframework-zend-expressive-aurarouter       < 3
Obsoletes:      php-zendframework-zend-expressive-fastroute        < 3
Obsoletes:      php-zendframework-zend-expressive-helpers          < 4
Obsoletes:      php-zendframework-zend-expressive-platesrenderer   < 2
Obsoletes:      php-zendframework-zend-expressive-router           < 3
Obsoletes:      php-zendframework-zend-expressive-template         < 2
Obsoletes:      php-zendframework-zend-expressive-twigrenderer     < 2
Obsoletes:      php-zendframework-zend-expressive-zendrouter       < 3
Obsoletes:      php-zendframework-zend-expressive-zendviewrenderer < 2


%description
This library provides a custom autoloader that aliases legacy
Zend Framework, Apigility, and Expressive classes to their
replacements under the Laminas Project.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p0 -b .rpm
find . -name \*.rpm -delete

mv LICENSE.md LICENSE


%build
mv src/autoload.php upstream.php
phpab --template fedora --output src/autoload.php src
grep -v '^<?php' upstream.php | tee -a src/autoload.php

: Full Laminas autoloader
cat << 'EOF' | tee lf.php
<?php
// load all %{namespace}, without Zend compat layer
foreach(glob('/usr/share/php/%{namespace}/*/autoload.php') as $f) {
	if (strpos($f, 'ZendFrameworkBridge')) {
		continue;
	}
	require_once $f;
}
foreach(glob('/usr/share/php/%{namespace}/*/*/autoload.php') as $f) {
	if (strpos($f, 'Session/compatibility')) {
		continue;
	}
	require_once $f;
}
EOF

: Full Zend autoloader
cat << 'EOF' | tee zf.php
<?php
// load all Zend with %{namespace} compat layer
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__) . '/%{namespace}/%{library}/autoload.php',
    dirname(__DIR__) . '/%{namespace}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p      %{buildroot}%{php_home}/%{namespace}/
cp -pr src    %{buildroot}%{php_home}/%{namespace}/%{library}
cp -pr config %{buildroot}%{php_home}/%{namespace}/%{library}/config
cp lf.php     %{buildroot}%{php_home}/%{namespace}/autoload.php

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/
cp zf.php     %{buildroot}%{php_home}/Zend/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\TestAsset\\', dirname(__DIR__) . '/test/TestAsset/classes');
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}\\ApiTools\\', dirname(__DIR__) . '/test/TestAsset/LaminasApiTools');
\Fedora\Autoloader\Autoload::addPsr4('Mezzio\\', dirname(__DIR__) . '/test/TestAsset/Mezzio');
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}\\', dirname(__DIR__) . '/test/TestAsset/Laminas');
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__) . '/test/classes.php',
]);
EOF

: check Zend autoloader
php %{buildroot}%{php_home}/Zend/autoload.php

: check Laminas autoloader
php %{buildroot}%{php_home}/%{namespace}/autoload.php

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
%dir %{php_home}/Zend
     %{php_home}/Zend/autoload.php
%dir %{php_home}/%{namespace}
     %{php_home}/%{namespace}/%{library}
     %{php_home}/%{namespace}/autoload.php


%changelog
* Wed Dec 14 2022 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0 (no change)
- raise dependency on PHP 8.0

* Mon Aug  1 2022 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Wed Feb 23 2022 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 7.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1 (no change)

* Wed Sep  8 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0 (no change)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Thu Jun 24 2021 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1 (no change)

* Fri Feb 26 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0 (no change)
- raise dependency on PHP 7.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 (no change)
- switch to phpunit9

* Wed Aug 19 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Sat Apr  4 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Thu Feb 13 2020 Remi Collet <remi@remirepo.net> - 1.0.1-5
- raise dependency on fedora/autoloader 1.0.1
- clean autoloader

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.0.1-3
- add full framework autoloader

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 1.0.1-2
- obsolete dropped packages

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
