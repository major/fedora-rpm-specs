# remirepo/fedora spec file for php-sebastian-complexity
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

# github
%global gh_commit    739b35e53379900cc9ac327b2147867b8b6efd88
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   complexity
# packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        %nil
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Complexity

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.2
Release:        5%{?dist}
Summary:        Calculating the complexity of PHP code units

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires: (php-composer(nikic/php-parser)     >= 4.7   with php-composer(nikic/php-parser)     < 5)
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json, "require": {
#        "php": ">=7.3",
#        "nikic/php-parser": "^4.7"
Requires:       php(language) >= 7.3
Requires:      (php-composer(nikic/php-parser)     >= 4.7   with php-composer(nikic/php-parser)     < 5)
# from phpcompatinfo report for version 2.0.0
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Library for calculating the complexity of PHP code units.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat <<EOF | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PhpParser4/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1 (no change)

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- initial package
