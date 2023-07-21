# NOTE on SAT implementations.
# Upstream wants MathSat, which is nonfree and closed source.  We can do
# without the solving capability, or we can look for an alternative:
# - glpk: either solves for floating point numbers or integers, but we need to
#   solve for rational solutions.  Looks infeasible.
# - CVC4: has a rational solver, unknown whether it accepts constraints
# - linbox: has a rational solver, unknown whether it accepts constraints
# - one of the coin-or-* packages might provide a suitable solver

Name:           cocoalib
Version:        0.99818
Release:        2%{?dist}
Summary:        C++ library for computations in commutative algebra

License:        GPL-3.0-or-later
URL:            https://cocoa.dima.unige.it/cocoa/cocoalib/
Source0:        %{url}/tgz/CoCoALib-%{version}.tgz
# Build a shared library instead of a static library
Patch0:         %{name}-shared.patch
# Fix error handling in Qsolve
Patch1:         %{name}-ffelem.patch
# Fix out of bounds vector accesses
Patch2:         %{name}-vec.patch
# Avoid using a variable uninitialized
Patch3:         %{name}-uninit.patch
# CVC5 patch to enable tracing
Patch4:         %{name}-cvc5.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libfrobby-devel
BuildRequires:  libgfan-devel
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)

%description
The CoCoA C++ library offers functions to perform calculations in
Computational Commutative Algebra, and some other related areas.  The
library is designed to be pleasant to use while offering good run-time
performance.

%package devel
Summary:        Headers and library links for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       gsl-devel%{?_isa}
Requires:       libgfan-devel%{?_isa}

%description devel
Headers and library links for developing applications that use %{name}.

%package doc
# The content is GFDL-1.2-no-invariants-only.  The remaining licenses cover the
# various fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GFDL-1.2-no-invariants-only AND Knuth-CTAN
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p0 -n CoCoALib-%{version}

# Use FlexiBLAS instead of the reference lapack/blas implementation.
# Do not throw away our choice of compiler flags.
# Fix the location of the cddlib headers.
sed -e 's,-lgslcblas  -llapack,-lflexiblas,' \
    -e 's/ -Wall  -pedantic/ $CXXFLAGS/' \
    -e 's,\(CDD_INC_DIR=\)".*",\1"%{_includedir}/cddlib",' \
    -i configure

# Do not suppress compiler command lines
sed -i 's/\$(MAKE) -s/\$(MAKE)/' Makefile doc/Makefile src/Makefile \
    src/AlgebraicCore/Makefile src/AlgebraicCore/TmpFactorDir/Makefile

%build
# Use Fedora's linker flags
sed -i 's|@RPM_LD_FLAGS@|%{build_ldflags}|' src/AlgebraicCore/Makefile

# This is NOT an autoconf-generated configure script!
./configure --prefix=%{_prefix} --only-cocoalib --threadsafe-hack \
  --with-cxxflags='%{build_cxxflags} -fPIC -I%{_includedir}/frobby -I%{_includedir}/gfanlib %{build_ldflags}' \
  --with-libcddgmp=%{_libdir}/libcddgmp.so \
  --with-libfrobby=%{_libdir}/libfrobby.so \
  --with-libgfan=%{_libdir}/libgfan.so \
  --with-libgsl=%{_libdir}/libgsl.so

%make_build library
%make_build doc

%install
# The Makefile ignores DESTDIR.  Install by hand.

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p src/AlgebraicCore/libcocoa.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcocoa.so.0.0.0 %{buildroot}%{_libdir}/libcocoa.so.0
ln -s libcocoa.so.0 %{buildroot}%{_libdir}/libcocoa.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}
cp -a include/CoCoA %{buildroot}%{_includedir}
rm -f %{buildroot}%{_includedir}/{MakeUnifiedHeader.sh,PREPROCESSOR_DEFNS.H-old}

# Remove files from the doc directories that we want to include in %%files
rm -f doc/CoCoALib-tasks/{HTMLTasks,HTMLTasks.C,Makefile,tasks.xml}
rm -f examples/CopyInfo
chmod a-x examples/*.sh

%check
export LD_LIBRARY_PATH=$PWD/lib
make check

%files
%license COPYRIGHT-full-text
%doc README
%{_libdir}/libcocoa.so.0*

%files devel
%{_includedir}/CoCoA
%{_libdir}/libcocoa.so

%files doc
%license doc/COPYING
%doc doc/*.html
%doc doc/*.pdf
%doc doc/CoCoALib-tasks
%doc doc/html
%doc examples

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99818-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Jerry James <loganjerry@gmail.com> - 0.99818-1
- Version 0.99818
- Drop upstreamed patches: noreturn, vector-size
- Add cvc5 patch to enable tracing
- Stop building for i386

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99800-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99800-4
- Rebuild for gsl-2.7.1

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 0.99800-3
- Convert License tags to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99800-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 0.99800-2
- Drop unnecessary Java dependency (rhbz#2104028)

* Thu Mar 24 2022 Jerry James <loganjerry@gmail.com> - 0.99800-1
- Version 0.99800
- Drop upstreamed -gfanlib and -no-copy patches
- Add -vector-size patch to fix FTBFS

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.99717-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Jerry James <loganjerry@gmail.com> - 0.99717-1
- Version 0.99717

* Mon Oct 11 2021 Jerry James <loganjerry@gmail.com> - 0.99716-1
- Version 0.99716
- Drop upstreamed -apply and -32bit patches

* Fri Sep 24 2021 Jerry James <loganjerry@gmail.com> - 0.99715-1
- Version 0.99715
- Add -32bit patch

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99713-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 0.99713-1
- Version 0.99713
- Add -no-copy patch

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 0.99712-1
- Version 0.99712

* Tue Jan 26 2021 Jerry James <loganjerry@gmail.com> - 0.99711-2
- Add -apply patch to fix FTBFS

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Jerry James <loganjerry@gmail.com> - 0.99711-1
- Version 0.99711
- Disable test-RingTwinFloat3 on 32-bit platforms

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.99710-3
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99710-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.99710-1
- Version 0.99710

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 0.99700-1
- Version 0.99700

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99650-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 0.99650-1
- Version 0.99650
- Drop upstreamed -include and -bigrat patches

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.99601-3
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Jerry James <loganjerry@gmail.com> - 0.99601-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99600-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.99600-2
- Build with openblas instead of atlas (bz 1618942)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 0.99600-1
- New upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99564-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Jerry James <loganjerry@gmail.com> - 0.99564-1
- New upstream version
- Drop upstreamed -return patch
- Add -include and -bigrat patches to fix FTBFS

* Mon Jun 11 2018 Jerry James <loganjerry@gmail.com> - 0.99563-2
- Make -doc subpackage noarch

* Sat Jun  9 2018 Jerry James <loganjerry@gmail.com> - 0.99563-1
- Initial RPM
