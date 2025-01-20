# remirepo/fedora spec file for php-myclabs-php-enum
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    e7be26966b7398204a234f8673fdad5ac6277802
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     myclabs
%global gh_project   php-enum

%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}

%global ns_vendor    MyCLabs
%global ns_project   Enum
%global php_home     %{_datadir}/php

%bcond_without       tests

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.8.5
Release:        2%{?dist}
Summary:        PHP Enum implementation

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snashop to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.5",
#        "squizlabs/php_codesniffer": "1.*"
#        "vimeo/psalm": "^4.6.2 || ^5.2"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.3 || ^8.0",
#        "ext-json": "*"
Requires:       php(language) >= 7.3
Requires:       php-json
# From phpcompatinfo report for version 1.6.1
Requires:       php-reflection
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
PHP Enum implementation inspired from SplEnum.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv stubs/Stringable.php src/

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
require_once __DIR__ . '/Stringable.php';
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee tests/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\Tests\\%{ns_project}\\', __DIR__ . '/../tests');
require __DIR__ . '/bootstrap.php';
EOF

ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap tests/autoload.php || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Remi Collet <remi@remirepo.net> - 1.8.5-1
- update to 1.8.5
- re-license spec file to CECILL-2.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug  4 2022 Remi Collet <remi@remirepo.net> - 1.8.4-1
- update to 1.8.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3

* Mon Jul  5 2021 Remi Collet <remi@remirepo.net> - 1.8.2-1
- update to 1.8.2

* Tue Jun 29 2021 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Tue Feb 16 2021 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 1.7.7-1
- update to 1.7.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 1.7.6-1
- update to 1.7.6

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 1.7.5-1
- update to 1.7.5

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 1.7.4-1
- update to 1.7.4
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May  6 2019 Remi Collet <remi@remirepo.net> - 1.7.1-1
- update to 1.7.1
- lower dependency on PHP 7.1

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- raise dependency on PHP 7.2

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 1.6.6-1
- update to 1.6.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Mon Oct 29 2018 Remi Collet <remi@remirepo.net> - 1.6.3-1
- update to 1.6.3

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> - 1.6.2-1
- update to 1.6.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1
- raise dependency on PHP 5.4
- add dependency on json extension

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Remi Collet <remi@remirepo.net> - 1.5.2-1
- Update to 1.5.2 (no change)
- use phpunit6 on F26+

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1.5.1-1
- initial package, version 1.5.1
- open https://github.com/myclabs/php-enum/pull/55 - perms
- open https://github.com/myclabs/php-enum/pull/56 - phpunit
