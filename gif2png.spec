%global debug_package %{nil}

Summary:	A GIF to PNG converter
Name:		gif2png
Version:	2.5.14
Release:	12%{?dist}
License:	BSD
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%name-%version.tar.gz
Source100:	test-0.gif
Source101:	test-1.gif
BuildRequires:  gcc
BuildRequires:	libpng-devel
BuildRequires: make


%description
The gif2png program converts files from the obsolescent Graphic Interchange
Format to Portable Network Graphics. The conversion preserves all graphic
information, including transparency, perfectly. The gif2png program can
even recover data from corrupted GIFs.

There exists a 'web2png' program in a separate package which is able
to convert entire directory hierarchies.


%prep
%autosetup


%build
%make_build


%install
%make_install

# web2png is Python 2 only, see https://bugzilla.redhat.com/show_bug.cgi?id=1787242
rm %{buildroot}%{_bindir}/web2png
rm %{buildroot}%{_mandir}/man1/web2png*

#disable tests for while
#%check
#P=./gif2png
#for i in %SOURCE100 %SOURCE101; do
#    rm -f _tmp.gif
#    install -p -m 0644 $i _tmp.gif
#    $P _tmp.gif
#    $P -f < "$i" > _tmp.png
#    $P -O -f < "$i" > _tmp.png
#done


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*



%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.14-3
- Package web2png has been removed
  See https://fedoraproject.org/wiki/Changes/RetirePython2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.14-1
- Update to 2.5.14
- Redirect segfault to a graceful exit. Tired of meaningless fuzzer bugs.

* Tue Apr 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.13-1
- New upstream release, fixes rhbz #1674965

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5.11-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.11-1
- Rebuilt to new upstream release, fixes rhbz#1368524 and rhbz#1423611

* Mon Jun 19 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.8-1809
- Spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-1808
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-1807
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1806
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1805
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1804
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1803
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-1801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr  3 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.8-1800
- updated to 2.5.8
- removed -overflow and libpng15 patches; related issues are fixed
  upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-1701
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.4-1700
- added patch for building with libpng15
- added %%check

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.5.4-1502
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-1501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.4-1500
- updated to 2.5.4

* Sun Nov  7 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.3-1500
- updated to 2.5.3 (NOTE: breaks cmdline API by removal of '-t' option)

* Tue Jan  5 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.2-1305
- catch another possible overflow when appending a numbered suffix
  (detected to Tomas Hoger)

* Sat Jan  2 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.2-1304
- changed -overflow patch to abort on bad filenames instead of
  processing truncated ones

* Fri Jan  1 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.2-1302
- fixed command line buffer overflow (#547515, CVE-2009-5018)

* Sat Nov 14 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.2-1300
- updated to 2.5.2
- removed Debian patches; issues are addressed by new upstream release
- set '-Wl,--as-needed' LDFLAGS

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.1-6
- made web2png noarch

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.1-4
- Autorebuild for GCC 4.3

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.1-3
- added Debian patchset to make it build with current libpng

* Sat Feb 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.1-2
- rebuilt for FC5

* Tue Jul  5 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.5.1-1
- Initial build.
