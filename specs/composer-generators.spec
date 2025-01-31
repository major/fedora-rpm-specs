# remirepo/fedora spec file for composer-generators
#
# Copyright (c) 2024 Remi Collet
# License: GPL-2.0-or-later
# https://www.gnu.org/licenses/gpl-2.0.en.html
#
# Please, preserve the changelog entries
#

Name:           composer-generators
Version:        0.1.1
Release:        1%{?dist}
# Use same license than RPM
License:        GPL-2.0-or-later
URL:            https://git.remirepo.net/cgit/rpms/composer-generators.git/
Summary:        Tools for composer enabled applications packager

# Sources
Source0:        composer.prov
Source1:        composer.attr
# Documentation
Source10:       LICENSE
Source11:       NEWS

BuildArch:      noarch
BuildRequires:  php-cli

Requires:       php-cli


%description
This package provides RPM generators which are used for
getting provides from composer enabled applications.

* find main project name and provide it
* find bundled libraries and provide them


%prep
%setup -c -T
cp -a %{sources} .


%install
install -Dpm 755 composer.prov %{buildroot}%{_rpmconfigdir}/composer.prov
install -Dpm 644 composer.attr %{buildroot}%{_fileattrsdir}/composer.attr


%check
: Syntax check only
%{_bindir}/php -l %{buildroot}%{_rpmconfigdir}/composer.prov


%files
%license LICENSE
%doc NEWS
%{_rpmconfigdir}/composer.prov
%{_fileattrsdir}/composer.attr


%changelog
* Mon Dec 30 2024 Remi Collet <remi@remirepo.net> - 0.1.1-1
- version 0.1.1

* Fri Oct 11 2024 Remi Collet <remi@remirepo.net> - 0.1.0-1
- Initial package
