# remirepo/fedora spec file for php-composer-xdebug-handler
#
# Copyright (c) 2018-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    f27e06cd9675801df441b3656569b328e04aa37c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   xdebug-handler

%global ns_vendor    Composer
%global ns_project   XdebugHandler

%global php_home     %{_datadir}/php
%bcond_without       tests

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.4.6
Release:        10%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Restarts a process without Xdebug

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5",
#        "phpstan/phpstan": "^0.12.55"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%else
BuildRequires:  php-PsrLog
BuildRequires:  php-phpunit-PHPUnit >= 4.8.35
%global phpunit %{_bindir}/phpunit
%endif
%endif
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0 || ^8.0",
#        "psr/log": "^1.0"
Requires:       php(language) >= 5.3.2
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
%else
Requires:       php-PsrLog
%endif
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Restart a CLI process without loading the xdebug extension.

Originally written as part of composer/composer, now extracted
and made available as a stand-alone library.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Log/autoload.php',
));
EOF


%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', dirname(__DIR__).'/tests');
EOF

%if %{with tests}
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} --verbose|| ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Remi Collet <remi@remirepo.net> - 1.4.6-1
- update to 1.4.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Remi Collet <remi@remirepo.net> - 1.4.5-1
- update to 1.4.5

* Sun Oct 25 2020 Remi Collet <remi@remirepo.net> - 1.4.4-1
- update to 1.4.4

* Wed Aug 19 2020 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2

* Mon Mar  2 2020 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- switch to phpunit8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Thu Nov 29 2018 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Sun Sep  2 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Thu Aug 23 2018 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.1.0-2
- fix dependency on PHPUnit

* Thu Apr 12 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Mon Mar 26 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
