#
# Fedora spec file for php-webflow-drupal-finder
#
# Copyright (c) 2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     webflo
%global github_name      drupal-finder
%global github_version   1.2.0
%global github_commit    123e248e14ee8dd3fbe89fb5a733a6cf91f5820e

%global composer_vendor  webflo
%global composer_project drupal-finder

# mikey179/vfsstream: ^1.6
%global mikey179_vfsstream_min_ver 1.6
%global mikey179_vfsstream_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       Provides a class to locate a Drupal installation in a given path

License:       GPLv2+
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Add license file
# https://github.com/webflo/drupal-finder/pull/50
# https://github.com/webflo/drupal-finder/pull/50.patch
Patch0:        %{name}-pr50.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php-json
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(mikey179/vfsstream) >= %{mikey179_vfsstream_min_ver} with php-composer(mikey179/vfsstream) < %{mikey179_vfsstream_max_ver})
%else
BuildRequires: php-composer(mikey179/vfsstream) >= %{mikey179_vfsstream_min_ver}
BuildRequires: php-composer(mikey179/vfsstream) <  %{mikey179_vfsstream_max_ver}
%endif
## phpcompatinfo for version 1.2.0
BuildRequires: php(language) >= 5.4.0
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php-json
# phpcompatinfo for version 1.2.0
Requires:      php(language) >= 5.4.0
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/DrupalFinder/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

# Add license file
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('DrupalFinder\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/DrupalFinder


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/DrupalFinder/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('DrupalFinder\\Tests\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/org/bovigo/vfs/autoload.php',
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55 php56} php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
%{phpdir}/DrupalFinder


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Initial package
