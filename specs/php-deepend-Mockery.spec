#
# Fedora spec file for php-deepend-Mockery
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    be9bf28d8e57d67883cba9fcadfcff8caab667f8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     padraic
%global gh_project   mockery

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

Name:           php-deepend-Mockery
Version:        0.9.11
Release:        16%{?dist}
Summary:        Mockery is a simple but flexible PHP mock object framework

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Autoloader
Source1:        %{gh_project}-autoload.php

# Use our autoloader
Patch0:         %{gh_project}-tests.patch

BuildArch:      noarch
%if %{with_tests}
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~4.0"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.0
BuildRequires:  php(language) >= 5.3.2
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(hamcrest/hamcrest-php) >= 1.1   with php-composer(hamcrest/hamcrest-php) < 2)
%else
BuildRequires:  php-composer(hamcrest/hamcrest-php) <  2
BuildRequires:  php-composer(hamcrest/hamcrest-php) >= 1.1
%endif
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.3.2",
#        "lib-pcre": ">=7.0",
#        "hamcrest/hamcrest-php": "~1.1"
Requires:       php(language) >= 5.3.2
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(hamcrest/hamcrest-php) >= 1.1   with php-composer(hamcrest/hamcrest-php) < 2)
%else
Requires:       php-composer(hamcrest/hamcrest-php) <  2
Requires:       php-composer(hamcrest/hamcrest-php) >= 1.1
%endif
# From phpcompatinfo report for version 0.9.7
Requires:       php-pcre
Requires:       php-spl
Requires:       php-reflection
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(mockery/mockery) = %{version}
Provides:       php-pear(pear.survivethedeepend.com/Mockery) = %{version}
Obsoletes:      php-channel-deepend <= 1.3


%description
Mockery is a simple but flexible PHP mock object framework for use in unit
testing. It is inspired by Ruby's flexmock and Java's Mockito, borrowing
elements from both of their APIs.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/Mockery/autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} library/Mockery/autoload.php

mv library/helpers.php library/Mockery/
sed -e 's:helpers.php:Mockery/helpers.php:' -i library/Mockery.php

%patch -P0 -p0 -b .rpm


%build
# Empty build section, most likely nothing required.


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp library/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
: Use installed tree and our autoloader
sed -e 's:@BUILD@:%{buildroot}/%{_datadir}/php:' -i tests/Bootstrap.php

: Run upstream test suite
ret=0
for cmd in php php70 php71 php72 php73; do
   if which $cmd; then
      $cmd %{_bindir}/phpunit --verbose || ret=1
   fi
done
exit $ret
%endif


%post
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
    pear.survivethedeepend.com/Mockery >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md docs
%doc composer.json
%{_datadir}/php/Mockery/
%{_datadir}/php/Mockery.php


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.11-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Shawn Iwinski <shawn@iwin.ski> - 0.9.11-4
- Disable tests by default
- Fix FTBFS (RHBZ #1799867)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Remi Collet <remi@remirepo.net> - 0.9.11-1
- update to 0.9.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 0.9.10-1
- update to 0.9.10

* Mon Sep 10 2018 Remi Collet <remi@remirepo.net> - 0.9.9-7
- use range dependencies
- ensure hamcrest v1 is used, fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 0.9.9-4
- add patches for PHP 7.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Remi Collet <remi@fedoraproject.org> - 0.9.9-2
- rebuild

* Tue Feb 28 2017 Remi Collet <remi@remirepo.net> - 0.9.9-1
- Update to 0.9.9

* Fri Feb 10 2017 Remi Collet <remi@remirepo.net> - 0.9.8-1
- Update to 0.9.8

* Fri Dec 23 2016 Remi Collet <remi@fedoraproject.org> - 0.9.7-1
- Update to 0.9.7

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6
- switch to fedora/autoloader

* Mon Jul 11 2016 Remi Collet <remi@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov  5 2015 Remi Collet <remi@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
- add autoloader using symfony/class-loader
- add dependency on hamcrest/hamcrest-php
- run test suite
- use github archive from commit reference
- add explicit spec license header

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-2
- fixed requires (Remi)
- add script which will delete older pear package if installed (Remi)
- fix provides/obsoletes (Remi)

* Tue Jul 15 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-1
- update to 0.9.1 (RHBZ #1119451)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Christof Damian <christof@damian.net> - 0.8.0-1
- upstream 0.8.0

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 0.7.2-4
- fix metadir location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Christof Damian <christof@damian.net> - 0.7.2-1
- upstream 0.7.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Christof Damian <christof@damian.net> - 0.6.3-2
- add license and readme file from github

* Fri May 28 2010 Christof Damian <christof@damian.net> - 0.6.0-1
- initial packaging
