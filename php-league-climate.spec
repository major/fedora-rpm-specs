#
# Fedora spec file for php-league-climate
#
# Copyright (c) 2016-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      climate
%global github_version   3.5.0
%global github_commit    0d2fdbf8829f60f6ba6433df68d6f3fe1271b8e6

%global composer_vendor  league
%global composer_project climate

# "php": "^7.1"
%global php_min_ver 7.1
# "mikey179/vfsStream": "^1.4"
#     NOTE: Min version not 1.4 because autoloader required
%global vfsstream_min_ver 1.6.0
%global vfsstream_max_ver 2.0
# "mockery/mockery": "^1.0"
#     NOTE: Min version not 1.0 because tests pass with 0.9 version available
%global mockery_min_ver 0.9.3
%global mockery_max_ver 2.0
# "psr/log": "^1.0"
%global psr_log_min_ver 1.0
%global psr_log_max_ver 2.0
# "seld/cli-prompt": "^1.0"
%global seld_cli_prompt_min_ver 1.0
%global seld_cli_prompt_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       Allows you to easily output colored text, special formats, and more

License:       MIT
URL:           http://climate.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-climate-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(mikey179/vfsStream) >= %{vfsstream_min_ver} with php-composer(mikey179/vfsStream) < %{vfsstream_max_ver})
BuildRequires: (php-composer(mockery/mockery) >= %{mockery_min_ver} with php-composer(mockery/mockery) < %{mockery_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(seld/cli-prompt) >= %{seld_cli_prompt_min_ver} with php-composer(seld/cli-prompt) < %{seld_cli_prompt_max_ver})
%else
BuildRequires: php-composer(mikey179/vfsStream) <  %{vfsstream_max_ver}
BuildRequires: php-composer(mikey179/vfsStream) >= %{vfsstream_min_ver}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(seld/cli-prompt) <  %{seld_cli_prompt_max_ver}
BuildRequires: php-composer(seld/cli-prompt) >= %{seld_cli_prompt_min_ver}
%endif
## phpcompatinfo (computed from version 3.2.1)
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(seld/cli-prompt) >= %{seld_cli_prompt_min_ver} with php-composer(seld/cli-prompt) < %{seld_cli_prompt_max_ver})
%else
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(seld/cli-prompt) <  %{seld_cli_prompt_max_ver}
Requires:      php-composer(seld/cli-prompt) >= %{seld_cli_prompt_min_ver}
%endif
# phpcompatinfo (computed from version 3.2.1)
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-posix
Requires:      php-reflection
Requires:      php-zlib
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
If you’re running PHP from the command line, CLImate is your new best bud.

CLImate allows you to easily output colored text, special formatting, and more.
It makes output to the terminal clearer and debugging a lot simpler.

Autoloader: %{phpdir}/League/CLImate/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('League\\CLImate\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/Seld/CliPrompt/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League/CLImate
cp -rp src/* %{buildroot}%{phpdir}/League/CLImate/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/League/CLImate/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\CLImate\\Tests\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Mockery1/autoload.php',
        '%{phpdir}/Mockery/autoload.php',
    ),
    '%{phpdir}/org/bovigo/vfs/autoload.php',
));
BOOTSTRAP

: Remove Composer vendor file load
sed '/require.*vendor\/mikey179/d' -i tests/FileTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php72 php73 php74; do
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
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc README.md
%dir %{phpdir}/League
     %{phpdir}/League/CLImate


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5.0-1
- Update to 3.5.0 (RHBZ #1674287)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep  3 2018 Remi Collet <remi@remirepo.net> - 3.4.1-3
- allow php-mockery (v1)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.4.1-1
- Update to 3.4.1 (RHBZ #1574020)

* Mon Apr 23 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.4-1
- Update to 3.2.4 (RHBZ #1549561)
- Update get source script to save source in same directory
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.1-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 11 2016 Shawn Iwinski <shawn@iwin.ski> - 3.2.1-1
- Initial package
