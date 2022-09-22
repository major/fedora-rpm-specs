#
# Fedora spec file for php-jakub-onderka-php-console-highlighter
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     JakubOnderka
%global github_name      PHP-Console-Highlighter
%global github_version   0.3.2
%global github_commit    7daa75df45242c8d5b75a22c00a201e7954e4fb5

%global composer_vendor  jakub-onderka
%global composer_project php-console-highlighter

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "jakub-onderka/php-console-color": "~0.1"
%global jakub_onderka_php_console_color_min_ver 0.1
%global jakub_onderka_php_console_color_max_ver 1.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       14%{?github_release}%{?dist}
Summary:       Highlight PHP code in console (terminal)

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Update tests to use createMock() instead of getMock() for PHPUnit 5.4+
# https://github.com/JakubOnderka/PHP-Console-Highlighter/pull/11
# https://patch-diff.githubusercontent.com/raw/JakubOnderka/PHP-Console-Highlighter/pull/11.patch
Patch0:        %{name}-pr11-phpunit-createMock.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(jakub-onderka/php-console-color) <  %{jakub_onderka_php_console_color_max_ver}
BuildRequires: php-composer(jakub-onderka/php-console-color) >= %{jakub_onderka_php_console_color_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.3.2)
BuildRequires: php-tokenizer
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(jakub-onderka/php-console-color) <  %{jakub_onderka_php_console_color_max_ver}
Requires:      php-composer(jakub-onderka/php-console-color) >= %{jakub_onderka_php_console_color_min_ver}
# phpcompatinfo (computed from version 0.3.2)
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/JakubOnderka/PhpConsoleHighlighter/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update tests to use createMock instead of getMock for PHPUnit 5.4+
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/JakubOnderka/PhpConsoleHighlighter/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JakubOnderka\\PhpConsoleHighlighter\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/JakubOnderka/PhpConsoleColor/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/JakubOnderka/PhpConsoleHighlighter/autoload.php \
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
%{phpdir}/JakubOnderka/PhpConsoleHighlighter


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.2-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Shawn Iwinski <shawn@iwin.ski> - 0.3.2-1
- Initial package
