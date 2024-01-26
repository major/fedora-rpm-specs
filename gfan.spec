Name:           gfan
Version:        0.6.2
Release:        18%{?dist}
Summary:        Software for Computing Gröbner Fans and Tropical Varieties
License:        GPL-2.0-or-later
URL:            https://math.au.dk/~jensen/software/gfan/gfan.html
Source0:        https://math.au.dk/~jensen/software/%{name}/%{name}%{version}.tar.gz
# Sent upstream 2011 Apr 27.  Fix warnings that could indicate runtime
# problems.
Patch0:         %{name}-warning.patch
# Treat plain "gfan" call as "gfan_bases" call (as done in previous versions)
# instead of warning that "gfan_bases" should be called and exiting
Patch1:         %{name}-permissive.patch
# Build a shared library
Patch2:         %{name}-shared.patch

BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glibc-langpack-en
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)
BuildRequires:  TOPCOM

Requires:       libgfan%{_isa} = %{version}-%{release}

Recommends:     TOPCOM

%global _docdir_fmt %{name}

%description
The software computes all marked reduced Gröbner bases of an ideal.
Their union is a universal Gröbner basis. Gfan contains algorithms for
computing this complex for general ideals and specialized algorithms
for tropical curves, tropical hypersurfaces and tropical varieties of
prime ideals. In addition to the above core functions the package
contains many tools which are useful in the study of Gröbner bases,
initial ideals and tropical geometry. Among these are an interactive
traversal program for Gröbner fans and programs for graphical renderings.

%package        doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Gfan examples and documentation files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
Gfan examples and documentation files.

%package        -n libgfan
Summary:        Polyhedral computations related to polynomial rings

%description    -n libgfan
Gfanlib has two major features:
1) high-level exact polyhedral cone and polyhedral fan classes;
2) fast exact mixed volume computation for lattice polytopes with overflow
   checking.

In particular, gfanlib is missing the Gröbner basis part of gfan.

%package        -n libgfan-devel
Summary:        Development files for libgfan
Requires:       libgfan%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    -n libgfan-devel
The libgfan-devel package contains libraries and header files for
developing applications that use libgfan.

%prep
%autosetup -n %{name}%{version} -p0

# Point to where the TOPCOM binaries will be installed
sed -i.orig "s|^\(#define MINKOWSKIPROGRAM \).*|\1\"%{_bindir}/essai\"|" \
  src/minkowskisum.cpp
touch -r src/minkowskisum.cpp.orig src/minkowskisum.cpp
rm -f src/minkowskisum.cpp.orig

# No need to install a simple upstream Makefile to rsync homepage
# directory to upstream page.
rm -f homepage/Makefile

%build
%make_build CC=gcc CXX=g++ \
  OPTFLAGS='%{build_cxxflags} -DGMPRATIONAL -I%{_includedir}/cddlib' \
  PREFIX=%{_prefix} \
  SOPLEX_LINKOPTIONS='%{build_ldflags}'

# Build the manual
cd doc
latex manual.tex
bibtex manual
latex manual.tex
latex manual.tex
dvipdf manual.dvi manual.pdf
cd -

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p src/libgfan.so.0.0.0 %{buildroot}%{_libdir}
ln -s libgfan.so.0.0.0 %{buildroot}%{_libdir}/libgfan.so.0
ln -s libgfan.so.0 %{buildroot}%{_libdir}/libgfan.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}/gfanlib
cp -p src/gfanlib*.h %{buildroot}%{_includedir}/gfanlib

# Fix the headers
for fil in %{buildroot}%{_includedir}/gfanlib/*.h; do
  sed -i.orig 's,#include "\(.*\)",#include <\1>,' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

# Install the binaries
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make install PREFIX=%{buildroot}%{_prefix}
cd %{buildroot}%{_bindir}
    ./%{name} installlinks
cd -


%check
# Some tests depend on US English collation order
export LC_ALL=en_US.UTF-8

# The xfig test output varies slightly by architecture, and is non-critical,
# so we skip that test.
rm -fr testsuite/0009RenderStairCase
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
./gfan _test


%files
%doc README
%license COPYING LICENSE
%{_bindir}/gfan*

%files doc
%doc doc/manual.pdf
%doc examples
%doc homepage

%files -n libgfan
%doc gfanlib/README.txt
%{_libdir}/libgfan.so.0*

%files -n libgfan-devel
%{_includedir}/gfanlib/
%{_libdir}/libgfan.so


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Jerry James <loganjerry@gmail.com> - 0.6.2-14
- Convert License tag to SPDX
- Recommend, rather than suggest, TOPCOM
- Move manual to the doc subpackage
- Minor spec file cleanups

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.2-6
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.6.2-5
- Rebuild for cddlib 0.94j

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.6.2-3
- Build and link with libgfan.so

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.6.2-1
- New upstream release
- License change to GPLv2+
- Manual is now free
- Drop upstreamed -format patch
- Drop unnecessary -respect-destdir patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5-13
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 10 2015 Jerry James <loganjerry@gmail.com> - 0.5-12
- Update URLs
- Link with RPM_LD_FLAGS
- Reenable tests

* Tue Feb 17 2015 Jerry James <loganjerry@gmail.com> - 0.5-11
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct  3 2013 Jerry James <loganjerry@gmail.com> - 0.5-8
- Update the project and source URLs
- Minor spec file cleanups

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5-5
- Disable back %%check as it fails only in ix86.

* Thu Jul 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5-4
- Use gfan itself to create symlinks.
- Create -doc subpackage and install the homepage dir as documentation.
- Reenable %%check.
- Add -permissive patch for sagemath interface.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.5-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5-1.1
- rebuild with new gmp

* Mon Apr 25 2011 Jerry James <loganjerry@gmail.com> - 0.5-1
- New upstream release.
- Drop BuildRoot tag, clean script, and clean at start of install script.
- Build against shared cddlib now that it is available.
- Fix some broken tests.
- Still cannot run the testsuite, as the tests will pass on one build attempt
  and then fail on another.  There is a Heisenbug somewhere....

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.3-7
- Explicitly BR cddlib-static in accordance with the Packaging
  Guidelines (cddlib-devel is still static-only).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Conrad Meyer <konrad@tylerc.org> - 0.3-5
- Include the right place for headers (fix FTBFS).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Conrad Meyer <konrad@tylerc.org> - 0.3-3
- Fix License tag.
- Fix build section.
- Remove doc/ in prep stage as it is non-free.

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 0.3-2
- BR texlive-latex.

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 0.3-1
- Initial package.
