# Automated testing is difficult, since we really want to visually inspect
# the results of the tests.  I have not been able to find a useful automated
# test for this package, so the maintainer should always run this before
# pushing a new version:
#
# gap -l "%%{gap_archdir};" <<< 'Test("tst/test.tst");'
#
# That test is more useful if the altasrep package is also installed.

%global pkgname browse
%global upname Browse

# When bootstrapping a new architecture, there is no gap-pkg-atlasrep or
# gap-pkg-ctbllib package yet.  Those packages are needed only for testing this
# one, but require this package to function at all.  Therefore, do the
# following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-atlasrep in bootstrap mode.
# 3. Build gap-pkg-tomlib.
# 4. Build gap-pkg-ctbllib in bootstrap mode.
# 5. Build gap-pkg-atlasrep in non-bootstrap mode.
# 6. Build this package in non-bootstrap mode.
# 7. Build gap-pkg-ctbllib in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        1.8.20
Release:        1%{?dist}
Summary:        GAP browser for 2-dimensional arrays of data

License:        GPL-3.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://www.math.rwth-aachen.de/~Browse/
Source0:        %{url}/%{upname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  pkgconfig(ncurses)

%if %{without bootstrap}
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-tomlib
%endif

Requires:       gap-core%{?_isa}

Recommends:     gap-pkg-atlasrep
Recommends:     gap-pkg-io%{?_isa}

# Don't Provide the ncurses glue
%global __provides_exclude_from ncurses\\.so

%description
The motivation for this package was to develop functions for an
interactive display of two-dimensional arrays of data, for example
character tables.  They should be displayed with labeled rows and
columns, the display should allow some markup for fonts or colors, it
should be possible to search for entries, to sort rows or columns, to
hide and unhide information, to bind commands to keys, and so on.

To achieve this our package now provides three levels of functionality,
where in particular the first level may also be used for completely
other types of applications:
- A low level interface to ncurses: This may be interesting for all
  kinds of applications which want to display text with some markup and
  colors, maybe in several windows, using the available capabilities of
  a terminal.
- A medium level interface to a generic function NCurses.BrowseGeneric:
  We introduce a new operation Browse which is meant as an interactive
  version of Display for GAP objects.  Then we provide a generic
  function for browsing two-dimensional arrays of data, handles labels
  for rows and columns, searching, sorting, binding keys to actions,
  etc.  This is for users who want to implement new methods for browsing
  two-dimensional data.
- Applications of these interfaces: We provide some applications of the
  ncurses interface and of the function NCurses.BrowseGeneric.  These
  may be interesting for end users, and also as examples for programmers
  of further applications.  This includes a method for browsing
  character tables, several games, and an interface for demos.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Gap browser documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-io-doc

%if %{without bootstrap}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-ctbllib-doc
%endif

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

# Give an executable script a shebang
sed -i '1i#!/bin/sh' bibl/getnewestbibfile

%build
export LC_ALL=C.UTF-8
# This is NOT an autoconf-generated configure script
./configure %{gap_archdir}
%make_build

# Link to main GAP documentation
mkdir ../pkg
ln -s ../%{upname} ../pkg
gap -l "$PWD/..;" makedocrel.g
rm -fr ../pkg

# Fix links
sed -i "s,$PWD/\.\./pkg,..,g" doc/*.html

%install
rm tst/*~
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a app bibl bin lib tst version *.g %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%files
%doc CHANGES README
%license doc/GPL
%{gap_archdir}/pkg/%{upname}/
%exclude %{gap_archdir}/pkg/%{upname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
* Thu Jan 19 2023 Jerry James <loganjerry@gmail.com> - 1.8.20-1
- Version 1.8.20

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.8.19-2
- Update for split GAP directories

* Fri Dec  9 2022 Jerry James <loganjerry@gmail.com> - 1.8.19-1
- Version 1.8.19

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.8.18-1
- Clarify license of the doc subpackage

* Tue Oct 18 2022 Jerry James <loganjerry@gmail.com> - 1.8.18-1
- Version 1.8.18

* Tue Oct  4 2022 Jerry James <loganjerry@gmail.com> - 1.8.17-1
- Version 1.8.17

* Sat Oct  1 2022 Jerry James <loganjerry@gmail.com> - 1.8.16-1
- Version 1.8.16

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.8.15-1
- Version 1.8.15
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.8.14-3
- Convert License tag to SPDX

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 1.8.14-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 1.8.14-1
- Version 1.8.14

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov  7 2021 Jerry James <loganjerry@gmail.com> - 1.8.13-1
- Version 1.8.13

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 18 2021 Jerry James <loganjerry@gmail.com> - 1.8.12-1
- Version 1.8.12

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Jerry James <loganjerry@gmail.com> - 1.8.11-1
- Version 1.8.11

* Wed Aug 19 2020 Jerry James <loganjerry@gmail.com> - 1.8.10-1
- Version 1.8.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 1.8.9-1
- Version 1.8.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 1.8.8-6
- Rebuild for changed bin dir name in gap 4.10.1

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.8.8-5
- Rebuild in non-bootstrap mode

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.8.8-4
- Rebuild for gap 4.10.0 in bootstrap mode
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  9 2018 Jerry James <loganjerry@gmail.com> - 1.8.8-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Jerry James <loganjerry@gmail.com> - 1.8.7-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.8.6-6
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.8.6-4
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Jerry James <loganjerry@gmail.com> - 1.8.6-2
- Add Requires(post) and Requires(postun)
- Mark documentation as such
- Add linker flags

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 1.8.6-1
- Initial RPM
