Name:           cddlib
Epoch:          1
Version:        0.94m
Release:        6%{?dist}
Summary:        A library for generating all vertices in convex polyhedrons
License:        GPL-2.0-or-later
URL:            https://people.inf.ethz.ch/fukudak/cdd_home/
Source0:        https://github.com/cddlib/cddlib/releases/download/%{version}/%{name}-%{version}.tar.gz
# Fix a segfault in blockelimination
Patch0:         https://github.com/cddlib/cddlib/commit/f83bdbc.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(latex)

%description
The C-library cddlib is a C implementation of the Double Description 
Method of Motzkin et al. for generating all vertices (i.e. extreme points)
and extreme rays of a general convex polyhedron in R^d given by a system 
of linear inequalities:

   P = { x=(x1, ..., xd)^T :  b - A∙x ≥ 0 }

where A is a given m×d real matrix, b is a given m-vector
and 0 is the m-vector of all zeros.

The program can be used for the reverse operation (i.e. convex hull
computation). This means that one can move back and forth between 
an inequality representation and a generator (i.e. vertex and ray) 
representation of a polyhedron with cdd. Also, cdd can solve a linear
programming problem, i.e. a problem of maximizing and minimizing 
a linear function over P.


%package devel
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        Headers for cddlib
Requires:       gmp-devel%{?_isa}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description devel
Include files for cddlib.


%package static
Summary:        Static libraries for cddlib

%description static
Static libraries for cddlib.


%package tools
Summary:        Sample binaries that use cddlib
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description tools
Sample binaries that use cddlib.


%prep
%autosetup -p1

# Fix the FSF's address
for f in `find . -type f -print0 | xargs -0 grep -Fl '675 Mass'`; do
  sed -i.orig \
    's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    $f
  touch -r $f.orig $f
  rm -f $f.orig
done

# Force rebuilding of the documentation
rm -f doc/cddlibman.pdf


%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Need one more invocation of pdflatex to get cross references correct
pushd doc
pdflatex cddlibman
popd


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Do not prematurely install documentation
rm -fr %{buildroot}%{_pkgdocdir}


%files
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libcdd.so.0*
%{_libdir}/libcddgmp.so.0*


%files devel
%doc doc/cddlibman.pdf examples*
%{_includedir}/cddlib
%{_libdir}/libcdd.so
%{_libdir}/libcddgmp.so
%{_libdir}/pkgconfig/%{name}.pc


%files static
%{_libdir}/libcdd.a
%{_libdir}/libcddgmp.a


%files tools
%{_bindir}/adjacency
%{_bindir}/adjacency_gmp
%{_bindir}/allfaces
%{_bindir}/allfaces_gmp
%{_bindir}/cddexec
%{_bindir}/cddexec_gmp
%{_bindir}/fourier
%{_bindir}/fourier_gmp
%{_bindir}/lcdd
%{_bindir}/lcdd_gmp
%{_bindir}/projection
%{_bindir}/projection_gmp
%{_bindir}/redcheck
%{_bindir}/redcheck_gmp
%{_bindir}/scdd
%{_bindir}/scdd_gmp
%{_bindir}/testcdd1
%{_bindir}/testcdd1_gmp
%{_bindir}/testcdd2
%{_bindir}/testcdd2_gmp
%{_bindir}/testlp1
%{_bindir}/testlp1_gmp
%{_bindir}/testlp2
%{_bindir}/testlp2_gmp
%{_bindir}/testlp3
%{_bindir}/testlp3_gmp
%{_bindir}/testshoot
%{_bindir}/testshoot_gmp

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94m-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Jerry James <loganjerry@gmail.com> - 1:0.94m-5
- Add patch to fix a segfault in blockelimination
- Clarify documentation-related licenses

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 1:0.94m-4
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94m-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94m-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94m-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Jerry James <loganjerry@gmail.com> - 1:0.94m-1
- Version 0.94m

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94l-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Jerry James <loganjerry@gmail.com> - 1:0.94l-1
- Version 0.94l

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 1:0.94j-4
- Drop cdd_both_reps.c and accompanying patch, replaced with cddexec

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  1 2018 Jerry James <loganjerry@gmail.com> - 0.94j-1
- New upstream release
- Add Epoch to deal with new dot in the version number

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 094i-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 094i-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 094h-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 094h-7
- Rebuild without linker aliases, no longer needed
- Update URLs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 094h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094h-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 094h-1
- New upstream release

* Thu Mar 12 2015 Jerry James <loganjerry@mgail.com> - 094g-13
- Rebuild with hardening flags

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 094g-12
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jerry James <loganjerry@gmail.com> - 094g-7
- Add function aliases in the GMP build for polymake
- License fixing code now handles names with spaces

* Sat Jul 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 094g-6
- Add libtool to build requires

* Sun Jul 22 2012 Conrad Meyer <konrad@tylerc.org> - 094g-5
- Add automake BR too

* Sun Jul 22 2012 Conrad Meyer <konrad@tylerc.org> - 094g-4
- Add autoconf BR as per mass rebuild build failure

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 094g-2
- Add sagemath patches

* Tue Apr 24 2012 Jerry James <loganjerry@gmail.com> - 094g-1
- New upstream release
- All patches upstreamed
- Non-free sources removed from upstream tarball

* Fri Apr 20 2012 Jerry James <loganjerry@gmail.com> - 094f-15
- Package the sample binaries in -tools for the use of projects such as LattE
- Add memleak patch from upstream

* Fri Feb 24 2012 Jerry James <loganjerry@gmail.com> - 094f-14
- Actually apply the const patch

* Fri Feb 24 2012 Jerry James <loganjerry@gmail.com> - 094f-13
- Add const qualifier to public function parameters
- Fix the FSF's address

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 094f-12
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 094f-11.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 094f-11.1
- rebuild with new gmp

* Thu Apr  7 2011 Jerry James <loganjerry@gmail.com> - 094f-11
- Build shared libraries as well as static
- Drop BuildRoot and the clean section

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-7
- Install headers with install -p to save timestamps.
- Install headers to namespaced directory.
- Generate pdf from latex source.

* Fri Oct 31 2008 Conrad Meyer <konrad@tylerc.org> - 094f-6
- Describe vividly the process whereby the non-free file is
  stripped from the source tarball.

* Thu Oct 30 2008 Conrad Meyer <konrad@tylerc.org> - 094f-5
- Tarball scrubbed of content we are unable to ship.

* Tue Oct 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-4
- Remove modules that do not meet licensing guidelines.
- Don't generate debuginfo.

* Tue Oct 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-3
- Fix permissions on documentation.

* Mon Oct 27 2008 Conrad Meyer <konrad@tylerc.org> - 094f-2
- Incorporate several suggestions from review.

* Thu Sep 25 2008 Conrad Meyer <konrad@tylerc.org> - 094f-1
- Initial package.
