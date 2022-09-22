# remirepo/fedora spec file for php-hamcrest
#
# Copyright (c) 2015-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    b37020aa976fa52d3de9aa904aa2522dc518f79c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     hamcrest
%global gh_project   hamcrest-php
%global with_tests   0%{!?_without_tests:1}

Name:           php-hamcrest
Version:        1.2.2
Release:        15%{?dist}
Summary:        PHP port of Hamcrest Matchers

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Use generated autoloader instead of composer one
Patch0:         bootstrap-autoload.patch
# Upstream patch for PHP 7+
Patch1:         %{name}-upstream.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php-composer(phpunit/phpunit)
# composer.json
#      "php": ">=5.3.2"
BuildRequires:  php(language) >= 5.3.2
# From phpcompatinfo report for 1.2.2
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for 1.2.2
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(hamcrest/hamcrest-php) = %{version}


%description
Hamcrest is a matching library originally written for Java,
but subsequently ported to many other languages.

%{name} is the official PHP port of Hamcrest and essentially follows
a literal translation of the original Java API for Hamcrest,
with a few Exceptions, mostly down to PHP language barriers.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/Hamcrest/autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm
%patch1 -p1 -b .upstream
find . -name \*.upstream -exec rm {} \;

# Move to Library tree
mv hamcrest/Hamcrest.php hamcrest/Hamcrest/Hamcrest.php


%build
# Library autoloader
%{_bindir}/phpab \
    --template fedora \
    --output hamcrest/Hamcrest/autoload.php \
    hamcrest/Hamcrest

cat << 'EOF' | tee -a hamcrest/Hamcrest/autoload.php

// Functions
require __DIR__ . '/Hamcrest.php';
EOF

# Test suite autoloader
%{_bindir}/phpab \
    --output tests/autoload.php \
    --exclude '*Test.php' \
    tests


%install
mkdir -p          %{buildroot}%{_datadir}/php
cp -pr hamcrest/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
cd tests
ret=0
for cmd in php56 php70 php71 php; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc CHANGES.txt README.md TODO.txt
%doc composer.json
%{_datadir}/php/Hamcrest


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Remi Collet <remi@fedoraproject.org> - 1.2.2-4
- add upstream patch for PHP 7, fix FTBFS
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- initial package