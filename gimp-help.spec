# NOTE: en/English is in the main package
# LANGUAGES: ca,Catalan da,Danish de,German el,Greek en_GB,British_English es,Spanish fr,French it,Italian ja,Japanese ko,Korean nl,Dutch nn,Norwegian_Nynorsk pt_BR,Brazilian_Portuguese ru,Russian sl,Slovenian sv,Swedish zh_CN,Simplified_Chinese
%global gimpsubver 2.0

Summary: Help files for GIMP
Name: gimp-help
Version: 2.10.0
Release: 9%{?dist}
License: GFDL and GPLv2+
URL: http://docs.gimp.org/
Source0: http://download.gimp.org/pub/gimp/help/gimp-help-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: dblatex
# BuildRequires: docbook2odf [orphaned]
BuildRequires: docbook-style-xsl
BuildRequires: gnome-doc-utils
BuildRequires: libxml2-python3
BuildRequires: libxslt
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: gimp-devel >= 2:2.10
BuildRequires: gettext
BuildRequires: graphviz
BuildRequires: pngnq
BuildRequires: pngcrush
BuildRequires: python3
BuildRequires: make
Requires: gimp >= 2:2.10
# BEGIN: OBSOLETE LANGUAGES
Obsoletes: gimp-help-sl < 2.10.0-1%{?dist}
Conflicts: gimp-help-sl < 2.10.0-1%{?dist}
Obsoletes: gimp-help-sv < 2.10.0-1%{?dist}
Conflicts: gimp-help-sv < 2.10.0-1%{?dist}
Obsoletes: gimp-help-hr < 2.10.0-1%{?dist}
Conflicts: gimp-help-hr < 2.10.0-1%{?dist}
Obsoletes: gimp-help-lt < 2.10.0-1%{?dist}
Conflicts: gimp-help-lt < 2.10.0-1%{?dist}
Obsoletes: gimp-help-pl < 2.10.0-1%{?dist}
Conflicts: gimp-help-pl < 2.10.0-1%{?dist}
# END: OBSOLETE LANGUAGES
Patch1: gimp-help-2.10.0-python3.patch
%description
This package contains a user manual written for the GNU Image Manipulation
Program.

# BEGIN: LANGUAGE SUB PACKAGES
%package ca
Summary: Catalan (ca) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ca)

%description ca
Catalan language support for gimp-help.

%package da
Summary: Danish (da) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-da)

%description da
Danish language support for gimp-help.

%package de
Summary: German (de) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-de)

%description de
German language support for gimp-help.

%package el
Summary: Greek (el) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-el)

%description el
Greek language support for gimp-help.

%package en_GB
Summary: British English (en_GB) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-en_GB)

%description en_GB
British English language support for gimp-help.

%package es
Summary: Spanish (es) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-es)

%description es
Spanish language support for gimp-help.

%package fi
Summary: Finnish (fi) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-fi)

%description fi
Finnish language support for gimp-help.

%package fr
Summary: French (fr) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-fr)

%description fr
French language support for gimp-help.

%package it
Summary: Italian (it) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-it)

%description it
Italian language support for gimp-help.

%package ja
Summary: Japanese (ja) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ja)

%description ja
Japanese language support for gimp-help.

%package ko
Summary: Korean (ko) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ko)

%description ko
Korean language support for gimp-help.

%package nl
Summary: Dutch (nl) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-nl)

%description nl
Dutch language support for gimp-help.

%package nn
Summary: Norwegian Nynorsk (nn) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-nn)

%description nn
Norwegian Nynorsk language support for gimp-help.

%package pt_BR
Summary: Brazilian Portuguese (pt_BR) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-pt_BR)

%description pt_BR
Brazilian Portuguese language support for gimp-help.

%package ro
Summary: Romanian (ro) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ro)

%description ro
Romanian language support for gimp-help.

%package ru
Summary: Russian (ru) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ru)

%description ru
Russian language support for gimp-help.

%package zh_CN
Summary: Simplified Chinese (zh_CN) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-zh_CN)

%description zh_CN
Simplified Chinese language support for gimp-help.

# END: LANGUAGE SUB PACKAGES

%prep
%setup -q
%patch1 -p1

%build
%configure
# don't attempt parallel builds, they tend to produce bad output without
# failing
make

%install
make DESTDIR=%{buildroot} install

rm -f files.list.*
f="$PWD/files.list"

pushd %{buildroot}%{_datadir}/gimp/%{gimpsubver}/help
for lang in *; do
    echo "%%lang($lang) %%{_datadir}/gimp/%%{gimpsubver}/help/$lang" > "$f.$lang"
done
popd

