#
# Fedora spec file for php-asm89-stack-cors
#
# Copyright (c) 2016-2018 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     asm89
%global github_name      stack-cors
%global github_version   1.2.0
%global github_commit    c163e2b614550aedcf71165db2473d936abbced6

%global composer_vendor  asm89
%global composer_project stack-cors

# "php": ">=5.5.9"
%global php_min_ver 5.5.9
# "symfony/http-foundation": "~2.7|~3.0|~4.0"
# "symfony/http-kernel": "~2.7|~3.0|~4.0"
#     NOTE: Min version not 2.7 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       10%{?github_release}%{?dist}
Summary:       Cross-origin resource sharing library and stack middleware

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-asm89-stack-cors-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
%else
BuildRequires: php-composer(symfony/http-foundation) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-foundation) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-pcre
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
Requires:      (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
%else
Requires:      php-composer(symfony/http-foundation) >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-foundation) <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-kernel) >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-kernel) <  %{symfony_max_ver}
%endif
# phpcompatinfo (computed from version 1.2.0)
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Library and middleware enabling cross-origin resource sharing for your
http-{foundation,kernel} using application. It attempts to implement the
W3C Candidate Recommendation [1] for cross-origin resource sharing.

Autoloader: %{phpdir}/Asm89/Stack/autoload-cors.php

[1] http://www.w3.org/TR/cors/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab \
    --template fedora \
    --output src/Asm89/Stack/autoload-cors.php \
    src/

cat <<'AUTOLOAD' | tee -a src/Asm89/Stack/autoload-cors.php

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony4/Component/HttpFoundation/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpFoundation/autoload.php',
        '%{phpdir}/Symfony/Component/HttpFoundation/autoload.php',
    ],
    [
        '%{phpdir}/Symfony4/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony/Component/HttpKernel/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Asm89 %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose \
            --bootstrap %{buildroot}%{phpdir}/Asm89/Stack/autoload-cors.php \
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
%dir %{phpdir}/Asm89
%dir %{phpdir}/Asm89/Stack
     %{phpdir}/Asm89/Stack/autoload-cors.php
     %{phpdir}/Asm89/Stack/Cors.php
     %{phpdir}/Asm89/Stack/CorsService.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Update to 1.2.0 (RHBZ #1528097)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Update get source script to save tarball in local directory

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1441443)
- Add max versions to BuildRequires
- Switch autoloader to php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
