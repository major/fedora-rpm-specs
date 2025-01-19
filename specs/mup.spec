%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           mup
Version:        7.0

Release:        7%{?dist}
Summary:        A music notation program that can also generate MIDI files
License:        Mup
URL:            http://www.arkkra.com/doc/overview.html

%define         versionnodot %(echo %{version} | tr -d ".")

Source0:        http://www.arkkra.com/ftp/pub/unix/mup%{versionnodot}src.tar.gz
Source1:        mupmate.desktop

# Newer Fedora build roots no longer include, gcc, gcc-c++ by default
# https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  glibc-devel
BuildRequires:  fltk-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXft-devel
BuildRequires:  desktop-file-utils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  man-db

%description
Mup is a program for printing music. It takes an input file containing ordinary
(ASCII) text describing music, and produces PostScript output for printing the
musical score described by the input.

%prep
%setup -q

# Preserve the timestamp of files that we copy from the Mup source tree
sed -i -e 's|cp |cp -p |' simple.makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LIBDIR="%{_datadir}/%{name}" DOCDIR="%{_pkgdocdir}" -f simple.makefile

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" LIBDIR="%{buildroot}%{_datadir}/%{name}" DOCDIR="%{buildroot}%{_pkgdocdir}" install -f simple.makefile

# License is handled separately
rm "%{buildroot}%{_pkgdocdir}/license.txt"

# Add docs that aren't installed by make install
cp -a AUTHORS ChangeLog NEWS README "%{buildroot}%{_pkgdocdir}"/.

# Remove docs that are not applicable
rm "%{buildroot}%{_pkgdocdir}/Macinst.html"
rm "%{buildroot}%{_pkgdocdir}/winrun.html"

mkdir -p %{buildroot}/%{_datadir}/applications
cp -p %{SOURCE1} %{buildroot}/%{_datadir}/applications/
desktop-file-validate %{buildroot}/%{_datadir}/applications/mupmate.desktop

%files
%license LICENSE
%{_pkgdocdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/mup
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep  4 2022 Greg Bailey <gbailey@lxpro.com> - 7.0-1
- Update to 7.0
- noteleft string
- mensural symbols and centered stems
- improved measuration time signature sizing when used with printedtime
- expression eval macros
- string() function
- shapes context

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Greg Bailey <gbailey@lxpro.com> - 6.7-1
- Update to 6.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb  4 2018 Greg Bailey <gbailey@lxpro.com> - 6.6-1
- Update to 6.6
- Revert null byte conversion errors patch (merged upstream)
- Ability to force "with" items to be above or below
- Mupmate Run option to convert PostScript to PDF via external converter
- Mupmate main window size changes are remembered
- MIDI file generation changes to better handle grace notes in endings
- Tags passed to user postscript are evaluated to their current value, not last

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Greg Bailey <gbailey@lxpro.com> - 6.5-3
- Patch null byte conversion errors (#1423973)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec  4 2016 Greg Bailey <gbailey@lxpro.com> - 6.5-1
- Update to 6.5
- Additional useaccs values: nonermuser and nonnatrmuser
- Abilty to force printing clef or time signature, even if they didn't change
- Transposition can be limited to just notes or just chords
- Grace notes allowed to have any non-dotted time value
- Barstyle options of all and between
- New subbarstyle parameter
- newscore can include scoresep
- Improved note spacing
- Alignment markers can be included in rom, bold, ital, boldital, and center
- Alternate double whole symbol
- gridsatend can be set in staff context

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Greg Bailey <gbailey@lxpro.com> - 6.4.1-1
- Update to 6.4.1:
- corrected problem with "extended" (non-ASCII) characters (broken by 6.4)
- properly parse multiple aliases (fixing the 6.4 feature PostScript hooks)

* Fri Jan  1 2016 Greg Bailey <gbailey@lxpro.com> - 6.4-1
- Update to 6.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 6.3-2
- rebuild (fltk)

* Thu Dec 11 2014 Greg Bailey <gbailey@lxpro.com> - 6.3-1
- Update to 6.3
- Revert "-Werror=format-security" patch (merged upstream)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Greg Bailey <gbailey@lxpro.com> - 6.2-2
- Patch errors resulting from the use of "-Werror=format-security" (#1037208)
- See https://fedorahosted.org/fesco/ticket/1185

* Mon Nov 25 2013 Greg Bailey <gbailey@lxpro.com> - 6.2-1
- Update to 6.2

* Wed Aug 07 2013 Greg Bailey <gbailey@lxpro.com> - 6.1-7
- Cleanup documentation directory macros (Chuck Anderson)

* Mon Aug 05 2013 Greg Bailey <gbailey@lxpro.com> - 6.1-6
- Install documentation to an unversioned subdir for Fedora >= 20 (#992308)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Greg Bailey <gbailey@lxpro.com> 6.1-4
- Include mupmate.desktop as an actual source file

* Fri Feb 15 2013 Greg Bailey <gbailey@lxpro.com> 6.1-3
- Change license tag to "Mup"

* Mon Jan 28 2013 Greg Bailey <gbailey@lxpro.com> 6.1-2
- Adapt filepaths to Filesystem Hierarchy Standard
- Add Mupmate desktop file so it appears in the desktop menu
- Original Arkkra mup.spec changelog available in extras/mup.spec

* Sat Jan 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 6.1-1
- Initial development

