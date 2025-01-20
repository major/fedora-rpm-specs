#
# Fedora spec file for php-guzzlehttp-psr7
#
# Copyright (c) 2015-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      psr7
%global github_version   1.9.0
%global github_commit    e98e3e6d4f86621a9b75f623996e6bbdeb4b9318

%global composer_vendor  guzzlehttp
%global composer_project psr7

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "psr/http-message": "~1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0
# "ralouphie/getallheaders": "^2.0.5 || ^3.0.0"
%global ralouphie_getallheaders_min_ver 2.0.5
%global ralouphie_getallheaders_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

# PHPUnit
%global phpunit_require phpunit9
%global phpunit_exec    phpunit9

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       PSR-7 message implementation

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-guzzlehttp-psr7-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-zlib
BuildRequires: %{phpunit_require}
%if %{with_range_dependencies}
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
BuildRequires: (php-composer(ralouphie/getallheaders) >= %{ralouphie_getallheaders_min_ver} with php-composer(ralouphie/getallheaders) < %{ralouphie_getallheaders_max_ver})
%else
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
BuildRequires: php-composer(ralouphie/getallheaders) <  %{ralouphie_getallheaders_max_ver}
BuildRequires: php-composer(ralouphie/getallheaders) >= %{ralouphie_getallheaders_min_ver}
%endif
## phpcompatinfo (computed from version 1.6.1)
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-xmlreader
BuildRequires: php-xmlwriter
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
Requires:      (php-composer(ralouphie/getallheaders) >= %{ralouphie_getallheaders_min_ver} with php-composer(ralouphie/getallheaders) < %{ralouphie_getallheaders_max_ver})
Recommends:     php-composer(laminas/laminas-httphandlerrunner)
%else
Requires:      php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:      php-composer(psr/http-message) >= %{psr_http_message_min_ver}
Requires:      php-composer(ralouphie/getallheaders) <  %{ralouphie_getallheaders_max_ver}
Requires:      php-composer(ralouphie/getallheaders) >= %{ralouphie_getallheaders_min_ver}
%endif
# phpcompatinfo (computed from version 1.6.1)
Requires:      php-filter
Requires:      php-hash
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/http-message-implementation) = 1.0

%description
PSR-7 message implementation, several stream decorators, and some helpful
functionality like query string parsing.

Autoloader: %{phpdir}/GuzzleHttp/Psr7/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Psr7\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/functions_include.php',
    '%{phpdir}/Psr/Http/Message/autoload.php',
    '%{phpdir}/ralouphie-getallheaders/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Laminas/HttpHandlerRunner/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp
cp -rp src %{buildroot}%{phpdir}/GuzzleHttp/Psr7


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/GuzzleHttp/Psr7/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Tests\\Psr7\\', __DIR__.'/tests');

if (!class_exists('PHPUnit\\Framework\\Error\\Warning')) {
  class_alias('PHPUnit_Framework_Error_Warning', 'PHPUnit\\Framework\\Error\\Warning');
}
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
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
%dir %{phpdir}/GuzzleHttp
     %{phpdir}/GuzzleHttp/Psr7


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Mon Mar 21 2022 Remi Collet <remi@remirepo.net> - 1.8.5-1
- update to 1.8.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 1.8.2-1
- update to 1.8.2

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1
- switch to phpunit9
- add weak dependency on laminas/laminas-httphandlerrunner

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.1-1
- Update to 1.6.1 (RHBZ #1727190)
- Conditionally use range dependencies
- Conditionally use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.2-1
- Updated to 1.4.2 (RHBZ #1434198)
- Don't use autoloader to load functions include

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-1
- Updated to 1.4.1 (RHBZ #1425429)
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-1
- Updated to 1.3.1 (RHBZ #1352354)

* Sun May 29 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1326975)

* Fri Mar 11 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Updated to 1.2.3 (RHBZ #1301276)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.1-1
- Updated to 1.2.1 (RHBZ #1277467)

* Sun Aug 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (RHBZ #1253997)
- Updated autoloader to load dependencies after self registration

* Sun Jul 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-3
- Use full paths in autoloader

* Wed Jul 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-2
- Add autoloader dependencies
- Modify autoloader

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
