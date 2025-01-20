# remirepo/fedora spec file for php-theseer-fDOMDocument
#
# Copyright (c) 2013-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    5cddd4f9076a9a2b85c5135935bba2dcb3ed7574
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   fDOMDocument
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    fDOMDocument
%global pear_channel pear.netpirates.net

Name:           php-theseer-fDOMDocument
Version:        1.6.7
Release:        9%{?dist}
Summary:        An Extension to PHP standard DOM

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
# For test
%global phpunit %{_bindir}/phpunit8
BuildRequires:  %{phpunit}
BuildRequires:  php-dom
BuildRequires:  php-libxml
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, requires
#        "php": ">=5.3.3",
#        "ext-dom": "*",
#        "lib-libxml": "*"
Requires:       php(language) >= 5.3.3
Requires:       php-dom
Requires:       php-libxml
# From phpcompatinfo report for version 1.6.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(theseer/fdomdocument) = %{version}


%description
An Extension to PHP's standard DOM to add various convenience methods
and exceptions by default


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}


%check
ret=0
for cmd in "php %{phpunit}" php74 php80 php81; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit8} \
      --bootstrap %{buildroot}%{php_home}/%{gh_project}/autoload.php \
      --verbose || ret=1
  fi
done
exit $ret


%post
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{php_home}/%{gh_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.7-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Remi Collet <remi@remirepo.net> - 1.6.7-1
- update to 1.6.7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Remi Collet <remi@remirepo.net> - 1.6.6-11
- switch to phpunit8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 1.6.6-6
- cleanup for EL-8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul  2 2017 Remi Collet <remi@remirepo.net> - 1.6.6-1
- Update to 1.6.6

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 1.6.5-1
- Update to 1.6.5 (no change)
- drop patch merged upstream

* Fri Apr 14 2017 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2
- use phpunit6 when available
- add fix for PHP 7.2 and PHPUnit 6 from
  https://github.com/theseer/fDOMDocument/pull/29

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Wed Nov 26 2014 Remi Collet <remi@fedoraproject.org> - 1.6.0-2
- switch from pear to github sources

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0
- provide php-composer(theseer/fdomdocument)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Sat Dec 21 2013 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3 (stable)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Apr 28 2013 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Version 1.4.1 (stable) - API 1.4.0 (stable)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Version 1.3.2 (stable) - API 1.3.0 (stable)
- run test units

* Thu Oct 11 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Version 1.3.1 (stable) - API 1.3.0 (stable)
- Initial packaging

