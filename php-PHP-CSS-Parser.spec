# spec file for php-PHP-CSS-Parser
#
# Copyright (c) 2013-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit  7642a0e1cabd81d95f91ebbea7d6de988c59edd3
%global gh_short   %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner   sabberworm
%global gh_project PHP-CSS-Parser

Name:           php-%{gh_project}
Summary:        A Parser for CSS Files
Version:        7.0.3
Release:        14%{?dist}
License:        MIT

URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}%{?gh_short:-%{gh_short}}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/phpab
# For tests
BuildRequires:  %{_bindir}/phpunit

# From phpcompatinfo for version 7.0.2
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-pcre

Provides:       php-composer(sabberworm/php-css-parser) = %{version}


%description
PHP CSS Parser: a Parser for CSS Files written in PHP.
Allows extraction of CSS files into a data structure, manipulation
of said structure and output as (optimized) CSS.

Autoloader: %{_datadir}/php/Sabberworm/CSS/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/Sabberworm/CSS/autoload.php \
             lib/Sabberworm/CSS


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr lib/Sabberworm %{buildroot}%{_datadir}/php/Sabberworm


%check
cd tests
%{_bindir}/phpunit --bootstrap bootstrap.php .

if which php70; then
   php70 %{_bindir}/phpunit --bootstrap bootstrap.php .
fi


%files
# LICENSE is in the README.md file
%doc *md
%{_datadir}/php/Sabberworm


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Remi Collet <remi@fedoraproject.org> - 7.0.3-1
- update to 7.0.3

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 7.0.2-2
- rebuild

* Tue Apr  5 2016 Remi Collet <remi@fedoraproject.org> - 7.0.2-1
- update to 7.0.2
- run test suite with both PHP 5 and 7 when available
- add an simple autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3.20141009giteb29754
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2.20141009giteb29754
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 Remi Collet <remi@fedoraproject.org> - 6.0.0-1.20141009giteb29754
- update to 6.0.0 + fix for PHP 5.3
- add provides php-composer(sabberworm/php-css-parser)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Remi Collet <remi@fedoraproject.org> - 5.1.2-1
- update to 5.1.2

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 5.1.1-2
- add upstream patch (required by Horde_Css_Parser)

* Mon Oct 28 2013 Remi Collet <remi@fedoraproject.org> - 5.1.1-1
- update to 5.1.1 (no change, only documentation)

* Sun Oct 27 2013 Remi Collet <remi@fedoraproject.org> - 5.1.0-1
- update to 5.1.0

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 5.0.8-1
- update to 5.0.8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Remi Collet <remi@fedoraproject.org> - 5.0.6-1
- update to 5.0.6

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 5.0.5-1
- Initial packaging