%files
%dir %{_datadir}/gimp/%{gimpsubver}/help
%{_datadir}/gimp/%{gimpsubver}/help/en
%doc AUTHORS ChangeLog NEWS README TERMINOLOGY
%license COPYING

# BEGIN: LANGUAGE FILE LISTS
%files ca -f files.list.ca
%files da -f files.list.da
%files de -f files.list.de
%files el -f files.list.el
%files en_GB -f files.list.en_GB
%files es -f files.list.es
%files fi -f files.list.fi
%files fr -f files.list.fr
%files it -f files.list.it
%files ja -f files.list.ja
%files ko -f files.list.ko
%files nl -f files.list.nl
%files nn -f files.list.nn
%files pt_BR -f files.list.pt_BR
%files ro -f files.list.ro
%files ru -f files.list.ru
%files zh_CN -f files.list.zh_CN
# END: LANGUAGE FILE LISTS

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Josef Ridky <jridky@redhat.com> - 2.10.0-3
- remplace Python 2 with Python 3 support (#1754462)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Josef Ridky <jridky@redhat.com> - 2.10.0-1
- new upstream release 2.10.0 (#1722969)
- remove unsupported languages (sl, sv)
- add new languages (fi, ro)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Josef Ridky <jridky@redhat.com> - 2.8.2-11
- fix FTBFS by set proper python invocation (#1604107)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Josef Ridky <jridky@redhat.com> - 2.8.2-9
- remove obsolete rm buildroot statement

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 04 2016 Nils Philippsen <nils@redhat.com> - 2.8.2-5
- remove obsolete %%clean, %%defattr, Group and BuildRoot tags

* Thu Mar 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.8.2-5
- Mark COPYING with %%license instead of %%doc

* Thu Mar 03 2016 Nils Philippsen <nils@redhat.com> - 2.8.2-5
- add supplements directives for language subpackages, see
  https://fedoraproject.org/wiki/Packaging:Langpacks for detail

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Tue Jun 23 2015 Nils Philippsen <nils@redhat.com> - 2.8.2-3
- fix website URL
- disable parallel building because it tends to produce bad output

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 05 2014 Nils Philippsen <nils@redhat.com> - 2.8.2-1
- version 2.8.2
- update source URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Nils Philippsen <nils@redhat.com> - 2.8.1-1
- version 2.8.1
- reenable parallel building
- add Brazilian Portuguese translation
- remove (empty) translations: Finnish, Hungarian, Lithuanian, Polish
- fix translation that makes xml2po.py/libxml2 crash

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Nils Philippsen <nils@redhat.com> - 2.8.0-7
- add GPLv2+ to license list (included tools used for building)

* Tue May 14 2013 Nils Philippsen <nils@redhat.com> - 2.8.0-6
- don't attempt parallel builds, they succeed or fail without a clear pattern

* Mon May 13 2013 Nils Philippsen <nils@redhat.com> - 2.8.0-5
- include all PO files missing from the tarball (#914031)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Nils Philippsen <nils@redhat.com> - 2.8.0-2
- add language subpackages

* Tue Jun 05 2012 Nils Philippsen <nils@redhat.com> - 2.8.0-1
- version 2.8.0
- add po files missing in tarball
- add new build requirements: dblatex, graphviz, pngnq, pngcrush
- fix file list generation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Nils Philippsen <nils@redhat.com> - 2.4.2-3
- Merge Review (#225798):
  - quote percent signs written into files list
  - enable parallel make

* Thu Dec 11 2008 Nils Philippsen <nils@redhat.com> - 2.4.2-2
- Merge Review (#225798):
  - ship AUTHORS, ChangeLog, COPYING, NEWS, README, TERMINOLOGY
  - don't own directories included in the gimp package
  - use %%defattr(-, root, root, -)

* Wed Nov 26 2008 Nils Philippsen <nils@redhat.com>
- Group: Documentation

* Fri Oct 10 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.2-1
- version 2.4.2

* Fri Apr 18 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.1-1
- version 2.4.1

* Mon Feb 04 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.0-1
- version 2.4.0
- mark language specific files with %%lang()
- add BR: gettext

* Wed Aug 08 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.2.0.13
- change licensing tag to GFDL

* Wed Aug 08 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.13
- version 2-0.13
- don't use "%%makeinstall ..." but "make DESTDIR=... install" for installing

* Thu Apr 12 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.12
- version 2-0.12

* Thu Jan 04 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.11
- version 2-0.11
- add disttag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2-0.1.0.10.1.1
- rebuild

* Mon Apr 24 2006 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.10

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 21 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.9

* Wed Feb 23 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.7

* Sat Jan 15 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.6

* Fri Jul 02 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.3

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 02 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.2

* Wed Mar 17 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.1
- initial build
