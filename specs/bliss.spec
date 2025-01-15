%global giturl  https://github.com/ds4dm/Bliss

Name:           bliss
Version:        0.77
Release:        9%{?dist}
Summary:        Compute automorphism groups and canonical labelings of graphs

License:        LGPL-3.0-only
URL:            https://users.aalto.fi/~tjunttil/bliss/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/Bliss-%{version}.tar.gz
# Man page written by Jerry James using text borrowed from the sources.
# The man page therefore has the same copyright and license as the sources.
Source1:        bliss.1
# Patch from Thomas Rehn, sent upstream 28 Oct 2011.  Fix one bug and add one
# performance enhancement.
Patch:          bliss-rehn.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Bliss is an open source tool for computing automorphism groups and
canonical forms of graphs.  It has both a command line user interface as
well as C++ and C programming language APIs.

%package devel
# The content is LGPL-3.0-only.  Other licenses are due to files installed by
# doxygen.
# html/bc_s.png: GPL-1.0-or-later
# html/bdwn.png: GPL-1.0-or-later
# html/closed.png: GPL-1.0-or-later
# html/doc.png: GPL-1.0-or-later
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/folderclosed.png: GPL-1.0-or-later
# html/folderopen.png: GPL-1.0-or-later
# html/jquery.js: MIT
# html/menu.js: MIT
# html/menudata.js: MIT
# html/nav_f.png: GPL-1.0-or-later
# html/nav_g.png: GPL-1.0-or-later
# html/nav_h.png: GPL-1.0-or-later
# html/open.png: GPL-1.0-or-later
# html/splitbar.png: GPL-1.0-or-later
# html/sync_off.png: GPL-1.0-or-later
# html/sync_on.png: GPL-1.0-or-later
# html/tab_a.png: GPL-1.0-or-later
# html/tab_b.png: GPL-1.0-or-later
# html/tab_h.png: GPL-1.0-or-later
# html/tab_s.png: GPL-1.0-or-later
# html/tabs.css: GPL-1.0-or-later
License:        LGPL-3.0-only AND MIT AND GPL-1.0-or-later
Summary:        Headers and library files for developing with bliss
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Headers and library files needed to develop applications that use the
bliss library.

%package libs
Summary:        Compute automorphism groups and canonical labelings of graphs

%description libs
A command-line bliss tool to access the functionality of the bliss
library.

%prep
%autosetup -n Bliss-%{version} -p0

%conf
# Do not override Fedora build flags.  The last sagemath version added an
# soname.  Duplicate it for compatibility.  Link the library with libgmp.
# Hidden symbols hide ALL symbols, meaning we can't use the library.
sed -e 's/ -O3//' \
    -e '/POSITION_INDEPENDENT/a\ \ VERSION 2.0.0 SOVERSION 2' \
    -e '/^install($/itarget_link_libraries(libbliss ${GMP_LIBRARIES})' \
    -e '/VISIBILITY/d' \
    -i CMakeLists.txt

# Fix installation directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' CMakeLists.txt
fi

%build
%cmake -DUSE_GMP:BOOL=ON
%cmake_build

# Build the documentation
doxygen

%install
%cmake_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
sed 's/@VERSION@/%{version}/' %{SOURCE1} > %{buildroot}%{_mandir}/man1/bliss.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/bliss.1

%files
%{_bindir}/bliss
%{_mandir}/man1/bliss.1*

%files devel
%doc html
%{_includedir}/bliss
%{_libdir}/libbliss.so
%{_libdir}/cmake/Bliss/

%files libs
%doc CHANGES.txt
%license COPYING COPYING.LESSER
%{_libdir}/libbliss.so.2*

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Jerry James <loganjerry@gmail.com> - 0.77-8
- Build the SCIP fork
- Do not build for 32-bit x86

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 0.77-3
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 0.77-1
- Version 0.77
- Switch to new upstream URLs

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 0.73-15
- Switch to github URLs

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.73-13
- Switch to using the sagemath sources
- Drop -error patch; nobody else uses it and it changes the contract

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 0.73-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.72-12
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar  6 2015 Jerry James <loganjerry@gmail.com> - 0.72-11
- Link with RPM_LD_FLAGS

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 0.72-10
- Note bundled jquery
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 0.72-4
- Apply bug fix and performance enhancement patch from Thomas Rehn

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.72-3
- Rebuild for GCC 4.7.

* Tue Nov 15 2011 Jerry James <loganjerry@gmail.com> - 0.72-2
- Add patch to avoid calling exit() in the library

* Wed Jul 20 2011 Jerry James <loganjerry@gmail.com> - 0.72-1
- Initial RPM
