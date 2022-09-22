#
# Fedora spec file for php-codeception-specify
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Codeception
%global github_name      Specify
%global github_version   1.1.0
%global github_commit    504ac7a882e6f7226b0cff44c72a6c0bbd0bad95

%global composer_vendor  codeception
%global composer_project specify

# "php": ">=7.1.0"
%global php_min_ver 7.1.0
# "myclabs/deep-copy": "~1.1"
%global myclabs_deep_copy_min_ver 1.1
%global myclabs_deep_copy_max_ver 2.0
# "phpunit/phpunit": "^7.0"

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?github_release}%{?dist}
Summary:       BDD code blocks for PHPUnit and Codeception

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit7
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver} with php-composer(myclabs/deep-copy) < %{myclabs_deep_copy_max_ver})
%else
BuildRequires: php-composer(myclabs/deep-copy) <  %{myclabs_deep_copy_max_ver}
BuildRequires: php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver}
%endif
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      phpunit7
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver} with php-composer(myclabs/deep-copy) < %{myclabs_deep_copy_max_ver})
%else
Requires:      php-composer(myclabs/deep-copy) <  %{myclabs_deep_copy_max_ver}
Requires:      php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BDD style code blocks for PHPUnit / Codeception

Specify allows you to write your tests in more readable BDD style, the
same way you might have experienced with Jasmine. Inspired by MiniTest
of Ruby now you combine BDD and classical TDD style in one test.

Autoloader: %{phpdir}/Codeception/Specify/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/Codeception/Specify/autoload.php src/
cat <<'AUTOLOAD' | tee -a src/Codeception/Specify/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/DeepCopy/autoload.php',
    '%{phpdir}/PHPUnit7/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Codeception %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Mock Composer autoload
mkdir vendor
ln -s %{buildroot}%{phpdir}/Codeception/Specify/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit7)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
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
%dir %{phpdir}/Codeception
     %{phpdir}/Codeception/Specify
     %{phpdir}/Codeception/Specify.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-2
- Update phpcompatinfo dependencies

* Mon May 27 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1515810)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-2
- Remove empty Suggests

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Initial package
