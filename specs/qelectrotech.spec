# fedora/remirepo spec file for qelectrotech
#
# Copyright (c) 2009-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global upver  0.9
%undefine _package_note_file

Name:        qelectrotech

Summary:     An electric diagrams editor
Summary(ar): مُحرّر مخططات كهربائية
Summary(be): Elektrische schema editor
Summary(ca): Editar esquemes elèctrics
Summary(cs): Editor výkresů elektrických obvodů
Summary(da): Elektrisk diagram redigering
Summary(de): Schaltpläne erstellen und bearbeiten
Summary(el): Επεξεργασία ηλεκτρικών διαγραμμάτων
Summary(es): Un editor de esquemas eléctricos
Summary(fr): Éditeur de schémas électriques
Summary(hr): Uredi elektro sheme
Summary(it): Un programma per disegnare schemi elettrici
Summary(nl): Elektrische schema editor
Summary(pl): Edytor schematów elektrycznych
Summary(pt): Um editor de esquemas eléctricos
Summary(ru): Редактор электрических схем

Epoch: 0
# Upstream version is a float so 0.11 < 0.2 < 0.21 < 0.3
# So use %.2f with upstream acknowledgment
# Remember to check upver macro on each update
Version:     0.90
Release:     7%{?dist}


# Prog is GPLv2 - Symbols/Elements are Creative Commons Attribution
License:    GPL-2.0-or-later

Url:        http://qelectrotech.org/
Source0:    https://git.tuxfamily.org/qet/qet.git/snapshot/qet-%{upver}.tar.gz

BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    desktop-file-utils
BuildRequires:    pkgconfig(sqlite3)
BuildRequires:    pkgconfig(Qt5Concurrent)
BuildRequires:    pkgconfig(Qt5Core)
BuildRequires:    pkgconfig(Qt5Gui)
BuildRequires:    pkgconfig(Qt5Network)
BuildRequires:    pkgconfig(Qt5PrintSupport)
BuildRequires:    pkgconfig(Qt5Sql)
BuildRequires:    pkgconfig(Qt5Svg)
BuildRequires:    pkgconfig(Qt5Widgets)
BuildRequires:    pkgconfig(Qt5Xml)
BuildRequires:    cmake(KF5WidgetsAddons)
BuildRequires:    cmake(KF5CoreAddons)

Requires:         qelectrotech-symbols = %{epoch}:%{version}-%{release}
%if 0%{?fedora}
Recommends:       electronics-menu
%endif


%description
QElectroTech is a Qt application to design electric diagrams. It uses XML
files for elements and diagrams, and includes both a diagram editor and an 
element editor.

%description -l be
QElectroTech is een QT toepassing voor het maken en beheren van elektrische
schema's. QET gebruikt XML voor de elementen en schema's en omvat een
schematische editor, itemeditor, en een titel sjabloon editor.

%description -l cs
QElectroTech je aplikací Qt určenou pro návrh nákresů elektrických obvodů.
Pro prvky a nákresy používá soubory XML, a zahrnuje v sobě jak editor nákresů,
tak editor prvků.

%description -l da
QElectroTech er et Qt5 program til at redigere elektriske diagrammer.
Det bruger XML filer for symboler og diagrammer og inkluderer diagram,
symbol og titelblok redigering.

%description -l el
Το QElectroTech είναι μια εφαρμογή Qt για σχεδίαση ηλεκτρικών διαγραμμάτων.
Χρησιμοποιεί αρχεία XML για στοιχεία και διαγράμματα, και περιλαμβάνει
επεξεργαστή διαγραμμάτων καθώς και επεξεργαστή στοιχείων.

%description -l es
QElectroTech es una aplicación Qt para diseñar esquemas eléctricos.
Utiliza archivos XML para los elementos y esquemas, e incluye un editor 
de esquemas y un editor de elemento.

%description -l fr
QElectroTech est une application Qt pour réaliser des schémas électriques.
QET utilise le format XML pour ses éléments et ses schémas et inclut un
éditeur de schémas ainsi qu'un éditeur d'élément.

