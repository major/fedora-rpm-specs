# remirepo/fedora spec file for php-hamcrest
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    8c3d0a3f6af734494ad8f6fbbee0ba92422859f3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     hamcrest
%global gh_project   hamcrest-php
%global ns_project   Hamcrest
%global major        2
%bcond_without       tests

Name:           php-hamcrest2
Version:        2.0.1
Release:        13%{?dist}
Summary:        PHP port of Hamcrest Matchers

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Use generated autoloader instead of composer one
Patch0:         bootstrap-autoload.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json, require-dev:
#               "phpunit/php-file-iterator": "^1.4 || ^2.0",
#               "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0"
BuildRequires:  phpunit7
# composer.json, require:
#      "php": "^5.3|^7.0|^8.0"
BuildRequires:  php(language) >= 5.3
# From phpcompatinfo report for 2.0.0
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

Requires:       php(language) >= 5.3
# From phpcompatinfo report for 2.0.0
Requires:       php-ctype
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

Autoloader: %{_datadir}/php/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find . -name \*.rpm -exec rm {} \;

# Move to Library tree
mv hamcrest/%{ns_project}.php hamcrest/%{ns_project}/%{ns_project}.php


%build
# Library autoloader
%{_bindir}/phpab \
    --template fedora \
    --output hamcrest/%{ns_project}/autoload.php \
    hamcrest/%{ns_project}

# Test suite autoloader
%{_bindir}/phpab \
    --output tests/autoload.php \
    --exclude '*Test.php' \
    tests generator


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr hamcrest/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_project}%{major}


%check
%if %{with tests}
cd tests
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc CHANGES.txt README.md
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.1-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  9 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- Update to 2.0.0
- rename to php-hamcrest2

* Fri Feb 17 2017 Remi Collet <remi@fedoraproject.org> - 1.2.2-4
- add upstream patch for PHP 7, fix FTBFS
- switch to fedora/autoloader

* Thu Oct 15 2015 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- initial package
