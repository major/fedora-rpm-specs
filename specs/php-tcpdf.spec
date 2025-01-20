# remirepo/Fedora spec file for php-tcpdf
#
# SPDX-FileCopyrightText:  Copyright 2013-2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
# see https://github.com/tecnickcom/TCPDF/releases
%global gh_commit    14ffa0e308f5634aa2489568b4b90b24073b6731
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     tecnickcom
%global gh_date      2024-12-23
%global gh_project   TCPDF
%global real_name    tcpdf

Name:           php-tcpdf
Summary:        PHP class for generating PDF documents and barcodes
Version:        6.8.0
Release:        2%{?dist}

URL:            http://www.tcpdf.org
License:        LGPL-3.0-or-later

Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz
# Disable opcache cahing for font metadata which may consume up to 90MB
Source1:        %{name}.blacklist

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel

Requires:       php(language) >= 7.1
Requires:       php-curl
# From phpcompatinfo report form version 6.3.0
Requires:       php-bcmath
Requires:       php-date
Requires:       php-gd
Requires:       php-hash
Requires:       php-json
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-posix
Requires:       php-tidy
Requires:       php-xml
Requires:       php-zlib
# mcrypt is optionnal and openssl is preferred
# imagick is optionnal (and conflicts with gmagick)
Recommends:     php-imagick
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Old name for compatibility
Provides:       php-composer(tecnick.com/tcpdf) = %{version}
# New name
Provides:       php-composer(tecnickcom/tcpdf)  = %{version}


%description
PHP class for generating PDF documents.

* no external libraries are required for the basic functions;
* all standard page formats, custom page formats, custom margins and units
  of measure;
* UTF-8 Unicode and Right-To-Left languages;
* TrueTypeUnicode, OpenTypeUnicode, TrueType, OpenType, Type1 and CID-0 fonts;
* font subsetting;
* methods to publish some XHTML + CSS code, Javascript and Forms;
* images, graphic (geometric figures) and transformation methods;
* supports JPEG, PNG and SVG images natively, all images supported by GD
  (GD, GD2, GD2PART, GIF, JPEG, PNG, BMP, XBM, XPM) and all images supported
  via ImagMagick (http: www.imagemagick.org/www/formats.html)
* 1D and 2D barcodes: CODE 39, ANSI MH10.8M-1983, USD-3, 3 of 9, CODE 93,
  USS-93, Standard 2 of 5, Interleaved 2 of 5, CODE 128 A/B/C, 2 and 5 Digits
  UPC-Based Extention, EAN 8, EAN 13, UPC-A, UPC-E, MSI, POSTNET, PLANET,
  RMS4CC (Royal Mail 4-state Customer Code), CBC (Customer Bar Code),
  KIX (Klant index - Customer index), Intelligent Mail Barcode, Onecode,
  USPS-B-3200, CODABAR, CODE 11, PHARMACODE, PHARMACODE TWO-TRACKS,
  Datamatrix ECC200, QR-Code, PDF417;
* ICC Color Profiles, Grayscale, RGB, CMYK, Spot Colors and Transparencies;
* automatic page header and footer management;
* document encryption up to 256 bit and digital signature certifications;
* transactions to UNDO commands;
* PDF annotations, including links, text and file attachments;
* text rendering modes (fill, stroke and clipping);
* multiple columns mode;
* no-write page regions;
* bookmarks and table of content;
* text hyphenation;
* text stretching and spacing (tracking/kerning);
* automatic page break, line break and text alignments including justification;
* automatic page numbering and page groups;
* move and delete pages;
* page compression (requires php-zlib extension);
* XOBject templates;
* PDF/A-1b (ISO 19005-1:2005) support.

By default, TCPDF uses the GD library which is know as slower than ImageMagick
solution. You can optionally install php-pecl-imagick; TCPDF will use it.


%package dejavu-lgc-sans-fonts
Summary:        DejaVu LGC sans-serif fonts for tcpdf
BuildRequires:  dejavu-lgc-sans-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-sans-fonts

