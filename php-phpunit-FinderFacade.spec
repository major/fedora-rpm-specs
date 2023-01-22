# remirepo/fedora spec file for php-phpunit-FinderFacade
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    167c45d131f7fc3d159f56f191a0a22228765e16
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   finder-facade
%global php_home     %{_datadir}/php
%global pear_name    FinderFacade
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpunit-FinderFacade
Version:        1.2.3
Release:        8%{?dist}
Summary:        Wrapper for Symfony Finder component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(theseer/fdomdocument) >= 1.6 with php-composer(theseer/fdomdocument) <  2)
BuildRequires:  (php-composer(symfony/finder) >= 2.3       with php-composer(symfony/finder) <  6)
%else
BuildRequires:  php-theseer-fDOMDocument
BuildRequires:  php-symfony-finder
%endif
%endif

# From composer.json "require": {
#        "php": "^7.1",
#        "theseer/fdomdocument": "^1.6",
#        "symfony/finder": "^2.3|^3.0|^4.0|^5.0"
Requires:       php(language) >= 7.1
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(theseer/fdomdocument) >= 1.6 with php-composer(theseer/fdomdocument) <  2)
Requires:       (php-composer(symfony/finder) >= 2.3       with php-composer(symfony/finder) <  6)
%else
Requires:       php-theseer-fDOMDocument
Requires:       php-symfony-finder
%endif
# From phpcompatinfo report for version 1.2.1
Requires:       php-ctype
# For our autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/finder-facade) = %{version}
# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


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
        '%{php_home}/Symfony3/Component/Finder/autoload.php',
        '%{php_home}/Symfony/Component/Finder/autoload.php',
    ],
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/FinderFacade


%if %{with_tests}
%check
php -r 'require "%{buildroot}%{php_home}/SebastianBergmann/FinderFacade/autoload.php";'

ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/FinderFacade/autoload.php \
      %{_bindir}/phpunit --verbose tests || ret=1
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
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/FinderFacade


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3 (no change)
- raise dependency on PHP 7.1
- raise dependency on theseer/fdomdocument 1.6
- allow symfony/finder v5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 1.2.2-5
- cleanup for EL-8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- use range dependencies on F27+

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 1.2.2-1
- Update to 1.2.2
- allow Symfony 4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May  9 2017 Remi Collet <remi@fedoraproject.org> - 1.2.1-3
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-3
- switch to $fedoraClassLoader autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- use $sfuloader

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- upgrade to 1.2.0
- raise dependency on symfony/finder 2.3
- generate autoloader (dropped upstream)
- fix license handling

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-6
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- sources from github
- run tests during build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sat Mar 23 2013 Remi Collet <remi@fedoraproject.org> - 1.0.6-3
- upstream patch for Finder 2.2.0 compatibility

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- Version 1.0.6 (stable) - API 1.0.1 (stable)
- modernize spec

* Thu Oct 11 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Version 1.0.5 (stable) - API 1.0.1 (stable)
- Initial packaging

