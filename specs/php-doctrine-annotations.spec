#
# Fedora spec file for php-doctrine-annotations
#
# Copyright (c) 2013-2023 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without tests

%global github_owner     doctrine
%global github_name      annotations
%global github_version   1.14.3
%global github_commit    fb0d71a7393298a7b232cbf4c8b1f73f3ec3d5af

%global composer_vendor  doctrine
%global composer_project annotations

# "php": "^7.1 || ^8.0"
%global php_min_ver      7.1
# "doctrine/cache": "^1.11 || ^2."
%global cache_min_ver    1.11
%global cache_max_ver    3
# "doctrine/lexer": "^1 || ^2"
#     NOTE: Min version not 1.0 because autoloader required
%global lexer_min_ver    1.0.1
%global lexer_max_ver    3
# "psr/cache": "^1 || ^2 || ^3"
%global psr_cache_min_ver 1
# only v1 is available for now
%global psr_cache_max_ver 2
# "symfony/cache": "^4.4 || ^5.2"
%global symfony_min_ver 4.4
%global symfony_max_ver 6


%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       PHP docblock annotations parser library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-annotations-get-source.sh to create full source.
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires:(php-composer(doctrine/cache) >= %{cache_min_ver} with php-composer(doctrine/cache) < %{cache_max_ver})
BuildRequires:(php-composer(doctrine/lexer) >= %{lexer_min_ver} with php-composer(doctrine/lexer) < %{lexer_max_ver})
BuildRequires:(php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires:(php-composer(symfony/cache) >= %{symfony_min_ver} with php-composer(symfony/cache) < %{symfony_max_ver})
# "phpunit/phpunit": "^7.5 || ^8.5 || ^9.5"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.5

## phpcompatinfo (computed from version 1.10.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
%endif
# Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-tokenizer
Requires:     (php-composer(doctrine/lexer) >= %{lexer_min_ver} with php-composer(doctrine/lexer) < %{lexer_max_ver})
Requires:     (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
# phpcompatinfo (computed from version 1.10.0)
Requires:      php-ctype
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
%{summary} (extracted from Doctrine Common).

Autoloader: %{phpdir}/Doctrine/Common/Annotations/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/Common/Annotations/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\Annotations\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Doctrine/Common/Lexer2/autoload.php',
        '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
    ],
    '%{phpdir}/Psr/Cache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Annotations/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Doctrine/Common/Cache2/autoload.php',
        '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    ], [
        '%{phpdir}/Symfony5/Component/Cache/autoload.php',
        '%{phpdir}/Symfony4/Component/Cache/autoload.php',
    ],
    dirname( __DIR__) . '/tests/Doctrine/Tests/TestInit.php',
    dirname( __DIR__) . '/tests/Doctrine/Tests/Common/Annotations/Fixtures/functions.php',
    dirname( __DIR__) . '/tests/Doctrine/Tests/Common/Annotations/Fixtures/SingleClassLOC1000.php',
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for CMD in "php %{phpunit}" php80 php81 php82; do
    if which $CMD; then
        set $CMD
        $1 ${2:-%{_bindir}/phpunit9} --verbose \
            -d pcre.recursion_limit=10000 \
            --filter '^((?!(testAvoidCallingFilemtimeTooMuch)).)*$' \
            || RETURN_CODE=1
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
%{phpdir}/Doctrine/Common/Annotations


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb  3 2023 Remi Collet <remi@remirepo.net> - 1.14.3-1
- update to 1.14.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Remi Collet <remi@remirepo.net> - 1.14.2-1
- update to 1.14.2

* Tue Dec 13 2022 Remi Collet <remi@remirepo.net> - 1.14.1-1
- update to 1.14.1
- allow doctrine/lexer v2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul  4 2022 Remi Collet <remi@remirepo.net> - 1.13.3-1
- update to 1.13.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug  6 2021 Remi Collet <remi@remirepo.net> - 1.13.2-1
- update to 1.13.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 1.13.1-1
- update to 1.13.1
- add runtime dependency on psr/cache
- add build dependency on symfony/cache

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 1.12.1-1
- update to 1.12.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 1.11.1-1
- update to 1.11.1

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Wed Aug 12 2020 Remi Collet <remi@remirepo.net> - 1.10.4-1
- update to 1.10.4
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.10.3-1
- update to 1.10.3 (no change)

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2

* Thu Apr  2 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Thu Apr  2 2020 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- switch to phpunit7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on PHP 7.1
- use phpunit6
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-4
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-1
- Updated to 1.2.7 (RHBZ #1258669 / CVE-2015-5723)
- Updated autoloader to load dependencies after self registration

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-2
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-1
- Updated to 1.2.6 (RHBZ #1211816)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Updated to 1.2.3 (BZ #1176942)

* Sun Oct 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.1-1
- Updated to 1.2.1 (BZ #1146910)
- %%license usage

* Thu Jul 17 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-2
- Removed skipping of test (php-phpunit-PHPUnit-MockObject patched to fix issue)

* Tue Jul 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (BZ #1116887)

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-5.20131220gita11349d
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")
- Updated dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4.20131220gita11349d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-3.20131220gita11349d
- Minor syntax changes

* Fri Jan 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-2.20131220gita11349d
- Conditional %%{?dist}
- Added conflict w/ PEAR-based DoctrineCommon pkg (version < 2.4)

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-1.20131220gita11349d
- Initial package
