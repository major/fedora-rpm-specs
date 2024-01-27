# spec file for php-phpdocumentor-reflection1
#
# Copyright (c) 2016 Remi Collet
#               2017 Remi Collet, Shawn Iwinski
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    fc40c3f604ac2287eb5c314174d5109b2c699372
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   Reflection
%global with_tests   0%{!?_without_tests:1}

%global with_php_parser 1

Name:           php-phpdocumentor-reflection1
Version:        1.0.7
Release:        20%{?dist}
Summary:        Reflection library to do Static Analysis for PHP Projects (Version 1)

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

%if %{with_php_parser}
# Temporary, bundled nikik/php-parser 0.9.4
%global php_parser_owner   nikic
%global php_parser_project PHP-Parser
%global php_parser_commit  1e5e280ae88a27effa2ae4aa2bd088494ed8594f
%global php_parser_version 0.9.4
Source1:        https://github.com/%{php_parser_owner}/%{php_parser_project}/archive/%{php_parser_commit}/%{php_parser_project}-%{php_parser_version}.tar.gz
Provides:       bundled(nikic/php-parser) = %{php_parser_version}
%endif

# Temporary, missing in old versions
Source2:        https://raw.githubusercontent.com/phpDocumentor/Reflection/develop/LICENSE

BuildArch:      noarch
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
# For tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-composer(psr/log) >= 1.0
BuildRequires:  php-composer(psr/log) <  2
%if ! %{with_php_parser}
BuildRequires:  php-composer(nikic/php-parser) >= 0.9.4
BuildRequires:  php-composer(nikic/php-parser) <  0.10
%endif
BuildRequires:  php-composer(phpdocumentor/reflection-docblock) >= 2.0
BuildRequires:  php-composer(phpdocumentor/reflection-docblock) <  3
# From composer.json, "require-dev": {
#        "behat/behat": "~2.4",
#        "phpunit/phpunit": "~4.0",
#        "mockery/mockery": "~0.8"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.0
BuildRequires:  php-composer(mockery/mockery) >= 0.8
BuildRequires:  php-composer(mockery/mockery) <  1
%endif

# From composer.json, require
#        "php": ">=5.3.3",
#        "psr/log": "~1.0",
#        "nikic/php-parser": "~0.9.4",
#        "phpdocumentor/reflection-docblock": "~2.0"
Requires:       php(language) >= 5.3.3
# For autoloader
Requires:       php-composer(psr/log) >= 1.0.1
Requires:       php-composer(psr/log) <  2
%if ! %{with_php_parser}
Requires:       php-composer(nikic/php-parser) >= 0.9.4
Requires:       php-composer(nikic/php-parser) <  0.10
%endif
Requires:       php-composer(phpdocumentor/reflection-docblock) >= 2.0
Requires:       php-composer(phpdocumentor/reflection-docblock) <  3
# From phpcompatinfo report for 1.0.7
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection) = %{version}

# Package rename (php-phpdocumentor-reflection => php-phpdocumentor-reflection1)
Obsoletes:      php-phpdocumentor-reflection < 1.0.7-5
Provides:       php-phpdocumentor-reflection = %{version}-%{release}
Conflicts:      php-symfony-property-info < 2.8.19-2


%description
Using this library it is possible to statically reflect one or more files
and create an object graph representing your application's structure,
including accompanying in-source documentation using DocBlocks.

The information that this library provides is similar to what the (built-in)
Reflection extension of PHP provides; there are however several advantages
to using this library:

* Due to its Static nature it does not execute procedural code in your
  reflected files where Dynamic Reflection does.
* Because the none of the code is interpreted by PHP (and executed)
  Static Reflection uses less memory.
* Can reflect complete files
* Can reflect a whole project by reflecting multiple files.
* Reflects the contents of a DocBlock instead of just mentioning there is one.
* Is capable of analyzing code written for any PHP version (starting at 5.2)
  up to and including your installed PHP version.

Features
* [Creates an object graph] containing the structure of your application much
  like a site map shows the structure of a website.
* Can read and interpret code of any PHP version starting with 5.2 up to and
  including your currently installed version of PHP.
* Due it's clean interface it can be in any application without a complex setup.

Autoloader: %{_datadir}/php/phpDocumentor/Reflection1/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a 1

mv src/phpDocumentor/Reflection src/phpDocumentor/Reflection1

%if %{with_php_parser}
# Include PHPParser in this library, as old deprecated version required
mv %{php_parser_project}-%{php_parser_commit}/lib/PHPParser \
    src/phpDocumentor/Reflection1/PHPParser
mv %{php_parser_project}-%{php_parser_commit}/LICENSE LICENSE-PHPParser
%endif

cp %{SOURCE2} LICENSE


%build
: Generate library autoloader
%{_bindir}/phpab \
  --template fedora \
  --output src/phpDocumentor/Reflection1/autoload.php \
  src/phpDocumentor/Reflection1

cat << 'EOF' | tee -a src/phpDocumentor/Reflection1/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Log/autoload.php',
    array(
        '%{_datadir}/php/phpDocumentor/Reflection/DocBlock2/autoload.php',
        '%{_datadir}/php/phpDocumentor/Reflection/DocBlock/autoload.php',
    ),
%if ! %{with_php_parser}
    '%{_datadir}/php/PhpParser/autoload.php',
%endif
));
EOF


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
: Fix path to Mockery
sed -e 's:vendor/mockery/mockery/library:/usr/share/php:' \
    phpunit.xml.dist > phpunit.xml

: Create tests autoloader
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests

cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{_datadir}/php/Mockery/autoload.php';
require_once '%{buildroot}%{_datadir}/php/phpDocumentor/Reflection1/autoload.php';
EOF

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in %{_bindir}/php %{?rhel:php54 php55} php56 php70 php71; do
    if [ "%{_bindir}/php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose || RETURN_CODE=1
    fi
done
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE*
%doc *.md
%doc composer.json
%{_datadir}/php/phpDocumentor/Reflection1


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-5
- Fix obsolete

* Thu Apr 13 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-4
- Package rename (php-phpdocumentor-reflection => php-phpdocumentor-reflection1)
- Switch autoloader to php-composer(fedora/autoloader)

* Thu Apr 13 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-3
- Add max versions to BuildRequires
- Prepare for php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2 dependency rename

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- initial package, version 1.0.7
- bundle nikic/php-parser 0.9.4
