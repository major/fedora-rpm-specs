#
# Fedora spec file for php-getid3
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    06c7482532ff2b3f9111b011d880ca6699c8542b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     JamesHeinrich
%global gh_project   getID3
%global pk_owner     james-heinrich
%global pk_project   getid3

Name:      php-%{pk_project}
Version:   1.9.23
Release:   5%{?dist}
Epoch:     1
License:   GPL-1.0-or-later OR LGPL-3.0-only OR MPL-2.0
Summary:   The PHP media file parser
URL:       https://www.getid3.org/
Source0:   %{name}-%{version}-%{gh_short}.tgz
Source1:   makesrc.sh

BuildArch: noarch
BuildRequires: php-fedora-autoloader-devel

# from composer.json
#        "php": ">=5.3.0"
Requires:  php(language) >= 5.3.0
# from phpcompatinfo for version 1.9.16
Requires:  php-simplexml
Requires:  php-ctype
Requires:  php-date
Requires:  php-exif
Requires:  php-filter
Requires:  php-gd
Requires:  php-iconv
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-xml
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Suggests: php-dba
Suggests: php-mysqli
Suggests: php-rar
Suggests: php-sqlite3
%endif
# Autoloader
Requires:  php-composer(fedora/autoloader)

Provides:  php-composer(%{pk_owner}/%{pk_project}) = %{version}


%description
getID3() is a PHP script that extracts useful information 
(such as ID3 tags, bitrate, playtime, etc.) from MP3s & 
other multimedia file formats (Ogg, WMA, WMV, ASF, WAV, AVI, 
AAC, VQF, FLAC, MusePack, Real, QuickTime, Monkey's Audio, MIDI and more).

Autoloader: %{_datadir}/php/getid3/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# From composer.json, "autoload": {
#        "classmap": ["getid3/"]
%{_bindir}/phpab --template fedora --output getid3/autoload.php getid3


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -a getid3 %{buildroot}%{_datadir}/php/


%check
php -r '
require "%{buildroot}%{_datadir}/php/getid3/autoload.php";
$ok = class_exists("getID3");
echo "Autoload: " . ($ok ? "Ok\n" : "fails\n");
echo "Version: " . getID3::VERSION . "\n";
$ok = ($ok && strpos(getID3::VERSION, "%{version}") !== false);
exit ($ok ? 0 : 1);
'


%files
%license licenses license.txt
%doc changelog.txt dependencies.txt readme.txt structure.txt demos
%doc composer.json
%{_datadir}/php/getid3


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Remi Collet <remi@remirepo.net> - 1.9.23-1
- update to 1.9.23
- fix license with SPDX ids

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 30 2022 Remi Collet <remi@remirepo.net> - 1.9.22-1
- update to 1.9.22

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Remi Collet <remi@remirepo.net> - 1.9.21-1
- update to 1.9.21

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Remi Collet <remi@remirepo.net> - 1.9.20-1
- update to 1.9.20

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Remi Collet <remi@remirepo.net> - 1.9.19-1
- update to 1.9.19

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 1.9.18-1
- update to 1.9.18
- use git snapshot for sources

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 1.9.17-1
- update to 1.9.17
- add weak dependencies on suggested extension

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.9.16-1
- update to 1.9.16

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Remi Collet <remi@remirepo.net> - 1.9.15-1
- Update to 1.9.15

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Remi Collet <remi@remirepo.net> - 1:1.9.14-1
- Update to 1.9.14
- handle all classes in autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Remi Collet <remi@fedoraproject.org> - 1:1.9.13-1
- update to 1.9.13
- use new URL http://www.getid3.org/
- use sources from github
- switch to fedora/autoloader
- add minimal check for autoloader

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 1:1.9.12-1
- update to 1.9.12
- add simple classmap autoloader #1319676

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Remi Collet <remi@fedoraproject.org> - 1:1.9.8-2
- fix minimal PHP version
- add explicit dependencies for all php extensions
- fix license handling
- provides php-composer(james-heinrich/getid3)

* Wed Aug 20 2014 Adam Williamson <awilliam@redhat.com> - 1:1.9.8-1
- new release 1.9.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 08 2013 Roma <roma@lcg.ufrj.br> - 1:1.9.7-1
- Updated to 1.9.7
- Changed license to LGPLv3+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Paulo Roma <roma@lcg.ufrj.br> - 1:1.9.3-1
- Downgraded to latest stable version.
- Got needed extensions by using:
  phpci print --recursive --report extension /usr/share/php/getid3/
- Added BR php-gd.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0b5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0b5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Fri Jul 31 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0.0b5-2
- Updated ampache patch.

* Thu Jun 04 2009 Paulo Roma <roma@lcg.ufrj.br> 2.0.0b5-1
- Updated to 2.0.0b5
- Patched with ampache fixes.

* Thu Jun 04 2009 Paulo Roma <roma@lcg.ufrj.br> 1.7.9-1
- Initial spec file.
