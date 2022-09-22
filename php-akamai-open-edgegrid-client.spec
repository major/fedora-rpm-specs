#
# Fedora spec file for php-akamai-open-edgegrid-client
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     akamai
%global github_name      AkamaiOPEN-edgegrid-php-client
%global github_version   1.0.0
%global github_commit    a368473f0f73fab96ffee03ee40d2f18694ff526

%global composer_vendor  akamai-open
%global composer_project edgegrid-client

# "php": ">=5.5"
%global php_min_ver 5.5
# "akamai-open/edgegrid-auth": "^1.0.0"
%global akamai_open_edgegrid_auth_min_ver 1.0
%global akamai_open_edgegrid_auth_max_ver 2.0
# "guzzlehttp/guzzle": "^6.1.1"
%global guzzle_min_ver 6.1.1
%global guzzle_max_ver 7.0
# "monolog/monolog": "^1.15"
%global monolog_min_ver 1.15
%global monolog_max_ver 2.0
# "psr/log": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       Implements the Akamai {OPEN} EdgeGrid Authentication

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Library version value and autoloader check
BuildRequires: php-cli
## composer.json
BuildRequires: php-composer(akamai-open/edgegrid-auth) <  %{akamai_open_edgegrid_auth_max_ver}
BuildRequires: php-composer(akamai-open/edgegrid-auth) >= %{akamai_open_edgegrid_auth_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(monolog/monolog) <  %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.0.0beta1)
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(akamai-open/edgegrid-auth) <  %{akamai_open_edgegrid_auth_max_ver}
Requires:      php-composer(akamai-open/edgegrid-auth) >= %{akamai_open_edgegrid_auth_min_ver}
Requires:      php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:      php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
# phpcompatinfo (computed from version 1.0.0beta1)
Requires:      php-json
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Akamai {OPEN} EdgeGrid Authentication [1] Client for PHP

This library implements the Akamai {OPEN} EdgeGrid Authentication scheme on top
of Guzzle [2], as both a drop-in replacement client, and middleware.

For more information visit the Akamai {OPEN} Developer Community [3].

Autoloader: %{phpdir}/Akamai/Open/EdgeGrid/autoload-client.php

[1] https://developer.akamai.com/introduction/Client_Auth.html
[2] https://github.com/guzzle/guzzle
[3] https://developer.akamai.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove CLI
rm -f src/Cli.php


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-client.php src/

cat <<'AUTOLOAD' | tee -a src/autoload-client.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php',
    '%{phpdir}/GuzzleHttp6/autoload.php',
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Akamai/Open
cp -rp src %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid


%check
: Library version value and autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/autoload-client.php";
    $version = \Akamai\Open\EdgeGrid\Client::VERSION;
    echo "Version $version (expected %{version}%{?github_prerelease})\n";
    exit(version_compare("%{version}%{?github_prerelease}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/autoload-client.php';
\Fedora\Autoloader\Autoload::addPsr4('Akamai\\Open\\EdgeGrid\\Tests\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
       $PHP_EXEC $PHPUNIT --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Akamai/Open/EdgeGrid/autoload-client.php
%{phpdir}/Akamai/Open/EdgeGrid/Client.php
%{phpdir}/Akamai/Open/EdgeGrid/Exception
%{phpdir}/Akamai/Open/EdgeGrid/Exception.php
%{phpdir}/Akamai/Open/EdgeGrid/Handler


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Update to 1.0.0 (RHBZ #1487625)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-0.1.beta1
- Update to 1.0.0beta1 (RHBZ #1408816)
- Added max versions to BuildRequires dependencies
- Removed compat autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.3-1
- Update to 0.6.3 (RHBZ #1408612)

* Sat Dec 24 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.2-2
- Minor spec-only modifications

* Thu Dec 22 2016 Remi Collet <remim@remirepo.net> - 0.6.2-1
- Update to 0.6.2 (RHBZ #1405781)
- Use php-composer(fedora/autoloader)

* Wed Dec 07 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.1-1
- Updated to 0.6.1 (RHBZ #1392697)

* Wed Nov 02 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.0-1
- Updated to 0.6.0 (RHBZ #1382986)
- Autoloader changed from Symfony ClassLoader to phpab classmap

* Sun Sep 25 2016 Shawn Iwinski <shawn@iwin.ski> - 0.5.0-1
- Updated to 0.5.0 (RHBZ #1376273)

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Updated to 0.4.6 (RHBZ #1371149)

* Sat Jul 23 2016 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-1
- Updated to 0.4.5 (RHBZ #1333785)
- Added library version value and autoloader check

* Tue Apr 12 2016 Shawn Iwinski <shawn@iwin.ski> - 0.4.4-1
- Initial package
