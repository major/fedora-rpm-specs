# remirepo/fedora spec file for php-swaggest-json-schema
#
# Copyright (c) 2019-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    d23adb53808b8e2da36f75bc0188546e4cbe3b45
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   php-json-schema
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   json-schema
# Namespace
%global ns_vendor    Swaggest
%global ns_project   JsonSchema
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.12.42
Release:        2%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        High definition PHP structures with JSON-schema based validation

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-json
BuildRequires:  php-mbstring
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(phplang/scope-exit)    >= 1.0   with php-composer(phplang/scope-exit)    < 2)
BuildRequires: (php-composer(swaggest/json-diff)    >= 3.8.2 with php-composer(swaggest/json-diff)    < 4)
%else
BuildRequires:  php-phplang-scope-exit              >= 1.0
BuildRequires:  php-swaggest-json-diff              >= 3.8.2
%endif
# For tests, from composer.json "require-dev": {
#    "phpunit/phpunit": "^5",
#    "phpunit/php-code-coverage": "^4",
#    "codeclimate/php-test-reporter": "^0.4.0"
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-spl
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#    "php": ">=5.4",
#    "ext-json": "*",
#    "ext-mbstring": "*",
#    "phplang/scope-exit": "^1.0",
#    "swaggest/json-diff": "^3.8.2",
#    "symfony/polyfill-mbstring": "^1.19"
Requires:       php(language) >= 5.4
Requires:       php-json
Requires:       php-mbstring
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(phplang/scope-exit)    >= 1.0   with php-composer(phplang/scope-exit)    < 2)
Requires:      (php-composer(swaggest/json-diff)    >= 3.8.2 with php-composer(swaggest/json-diff)    < 4)
%else
Requires:       php-phplang-scope-exit              >= 1.0
Requires:       php-swaggest-json-diff              >= 3.8.2
%endif
# From phpcompatinfo report for 0.12.17
Requires:       php-date
Requires:       php-filter
Requires:       php-pcre
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
High definition PHP structures with JSON-schema based validation.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Fix layout
mkdir src/spec
cp -p spec/*.json src/spec/
sed -e 's:/../spec/:/spec/:' -i src/RemoteRef/Preloaded.php


%build
: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/PhpLang/scope-exit-autoload.php',
    '%{_datadir}/php/Swaggest/JsonDiff/autoload.php',
]);
EOF


%install
: Library
mkdir -p         %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src       %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests/src');

class PHPUnit_Framework_TestCase extends \PHPUnit\Framework\Testcase {
	function setExpectedException($e, $m = '') {
		$this->expectException($e);
		if ($m) $this->expectExceptionMessage($m);
	}
}
EOF

# For phpunit9
sed -e '/setUp()/s/$/:void/' \
  -i tests/src/PHPUnit/Example/ExampleTest.php

# Skip online tests: testInvalid, testValidate
# Skip because of phpunit9: testPatternPropertiesMismatch
ret=0
for cmd in php php80 php81 php82 php83; do
   if which $cmd; then
      $cmd %{phpunit} \
        --no-coverage \
        --filter '^((?!(SwaggerTest::testInvalid|SwaggerTest::testValidate|testPatternPropertiesMismatch)).)*$' \
        || ret=1
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
%doc CHANGELOG.md
%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Oct  6 2023 Remi Collet <remi@remirepo.net> - 0.12.42-2
- switch to phpunit9

* Wed Sep 13 2023 Remi Collet <remi@remirepo.net> - 0.12.42-1
- update to 0.12.42

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Remi Collet <remi@remirepo.net> - 0.12.41-1
- update to 0.12.41

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Remi Collet <remi@remirepo.net> - 0.12.39-1
- update to 0.12.39 (no change)

* Wed Sep 22 2021 Remi Collet <remi@remirepo.net> - 0.12.38-1
- update to 0.12.38
- raise dependency on swaggest/json-diff 3.8.2

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 0.12.37-1
- update to 0.12.37

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 0.12.36-1
- update to 0.12.36

* Fri Jun 18 2021 Remi Collet <remi@remirepo.net> - 0.12.35-1
- update to 0.12.35

* Thu Jun 17 2021 Remi Collet <remi@remirepo.net> - 0.12.34-1
- update to 0.12.34

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 0.12.33-1
- update to 0.12.33

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 0.12.32-1
- update to 0.12.32

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 0.12.31-1
- update to 0.12.31

* Thu Sep 10 2020 Remi Collet <remi@remirepo.net> - 0.12.30-1
- update to 0.12.30

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Remi Collet <remi@remirepo.net> - 0.12.29-1
- update to 0.12.29

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 0.12.28-1
- update to 0.12.28

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 0.12.25-1
- update to 0.12.25

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 0.12.24-1
- update to 0.12.24

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 0.12.23-1
- update to 0.12.23

* Tue Oct 22 2019 Remi Collet <remi@remirepo.net> - 0.12.22-1
- update to 0.12.22

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 0.12.21-1
- update to 0.12.21

* Mon Sep 23 2019 Remi Collet <remi@remirepo.net> - 0.12.20-1
- update to 0.12.20

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 0.12.19-1
- update to 0.12.19

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 0.12.17-1
- initial package
