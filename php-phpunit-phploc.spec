# remirepo/fedora spec file for php-phpunit-phploc
#
# Copyright (c) 2009-2020 Guillaume Kulakowski, Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without tests

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    af0d5fc84f3f7725513ba59cdcbe670ac2a4532a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phploc
%global php_home     %{_datadir}/php
%global pear_name    phploc
%global pear_channel pear.phpunit.de
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPLOC

Name:           php-phpunit-phploc
Version:        7.0.2
Release:        5%{?dist}
Summary:        A tool for quickly measuring the size of a PHP project

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix for RPM, use autoload
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  (php-composer(sebastian/cli-parser)      >= 1.0   with php-composer(sebastian/cli-parser)      < 2)
BuildRequires:  (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0   with php-composer(phpunit/php-file-iterator) < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires: %{phpunit}
%endif

# From composer.json, "require": {
#        "php": ">=7.3",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "sebastian/finder-facade": "^2.0",
#        "sebastian/version": "^3.0",
#        "symfony/console": "^4.0 || ^5.0"
Requires:       php(language) >= 7.3
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       (php-composer(sebastian/cli-parser)      >= 1.0   with php-composer(sebastian/cli-parser)      < 2)
Requires:       (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
Requires:       (php-composer(phpunit/php-file-iterator) >= 3.0   with php-composer(phpunit/php-file-iterator) < 4)
# From phpcompatinfo report for version 7.0.0
Requires:       php-spl
Requires:       php-tokenizer
# For our autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phploc/phploc) = %{version}
# For compat
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       phploc = %{version}


%description
phploc is a tool for quickly measuring the size of a PHP project.

The goal of phploc is not not to replace more sophisticated tools such as phpcs,
pdepend, or phpmd, but rather to provide an alternative to them when you just
need to get a quick understanding of a project's size.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
%{_bindir}/phpab \
  --output   src/autoload.php \
  --template fedora \
  src

cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/CliParser/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator3/autoload.php',
    '%{php_home}/%{ns_vendor}/Version3/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 phploc %{buildroot}%{_bindir}/phploc


%if %{with tests}
%check
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

ret=0
for cmd in "php %{phpunit}" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} \
      --verbose || ret=1
  fi
done
exit $ret
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/phploc


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Remi Collet <remi@remirepo.net> - 7.0.2-1
- update to 7.0.2

* Tue Aug 18 2020 Remi Collet <remi@remirepo.net> - 7.0.1-1
- update to 7.0.1
- sources from git snapshot
- add dependency on sebastian/cli-parser
- add dependency on phpunit/php-file-iterator
- drop depency on sebastian/finder-facade
- drop depency on symfony/console

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Remi Collet <remi@remirepo.net> - 6.0.2-1
- update to 6.0.2
- raise depency on PHP 7.3
- raise depency on sebastian/finder-facade 2
- raise depency on sebastian/version 3
- allow symfony 5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- raise dependency on PHP 7.2
- add dependency on php-json
- only allow Symfony 4
- use phpunit8 for upstream test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 4.0.1-4
- add patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 4.0.1-2
- use range dependencies on F27+
- undefine __brp_mangle_shebangs

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 4.0.1-1
- Update to 4.0.1
- allow Symfony 4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun  7 2017 Remi Collet <remi@remirepo.net> - 4.0.0-1
- Update to 4.0.0
- use phpunit6 when available
- drop dependency on sebastian/git
- raise dependency on sebastian/version 2.0

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 3.0.1-3
- switch to fedora/autoloader
- use Symfony 3 when available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 26 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1
- raise dependency on sebastian/git >= 2.1

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-2
- update to 3.0.0
- raise minimal php version to 5.6
- raise dependency on PHPUnit ~5
- allow symfony 3
- allow sebastian/version 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- update to 2.1.5
- simplify autoloader

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- update to 2.1.4

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-3
- switch to $fedoraClassLoader autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- update to 2.1.3
- improve autoloader
- lower minimal PHP version to 5.3.3
- fix license handling

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- update to 2.1.2
- ensure compatibility with SCL

* Mon Apr 13 2015 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- update to 2.1.1

* Wed Mar 11 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- raise dependencies on sebastian/git 2.0, symfony/console 2.5
- raise minimal PHP version to 5.4

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- update to 2.0.6
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- update to 2.0.5
- sources from github
- run test suite during build
- add dependencies on php-symfony-console php-phpunit-git php-phpunit-Version
- drop dependency on php-ezc-Console

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Christof Damian <christof@damian.net> - 1.7.4-1
- upstream 1.7.4
- use metadir, fixes FTBFS #914376

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.6.4-1
- upstream 1.6.4

* Tue Nov  1 2011 Christof Damian <christof@damian.net> - 1.6.2-1
- upstream 1.6.2

* Fri Feb 18 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.6.1-2
- Change pearinstaller version for RHEL6

* Sat Feb 12 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.6.1-1
- upstream 1.6.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Christof Damian <christof@damian.net> 1.5.1-1
- upstream 1.5.1
- changed requirements
- replaced define macros with global

* Thu Jan 14 2010 Christof Damian <christof@damian.net> - 1.5.0-2
- add php 5.2.0 dependency
- remove hack to lower pear requirement

* Sun Jan  3 2010 Christof Damian <christof@damian.net> - 1.5.0-1
- upstream 1.5.0

* Fri Dec 18 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.4.0-2
- /usr/share/pear/PHPLOC wasn't owned

* Sat Dec 12 2009 Christof Damian <christof@damian.net> - 1.4.0-1
- upstream 1.4.0

* Sat Nov 7 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.0-2
- F-(10|11) compatibility

* Tue Oct 13 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.2.0-1
- Initial packaging
