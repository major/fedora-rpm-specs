# remirepo/fedora spec file for php-phpunit-DbUnit
#
# Copyright (c) 2010-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    5c35d74549c21ba55d0ea74ba89d191a51f8cf25
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   dbunit
%global php_home     %{_datadir}/php
%global pear_name    DbUnit
%global pear_channel pear.phpunit.de
%global with_tests   0%{!?_without_tests:1}

Name:           php-phpunit-DbUnit
Version:        2.0.3
Release:        14%{?dist}
Summary:        DbUnit port for PHP/PHPUnit

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Autoloader full path
Patch0:         %{gh_project}-2.0.0-autoload.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php-pdo
BuildRequires:  php-phpunit-PHPUnit
%endif

# From composer.json
#        "php": "^5.4 || ^7.0",
#        "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0",
#        "symfony/yaml": "^2.1 || ^3.0",
#        "ext-pdo": "*",
#        "ext-simplexml": "*"
Requires:       php(language) >= 5.4
Requires:       php-pdo
Requires:       php-simplexml
Requires:       php-phpunit-PHPUnit
Requires:       php-symfony4-yaml
# From phpcompatinfo report for version 1.3.0
Requires:       php-libxml
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/dbunit) = %{version}


%description
DbUnit port for PHP/PHPUnit.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
: Generate library autoloader
%{_bindir}/phpab \
   --output src/Extensions/Database/Autoload.php \
   src/Extensions/Database


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr src     %{buildroot}%{php_home}/PHPUnit

install -D -p -m 755 dbunit %{buildroot}%{_bindir}/dbunit


%if %{with_tests}
%check
: Generate tests autoloader
%{_bindir}/phpab --template fedora --output tests/bs.php tests

: Run tests - set include_path to ensure PHPUnit autoloader use it
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d include_path=.:%{buildroot}%{php_home}:%{php_home} \
      %{_bindir}/phpunit \
       --bootstrap tests/bs.php \
       --configuration ./build/phpunit.xml
  fi
done
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog.md
%doc samples
%doc composer.json
%{_bindir}/dbunit
%{php_home}/PHPUnit/Extensions/Database


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Remi Collet <remi@fedoraproject.org> - 1.2.4-11
- switch to Symfony 4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@fedoraproject.org> - 1.2.4-4
- use package name for dependencies

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3
- switch to fedora/autoloader

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2 (no change)
- raise dependency on PHP version 5.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1
- drop pear provides

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHPUnit 4.0
- fix license handling

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2
- switch all dependencies to composer

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-4
- fix FTBFS, add BR php-pdo
- add composer provides
- add composer.json as doc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-2
- sources from github
- run tests during build

* Tue Apr 01 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Fri Nov 01 2013 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- add requires: symfony2/Yaml

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- Version 1.2.3 (stable) - API 1.2.0 (stable)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Version 1.2.2 (stable) - API 1.2.0 (stable)
- modernize spec

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Version 1.2.1 (stable) - API 1.2.0 (stable)
- raise dependencies: php 5.3.3, PHPUnit 3.7.0,
  Yaml 2.1.0 (instead of YAML from symfony 1)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Version 1.1.2 (stable) - API 1.1.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Version 1.1.1 (stable) - API 1.1.0 (stable)

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)

* Fri Aug 19 2011 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Version 1.0.3 (stable) - API 1.0.0 (stable)

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.2-1
- Version 1.0.2 (stable) - API 1.0.0 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.1-2
- rebuild for doc in /usr/share/doc/pear

* Wed Feb 16 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.1-1
- Version 1.0.1 (stable) - API 1.0.0 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-2
- lower PEAR dependency to allow el6 build
- fix URL

* Sun Sep 26 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1
- initial generated spec + clean


