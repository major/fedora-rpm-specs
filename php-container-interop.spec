#
# Fedora spec file for php-container-interop
#
# Copyright (c) 2016-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     container-interop
%global github_name      container-interop
%global github_version   1.2.0
%global github_commit    79cbf1341c22ec75643d841642dd5d6acd83bdb8

%global composer_vendor  container-interop
%global composer_project container-interop

# "psr/container": "~1.0"
%global psr_container_min_ver 1.0
%global psr_container_max_ver 2.0


%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-%{composer_project}
Version:   %{github_version}
Release:   16%{?github_release}%{?dist}
Summary:   Promoting the interoperability of container objects (DIC, SL, etc.)

Group:     Development/Libraries
License:   MIT
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch
# Tests
BuildRequires: php-cli
## composer.json
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) <  %{psr_container_max_ver})
## phpcompatinfo (computed from version 1.2.0)
BuildRequires: php(language) >= 5.3.0
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) <  %{psr_container_max_ver})
# phpcompatinfo (computed from version 1.2.0)
Requires:  php(language) >= 5.3.0
# Autoloader
Requires:  php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:  php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
container-interop tries to identify and standardize features in container
objects (service locators, dependency injection containers, etc.) to achieve
interopererability.

Through discussions and trials, we try to create a standard, made of common
interfaces but also recommendations.

If PHP projects that provide container implementations begin to adopt these
common standards, then PHP applications and projects that use containers can
depend on the common interfaces instead of specific implementations. This
facilitates a high-level of interoperability and flexibility that allows users
to consume any container implementation that can be adapted to these interfaces.

The work done in this project is not officially endorsed by the PHP-FIG [1],
but it is being worked on by members of PHP-FIG and other good developers. We
adhere to the spirit and ideals of PHP-FIG, and hope this project will pave the
way for one or more future PSRs.

Autoloader: %{phpdir}/Interop/Container/autoload.php

[1] http://www.php-fig.org/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/Interop/Container/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Interop\\Container\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Container/autoload.php',
));
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
: Test autoloader
php -r '
require "%{buildroot}%{phpdir}/Interop/Container/autoload.php";
exit (interface_exists("Interop\\Container\\ContainerInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%doc docs
%dir %{phpdir}/Interop
     %{phpdir}/Interop/Container


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Remi Collet <remi@remirepo.net> - 1.2.0-13
- use range dependencies

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 02 2017 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-3
- Add dependency version macros

* Sun Apr 02 2017 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-2
- Update autoloader for PHP < 5.4 (i.e. EPEL 6)

* Thu Mar 02 2017 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- add dependency on psr/container
- switch to fedora/autoloader
- add minimal autoloader check

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