%description dejavu-lgc-sans-fonts
This package allow to use system DejaVu LGC sans-serif variable-width
font faces in TCPDF.

%package dejavu-lgc-sans-mono-fonts
Summary:        DejaVu LGC mono-spaced fonts for tcpdf
BuildRequires:  dejavu-lgc-sans-mono-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-sans-mono-fonts

%description dejavu-lgc-sans-mono-fonts
This package allow to use system DejaVu LGC sans-serif mono-spaced
font faces in TCPDF.

%package dejavu-lgc-serif-fonts
Summary:        DejaVu LGC serif fonts for tcpdf
BuildRequires:  dejavu-lgc-serif-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-serif-fonts

%description dejavu-lgc-serif-fonts
This package allow to use system DejaVu LGC serif variable-width
font faces in TCPDF.

%package dejavu-sans-fonts
Summary:        DejaVu sans-serif fonts for tcpdf
BuildRequires:  dejavu-sans-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-sans-fonts

%description dejavu-sans-fonts
This package allow to use system DejaVu sans-serif variable-width
font faces in TCPDF.

%package dejavu-sans-mono-fonts
Summary:        DejaVu mono-spaced fonts for tcpdf
BuildRequires:  dejavu-sans-mono-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-sans-mono-fonts

%description dejavu-sans-mono-fonts
This package allow to use system DejaVu sans-serif mono-spaced
font faces in TCPDF.

%package dejavu-serif-fonts
Summary:        DejaVu serif fonts for tcpdf
BuildRequires:  dejavu-serif-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-serif-fonts

%description dejavu-serif-fonts
This package allow to use system DejaVu serif variable-width
font faces in TCPDF.

%package gnu-free-mono-fonts
Summary:        GNU FreeFonts mono-spaced for tcpdf
BuildRequires:  gnu-free-mono-fonts
Requires:       gnu-free-mono-fonts
Requires:       %{name} = %{version}-%{release}

%description gnu-free-mono-fonts
This package allow to use system GNU FreeFonts mono-spaced font faces in TCPDF.

%package gnu-free-sans-fonts
Summary:        GNU FreeFonts sans-serif for tcpdf
BuildRequires:  gnu-free-sans-fonts
Requires:       gnu-free-sans-fonts
Requires:       %{name} = %{version}-%{release}

%description gnu-free-sans-fonts
This package allow to use system GNU FreeFont sans-serif font faces in TCPDF.

%package gnu-free-serif-fonts
Summary:        GNU FreeFonts serif for tcpdf
BuildRequires:  gnu-free-serif-fonts
Requires:       gnu-free-serif-fonts
Requires:       %{name} = %{version}-%{release}

%description gnu-free-serif-fonts
This package allow to use system GNU FreeFont serif font faces in TCPDF.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

#: Fix version
#sed -e '/tcpdf_version/s/6.6.0/%{version}/' -i include/tcpdf_static.php

: Check version
grep tcpdf_version include/tcpdf_static.php | grep %{version}

