# remirepo/fedora spec file for php-phpunit-phpcpd
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global gh_commit    dfed51c1288790fc957c9433e2f49ab152e8a564
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcpd
%global php_home     %{_datadir}/php
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
# Packagist
%global pk_vendor    sebastian
%global pk_project   phpcpd
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCPD

Name:           php-phpunit-%{pk_project}
Version:        3.0.1
Release:        11%{?dist}
Summary:        Copy/Paste Detector (CPD) for PHP code

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Fix for RPM, use autoload
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language)  >= 5.6
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  php-composer(sebastian/finder-facade) <  2
BuildRequires:  php-composer(sebastian/finder-facade) >= 1.1
BuildRequires:  php-composer(sebastian/version)       <  3
BuildRequires:  php-composer(sebastian/version)       >= 1.0
%if 0%{?fedora} >= 26
BuildRequires:  php-composer(symfony/console)         <  5
%else
BuildRequires:  php-composer(symfony/console)         <  4
%endif
BuildRequires:  php-composer(symfony/console)         >= 2.7
BuildRequires:  php-composer(phpunit/php-timer)       <  2
BuildRequires:  php-composer(phpunit/php-timer)       >= 1.0.6
%endif

# From composer.json, requires
#        "php": "^5.6|^7.0",
#        "sebastian/finder-facade": "^1.1",
#        "sebastian/version": "^1.0|^2.0",
#        "symfony/console": "^2.7|^3.0|^4.0",
#        "phpunit/php-timer": "^1.0.6"
Requires:       php(language) >= 5.6
Requires:       php-composer(sebastian/finder-facade) <  2
Requires:       php-composer(sebastian/finder-facade) >= 1.1
Requires:       php-composer(sebastian/version)       <  3
Requires:       php-composer(sebastian/version)       >= 1.0
%if 0%{?fedora} >= 26
Requires:       php-composer(symfony/console)         <  5
%else
Requires:       php-composer(symfony/console)         <  4
%endif
Requires:       php-composer(symfony/console)         >= 2.8
Requires:       php-composer(phpunit/php-timer)       >= 1.0.6
# From phpcompatinfo report for version 3.0.0
Requires:       php-cli
Requires:       php-dom
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xml

Provides:       %{pk_project} = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
phpcpd is a Copy/Paste Detector (CPD) for PHP code.

The goal of phpcpd is not not to replace more sophisticated tools such as phpcs,
pdepend, or phpmd, but rather to provide an alternative to them when you just
need to get a quick overview of duplicated code in a project.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
phpab \
  --output   src/autoload.php \
  --template fedora \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/FinderFacade/autoload.php',
    '%{php_home}/%{ns_vendor}/Version/autoload.php',
    [
        '%{php_home}/Symfony4/Component/Console/autoload.php',
        '%{php_home}/Symfony3/Component/Console/autoload.php',
        '%{php_home}/Symfony/Component/Console/autoload.php',
    ],
    '%{php_home}/PHP/Timer/Autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 phpcpd %{buildroot}%{_bindir}/phpcpd


%check
%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

ret=0;
for cmd in php php56 php70 php71 php72; do
   if which $cmd; then
      $cmd %{_bindir}/phpunit --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/%{pk_project}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1
- allow Symfony 4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0
- raise dependency on PHP 5.6
- drop dependency on theseer/fdomdocument
- raise dependency on sebastian/version 2.0
- cleanup update from pear
- switch to fedora/autoloader

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- allow sebastian/version 2.0
- raise dependency on Symfony >= 2.7
- run test suite with both PHP 5 and 7 when available
- allow to run with PHP from SCL
- provide php-composer(sebastian/phpcpd)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- use composer dependencies
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May  4 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1
- sources from github
- run test suite during build
- drop dependency on php-ezc-ConsoleTools
- add dependency on php-symfony-console

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.4.1-2
- Add macro for EPEL

* Wed Apr 10 2013 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.4.1-1
- Upstream 1.4.1

* Wed Apr 10 2013 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.5-4
- Fix metadata location, FTBFS #914374

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.5-1
- Upstream 1.3.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.4-1
- Upstream 1.3.4

* Mon Nov 07 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.3-3
- Update dependencies

* Sun Nov 06 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.3-2
- Fix search and replace issue

* Sat Nov 05 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.3.3-1
- Upstream 1.3.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 17 2010 Christof Damian <christof@damian.net> - 1.3.2-1
- Upstream 1.3.2
- New requirement phpunit/PHP_Timer
- Increased requirement phpunit/File_Iterator to 1.2.2

* Wed Feb 10 2010 Christof Damian <christof@damian.net> 1.3.1-1
- Upstream 1.3.1
- Change define macros to global
- Use channel macro in postun
- Raise requirements

* Thu Jan 14 2010 Christof Damian <christof@damian.net> - 1.3.0-2
- Forgot tgz file

* Thu Jan 14 2010 Christof Damian <christof@damian.net> - 1.3.0-1
- Upstream 1.3.0
- Add php 5.2.0 dependency
- Raise pear require

* Fri Dec 18 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.2-2
- /usr/share/pear/PHPCPD wasn't owned

* Sat Dec 12 2009 Christof Damian <christof@damian.net> - 1.2.2-1
- Upstream 1.2.2

* Thu Oct 15 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.0-1
- Initial packaging
