Name: 		utrac
Version:	0.3.0
Release:	41%{?dist}
Summary: 	Universal Text Recognizer and Converter
Summary(fr): 	Reconnaisseur et convertisseur universel de texte

License: 	GPL-2.0-or-later
Url: 		http://utrac.sourceforge.net
Source:		http://utrac.sourceforge.net/download/utrac-0.3.0.tar.gz
Patch0:		utrac-destdir.patch
Patch1:		utrac.h.utf8
Patch2:		utrac-prefix.patch

BuildRequires: make
BuildRequires:  gcc
%description
Utrac is a command line tool and a library that recognize the encoding
of an input file (ex: UTF-8, ISO-8859-1, CP437...) and its end-of-line
type (CR, LF, CRLF).
It has three main features:
- Automatic recognition (depending on the file and on the system's locale),
  reliable in most cases;
- Assistance for verification or manual recognition;
- Conversion to an other charset and/or end-of-line type.

%description -l fr
Utrac est un outil en ligne de commande et une bibliothèque qui reconnait
l'encodage d'un fichier d'entrée (par ex: UTF-8, ISO-8859-1, CP437...) et son
type de fin de ligne (CR, LF, CRLF).
Ses trois fonctionnalités principales sont :
- reconnaissance automatique (suivant le fichier et la localisation du
  système) fiable dans la plupart des cas ;
- assistance à la vérification ou à la reconnaissance manuelle ;
- conversion dans un autre jeu de caractères et/ou type de fin de ligne.

%package	devel
Summary:	Library and file header for utrac
Summary(fr):	Bibliothèque et fichier d'en-têtes pour utrac
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description devel
The %{name}-devel package includes the static library and the header files
for compiling programs that use the utrac library.

%description -l fr devel
Le paquetage %{name}-devel contient la bibliothèque statique et le fichier
d'en-têtes nécessaires à la compilation des programmes qui utilisent la
bibliothèque utrac.

%prep
%setup -q
%patch -P0
%patch -P1 -p1
%patch -P2
%{__sed} -i -e 's/^\(CFLAGS.*\)/\1 $(RPM_OPT_FLAGS)/' Makefile
%{__sed} -i -e '/^\s*strip /d' Makefile

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -std=gnu17"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT \
             PREFIX_PATH=%{_prefix} \
             BIN_PATH=%{_bindir} \
             LIB_PATH=%{_libdir} \
             INC_PATH=%{_includedir} \
             MAN_PATH=%{_mandir}/man1 \
             SHARE_PATH=%{_datadir}/%{name}
make install-lib DESTDIR=$RPM_BUILD_ROOT \
             PREFIX_PATH=%{_prefix} \
             BIN_PATH=%{_bindir} \
             LIB_PATH=%{_libdir} \
             INC_PATH=%{_includedir} \
             MAN_PATH=%{_mandir}/man1 \
             SHARE_PATH=%{_datadir}/%{name}

%files
%doc CHANGES COPYING README TODO
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%files devel
%{_libdir}/*.a
%{_includedir}/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.0-37
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-26
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 04 2010 Jon Ciesla <limb@jcomserv.net> - 0.3.0-13
- Added virtual provides for -static, BZ 609623.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.0-10
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 3.0.3-3
  - Licence tag clarification

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-8
  - FE6 rebuild

* Thu May 18 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-7
  - Increase release to fix a cvs error.

* Thu May 18 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-6
  - Honor $RPM_OPT_FLAGS flags.
    Contribution of Ville Skyttä <ville[DOT]skytta[AT]iki[DOT]fi>.

* Tue Nov  8 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-5
  - Patch to change prefix. Fix #172601

* Tue Sep 27 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-4
  - Change Source tag to allow direct download

* Tue Sep 27 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-3
  - Change Source tag to allow direct download
  - Update and rename Makefile patch
  - Override utrac variables in install section
  - Add "-l fr" forgotten option in french description
  - Remove "rm -rf $RPM_BUILD_DIR/%%{name}-%%{version}" statement in %%clean section
  - Remove useless INSTALL file
  - Package don't own /usr/share/man/man1
  - Contribution of Aurélien Bompard <gauret[AT]free[DOT]fr>
    Thanks to him

* Tue Sep 13 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-2
  - Add french summary and description

* Mon Sep 12 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.3.0-1
  - New version
  - Patch0 to easy installation
  - Patch1 to set default encoding recognition as utf8

* Thu Jan 20 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.2-0.fdr.1
  - Initial Fedora RPM
