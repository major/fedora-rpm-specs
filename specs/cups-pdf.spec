Summary:        Extension for creating pdf-Files with CUPS
Summary(fr):    Extension de CUPS pour créer des fichiers PDF
Name:           cups-pdf
Version:        3.0.1
Release:        23%{?dist}
URL:            https://www.cups-pdf.de/
License:        GPL-2.0-or-later

Source0:        https://www.cups-pdf.de/src/%{name}_%{version}.tar.gz
Source1:        INSTALL.fedora.cups-pdf

# Default value for Out ${DESKTOP}
Patch1:         cups-pdf-conf.patch
# Handle ${DESKTOP} from config
Patch2:         cups-pdf-desktop.patch
# Handle new lines in title
Patch3:         cups-pdf-title.patch
# Fix build warning
Patch4:         cups-pdf-build.patch
# Report error/success in log
Patch5:         cups-pdf-result.patch
# Replace removed gs .setpdfwrite option
Patch6:         cups-pdf-setpdfwrite.patch
# Fix processing of lines with embedded null characters
Patch7:         cups-pdf-fix-null-chars.patch

BuildRequires:  gcc
BuildRequires:  cups-devel

Requires:       ghostscript, cups
Requires(post): %{_bindir}/pgrep


# These are the defaults paths defined in config.h
# CUPS-PDF spool directory
%global CPSPOOL   %{_localstatedir}/spool/cups-pdf/SPOOL

# CUPS-PDF output directory
%global CPOUT     %{_localstatedir}/spool/cups-pdf

# CUPS-PDF log directory
%global CPLOG     %{_localstatedir}/log/cups

# CUPS-PDF cups-pdf.conf config file
%global ETCCUPS   %(cups-config --serverroot 2>/dev/null || echo %{_sysconfdir}/cups)

# Additional path to backend directory
%global CPBACKEND %(cups-config --serverbin  2>/dev/null || echo %{_libdir}/cups)/backend


%description
"cups-pdf" is a backend script for use with CUPS - the "Common UNIX Printing
System" (see more for CUPS under https://www.cups.org/). 
"cups-pdf" uses the ghostscript pdfwrite device to produce PDF Files.

This version has been modified to store the PDF files on the Desktop of the 
user. This behavior can be changed by editing the configuration file.

%description -l fr
"cups-pdf" est un script de traitement CUPS - le "Common UNIX Printing System"
(plus d'informations sur CUPS à l'adresse https://www.cups.org/). 
"cups-pdf" utilise ghostscript pour construire des fichiers au format PDF.

Cette version a été modifiée pour produire les fichiers PDF sur le bureau
de l'utilisateur (dossier Desktop du répertoire d'accueil de l'utilisateur).
Ce comportement peut être modifié en éditant le fichier de configuration.


%prep
echo CIBLE = %{name}-%{version}-%{release}
%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} INSTALL.RPM

%patch -P1 -p0 -b .oldconf
%patch -P2 -p0 -b .desktop
%patch -P3 -p0 -b .title
%patch -P4 -p0 -b .build
%patch -P5 -p0 -b .result
%patch -P6 -p0 -b .setpdfwrite
%patch -P7 -p1 -b .nullchars


%build
pushd src
%{__cc} $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_GNU_SOURCE -o cups-pdf cups-pdf.c -lcups
popd


%install
mkdir -p %{buildroot}%{CPBACKEND}
mkdir -p %{buildroot}%{CPSPOOL}
mkdir -p %{buildroot}%{CPOUT}
mkdir -p %{buildroot}%{CPLOG}
mkdir -p %{buildroot}%{CPBACKEND}
mkdir -p %{buildroot}%{ETCCUPS}
mkdir -p %{buildroot}%{_datadir}/cups/model/
install -p -m644 extra/{CUPS-PDF_noopt,CUPS-PDF_opt}.ppd  %{buildroot}%{_datadir}/cups/model/
install -p -m644 extra/cups-pdf.conf %{buildroot}%{ETCCUPS}/
install -p -m700 src/cups-pdf %{buildroot}%{CPBACKEND}/



%post
# First install : create the printer if cupsd is running
if [ "$1" -eq "1" ] && %{_bindir}/pgrep -u root -f %{_sbindir}/cupsd >/dev/null
then
    /usr/sbin/lpadmin -p Cups-PDF -v cups-pdf:/ -m CUPS-PDF_noopt.ppd -E || :
