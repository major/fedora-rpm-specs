# remirepo/fedora spec file for php-hamcrest2
#
# SPDX-FileCopyrightText:  Copyright 2015-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_owner     hamcrest
%global gh_project   hamcrest-php
%global ns_project   Hamcrest
%global major        3
%bcond_without       tests

Name:           php-hamcrest%{major}
Version:        3.0.0
Release:        1%{?dist}
Summary:        PHP port of Hamcrest Matchers

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot with tests
Source0:        %{name}-%{version}.tgz
Source1:        makesrc.sh

# Use generated autoloader instead of composer one
Patch0:         bootstrap-autoload.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json, require-dev:
#               "phpunit/php-file-iterator": "^1.4 || ^2.0 || ^3.0",
#               "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0 || ^8.0 || ^9.0",
#               "phpstan/phpstan": "^2.1",
#               "phpstan/phpstan-phpunit": "^2.0"
BuildRequires:  phpunit9
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-ctype
BuildRequires:  php-dom
%endif

# composer.json, require:
#               "php": "^7.4|^8.0",
#               "ext-ctype": "*",
#               "ext-dom": "*"
Requires:       php(language) >= 7.4
Requires:       php-ctype
Requires:       php-dom
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
%setup -q -n %{gh_project}-%{version}

%patch -P0 -p0 -b .rpm
find . -name \*.rpm -exec rm {} \; -print

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
for cmd in php php82 php83 php84 php85 php86; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE.txt
%doc CHANGES.txt README.md
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}


%changelog
* Tue Aug 25 2026 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-hamcrest3
- install in /usr/share/php/Hamcrest3

* Tue May  6 2025 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1
- raise dependency on PHP 7.4

* Wed Jan 22 2025 Remi Collet <remi@remirepo.net> - 2.0.1-12
- switch to phpunit9
- re-license spec file to CECILL-2.1

* Thu Jul  9 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- switch to phpunit7

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
