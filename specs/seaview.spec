Name:           seaview
Version:        5.0
Release:        12%{?dist}
Summary:        Graphical multiple sequence alignment editor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://doua.prabi.fr/software/seaview
Source0:        ftp://pbil.univ-lyon1.fr/pub/mol_phylogeny/seaview/archive/seaview_5.0.tar.gz
Source1:        seaview.desktop
Patch0:         seaview-chris.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXinerama-devel

%description
SeaView is a graphical multiple sequence alignment editor developed by Manolo
Gouy.  SeaView is able to read and write various alignment formats (NEXUS, MSF,
CLUSTAL, FASTA, PHYLIP, MASE).  It allows to manually edit the alignment, and
also to run DOT-PLOT or CLUSTALW/MUSCLE programs to locally improve the
alignment.


%prep
%setup -q -n seaview
%patch -P0 -p 1 -b .chris


%build
make %{?_smp_mflags}


%check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seaview
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 seaview $RPM_BUILD_ROOT/%{_bindir}
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 0644 -p seaview.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/seaview.xpm
install -m 0644 -p seaview.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/seaview.svg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
install -m 0644 -p seaview.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/seaview.appdata.xml
install -m 644 seaview.1 $RPM_BUILD_ROOT/%{_mandir}/man1



%files
%doc seaview.1.xml seaview.html
%{_bindir}/seaview
%{_datadir}/seaview/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Christian Iseli <Christian.Iseli@unil.ch> - 5.0-1
- New upstream version
- Fix FTBFS bugzilla 1800081

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Christian Iseli <Christian.Iseli@unil.ch> - 4.6.2.1-1
- New upstream version
- Fix update request bugzilla 1510609

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Christian Iseli <Christian.Iseli@unil.ch> - 4.6-1
- New upstream version
- update Icon in desktop file
- install new appdata file
- Fix update request bugzilla 1317223

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Christian Iseli <Christian.Iseli@unil.ch> - 4.5.4.4-1
- New upstream version
- Fix FTBFS bugzilla 1222300

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.5.2-3
- rebuild (fltk)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Richard Hughes <richard@hughsie.com> - 4.5.2-1
- Update to latest upstream version
- Install the .svg file and use it in the .desktop file to allow seaview
  to be processed by the metadata builder and be visible in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  8 2014 Christian Iseli <Christian.Iseli@unil.ch> - 4.5.0-1
- New upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Christian Iseli <Christian.Iseli@unil.ch> - 4.4.0-1
- New upstream version
- Source files perm are now ok

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 4.3.2-4
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Christian Iseli <Christian.Iseli@unil.ch> - 4.3.2-1
- New upstream version
- Fix for failed mass rebuild: removed -lXext at link step
- put seaview.html in doc
- example file has disappeared

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 26 2011 Christian Iseli <Christian.Iseli@unil.ch> - 4.2.12-1
- New upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.6-2
- Rebuild to solve libfltk broken dep

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.6-1
- New upstream version

* Wed Feb 17 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.2-2
- Fix thinko

* Wed Feb 17 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.2-1
- New upstream version
- Update patch file to cause link against fontconfig library to resolve
  bugzilla 564977

* Fri Jan  8 2010 Christian Iseli <Christian.Iseli@licr.org> - 4.2.1-1
- New upstream version
- tarball does not expand to a versioned directory
- seaview.help -> seaview.html
- resync patches
- add man page
- remove exec bit on source files (they end up in the debug package)
- add doc files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Christian Iseli <Christian.Iseli@licr.org> - 4.0-1
- New upstream version
- Fix GCC 4.4 compile issues
- README and protein.mase are gone

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 12 2008 Christian Iseli <Christian.Iseli@licr.org> - 2.4-1
- New upstream version 2.4
- Cleanup changelog formatting

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-2
- Autorebuild for GCC 4.3

* Mon Sep 10 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.0-1
- New upstream version, with a true version number :)

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070616
- Fix License tag to GPLv2+.

* Thu Jun 28 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070615
- New upstream tarball.
- Add desktop file and icon.

* Wed Jun 13 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.1.20070515
- Actually follow pre-release strategy for version/release...
- New upstream "version".

* Tue May  8 2007 Christian Iseli <Christian.Iseli@licr.org> - 0-0.20070417
- Follow pre-release strategy for version/release.

* Mon May  7 2007 Christian Iseli <Christian.Iseli@licr.org> - 0.20070417-0
- Create spec file.