%description -l it
QElectroTech è una applicazione fatta in Qt per disegnare schemi elettrici.
QET usa il formato XML per i suoi elementi e schemi, includendo anche un
editor per gli stessi.

%description -l nl
QElectroTech is een Qt applicatie om elektrische schema's te ontwerpen.
Het maakt gebruik van XML-bestanden voor elementen en diagrammen, en omvat
zowel een diagram bewerker, een element bewerker, en een bloksjabloon bewerker.

%description -l pl
QElectroTech to aplikacja napisana w Qt, przeznaczona do tworzenia schematów
elektrycznych. Wykorzystuje XML do zapisywania plików elementów i projektów.
Posiada edytor schematów i elementów.

%description -l pt
QElectroTech é uma aplicação baseada em Qt para desenhar esquemas eléctricos.
QET utiliza ficheiros XML para os elementos e para os esquemas e inclui um
editor de esquemas e um editor de elementos.

%description -l ru
QElectroTech - приложение написанное на Qt и предназначенное для разработки
электрических схем. Оно использует XML-файлы для элементов и схем, и включает,
как редактор схем, так и редактор элементов.


%package symbols
Summary:     Elements collection for QElectroTech
Summary(be): Elementen collectie voor QElectroTech
Summary(cs): Sbírka prvků pro QElectroTech
Summary(da): Symbol samling for QElectroTech
Summary(de): Bauteilsammlung für QElectroTech
Summary(el): Συλλογή στοιχείων του QElectroTech
Summary(es): Collección de elementos para QElectroTech
Summary(fr): Collection d'éléments pour QElectroTech
Summary(it): Collezione di elementi per QElectroTech
Summary(nl): Elementen collectie voor QElectroTech
Summary(pl): Kolekcja elementów QElectroTech
Summary(pt): Colecção de elementos para QElectroTech
Summary(ru): Коллекция элементов для QElectroTech
License:     CC-BY-3.0
BuildArch:   noarch
Requires:    qelectrotech = %{epoch}:%{version}-%{release}


%description symbols
Elements collection for QElectroTech.

%description -l be symbols
Elementen collectie voor QElectroTech.

%description -l cs symbols
Sbírka prvků pro QElectroTech.

%description -l da symbols
Symbol samling for QElectroTech.

%description -l de symbols
Bauteilsammlung für QElectroTech.

%description -l el symbols
Συλλογή στοιχείων του QElectroTech.

%description -l es symbols
Collección de elementos para QElectroTech.

%description -l fr symbols
Collection d'éléments pour QElectroTech.

%description -l it symbols
Collezione di elementi per QElectroTech.

%description -l nl symbols
Elementen collectie voor QElectroTech.

%description -l pl symbols
Kolekcja elementów QElectroTech.

%description -l pt symbols
Colecção de elementos para QElectroTech.

%description -l ru symbols
Коллекция элементов для QElectroTech.


%prep
%setup -q -n qet-%{upver}

sed -e s,/usr/local/,%{_prefix}/, \
    -e /QET_MAN_PATH/s,'man/','share/man', \
    -e /QET_MIME/s,../,, \
    -i %{name}.pro

%{qmake_qt5} \
  'QMAKE_COPY_DIR = cp -f -r --preserve=timestamps' \
  qelectrotech.pro


%build
make %{?_smp_mflags}


%install
rm -f *.lang
INSTALL_ROOT=%{buildroot} make install

# We only provides UTF-8 files
rm -rf %{buildroot}/usr/doc/%{name} \
       %{buildroot}%{_datadir}/%{name}/examples \
       %{buildroot}%{_mandir}/fr.ISO8859-1 \
       %{buildroot}%{_mandir}/fr

mv %{buildroot}%{_mandir}/fr.UTF-8 %{buildroot}%{_mandir}/fr