: remove bundled fonts
rm -rf fonts/dejavu-fonts-ttf* fonts/freefont-* fonts/ae_fonts_*
for fic in fonts/*.z
do
  rm -f $fic ${fic/.z/.php}
done
ls fonts | sed -e 's|^|%{_datadir}/php/%{real_name}/fonts/|' >corefonts.lst


%build
: empty build section, nothing required


%install
: Library
install -d     %{buildroot}%{_datadir}/php/%{real_name}
cp -a *.php    %{buildroot}%{_datadir}/php/%{real_name}/
cp -a include  %{buildroot}%{_datadir}/php/%{real_name}/
cp -a fonts    %{buildroot}%{_datadir}/php/%{real_name}/
install -d     %{buildroot}%{_datadir}/php/%{real_name}/images
install -m 0644 examples/images/_blank.png \
               %{buildroot}%{_datadir}/php/%{real_name}/images/

: Autoloader
php -d memory_limit=2G\
  %{_bindir}/phpab \
    --template fedora \
    --output %{buildroot}%{_datadir}/php/%{real_name}/autoload.php \
    %{buildroot}%{_datadir}/php/%{real_name}

: Configuration
install -d     %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 config/*.php \
               %{buildroot}%{_sysconfdir}/%{name}

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/opcache-%{name}.blacklist
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php-zts.d/opcache-%{name}.blacklist

: Tools
install -d %{buildroot}%{_bindir}
install -m 0755 tools/%{real_name}_addfont.php \
           %{buildroot}%{_bindir}/%{real_name}_addfont

# Fonts
for ttf in \
    /usr/share/fonts/dejav*/*ttf \
    /usr/share/fonts/gnu-free/*ttf \
; do php -d memory_limit=1G tools/tcpdf_addfont.php \
    --addcbbox \
    --flags 32 \
    --fonts $ttf \
    --link \
    --outpath %{buildroot}%{_datadir}/php/%{real_name}/fonts/
done

ls %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavuserif* |
    sed -e 's:^%{buildroot}::' | tee dejavu-serif.lst

if [ -f %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavumathtexgyre ]; then
 ls %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavumathtexgyre* |
    sed -e 's:^%{buildroot}::' | tee -a dejavu-serif.lst
fi


%check
php -r 'require "%{buildroot}%{_datadir}/php/%{real_name}/autoload.php";
  printf("%{name} version %s\n", $ver=TCPDF_STATIC::getTCPDFVersion());
  exit ($ver === "%{version}" ? 0 : 1);
'


%files -f corefonts.lst
%doc README.md CHANGELOG.TXT examples
%doc composer.json
%license LICENSE.TXT
%{_bindir}/%{real_name}_addfont
%dir %{_datadir}/php/%{real_name}
%dir %{_datadir}/php/%{real_name}/fonts
%{_datadir}/php/%{real_name}/include
%{_datadir}/php/%{real_name}/images
%{_datadir}/php/%{real_name}/*php
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/php.d/opcache-%{name}.blacklist
%config(noreplace) %{_sysconfdir}/php-zts.d/opcache-%{name}.blacklist

%files dejavu-lgc-sans-fonts
%{_datadir}/php/%{real_name}/fonts/dejavulgcsans*
%exclude %{_datadir}/php/%{real_name}/fonts/dejavulgcsansmono*

%files dejavu-lgc-sans-mono-fonts
%{_datadir}/php/%{real_name}/fonts/dejavulgcsansmono*

%files dejavu-lgc-serif-fonts
%{_datadir}/php/%{real_name}/fonts/dejavulgcserif*

%files dejavu-sans-fonts
%{_datadir}/php/%{real_name}/fonts/dejavusans*
%exclude %{_datadir}/php/%{real_name}/fonts/dejavusansmono*

%files dejavu-sans-mono-fonts
%{_datadir}/php/%{real_name}/fonts/dejavusansmono*

%files dejavu-serif-fonts -f dejavu-serif.lst

%files gnu-free-mono-fonts
%{_datadir}/php/%{real_name}/fonts/freemono*

%files gnu-free-sans-fonts
%{_datadir}/php/%{real_name}/fonts/freesans*

%files gnu-free-serif-fonts
%{_datadir}/php/%{real_name}/fonts/freeserif*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Remi Collet <remi@remirepo.net> - 6.8.0-1
- update to 6.8.0
- raise dependency on PHP 7.1

* Mon Dec 16 2024 Remi Collet <remi@remirepo.net> - 6.7.8-1
- update to 6.7.8
- re-license spec file to CECILL-2.1

* Mon Oct 28 2024 Remi Collet <remi@remirepo.net> - 6.7.7-1
- update to 6.7.7

* Mon Oct  7 2024 Remi Collet <remi@remirepo.net> - 6.7.6-1
- update to 6.7.6

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Remi Collet <remi@remirepo.net> - 6.7.5-1
- update to 6.7.5

* Thu Mar 21 2024 Remi Collet <remi@remirepo.net> - 6.7.4-1
- update to 6.7.4

* Thu Mar 21 2024 Remi Collet <remi@remirepo.net> - 6.7.3-1
- update to 6.7.3

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 6.7.2-1
- update to 6.7.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep  8 2023 Remi Collet <remi@remirepo.net> - 6.6.5-1
- update to 6.6.5 (no change)

* Wed Sep  6 2023 Remi Collet <remi@remirepo.net> - 6.6.3-1
- update to 6.6.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Remi Collet <remi@remirepo.net> - 6.6.2-1
- update to 6.6.2

* Tue Dec 13 2022 Remi Collet <remi@remirepo.net> - 6.6.1-1
- update to 6.6.1

* Tue Dec  6 2022 Remi Collet <remi@remirepo.net> - 6.6.0-1
- update to 6.6.0

* Tue Aug 16 2022 Remi Collet <remi@remirepo.net> - 6.5.0-1
- update to 6.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 6.4.4-1
- update to 6.4.4

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Remi Collet <remi@remirepo.net> - 6.4.2-1
- update to 6.4.2

* Mon Mar 29 2021 Remi Collet <remi@remirepo.net> - 6.4.1-2
- update to 6.4.1

* Mon Mar 29 2021 Remi Collet <remi@remirepo.net> - 6.4.1-1
- update to 6.4.1

* Tue Mar  9 2021 Remi Collet <remi@remirepo.net> - 6.3.5-4.20201209.456b794
- update to git snapshot to include fixes for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Remi Collet <remi@remirepo.net> - 6.3.5-2
- fix dejavu fonts path, FTBFS #1865226
- add DejaVuMathTeXGyre.ttf

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 6.3.5-1
- update to 6.3.5

* Wed Feb 12 2020 Remi Collet <remi@remirepo.net> - 6.3.4-1
- update to 6.3.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Remi Collet <remi@remirepo.net> - 6.3.2-1
- update to 6.3.2

* Fri Sep 20 2019 Remi Collet <remi@remirepo.net> - 6.3.1-1
- update to 6.3.1
- drop patch merged upstream

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 6.2.26-4
- add patch for 7.4 from
  https://github.com/tecnickcom/TCPDF/pull/134

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 6.2.26-1
- update to 6.2.26

* Mon Sep 24 2018 Remi Collet <remi@remirepo.net> - 6.2.25-1
- update to 6.2.25

* Sat Sep 15 2018 Remi Collet <remi@remirepo.net> - 6.2.22-1
- update to 6.2.22

* Fri Sep 14 2018 Remi Collet <remi@remirepo.net> - 6.2.21-1
- update to 6.2.21

* Fri Sep 14 2018 Remi Collet <remi@remirepo.net> - 6.2.19-1
- update to 6.2.19

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 6.2.17-1
- update to 6.2.17

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 6.2.16-1
- Update to 6.2.16

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Remi Collet <remi@fedoraproject.org> - 6.2.13-4
- add patch for PHP 7.2 from
  https://github.com/tecnickcom/TCPDF/pull/74/files
- disable opcache caching for fonts

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Remi Collet <remi@fedoraproject.org> - 6.2.13-1
- update to 6.2.13
- add classmap autoloader using fedora/autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 6.2.12-1
- update to 6.2.12
- provide php-composer(tecnickcom/tcpdf)

* Thu Sep 10 2015 Remi Collet <remi@fedoraproject.org> - 6.2.11-1
- update to 6.2.11
- fix PNGs with alpha #1261649

* Wed Jul 29 2015 Remi Collet <remi@fedoraproject.org> - 6.2.10-1
- update to 6.2.10
- sources from github (instead of sourceforge)
- drop dependency on php-mcrypt

* Sat Jun 27 2015 Remi Collet <remi@fedoraproject.org> - 6.2.9-1
- update to 6.2.9

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Remi Collet <remi@fedoraproject.org> - 6.2.8-1
- update to 6.2.8

* Tue Jan 13 2015 Remi Collet <remi@fedoraproject.org> - 6.2.4-1
- update to 6.2.4

* Wed Dec 10 2014 Remi Collet <remi@fedoraproject.org> - 6.1.1-1
- update to 6.1.1

* Mon Nov 10 2014 Remi Collet <remi@fedoraproject.org> - 6.0.098-1
- update to 6.0.098

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 6.0.095-1
- update to 6.0.095

* Thu Oct  2 2014 Remi Collet <remi@fedoraproject.org> - 6.0.094-1
- update to 6.0.094

* Wed Sep 17 2014 Robert Scheck <robert@fedoraproject.org> - 6.0.091-2
- buildrequire php-cli >= 5.3 (#1121745)
- added provides for php-* if package is used on EL-5 (#1121745)
- corrected inter-package dependencies (Remi Collet)

* Fri Aug 15 2014 Remi Collet <remi@fedoraproject.org> - 6.0.091-1
- update to 6.0.091
- provide php-composer(tecnick.com/tcpdf)

* Thu Jul 17 2014 Remi Collet <remi@fedoraproject.org> - 6.0.089-1
- update to 6.0.089

* Mon Jun 23 2014 Remi Collet <remi@fedoraproject.org> - 6.0.086-1
- update to 6.0.086

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.082-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Remi Collet <remi@fedoraproject.org> - 6.0.082-1
- update to 6.0.082
- include cbbox metrics in fonts metadata

* Mon Apr 28 2014 Remi Collet <remi@fedoraproject.org> - 6.0.072-1
- update to 6.0.072

* Tue Apr  8 2014 Remi Collet <remi@fedoraproject.org> - 6.0.064-1
- update to 6.0.064

* Tue Feb  4 2014 Remi Collet <remi@fedoraproject.org> - 6.0.059-1
- update to 6.0.059

* Sun Jan  5 2014 Remi Collet <remi@fedoraproject.org> - 6.0.053-1
- update to 6.0.053

* Thu Nov 28 2013 Remi Collet <remi@fedoraproject.org> - 6.0.049-1
- update to 6.0.049
- fix but with same PNG image included twice, #1035392

* Thu Nov 21 2013 Remi Collet <remi@fedoraproject.org> - 6.0.047-1
- update to 6.0.047

* Sun Oct 27 2013 Remi Collet <remi@fedoraproject.org> - 6.0.042-1
- update to 6.0.042

* Sat Sep 28 2013 Remi Collet <remi@fedoraproject.org> - 6.0.035-1
- update to 6.0.035

* Thu Sep 19 2013 Remi Collet <remi@fedoraproject.org> - 6.0.031-1
- update to 6.0.031

* Mon Sep  2 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 6.0.024-1
- update to 6.0.024

* Tue Aug  6 2013 Remi Collet <remi@fedoraproject.org> - 6.0.023-1
- update to 6.0.023

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul  6 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 6.0.020-1
- update to 6.0.020

* Sat Jun  1 2013 Remi Collet <remi@fedoraproject.org> - 6.0.018-1
- update to 6.0.018
- barcode examples now works out of the box

* Sat May 18 2013 Remi Collet <remi@fedoraproject.org> - 6.0.017-2
- split fonts, 1 subpackage per font package
- spec cleanups

* Sat May 18 2013 Remi Collet <remi@fedoraproject.org> - 6.0.017-1
- update to 6.0.017

* Thu May 16 2013 Remi Collet <remi@fedoraproject.org> - 6.0.016-1
- update to 6.0.016
- add /usr/share/php/tcpdf/images dir

* Wed May 15 2013 Remi Collet <remi@fedoraproject.org> - 6.0.015-1
- update to 6.0.015
- clean spec (upstream changes for packaging)
- drop .php suffix from tools

* Tue May 14 2013 Remi Collet <remi@fedoraproject.org> - 6.0.014-1
- update to 6.0.014
- drop patch merged upstream

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 6.0.013-2
- split fonts in sub-packages

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 6.0.013-1
- update to 6.0.013
- use available system TTF fonts

* Sun May 12 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 6.0.012-3
- Fix README.cache file permissions

* Fri May 10 2013 Remi Collet <remi@fedoraproject.org> - 6.0.012-2
- improve cache ownership, on folder per web server
- drop bundled fonts

* Thu May 09 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 6.0.012-1
- Initial packaging
