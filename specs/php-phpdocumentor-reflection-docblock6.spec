# Fedora/remirepo spec file for php-phpdocumentor-reflection-docblock5
#
# SPDX-FileCopyrightText:  Copyright 2014-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    2f5cbed597cb261d1ea458f3da3a9ad32e670b1e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global major        6
%bcond_without       tests

Name:           php-phpdocumentor-reflection-docblock%{major}
Version:        6.0.1
Release:        1%{?dist}
Summary:        DocBlock parser

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}

# GitHub export does not include tests.
# Run php-phpdocumentor-reflection-docblock-get-source.sh to create full source.
Source0:       %{name}-%{version}-%{gh_short}.tar.gz
Source1:       makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-filter
BuildRequires: (php-composer(phpdocumentor/type-resolver)     >= 2.0   with php-composer(phpdocumentor/type-resolver)     < 3)
BuildRequires: (php-composer(webmozart/assert)                >= 1.9.1 with php-composer(webmozart/assert)                < 3)
BuildRequires: (php-composer(phpdocumentor/reflection-common) >= 2.2   with php-composer(phpdocumentor/reflection-common) < 3)
BuildRequires: (php-composer(phpstan/phpdoc-parser)           >= 2.0   with php-composer(phpstan/phpdoc-parser)           < 3)
BuildRequires: (php-composer(doctrine/deprecations)           >= 1.1   with php-composer(doctrine/deprecations)           < 2)
# From composer.json, require-dev
#        "mockery/mockery": "~1.3.5 || ~1.6.0",
#        "phpunit/phpunit": "^9.5",
#        "phpstan/phpstan": "^1.8",
#        "phpstan/phpstan-mockery": "^1.1",
#        "phpstan/extension-installer": "^1.1",
#        "phpstan/phpstan-webmozart-assert": "^1.2",
#        "psalm/phar": "^5.26",
#        "shipmonk/dead-code-detector": "^0.5.1"
BuildRequires:  phpunit9 >= 9.5
%global phpunit %{_bindir}/phpunit9
BuildRequires: (php-composer(mockery/mockery) >= 1.6 with php-composer(mockery/mockery) <  2)
# From phpcompatinfo report for 5.0.0
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

# From composer.json, require
#        "php": "^7.4 || ^8.0",
#        "phpdocumentor/type-resolver": "^2.0",
#        "webmozart/assert": "^1.9.1 || ^2",
#        "phpdocumentor/reflection-common": "^2.2",
#        "ext-filter": "*",
#        "phpstan/phpdoc-parser": "^2.0",
#        "doctrine/deprecations": "^1.1"
Requires:       php(language) >= 7.4
Requires:       php-filter
Requires:      (php-composer(phpdocumentor/type-resolver)     >= 2.0   with php-composer(phpdocumentor/type-resolver)     < 3)
Requires:      (php-composer(webmozart/assert)                >= 1.9.1 with php-composer(webmozart/assert)                < 3)
Requires:      (php-composer(phpdocumentor/reflection-common) >= 2.2   with php-composer(phpdocumentor/reflection-common) < 3)
Requires:      (php-composer(phpstan/phpdoc-parser)           >= 2.0   with php-composer(phpstan/phpdoc-parser)           < 3)
Requires:      (php-composer(doctrine/deprecations)           >= 1.1   with php-composer(doctrine/deprecations)           < 2)
# From phpcompatinfo report for 4.3.2
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}


%description
The ReflectionDocBlock component of phpDocumentor provides a DocBlock
parser that is fully compatible with the PHPDoc standard.

With this component, a library can provide support for annotations via
DocBlocks or otherwise retrieve information that is embedded in a DocBlock.

