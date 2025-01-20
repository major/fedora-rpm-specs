# remirepo/fedora spec file for php-pragmarx-google2fa5
#
# Copyright (c) 2018-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    17c969c82f427dd916afe4be50bafc6299aef1b4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     antonioribeiro
%global gh_project   google2fa
# Packagist
%global pk_vendor    pragmarx
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PragmaRX
%global ns_project   Google2FA
%global major        5

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.0.0
Release:        14%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Google Two-Factor Authentication for PHP Package

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  (php-composer(paragonie/constant_time_encoding) >= 1.0   with php-composer(paragonie/constant_time_encoding) < 3)
BuildRequires:  (php-composer(paragonie/random_compat) >= 2.0            with php-composer(paragonie/random_compat)          < 3)
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
# For tests, from composer.json "require-dev": {
#       "phpunit/phpunit": "~4|~5|~6"
BuildRequires:  phpunit7
%global phpunit %{_bindir}/phpunit7
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.4",
#        "paragonie/constant_time_encoding": "~1.0|~2.0",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "~1.2"
# Use 5.6 and avoid polyfill
Requires:       php(language) >= 5.6
# Only use constant_time_encoding v1 available in Fedora for autoloader path
Requires:       (php-composer(paragonie/constant_time_encoding) >= 1.0   with php-composer(paragonie/constant_time_encoding) < 3)
# Only use random_compat v2 available in Fedora for autoloader path
Requires:       (php-composer(paragonie/random_compat) >= 2.0            with php-composer(paragonie/random_compat)          < 3)
# From phpcompatinfo report for 5.0.0
Requires:       php-hash
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Google2FA is a PHP implementation of the Google Two-Factor Authentication
Module, supporting the HMAC-Based One-time Password (HOTP) algorithm
specified in RFC 4226 and the Time-based One-time Password (TOTP) algorithm
specified in RFC 6238.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php',
    '%{_datadir}/php/random_compat/autoload.php',
]);
AUTOLOAD


%build
: Nothing to build


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
EOF

ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
   if which $cmdarg; then
       set $cmdarg
       $1 ${2:-%{_bindir}/phpunit7} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE.md RELICENSED.md
%doc composer.json
%doc README.md changelog.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 5.0.0-5
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-pragmarx-google2fa5
- move to /usr/share/php/PragmaRX/Google2FA5
- drop dependency on bacon/bacon-qr-code

* Wed Aug 29 2018 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 3.0.1-2
- allow paragonie/constant_time_encoding v2

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1
- license have be changed to MIT

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 2.0.7-2
- add GPLv3+ to License field and ask upstream for clarification
  https://github.com/antonioribeiro/google2fa/issues/95

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 2.0.7-1
- initial package
