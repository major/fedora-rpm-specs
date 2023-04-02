# remirepo/fedora spec file for php-phpunit-File-Iterator
#
# Copyright (c) 2009-2023 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global gh_commit    730b01bc3e867237eaac355e06a36b85dd93a8b4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-file-iterator
%global php_home     %{_datadir}/php
%global pear_name    File_Iterator
%global pear_channel pear.phpunit.de
# Circular dependency with phpunit
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}

Name:           php-phpunit-File-Iterator
Version:        1.4.5
Release:        13%{?dist}
Summary:        FilterIterator implementation that filters files based on a list of suffixes

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

Patch0:         %{gh_project}-php8.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
#        "php": ">=5.3.3"
Requires:       php(language) >= 5.3.3
# From phpcompatinfo report for 1.3.4
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/php-file-iterator) = %{version}

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
FilterIterator implementation that filters files based on a list of suffixes.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Restore PSR-0 tree
# see https://github.com/sebastianbergmann/php-file-iterator/issues/26
mkdir -p File/Iterator/
mv src/* File/Iterator/
mv       File/Iterator/Iterator.php File/Iterator.php

%patch0 -p1


%build
%{_bindir}/phpab \
   --template fedora \
   --output   File/Iterator/Autoload.php \
   File


%install
mkdir -p    %{buildroot}%{php_home}
cp -pr File %{buildroot}%{php_home}/File


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog.md README.md composer.json
%{php_home}/File


%changelog
* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.4.5-13
- minimal fix for PHP 8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 1.4.5-1
- Update to 1.4.5

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 1.4.3-1
- Update to 1.4.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2 (no change)
- switch to fedora/autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1 (only CS)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr  2 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- fix license handling

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-5
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-3
- cleanup pear registry

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-2
- get sources from github

* Sun Nov  3 2013 Christof Damian <christof@damian.net> - 1.3.4-1
- upstream 1.3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 1.3.3-3
- fix metadata location, FTBFS #914369

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Christof Damian <christof@damian.net> - 1.3.3-1
- upstream 1.3.3

* Sun Sep 23 2012 Christof Damian <christof@damian.net> - 1.3.2-1
- upstream 1.3.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Version 1.3.1 (stable) - API 1.3.0 (stable)
- unmacro current command
- remove pear version hack

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Christof Damian <christof@damian.net> - 1.3.0-1
- upstream 1.3.0

* Sat Mar  5 2011 Christof Damian <christof@damian.net> - 1.2.6-2
- fix pear requirement

* Fri Mar  4 2011 Christof Damian <christof@damian.net> - 1.2.6-1
- upstream 1.2.6

* Mon Feb 28 2011 Christof Damian <cdamian@robin.gotham.krass.com> - 1.2.4-1
- upstream 1.2.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 17 2010 Christof Damian <christof@damian.net> - 1.2.3-1
- upstream 1.2.3

* Thu Jul 22 2010 Christof Damian <christof@damian.net> - 1.2.2-2
- fix minimum pear requirement

* Thu Jul 22 2010 Christof Damian <christof@damian.net> - 1.2.2-1
- upstream 1.2.2, bugfix

* Sat May  8 2010 Christof Damian <christof@damian.net> - 1.2.1-1
- upstream 1.2.1

* Tue Feb  9 2010 Christof Damian <christof@damian.net> - 1.2.0-1
- upstream 1.2.0
- increased php-common requirements to 5.2.7
- increased php-pear requirement
- use global instead of define
- use channel macro in postun

* Thu Dec 17 2009 Christof Damian <christof@damian.net> 1.1.1-2
- version 1.1.1 lowered the php requirement

* Thu Dec 17 2009 Christof Damian <christof@damian.net> 1.1.1-1
- upstream 1.1.1

* Mon Nov 30 2009 Christof Damian <christof@damian.net> 1.1.0-4
- own pear directories

* Sat Nov 28 2009 Christof Damian <christof@damian.net> 1.1.0-3
- fixed php-pear buildrequire
- just require php-common

* Thu Nov 26 2009 Christof Damian <christof@damian.net> 1.1.0-2
- fix package.xml to work with older pear versions

* Wed Nov 25 2009 Christof Damian <christof@damian.net> 1.1.0-1
- Initial packaging
