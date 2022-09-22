#
# Fedora spec file for php-jakubledl-dissect
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     jakubledl
%global github_name      dissect
%global github_version   1.0.1
%global github_commit    d3a391de31e45a247e95cef6cf58a91c05af67c4

%global composer_vendor  jakubledl
%global composer_project dissect

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "symfony/console": "~2.1"
#     NOTE: Min version not 2.1 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       Lexing and parsing in pure PHP

License:       Unlicense
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Bin adjustment
Patch0:        %{name}-bin.patch
# Fix "PHP Fatal error:  Redefinition of parameter $_"
Patch1:        %{name}-fix-redefinition-of-parameter.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
## phpcompatinfo (computed from version 1.0.1)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-xml
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.1)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
Requires:      php-xml
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(symfony/console)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Dissect is a set of tools for lexical and syntactical analysis written in pure
PHP.

Autoloader: %{phpdir}/Dissect/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

%patch0 -p1
sed \
    -e 's#__VERSION__#%{version}#' \
    -e 's#__PHPDIR__#%{phpdir}#' \
    -i bin/dissect.php

%patch1 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Dissect/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Dissect\\', __DIR__);

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}/Symfony/Component/Console/autoload.php',
));
AUTOLOAD


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Dissect %{buildroot}%{phpdir}/

: Bin
mkdir %{buildroot}/%{_bindir}
install -pm 0755 bin/dissect.php %{buildroot}/%{_bindir}/dissect


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Dissect/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Dissect\\', __DIR__.'/tests/Dissect');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license UNLICENSE
%doc *.md
%doc composer.json
%doc docs
%{phpdir}/Dissect
%{_bindir}/dissect


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Initial package
