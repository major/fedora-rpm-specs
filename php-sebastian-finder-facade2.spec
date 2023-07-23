# remirepo/fedora spec file for php-sebastian-finder-facade2
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9d3e74b845a2ce50e19b25b5f0c2718e153bee6c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   finder-facade
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   FinderFacade
%global major        2
%global php_home     %{_datadir}/php
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.0
Release:        8%{?dist}
Summary:        Wrapper for Symfony Finder component version %{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-ctype
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  phpunit9
BuildRequires:  (php-composer(theseer/fdomdocument) >= 1.6 with php-composer(theseer/fdomdocument) < 2)
BuildRequires:  (php-composer(symfony/finder)       >= 4.1 with php-composer(symfony/finder)       < 6)
%endif

# From composer.json "require": {
#        "php": "^7.3",
#        "ext-ctype": "*",
#        "theseer/fdomdocument": "^1.6",
#        "symfony/finder": "^4.1|^5.0"
Requires:       php(language) >= 7.3
Requires:       php-ctype
Requires:       (php-composer(theseer/fdomdocument) >= 1.6 with php-composer(theseer/fdomdocument) < 2)
Requires:       (php-composer(symfony/finder)       >= 4.1 with php-composer(symfony/finder)       < 6)
# From phpcompatinfo report for version 2.0.0
# none
# For our autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/finder-facade) = %{version}


%description
Convenience wrapper for Symfony's Finder component.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab \
  --output   src/autoload.php \
  --template fedora \
  src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/TheSeer/fDOMDocument/autoload.php',
    [
        '%{php_home}/Symfony5/Component/Finder/autoload.php',
        '%{php_home}/Symfony4/Component/Finder/autoload.php',
    ],
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with_tests}
%check
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
exit (class_exists("%{ns_vendor}\\%{ns_project}\\%{ns_project}") ? 0 : 1);
'

mkdir vendor
touch vendor/autoload.php

ret=0
for cmd in php php73 php74; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9 --verbose tests || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.3
- raise dependency on Symfony 4.1
- rename to php-sebastian-finder-facade2
- move to /usr/share/php/SebastianBergmann/FinderFacade2

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3 (no change)
- raise dependency on PHP 7.1
- raise dependency on theseer/fdomdocument 1.6
- allow symfony/finder v5

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 1.2.2-5
- cleanup for EL-8

* Tue Feb  6 2018 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- use range dependencies on F27+

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 1.2.2-1
- Update to 1.2.2
- allow Symfony 4

* Tue May  9 2017 Remi Collet <remi@fedoraproject.org> - 1.2.1-3
- switch to fedora/autoloader

* Wed Feb 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- run test suite with both PHP 5 and 7 when available

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-3
- switch to $fedoraClassLoader autoloader

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- use $sfuloader

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- upgrade to 1.2.0
- raise dependency on symfony/finder 2.3
- generate autoloader (dropped upstream)
- fix license handling

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-6
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- sources from github
- run tests during build

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Mon May 27 2013 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (no change)

* Wed Mar  6 2013 Remi Collet <remi@fedoraproject.org> - 1.0.6-2
- upstream patch for Finder 2.2.0 compatibility

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- Version 1.0.6 (stable) - API 1.0.1 (stable)

* Thu Oct 11 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Version 1.0.5 (stable) - API 1.0.1 (stable)
- Initial packaging
