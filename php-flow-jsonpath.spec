#
# Fedora spec file for php-flow-jsonpath
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     FlowCommunications
%global github_name      JSONPath
%global github_version   0.3.4
%global github_commit    00aa9c361e4d0a210dd95f3c917a1e0dde3a957f

%global composer_vendor  flow
%global composer_project jsonpath

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       JSONPath implementation for parsing, searching and flattening arrays

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Add LICENSE file
# https://github.com/FlowCommunications/JSONPath/pull/20
Patch0:        %{name}-add-license-file.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.3.4)
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.3.4)
Requires:      php-json
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This is a JSONPath [1] implementation for PHP based on Stefan Goessner's
JSONPath script.

JSONPath is an XPath-like expression language for filtering, flattening and
extracting data.

I believe that is improves on the original script (which was last updated in
2007) by doing a few things:
* Object-oriented code (should be easier to manage or extend in future)
* Expressions are parsed into tokens using some code cribbed from Doctrine
  Lexer and cached
* There is no eval() in use
* Performance is pretty much the same
* Any combination of objects/arrays/ArrayAccess-objects can be used as the data
  input which is great if you're de-serializing JSON in to objects or if you
  want to process your own data structures.

Autoloader: %{phpdir}/Flow/JSONPath/autoload.php

[1] http://goessner.net/articles/JsonPath/


%prep
%setup -qn %{github_name}-%{github_commit}

: Add LICENSE file
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Flow/JSONPath/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Flow\\JSONPath\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Flow
cp -rp src/Flow/JSONPath %{buildroot}%{phpdir}/Flow/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Flow/JSONPath/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Flow\\JSONPath\\Test\\', __DIR__.'/tests/Flow/JSONPath/Test');
BOOTSTRAP

: Mock Composer autoloader
mkdir vendor
ln -s %{buildroot}%{phpdir}/Flow/JSONPath/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
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
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Flow
     %{phpdir}/Flow/JSONPath


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 0.3.4-1
- Initial package