Autoloader: %{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

sed 's#vendor/mockery/mockery/library/Mockery#%{_datadir}/php/Mockery1#' phpunit.xml.dist \
    > phpunit.xml

# single directory tree
mv src/*php      src/DocBlock/
mv src/Exception src/DocBlock/


%build
phpab \
  --template fedora \
  --output src/DocBlock/autoload.php \
  src/

cat << 'AUTOLOAD' | tee -a src/DocBlock/autoload.php

$deps = [
    '%{_datadir}/php/Webmozart/Assert/autoload.php',
];
if (PHP_VERSION_ID > 80200) {
    array_unshift($deps, '%{_datadir}/php/Webmozart/Assert2/autoload.php');
}

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/phpDocumentor/Reflection/TypeResolver2/autoload.php',
    '%{_datadir}/php/phpDocumentor/Reflection2/autoload-common.php',
    $deps,
    '%{_datadir}/php/PHPStan/PhpDocParser/autoload.php',
    '%{_datadir}/php/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD


%install
mkdir -p            %{buildroot}%{_datadir}/php/phpDocumentor/Reflection
cp -pr src/DocBlock %{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}


%check
%if %{with tests}
sed -e '/autoload.php/d' -i docs/examples/*.php

phpab \
  --template fedora \
  --output bootstrap.php \
  tests/unit tests/integration

cat <<BOOTSTRAP | tee -a bootstrap.php

\Fedora\Autoloader\Dependencies::required([
    '%{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php',
    '%{_datadir}/php/Mockery1/autoload.php',
]);
BOOTSTRAP

RETURN_CODE=0
for PHP_EXEC in "php %{phpunit}" php81 php82 php83 php84 php85; do
    if which $PHP_EXEC; then
        set $PHP_EXEC
        $1 -d auto_prepend_file=$PWD/bootstrap.php \
            ${2:-%{_bindir}/phpunit9} \
                --bootstrap bootstrap.php \
                --filter '^((?!(testDescriptionsCanEscapeAtSignsAndClosingBraces)).)*$' \
                --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc docs
%doc composer.json
%dir %{_datadir}/php/phpDocumentor/Reflection
     %{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}


%changelog
* Wed Feb 25 2026 Remi Collet <remi@remirepo.net> - 6.0.1-1
- update to 6.0.1
- rename to php-phpdocumentor-reflection-docblock6
- move to /usr/share/php/phpDocumentor/Reflection/DocBlock6
- raise dependency on phpdocumentor/type-resolver 2.0
- raise dependency on phpstan/phpdoc-parser 2.0

* Thu Dec 25 2025 Remi Collet <remi@remirepo.net> - 5.6.6-1
- update to 5.6.6
- allow webmozart/assert version 2

* Fri Nov 28 2025 Remi Collet <remi@remirepo.net> - 5.6.5-1
- update to 5.6.5

* Wed Nov 19 2025 Remi Collet <remi@remirepo.net> - 5.6.4-1
- update to 5.6.4

* Thu Aug 28 2025 Remi Collet <remi@remirepo.net> - 5.6.3-1
- update to 5.6.3

* Mon Apr 14 2025 Remi Collet <remi@remirepo.net> - 5.6.2-1
- update to 5.6.2

* Mon Dec 23 2024 Remi Collet <remi@remirepo.net> - 5.6.1-2
- allow phpstan/phpdoc-parser v2

* Mon Dec  9 2024 Remi Collet <remi@remirepo.net> - 5.6.1-1
- update to 5.6.1
- re-license spec file to CECILL-2.1

* Tue Nov 12 2024 Remi Collet <remi@remirepo.net> - 5.6.0-1
- update to 5.6.0

* Wed Nov  6 2024 Remi Collet <remi@remirepo.net> - 5.5.1-1
- update to 5.5.1

* Tue Nov  5 2024 Remi Collet <remi@remirepo.net> - 5.5.0-1
- update to 5.5.0

* Wed May 22 2024 Remi Collet <remi@remirepo.net> - 5.4.1-1
- update to 5.4.1

* Thu Apr 25 2024 Remi Collet <remi@remirepo.net> - 5.4.0-1
- update to 5.4.0
- raise dependency on PHP 7.4
- raise dependency on phpdocumentor/type-resolver 1.7
- add dependency on phpstan/phpdoc-parser
- add dependency on doctrine/deprecations

* Wed Oct 20 2021 Remi Collet <remi@remirepo.net> - 5.3.0-1
- update to 5.3.0

* Fri Sep 18 2020 Remi Collet <remi@remirepo.net> - 5.2.2-1
- update to 5.2.2

* Mon Aug 17 2020 Remi Collet <remi@remirepo.net> - 5.2.1-1
- update to 5.2.1

* Tue Jul 21 2020 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0
- raise dependency on phpdocumentor/type-resolver 1.3
- raise dependency on webmozart/assert 1.9.1
- raise dependency on phpdocumentor/reflection-common 2.2
- raise build dependency on mockery/mockery 1.3.2
- switch to phpunit9

* Wed Feb 26 2020 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- drop unneeded hack as our PR was merged upstream

* Wed Feb 12 2020 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-phpdocumentor-reflection-docblock5
- move to /usr/share/php/phpDocumentor/Reflection/DocBlock5
- raise dependency on PHP 7.2
- raise dependency on type-resolver 1
- raise dependency on reflection-common 2
- switch to phpunit8

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 4.3.4-1
- update to 4.3.4

* Fri Dec 20 2019 Remi Collet <remi@remirepo.net> - 4.3.3-1
- update to 4.3.3

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 4.3.2-1
- update to 4.3.2
- allow reflection-common 2.0
- allow type-resolver 1.0

* Thu May  2 2019 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 4.3.0-1
- Update to 4.3.0

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 4.2.0-1
- Update to 4.2.0
- rename to php-phpdocumentor-reflection-docblock4
- move to /usr/share/php/phpDocumentor/Reflection/DocBlock4
- raise dependency on PHP 7.0
- raise dependency on phpdocumentor/type-resolver 0.4.0
- use phpunit6 and php-mockery for test suite

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 3.2.2-1
- Update to 3.2.2

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 3.2.1-2
- add patch to fix BC break, thanks to Koschei,  from
  https://github.com/phpDocumentor/ReflectionDocBlock/pull/113

* Sat Aug 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.1-1
- Update to 3.2.1 (RHBZ #1471379)

* Tue Jul 18 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.0-1
- Update to 3.2.0 (RHBZ #1471379)

* Fri May  5 2017 Shawn Iwinski <shawn@iwin.ski>, Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1
- raise dependency on PHP 5.5
- add dependency on phpdocumentor/reflection-common
- add dependency on phpdocumentor/type-resolver
- add dependency on webmozart/assert
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- LICENSE is in upstream archive

* Tue Feb  3 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-2
- add LICENSE from upstream repository

* Fri Dec 19 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- initial package
- open https://github.com/phpDocumentor/ReflectionDocBlock/issues/40
  for missing LICENSE file
