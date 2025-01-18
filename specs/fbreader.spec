%global obsNVR 0.12.11

Name:           fbreader
Version:        0.99.4
Release:        18%{?dist}
Summary:        E-book reader

License:        GPL-2.0-or-later
URL:            http://www.fbreader.org/
Source0:        http://www.fbreader.org/files/desktop/fbreader-sources-%{version}.tgz
Patch0:         %{name}-0.99.4-optflags.patch
Patch1:         %{name}-0.99.4-default_browser.patch

# libunibreak dropped i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  fribidi-devel
BuildRequires:  libcurl-devel
BuildRequires:  libunibreak-devel
BuildRequires:  qt4-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires: make

# needed because sometimes the API change without soname bump
Requires:       zlibrary%{?_isa} = %{version}-%{release}
Provides:       %{name}-qt = %{version}-%{release}
Obsoletes:      %{name}-qt < %{obsNVR}
Obsoletes:      %{name}-gtk < %{obsNVR}

# bz #1624218
ExcludeArch:    armv7hl

%description
FBReader is an e-book reader, with the following main features:

* Supports several formats: fb2, HTML, CHM, plucker, Palmdoc, zTxt
  (Weasel), TCR (psion), RTF, OEB, OpenReader, mobipocket, plain text.
* Direct reading from tar, zip, gzip and bzip2 archives. (Multiple
  books in one archive are supported.)
* Automatic library building.
* Automatic encoding detection is supported.
* Automatically generated contents table.
* Embedded images support.
* Footnotes/hyperlinks support.
* Position indicator.
* Keeps the last open book and the last read positions for all opened
  books between runs.
* List of last opened books.
* Automatic hyphenations. Liang's algorithm is used. The same
  algorithm is used in TeX, and TeX hyphenation patterns are used in
  FBReader. Patterns for Czech, English, Esperanto, French, German and
  Russian are included in the current version.
* Text search.
* Full-screen mode.
* Screen rotation by 90, 180 and 270 degrees.


%package -n     zlibrary
Summary:        Cross-platform GUI library
Provides:       zlibrary-ui-qt = %{version}-%{release}
Obsoletes:      zlibrary-ui-qt < %{obsNVR}
Obsoletes:      zlibrary-ui-gtk < %{obsNVR}

%description -n zlibrary
ZLibrary is a cross-platform library to build applications running on
desktop Linux, Windows, and different Linux-based PDAs.


%package -n     zlibrary-devel
Summary:        Development files for zlibrary
Requires:       zlibrary%{?_isa} = %{version}-%{release}

%description -n zlibrary-devel
This package contains the libraries amd header files that are needed
for writing applications with Zlibrary.


%prep
%autosetup -p 1


%build
%make_build


%install
%make_install LIBDIR=%{_libdir}
%make_install do_install_dev LIBDIR=%{_libdir}
desktop-file-install \
  --remove-category="Application" \
  --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/FBReader.desktop



%ldconfig_scriptlets -n zlibrary


%files
%license fbreader/LICENSE
%doc ChangeLog
%{_bindir}/FBReader
%{_datadir}/FBReader
%{_datadir}/applications/FBReader.desktop
%{_datadir}/pixmaps/FBReader.png
%{_datadir}/pixmaps/FBReader

%files -n zlibrary
%doc fbreader/LICENSE
%{_libdir}/lib*.so.*
%{_datadir}/zlibrary

%files -n zlibrary-devel
%{_includedir}/*
%{_libdir}/lib*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Vojtech Trefny <vtrefny@redhat.com> - 0.99.4-16
- Rebuilt for libunibreak 6 (#2269138)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Sandro <devel@penguinpee.nl> - 0.99.4-13
- Stop building for i686

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.99.4-2
- Exclude building on armv7hl (bz #1624218)

* Wed Aug 29 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.99.4-1
- Update to 0.99.4
- Obsolete zlibrary-ui-{gtk,qt} - only Qt4 is supported now

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.10-17
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.12.10-13
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.12.10-11
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.12.10-10
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.12.10-6
- Rebuild for new libpng

* Mon Aug  1 2011 Michel Salim <salimma@fedoraproject.org> - 0.12.10-5
- Fix incorrect alternative-removal scriptlet

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.12.10-3
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.10-2
- Fix for compiling under GCC 4.5 (filed upstream, #384)

* Mon Jun  7 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.10-1
- Update to 0.12.10

* Sun Mar 28 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.9-1
- Update to 0.12.9

* Sat Feb 13 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2
- Fix overlap between fbreader and zlibrary

* Tue Jan 26 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Sat Oct 17 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.7-4
- Provide virtual packages for each available interface
- Use alternatives to select the user interface (see README.Fedora)

* Thu Sep 17 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.7-3
- Split out zlibrary and zlibrary-ui subpackages (fixes bz# 523946)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.7-1
- Update to 0.10.7

* Tue Feb 24 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.3-3
- Fix for GCC 4.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.3-1
- Update to 0.10.3

* Wed Jan 28 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Wed Jan 14 2009 Michel Salim <salimma@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Thu Jul 31 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.17-1
- Update to 0.8.17

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.12-2
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.12-1
- Update to 0.8.12

* Mon Jan  7 2008 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.10-1
- Update to 0.8.10
- Remove workaround for PDB issues on x86_64; fixed upstream

* Thu Dec 20 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.8a-1
- Update to 0.8.8a
- Workaround for PDB format handler when reading certain files

* Wed Dec 19 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.8-2
- Fix inclusion of debug files where libdir=/usr/lib (bz #411891)

* Sun Dec  2 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.8-1
- Update to 0.8.8

* Thu Oct 18 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.6d-3
- Generate proper -debuginfo subpackage (bz #329841, Ville Skytta)
- Add README.Fedora detailing zTXT bug on x86_64

* Sat Sep 22 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.6d-2
- Fix vendor tag
- Use compiler flags provided by the system

* Sun Sep 16 2007 Michel Alexandre Salim <michel.sylvan@gmail.com> - 0.8.6d-1
- Initial package
