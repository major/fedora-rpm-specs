# remirepo/fedora spec file for php-phplang-scope-exit
#
# Copyright (c) 2019-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    8b5a1cbc54df7c1d14916711fb339e67d08cb3dd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phplang
%global gh_project   scope-exit
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PhpLang
%global ns_project   %nil
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.0
Release:        14%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Emulation of SCOPE_EXIT construct from C++

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language)
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "*",
BuildRequires:  phpunit10
%global phpunit %{_bindir}/phpunit10
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

Requires:       php(language)
# From phpcompatinfo report for 1.0.3
# only Core
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This simple class provides an implementation of C++'s SCOPE_EXIT, or GoLang's
defer.

To use, assign an instance of this object to a local variable. When that
variable falls out of scope (or is explicitly unset), the callback passed
to the constructor will be invoked. This is useful, for example, to aid
cleanup at the end of a function.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
%{_bindir}/phpab -t fedora -o src/%{pk_project}-autoload.php src


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php';
class_alias('PHPUnit\\Framework\\TestCase', 'PHPUnit_Framework_TestCase');
EOF

ret=0
for cmd in php php81 php82 php83; do
   if which $cmd; then
      $cmd %{phpunit} \
         --do-not-cache-result \
         --no-coverage \
         --no-configuration \
         . || ret=1
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
%{_datadir}/php/%{ns_vendor}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Remi Collet <remi@remirepo.net> - 1.0.0-12
- switch to phpunit10, fix FTBFS #2261502

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Remi Collet <remi@remirepo.net> - 1.0.0-2
- add commit to include LICENSE file (no change)

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
- open https://github.com/phplang/scope-exit/issues/2 missing LICENSE
- open https://github.com/phplang/scope-exit/pull/3 add LICENSE
