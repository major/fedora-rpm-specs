#
# Fedora spec file for php-clue-stream-filter
#
# Copyright (c) 2017-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     clue
%global github_name      php-stream-filter
%global github_version   1.6.0
%global github_commit    d6169430c7731d8509da7aecd0af756a5747b78e

%global composer_vendor  clue
%global composer_project stream-filter

# "php": ">=5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       A simple and modern approach to stream filtering in PHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-clue-stream-filter-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.3
## phpcompatinfo (computed from version 1.5.0)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.5.0)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Clue/StreamFilter/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Clue\\StreamFilter\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Clue
cp -rp src %{buildroot}%{phpdir}/Clue/StreamFilter


%check
%if %{with tests}
: Mock Composer autoloader
mkdir vendor
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Clue/StreamFilter/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Clue\\Tests\\StreamFilter\\', dirname(__DIR__).'/tests');
AUTOLOAD

: Upstream tests
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php74 php80 php81; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} --verbose \
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
%dir %{phpdir}/Clue
     %{phpdir}/Clue/StreamFilter


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Shawn Iwinski <shawn@iwin.ski> - 1.4.1-1
- Update to 1.4.1 (RHBZ #1698047)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Shawn Iwinski <shawn@iwin.ski> - 1.4.0-1
- Update to 1.4.0 (RHBZ #1482951)
- Merge default and SCL tests (normailzed to what other specs use)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-2
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Initial package
