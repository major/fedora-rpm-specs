# remirepo/fedora spec file for php-phpunit-dbunit4
#
# Copyright (c) 2010-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e77b469c3962b5a563f09a2a989f1c9bd38b8615
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   dbunit
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   dbunit
# Namespace
%global ns_vendor    PHPUnit7
%global ns_project   DbUnit
%global with_tests   0%{!?_without_tests:1}
%global ver_major    4
%global ver_minor    0
%global ver_patch    0
%global specrel      3

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        %{ver_major}.%{ver_minor}.%{ver_patch}
Release:        %{specrel}%{?dist}.10
Summary:        Extension for database interaction testing for PHPUnit 7

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-pdo
BuildRequires:  php-simplexml
BuildRequires:  phpunit7
%if 0%{?fedora} >= 27
BuildRequires:  (php-composer(symfony/yaml) >= 3.0 with php-composer(symfony/yaml) <  5)
%else
BuildRequires:  php-symfony4-yaml
%endif
%endif

# From composer.json
#        "php": "^7.1",
#        "phpunit/phpunit": "^7.0",
#        "symfony/yaml": "^3.0 || ^4.0",
#        "ext-pdo": "*",
#        "ext-simplexml": "*"
Requires:       php(language) >= 7.1
Requires:       php-pdo
Requires:       php-simplexml
Requires:       phpunit7
%if 0%{?fedora} >= 27
Requires:       (php-composer(symfony/yaml) >= 3.0 with php-composer(symfony/yaml) <  5)
%else
Requires:       php-symfony4-yaml
%endif
# From phpcompatinfo report for version 3.0.0
Requires:       php-reflection
Requires:       php-libxml
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Extension for database interaction testing for PHPUnit 7.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}



%build
: Generate library autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
foreach(['Symfony4', 'Symfony3'] as $sym) {
    if (is_dir("/usr/share/php/$sym/Component/Yaml")) {
        \Fedora\Autoloader\Autoload::addPsr4('Symfony\\Component\\Yaml', "/usr/share/php/$sym/Component/Yaml");
        break;
    }
}
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%if %{with_tests}
%check
: Generate tests autoloader
mkdir vendor
touch vendor/autoload.php

: Run tests
ret=0
for cmd in php php71 php72; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \
      %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 4.0.0-3
- provide php-composer(phpunit/dbunit)

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 4.0.0-2
- fix description

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- switch dependency from phpunit6 to phpunit7
- rename to php-phpunit-dbunit4
- move to /usr/share/php/PHPUnit7/DbUnit
- raise dependency on PHP 7.1

* Tue Jan 23 2018 Remi Collet <remi@remirepo.net> - 3.0.3-1
- Update to 3.0.3
- use range dependencies on F27+

* Tue Dec 19 2017 Remi Collet <remi@remirepo.net> - 3.0.2-3
- fix autoloader for symfony/yaml

* Mon Nov 20 2017 Remi Collet <remi@remirepo.net> - 3.0.2-2
- fix autoloader for Symfony 4

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 3.0.2-1
- Update to 3.0.2
- Allow Symfony 4
- ensure current version is used by test suite

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- rename to php-phpunit-dbunit3
- change dependency to phpunit6

* Sun Dec  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3
- switch to fedora/autoloader

* Tue Nov  3 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2 (no change)
- lower dependency on PHP version 5.4
- lower dependency on PHPUnit version 4

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1 (no change)

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP version 5.6
- raise dependency on PHPUnit version 5

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Fri Jun  5 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHPUnit 4.0
- disable test suite on EL-5

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2
- switch all dependencies to composer

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-4
- fix FTBFS, add BR php-pdo
- add composer provides
- add composer.json as doc

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

* Tue Mar 05 2013 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- Version 1.2.3 (stable) - API 1.2.0 (stable)

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Version 1.2.2 (stable) - API 1.2.0 (stable)

* Sat Oct  6 2012 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Version 1.2.1 (stable) - API 1.2.0 (stable)

* Thu Sep 20 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 (stable) - API 1.2.0 (stable)
- raise dependencies: php 5.3.3, PHPUnit 3.7.0,
  Yaml 2.1.0 (instead of YAML from symfony 1)

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


