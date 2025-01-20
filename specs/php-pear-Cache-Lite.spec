# Spec file for php-pear-Cache-Lite
#
# Copyright (c) 2008-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global pear_name    Cache_Lite
%global gh_commit    fc7c6703cfbddc55c80c5ae3926dcc80c1d993f9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     pear
%global gh_project   Cache_Lite

Summary:        Fast and Safe little cache system for PHP
Name:           php-pear-Cache-Lite
Version:        2.0.0
Release:        5%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language)  >= 7.4
BuildRequires:  php-date
BuildRequires:  php-autoloader(pear/pear-core-minimal) >= 1.10
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json  "require-dev": {
#        "phpunit/phpunit": "^9"
BuildRequires:  phpunit9
%endif

# from composer.json "require": {
#        "php": ">=7.4.0",
#        "pear/pear-core-minimal": "^1.10"
Requires:       php(language)  >= 7.4
Requires:       php-autoloader(pear/pear-core-minimal) >= 1.10
Requires:       php-date

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/cache_lite) = %{version}


%description
This package is a little cache system optimized for file containers. It is
fast and safe (because it uses file locking and/or anti-corruption tests).


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
phpab --template fedora --output Cache/Lite/autoload.php Cache
cat << 'EOF' | tee -a Cache/Lite/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{pear_phpdir}/PEAR/autoload.php',
]);
EOF


%install
mkdir -p     %{buildroot}%{pear_phpdir}/
cp -pr Cache %{buildroot}%{pear_phpdir}/Cache


%if %{with tests}
%check
mkdir vendor
ln -s %{buildroot}%{pear_phpdir}/Cache/Lite/autoload.php vendor/autoload.php

: Upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
%endif


%post
# no more from pear channel
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null || :
fi


%files
%license LICENSE
%doc composer.json
%doc docs
%doc *.md
%{pear_phpdir}/Cache


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Mar 21 2023 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- sources from github instead or pear channel

* Mon Feb 20 2023 Remi Collet <remi@remirepo.net> - 1.8.3-9
- fix PHP 8.2 deprecations in test suite
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3
- drop patch merged upstream

* Tue Nov 19 2019 Remi Collet <remi@remirepo.net> - 1.8.2-5
- add patch for PHP 7.4 from
  https://github.com/pear/Cache_Lite/pull/11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.8.2-1
- update to 1.8.2

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.8.0-4
- add patch for PHP 7.2 from https://github.com/pear/Cache_Lite/pull/7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Remi Collet <remi@fedoraproject.org> - 1.8.0-1
- update to 1.8.0
- raise dependency on PHP >= 5.4
- raise dependency on PEAR >= 1.10.1

* Tue Jun 28 2016 Remi Collet <remi@fedoraproject.org> - 1.7.16-5
- add patch to avoid PHP 7 warning

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Remi Collet <remi@fedoraproject.org> - 1.7.16-1
- update to 1.7.16 (stable)
- add patch to avoid deprecated warning

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.7.15-4
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.7.15-3
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Remi Collet <remi@fedoraproject.org> - 1.7.14-1
- Version 1.7.15 (stable) - API 1.7.7 (stable)
- fix https://pear.php.net/bugs/19433 corrupted archive
- fix https://pear.php.net/bugs/19434 bad file role

* Wed May 23 2012 Remi Collet <remi@fedoraproject.org> - 1.7.14-1
- Version 1.7.14 (stable) - API 1.7.7 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.12-1
- Version 1.7.12 (stable) - API 1.7.7 (stable)

* Tue May 31 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.11-1
- Version 1.7.11 (stable) - API 1.7.7 (stable)
- Updated LICENSE file

* Mon May 30 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.10-1
- Version 1.7.10 (stable) - API 1.7.7 (stable)
- TOFIX: LICENSE file provided is outdated
  http://pear.php.net/bugs/18571

* Wed Apr 06 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.9-2
- doc in /usr/share/doc/pear

* Wed Mar 02 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.9-1
- Version 1.7.9 (stable) - API 1.7.7 (stable)
- define timezone during build
- run test suite during %%check

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 08 2010 Remi Collet <Fedora@FamilleCollet.com> 1.7.8-3
- spec cleanup
- rename Cache_Lite.xml to php-pear-Cache-Lite.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Remi Collet <Fedora@FamilleCollet.com> 1.7.8-1
- update to 1.7.8 (bugfix)

* Sun Mar 08 2009 Remi Collet <Fedora@FamilleCollet.com> 1.7.7-1
- update to 1.7.7 (bugfix)

* Thu Jan 29 2009 Remi Collet <Fedora@FamilleCollet.com> 1.7.6-1
- now Requires php-pear(PEAR) >= 1.5.4

* Fri Jan 09 2009 Remi Collet <Fedora@FamilleCollet.com> 1.7.5-1
- update to 1.7.5

* Mon Jun 09 2008 Remi Collet <Fedora@FamilleCollet.com> 1.7.4-1
- update to 1.7.4

* Tue Apr 15 2008 Remi Collet <Fedora@FamilleCollet.com> 1.7.3-1
- initial RPM