desktop-file-install --vendor="" \
   --add-category=Electronics \
   --dir=%{buildroot}%{_datadir}/applications/ \
         %{buildroot}%{_datadir}/applications/%{name}.desktop

# QT translation provided by QT.
rm -f %{buildroot}%{_datadir}/%{name}/lang/qt_*.qm

%find_lang qet          --with-qt
%find_lang qelectrotech --with-man
cat qet.lang >>qelectrotech.lang

%files -f %{name}.lang
%doc CREDIT examples
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lang
%{_mandir}/man1/%{name}.*


%files symbols
%license ELEMENTS.LICENSE
%{_datadir}/%{name}/elements
%{_datadir}/%{name}/titleblocks


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Remi Collet <remi@remirepo.net> - 0.90-1
- update to 0.90
- use SPDX license id

* Wed Aug  3 2022 Remi Collet <remi@remirepo.net> - 0.80-4
- undefine _package_note_file to fix FTBFS #2113668

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 0.80-1
- update to 0.80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Remi Collet <remi@remirepo.net> - 0.70-1
- update to 0.70

* Wed Jun 26 2019 Remi Collet <remi@remirepo.net> - 0.70~rc2-1
- update to 0.70rc2

* Fri Apr 12 2019 Remi Collet <remi@remirepo.net> - 0.70~rc1-1
- update to 0.70rc1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Remi Collet <remi@remirepo.net> - 0.61-1
- update to 0.61

* Thu Jul 19 2018 Remi Collet <remi@remirepo.net> - 0.60-3
- add upstream patch for Qt 5.11, fix FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 0.60-1
- update to 0.6

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 0.50-8
- missing BR on C/C++ compilers

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.50-2
- use %%{qmake_qt5} macro to ensure proper build flags

* Fri Nov 27 2015 Remi Collet <remi@fedoraproject.org> - 0.50-1
- update to 0.5
- add be and nl spec translations

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.40-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Remi Collet <remi@fedoraproject.org> - 0.40-1
- Version 0.4 finale
- fix license handling

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.30-4
- update mime scriptlets, drop extraneous scriptlet deps

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 28 2013 Remi Collet <remi@fedoraproject.org> - 0.30-1
- Version 0.3 finale

* Tue Sep 10 2013 Remi Collet <remi@fedoraproject.org> - 0.30-0.10.rc
- 0.3 Release Candidate

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Remi Collet <remi@fedoraproject.org> - 0.30-0.8.beta
- 0.3beta

* Tue Apr 16 2013 Remi Collet <remi@fedoraproject.org> - 0.30-0.7.svn2116
- pull latest changes from SVN

* Sun Feb 24 2013 Remi Collet <remi@fedoraproject.org> - 0.30-0.6.svn2045
- pull latest changes from SVN (gcc 4.8 fixes)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-0.5.svn1844
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-0.4.svn1844
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Remi Collet <remi@fedoraproject.org> - 0.30-0.3.svn1844
- pull latest change (packaging request) from SVN
- preserve timestamps on elements collection
- add missing titleblocks
- add cs + pl summary and description

* Sun May 13 2012 Remi Collet <remi@fedoraproject.org> - 0.30-0.2.alpha
- modernize scriptlets

* Sun May 13 2012 Remi Collet <remi@fedoraproject.org> - 0.30-0.1.alpha
- update to 0.3a

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4.1
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 07 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.22-1.1
- set symbols as noarch on EL-6

* Sat Mar 13 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.22-1
- update to 0.22

* Sat Mar 06 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.21-1
- update to 0.21
- more translations (sumnary and description)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.20-1
- update to 0.2 finale

* Sat Jun 20 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.20-0.2.rc2
- update to RC2

* Thu Jun 18 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.20-0.2.rc1
- changes from review (#505867)
- add multi-lang sumnary (taken from .desktop)
- add multi-lang description (taken from README)
- rename qlectrotech-elements to -symbols
- use electronics-menu

* Sun Jun 14 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.20-0.1.rc1
- initial RPM for fedora

