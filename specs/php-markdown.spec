# Fedora spec file for php-markdown
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    5024d623c1a057dcd2d076d25b7d270a1d0d55f3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     michelf
%global gh_project   php-markdown

Name:        php-markdown
Version:     2.0.0
Release:     5%{?dist}
Summary:     Markdown implementation in PHP

License:     BSD-3-Clause
URL:         https://michelf.ca/projects/php-markdown/
Source0:     https://github.com/michelf/php-markdown/archive/%{version}/%{name}-%{version}.tar.gz
Source1:     makesrc.sh

BuildArch:   noarch
BuildRequires: php-fedora-autoloader-devel
# For tests
#       "require-dev": {
#               "phpunit/phpunit": ">=4.3 <5.8"
BuildRequires: phpunit10

Requires:    php(language) >= 7.4
Requires:    php-pcre
Requires:    php-composer(fedora/autoloader)

Provides:    php-composer(michelf/php-markdown) = %{version}


%description
This is a PHP implementation of John Gruber's Markdown.
It is almost completely compliant with the reference implementation.

This packages provides the classic version %{classic_version} and the new
library version %{version}.

Autoloader: %{_datadir}/php/Michelf/markdown-autoload.php


%prep
%setup -q
mv License.md LICENSE


%build
: Generate simple autoloader
%{_bindir}/phpab \
    --template fedora \
    --output Michelf/markdown-autoload.php \
    Michelf
cat Michelf/markdown-autoload.php


%install
install -d %{buildroot}%{_datadir}/php/

# PSR-0 library
cp -pr Michelf %{buildroot}%{_datadir}/php/Michelf


%check
php -r '
require_once "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
  $ver = Michelf\Markdown::MARKDOWNLIB_VERSION;
  echo "Version=$ver, expected=%{version}\n";
  return (version_compare($ver, "%{version}", "=") ? 0 : 1);
'
cat << 'EOF' | tee bs.php
<?php
require "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
require "test/bootstrap.php";
EOF

ret=0
for php in php php74 php81 php82 php83
do
  if which $php
  then
    $php %{_bindir}/phpunit10 --bootstrap bs.php || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
# Library version
%{_datadir}/php/Michelf


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Sérgio Basto <sergio@serjux.com> - 2.0.0-1
- Update php-markdown to 2.0.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.9.1-5
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0
- run upstream test suite

* Fri Jul 26 2019 Remi Collet <remi@remirepo.net> - 1.8.0-6
- drop old classic version
- use git snapshot as next version will have test suite
- add patch for PHP 7.4, adapted for 1.8.0 from
  https://github.com/michelf/php-markdown/pull/316

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- Mardown PSR-0/PSR-4 library version 1.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- Mardown PSR-0 library version 1.7.0
- switch to fedora/autoloader
- add minimal %%check for version and autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Mardown PSR-0 library version 1.6.0
- add simple autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- Mardown PSR-0 library version 1.5.0
- fix license handling
- add provides php-composer(michelf/php-markdown)
- fix project URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Mardown PSR-0 library version 1.4.1

* Mon Dec 02 2013 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Mardown PSR-0 library version 1.4.0 (sources 1.2.8)
- Mardown classic library version 1.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Remi Collet <remi@fedoraproject.org> - 1.2.7-1
- Mardown PSR-0 library version 1.2.7 (added)
- Mardown classic library version 1.0.1q (updated)

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1p-1
- Updated to 1.0.1p
- don't requires php

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.irg> 1.0.1n-1
- Updated to 1.0.1n

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1m-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.irg> 1.0.1m-2
- Fixed mixed use of space and tabs, using install in place of cp

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.1m-1
- Initial package
