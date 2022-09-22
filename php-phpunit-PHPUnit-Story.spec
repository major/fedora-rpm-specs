# spec file for php-phpunit-PHPUnit-Story
#
# Copyright (c) 2013-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    b8579ada6ede4fd2f4b49e8549a8a176606cae68
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit-story
%global php_home     %{_datadir}/php
%global pear_name    PHPUnit_Story
%global pear_channel pear.phpunit.de
# Circular dependency with phpunit
%global with_tests   0%{?_with_tests:1}

Name:           php-phpunit-PHPUnit-Story
Version:        1.0.2
Release:        20%{?dist}
Summary:        Story extension for PHPUnit to facilitate Behaviour-Driven Development

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
Requires:       php(language) >= 5.3.3
Requires:       php-spl
Requires:       php-phpunit-PHPUnit >= 3.6.0
Requires:       php-composer(fedora/autoloader)

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
# Composer
Provides:       php-composer(phpunit/phpunit-story) = %{version}


%description
Story extension for PHPUnit to facilitate Behaviour-Driven Development


%prep
%setup -q -n %{gh_project}-%{gh_commit}

rm PHPUnit/Extensions/Story/Autoload.php*


%build
%{_bindir}/phpab \
  --output   PHPUnit/Extensions/Story/Autoload.php \
  --template fedora \
  PHPUnit


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr PHPUnit %{buildroot}%{php_home}


%if %{with_tests}
%check
sed -e 's/by Sebastian Bergmann/by Sebastian Bergmann and contributors/' \
    -e 's/%sMb/%sMB/' \
    -e 's/\.\.\.\..*$/....%s/' \
    -i Tests/Functional/*phpt

: Run upstream test suite
%{_bindir}/php -d include_path=.:%{buildroot}%{_datadir}/php:%{_datadir}/php \
%{_bindir}/phpunit --verbose
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc ChangeLog.markdown LICENSE composer.json
%{php_home}/PHPUnit/Extensions/Story


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-8
- switch to fedora/autoloader
- provide php-composer(phpunit/phpunit-story)
- enable test suite

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-4
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-3
- sources from github
- run test suite when build --with tests

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (no change)

* Thu Mar 28 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