fi


%postun
if [ "$1" -eq "0" ]; then
    # Delete the printer
    /usr/sbin/lpadmin -x Cups-PDF || :
fi


%files
%license COPYING
%doc ChangeLog README INSTALL.RPM
%dir %{CPSPOOL}
%dir %{CPOUT}
%attr(700, root, root) %{CPBACKEND}/cups-pdf
%config(noreplace) %{ETCCUPS}/cups-pdf.conf
%{_datadir}/cups/model/CUPS-PDF_noopt.ppd
%{_datadir}/cups/model/CUPS-PDF_opt.ppd


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022  Robert Marcano <robert@marcanoonline.com> - 3.0.1-16
- Fix handling of source Postscript files with embedded null inside the document lines (#2050615).

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Adam Williamson <awilliam@redhat.com> - 3.0.1-13
- Rebuild with no changes to work around Bodhi limitations

* Thu Jun 03 2021 Robert Marcano <robert@marcanoonline.com> - 3.0.1-12
- Fix use of removed '.setpdfwrite' in GS call (#1965717).
- Change default configuration to add suffix to the generated filename in order to avoid
overwriting previously generated files (#1419308)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Robert Marcano <robert@marcanoonline.com> - 3.0.1-6
- Add BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Robert Marcano <robert@marcanoonline.com> - 3.0.1-1
- Update to upstream release 3.0.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Remi Collet <remi@fedoraproject.org> 2.6.1-7
- report success/error in log file #1010434

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> 2.6.1-6
- log path of generated PDF #1007143

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Remi Collet <remi@fedoraproject.org> 2.6.1-4
- fix title detection
- fix build warning
- rename INSTALL.fedora to INSTALL.RPM

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Remi Collet <Fedora@FamilleCollet.com> 2.6.1-1
- update to 2.6.1
- fix %%post scriptlet (#757760)

* Sat Feb 19 2011 Remi Collet <Fedora@FamilleCollet.com> 2.5.1-1
- update to 2.5.1 (bugfix)
- remove old SELinux stuff from spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Remi Collet <Fedora@FamilleCollet.com> 2.5.0-4
- spec cleanup

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Remi Collet <Fedora@FamilleCollet.com> 2.5.0-1
- update to 2.5.0
- Add SElinux notes in INSTALL.fedora 

* Fri Mar 28 2008 Remi Collet <Fedora@FamilleCollet.com> 2.4.8-1
- update to 2.4.8

* Mon Mar 24 2008 Remi Collet <Fedora@FamilleCollet.com> 2.4.7-1
- update to 2.4.7

* Mon Mar 17 2008 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-7
- remove SElinux on F >= 9 (in selinux-policy, see #436671)

* Sat Feb  9 2008 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-6.fc9.2
- rebuild with gcc-4.3

* Thu Dec 06 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-6.fc9.1
- change module version from 2.4.6.1 to 2.4.7

* Tue Dec 04 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-6
- handle unconfined_home_dir_t and unconfined_home_t

* Thu Nov 29 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-5
- update default conf: use ${DESKTOP}

* Sat Nov 24 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-4
- add cups-pdf-desktop.patch to work with xdg prefs

* Thu Aug 23 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-3
- Fix License
- F-8 rebuild (BuildID)

* Sun May 06 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-2
- spec changes for RHEL 4 and Fedora Core 3 and 4 (no selinux)

* Sun May 06 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.6-1
- update to 2.4.6

* Sun Apr 08 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.5-1
- update to 2.4.5

* Sat Feb 03 2007 Remi Collet <Fedora@FamilleCollet.com> 2.4.4-1
- update to 2.4.4

* Mon Nov 13 2006 Remi Collet <Fedora@FamilleCollet.com> 2.4.2-2
- review comments (URL, INSTALL.fedora as Source2, descr. rewrap)

* Mon Nov 13 2006 Remi Collet <Fedora@FamilleCollet.com> 2.4.2-1
- clean spec for Extras
- don't use "service cups restart", only test if cups is running

* Tue Oct 24 2006 Remi Collet <rpms@FamilleCollet.com> 2.4.2-1.fc6.remi
- FC6 build

* Sat Oct  7 2006 Remi Collet <rpms@FamilleCollet.com> 2.4.2-1.fc5.remi
- update to 2.4.2

* Tue May 16 2006 Remi Collet <rpms@FamilleCollet.com> 2.4.0-1.fc{3,4,5}.remi
- update to 2.4.0
- add SElinux module
- spec cleanning

* Tue May 16 2006 Remi Collet <rpms@FamilleCollet.com> 2.3.0-1.fc{3,4,5}.remi
- update to 2.3.0
- chmod 700 on %%{CPBACKEND}/cups-pdf for cups-1.2.0 on FC5

* Fri Apr 14 2006 Remi Collet <rpms@FamilleCollet.com> 2.2.0-1.fc{3,4,5}.remi
- update to 2.2.0

* Sat Apr  8 2006 Remi Collet <rpms@FamilleCollet.com> 2.1.1-1.fc{3,4,5}.remi
- update to 2.1.1

* Sun Mar 26 2006 Remi Collet <RPMS@FamilleCollet.com> 2.1.0-1.fc{3,4,5}.remi
- update to 2.1.0

* Sun Jan 29 2006 Remi Collet <RPMS@FamilleCollet.com> 2.0.5-1.fc{3,4}.remi
- update to 2.0.5

* Sun Jan 29 2006 Remi Collet <remi.collet@univ-reims.fr> 2.0.4-1.fc{3,4}.remi
- update to 2.0.4

* Sat Jan  7 2006 Remi Collet <remi.collet@univ-reims.fr> 2.0.3-1.fc{3,4}.remi
- update to 2.0.3

* Wed Jan  4 2006 Remi Collet <remi.collet@univ-reims.fr> 2.0.1-1.fc{3,4}.remi
- update to 2.0.1

* Tue Jan  3 2006 Remi Collet <remi.collet@univ-reims.fr> 2.0.0-2.fc#.remi
- output to Desktop
- defattr

* Fri Dec 23 2005 Remi Collet <remi.collet@univ-reims.fr> 2.0.0-1.fc4.remi
- update to 2.0.0 final

* Sat Nov  5 2005 Remi Collet <remi.collet@univ-reims.fr> 2.0-0.1.fc3.remi
- rebuild for FC3

* Sat Nov  5 2005 Remi Collet <remi.collet@univ-reims.fr> 2.0-0.1.fc4.remi
- update to 2.0 beta2
- rebuild for FC4
- conditionnal "post" and "postun" script, more robust
- cups-pdf-conf.patch (Out in $HOME)

* Mon Sep 26 2005 Christian Ellsworth C. <k.ellsworth@gmail.com>
- adapted to fit the new runtime config file of version 2.0

* Sat Sep 10 2005 Remi Collet <remi.collet@univ-reims.fr> 1.7.4-1.fc4.remi
- adapted to cups-pdf 1.7.4
- added auto remove a cups-pdf printer in "postun"
- added CHANGELOG, COPYING, README
- creating cups-pdf-home.patch

* Sat Mar 05 2005 Christian Ellsworth C. <k.ellsworth@gmail.com>
- adapted to cups-pdf 1.7.0
- added auto configure a cups-pdf printer

* Tue Feb 22 2005 Christian Ellsworth C. <k.ellsworth@gmail.com>
- adapted to cups-pdf 1.6.6

* Thu Aug 12 2004 Volker Behr <vrbehr@cip.physik.uni-wuerzburg.de>
- adapted to cups-pdf 1.5.2 

* Sat Jan 31 2004 Volker Behr <vrbehr@cip.physik.uni-wuerzburg.de>
- adapetd to cups-pdf 1.4.0 and new building environment

* Wed Jan 14 2004 Mark Lane <harddata.com>
- fixed the specfile so that x86_64 version installs the filter
- in /usr/lib64 instead of /usr/lib

* Sun Nov 02 2003 Volker Behr <vrbehr@cip.physik.uni-wuerzburg.de>
- third release of cups-pdf, RPM-Edition for cups-pdf 1.3

* Tue Sep 09 2003 Dirk Schwier <rpms@raumhochdrei.de>
- second Release of cups-pdf, RPM-Edition for cups-pdf 1.1

* Tue May 27 2003 Dirk Schwier <rpms@raumhochdrei.de>
- we're proud to present the first version of cups-pdf, RPM-Edition
