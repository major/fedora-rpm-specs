# remirepo/fedora spec file for php-brick-math
#
# Copyright (c) 2020-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# Github
%global gh_commit    f510c0a40911935b77b86859eb5223d58d660df1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     brick
%global gh_project   math
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Brick
%global ns_project   Math

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.12.1
Release:        3%{?dist}
Summary:        Arbitrary-precision arithmetic library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 8.1
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^10.1",
#        "php-coveralls/php-coveralls": "^2.2",
#        "vimeo/psalm": "^5.16.0"
%if %{with tests}
BuildRequires:  phpunit10 >= 10.1
%global phpunit %{_bindir}/phpunit10
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^8.0"
Requires:       php(language) >= 8.1
# From phpcompatifo report for 0.9.1
Requires:       php-pcre
Requires:       php-spl
# See Brick\Math\Internal\Calculator::detect()
Requires:      (php-gmp or php-bcmath)

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
A PHP library to work with arbitrary precision numbers.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Brick\\Math\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: Run upstream test suite
ret=0
# don't test Native with is terribly slow, as bcmath/gmp are set as mandatory
for calc in GMP BCMath; do
  export CALCULATOR=$calc
  for cmdarg in "php %{phpunit}" php81 php82 php83; do
    if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit10} \
        --no-coverage || ret=1
    fi
  done
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May  2 2024 Remi Collet <remi@remirepo.net> - 0.12.1-1
- update to 0.12.1
- raise dependency on PHP 8.1
- switch to phpunit10

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Remi Collet <remi@remirepo.net> - 0.11.0-1
- update to 0.11.0
- raise dependency on PHP 8.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Remi Collet <remi@remirepo.net> - 0.10.2-1
- update to 0.10.2

* Wed Aug  3 2022 Remi Collet <remi@remirepo.net> - 0.10.1-1
- update to 0.10.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Remi Collet <remi@remirepo.net> - 0.10.0-1
- update to 0.10.0
- raise dependency on PHP 7.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 0.9.3-1
- update to 0.9.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 0.9.2-1
- update to 0.9.2
- switch to phpunit9

* Thu Oct  1 2020 Remi Collet <remi@remirepo.net> - 0.9.1-1
- initial package
