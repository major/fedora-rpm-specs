# remirepo/fedora spec file for php-brick-varexporter
#
# Copyright (c) 2020-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    2fd038f7c9d12d468130c6e1b3ce06e4160a7dbb
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     brick
%global gh_project   varexporter
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Brick
%global ns_project   VarExporter

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.4.0
Release:        3%{?dist}
Summary:        A powerful alternative to var_export

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.4
BuildRequires: (php-composer(nikic/php-parser) >= 4.0   with php-composer(nikic/php-parser) < 5)
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#    "phpunit/phpunit": "^8.5 || ^9.0",
#    "php-coveralls/php-coveralls": "^2.2",
#    "vimeo/psalm": "5.15.0"
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#    "php": "^7.4 || ^8.0",
#    "nikic/php-parser": "^4.0"
Requires:       php(language) >= 7.2
Requires:      (php-composer(nikic/php-parser) >= 4.0   with php-composer(nikic/php-parser) < 5)
# From phpcompatifo report for 0.3.2
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This library aims to provide a prettier, safer, and powerful alternative
to var_export(). The output is valid and standalone PHP code, that does
not depend on the brick/varexporter library.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '/usr/share/php/PhpParser4/autoload.php',
]);

EOF

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Brick\\VarExporter\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82 php83; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep  4 2023 Remi Collet <remi@remirepo.net> - 0.4.0-1
- update to 0.4.0
- raise dependency on PHP 7.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 25 2023 Remi Collet <remi@remirepo.net> - 0.3.8-1
- update to 0.3.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Remi Collet <remi@remirepo.net> - 0.3.7-1
- update to 0.3.7

* Thu Jun 16 2022 Remi Collet <remi@remirepo.net> - 0.3.6-1
- update to 0.3.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Remi Collet <remi@remirepo.net> - 0.3.5-3
- add upstream patch to fix test suite with PHP 8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Remi Collet <remi@remirepo.net> - 0.3.5-1
- update to 0.3.5

* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 0.3.4-1
- update to 0.3.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Remi Collet <remi@remirepo.net> - 0.3.3-1
- update to 0.3.3
- switch to phpunit9

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 0.3.2-1
- initial package
