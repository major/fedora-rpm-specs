# remirepo/fedora spec file php-felixfbecker-advanced-json-rpc3
#
# Copyright (c) 2017-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    b5f37dbff9a8ad360ca341f3240dc1c168b45447
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     felixfbecker
%global gh_project   php-advanced-json-rpc

%global pk_vendor    %{gh_owner}
%global pk_project   advanced-json-rpc

%global ns_vendor    %nil
%global ns_project   AdvancedJsonRpc
%global major        3
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.2.1
Release:        10%{?dist}
Summary:        A more advanced JSONRPC implementation

License:        ISC
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(netresearch/jsonmapper)            >= 1.0    with php-composer(netresearch/jsonmapper)            <  5)
BuildRequires:  (php-composer(phpdocumentor/reflection-docblock) >= 4.3.4  with php-composer(phpdocumentor/reflection-docblock) <  6)
%else
BuildRequires:  php-netresearch-jsonmapper
BuildRequires:  php-phpdocumentor-reflection-docblock4
%endif
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.0 || ^8.0""
BuildRequires:  phpunit8
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0",
#        "netresearch/jsonmapper": "^1.0 || ^2.0 || ^3.0 || ^4.0",
#        "phpdocumentor/reflection-docblock": "^4.3.4 || ^5.0.0"
Requires:       php(language) >= 7.1
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(netresearch/jsonmapper)            >= 1.0    with php-composer(netresearch/jsonmapper)            <  5)
Requires:       (php-composer(phpdocumentor/reflection-docblock) >= 4.3.4  with php-composer(phpdocumentor/reflection-docblock) <  6)
%else
Requires:       php-netresearch-jsonmapper
Requires:       php-phpdocumentor-reflection-docblock4
%endif
# From phpcompatinfo report for version 3.0.1
Requires:       php-reflection
Requires:       php-json
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Advanced JSONRPC

Provides basic classes for requests and responses in JSONRPC and a
Dispatcher class that can decode a JSONRPC request and call appropiate
methods on a target, coercing types of parameters by type-hints and
@param tags.

Supports nested targets:
If the method is something like myNestedTarget->theMethod, the dispatcher
will look for a myNestedTarget property on the target and call theMethod
on it.

The delimiter is configurable and defaults to the PHP object operator ->.

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{php_home}/phpDocumentor/Reflection/DocBlock5/autoload.php',
        '%{php_home}/phpDocumentor/Reflection/DocBlock4/autoload.php',
    ],
    '%{php_home}/netresearch/jsonmapper/autoload.php',
]);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p    %{buildroot}%{php_home}
cp -pr lib  %{buildroot}%{php_home}/%{ns_project}%{major}


%check
%if %{with_tests}
cat << 'EOF' | tee bootstrap.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\Tests\\', __DIR__ . '/tests');
EOF

ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --do-not-cache-result \
      --no-coverage \
      --bootstrap bootstrap.php \
      --verbose tests || ret=1
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
%doc README.md
%{php_home}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1 (no change)
- allow netresearch/jsonmapper 4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (no change)
- raise dependency on PHP 7.1
- raise dependency on phpdocumentor/reflection-docblock 4.3.4
- switch to phpunit8

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 3.1.1-3
- allow netresearch/jsonmapper 3.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1 (no change)
- allow netresearch/jsonmapper 2.0

* Wed Feb 12 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0 (no change)
- allow phpdocumentor/reflection-docblock v5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 3.0.4-1
- update to 3.0.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)
- add upstream LICENSE file

* Mon Sep 10 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2
- sources from git snapshot

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 3.0.1-2
- missing dependencies

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1
- rename to php-felixfbecker-advanced-json-rpc3
- move to /usr/share/php/AdvancedJsonRpc3
- raise dependency on phpdocumentor/reflection-docblock 4.0
- use phpunit6

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 2.0.3-1
- initial package, version 2.0.3
- open https://github.com/felixfbecker/php-advanced-json-rpc/issues/11 - LICENSE
