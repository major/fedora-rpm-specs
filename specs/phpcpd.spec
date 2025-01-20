# remirepo/fedora spec file for phpcpd
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without tests

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    f3683aa0db2e8e09287c2bb33a595b2873ea9176
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcpd
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    sebastian
%global pk_project   phpcpd
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCPD

Name:           %{pk_project}
Version:        6.0.3
Release:        12%{?dist}
Summary:        Copy/Paste Detector (CPD) for PHP code

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix for RPM, use autoload
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language)  >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  phpunit9
BuildRequires:  (php-composer(sebastian/cli-parser)      >= 1.0   with php-composer(sebastian/cli-parser)      < 2)
BuildRequires:  (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0   with php-composer(phpunit/php-file-iterator) < 4)
BuildRequires:  (php-composer(phpunit/php-timer)         >= 5.0   with php-composer(phpunit/php-timer)         < 6)
%endif

# From composer.json, requires
#        "php": ">=7.3",
#        "ext-dom": "*",
#        "sebastian/cli-parser": "^1.0",
#        "sebastian/version": "^3.0",
#        "phpunit/php-file-iterator": "^3.0",
#        "phpunit/php-timer": "^5.0"
Requires:       php(language) >= 7.3
Requires:       php-dom
Requires:       (php-composer(sebastian/cli-parser)      >= 1.0   with php-composer(sebastian/cli-parser)      < 2)
Requires:       (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
Requires:       (php-composer(phpunit/php-file-iterator) >= 3.0   with php-composer(phpunit/php-file-iterator) < 4)
Requires:       (php-composer(phpunit/php-timer)         >= 5.0   with php-composer(phpunit/php-timer)         < 6)
# From phpcompatinfo report for version 3.0.0
Requires:       php-cli
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xml

Obsoletes:      php-phpunit-%{pk_project} < 4
Provides:       php-phpunit-%{pk_project} = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
phpcpd is a Copy/Paste Detector (CPD) for PHP code.

The goal of phpcpd is not not to replace more sophisticated tools such as phpcs,
pdepend, or phpmd, but rather to provide an alternative to them when you just
need to get a quick overview of duplicated code in a project.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm


%build
phpab \
  --output   src/autoload.php \
  --template fedora \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/CliParser/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator3/autoload.php',
    '%{php_home}/%{ns_vendor}/Timer5/autoload.php',
    '%{php_home}/%{ns_vendor}/Version3/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 phpcpd %{buildroot}%{_bindir}/phpcpd


%check
%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

ret=0;
for cmd in php php73 php74 php80; do
   if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite skipped
%endif


%files
%license LICENSE
%doc README.md composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/%{pk_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 6.0.3-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Remi Collet <remi@remirepo.net> - 6.0.3-1
- update to 6.0.3

* Tue Aug 18 2020 Remi Collet <remi@remirepo.net> - 6.0.2-1
- update to 6.0.2
- add dependency on phpunit/php-file-iterator
- add dependency on sebastian/cli-parser
- raise dependency on phpunit/php-timer 5
- drop depency on sebastian/finder-facade
- drop depency on symfony/console
- sources from git snapshot
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2
- raise depency on phpunit/php-timer 3
- raise depency on sebastian/version 3
- raise depency on PHP 7.3
- raise depency on sebastian/finder-facade 2
- raise depency on symfony/console 4
- use phpunit8 for test suite

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 4.0.0-1
- Update to 4.0.0
- rename to phpcpd (and obsolete php-phpunit-phpcpd)
- raise dependency on PHP 7.1
- raise dependency on phpunit/php-timer 2.0
- use phpunit7 for test suite

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 3.0.1-2
- use range dependencies on F27+

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1
- allow Symfony 4

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0
- raise dependency on PHP 5.6
- drop dependency on theseer/fdomdocument
- raise dependency on sebastian/version 2.0
- cleanup update from pear
- switch to fedora/autoloader

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4  (no change)
- allow sebastian/version 2.0

* Sun Apr 17 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3
- raise dependency on Symfony >= 2.7
- run test suite with both PHP 5 and 7 when available
- allow to run with PHP from SCL
- provide php-composer(sebastian/phpcpd)

* Thu Mar 26 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- use composer dependencies
- fix license handling

* Sun May  4 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1
- sources from github
- run test suite during build

* Fri Nov 08 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- drop dependency on components.ez.no/ConsoleTools
- add dependency on pear.symfony.com/Console >= 2.2.0
- raise dependency on pear.phpunit.de/FinderFacade >= 1.1.0

* Tue Jul 30 2013 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Thu Apr 04 2013 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- new dependency on pear.phpunit.de/Version

* Thu Oct 11 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.4.0-1
- Update to 1.4.0
- use FinderFacade instead of File_Iterator
- raise dependecies: php >= 5.3.3, PHP_Timer >= 1.0.4

* Sat Nov 26 2011 Remi Collet <RPMS@FamilleCollet.com> - 1.3.5-1
- Update to 1.3.5

* Tue Nov 22 2011 Remi Collet <RPMS@FamilleCollet.com> - 1.3.4-1
- upstream 1.3.4, rebuild for remi repository

* Sun Nov 20 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.4-1
- upstream 1.3.4

* Mon Nov 07 2011 Remi Collet <RPMS@FamilleCollet.com> - 1.3.3-1
- upstream 1.3.3, rebuild for remi repository

* Sat Nov 05 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.3-1
- upstream 1.3.3

* Sun Oct 17 2010 Remi Collet <RPMS@FamilleCollet.com> - 1.3.2-1
- rebuild for remi repository

* Sun Oct 17 2010 Christof Damian <christof@damian.net> - 1.3.2-1
- upstream 1.3.2
- new requirement phpunit/PHP_Timer
- increased requirement phpunit/File_Iterator to 1.2.2

* Fri Feb 12 2010 Remi Collet <RPMS@FamilleCollet.com> - 1.3.1-1
- rebuild for remi repository

* Wed Feb 10 2010 Christof Damian <christof@damian.net> 1.3.1-1
- upstream 1.3.1
- change define macros to global
- use channel macro in postun
- raise requirements

* Sat Jan 16 2010 Remi Collet <RPMS@FamilleCollet.com> - 1.3.0-2
- rebuild for remi repository

* Thu Jan 14 2010 Christof Damian <christof@damian.net> - 1.3.0-2
- forgot tgz file

* Thu Jan 14 2010 Christof Damian <christof@damian.net> - 1.3.0-1
- upstream 1.3.0
- add php 5.2.0 dependency
- raise pear require

* Fri Dec 18 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.2-2
- /usr/share/pear/PHPCPD wasn't owned

* Fri Dec 18 2009 Remi Collet <RPMS@FamilleCollet.com> - 1.2.2-1
- rebuild for remi repository

* Sat Dec 12 2009 Christof Damian <christof@damian.net> - 1.2.2-1
- upstream 1.2.2

* Wed Nov 18 2009 Remi Collet <RPMS@FamilleCollet.com> - 1.2.0-1
- rebuild for remi repository

* Thu Oct 15 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.0-1
- Initial packaging
