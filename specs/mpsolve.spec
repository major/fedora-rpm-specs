# The octave_pkg_install macro assumes a package that is only octave code, not
# an addon like in this package.  We define our own version of the macro here
# to operate only on the correct directory.
%global my_octave_pkg_install \
mkdir -p %{buildroot}%{octprefix} \
mkdir -p %{buildroot}%{octarchprefix} \
%octave_cmd pkg("prefix","%{buildroot}%{octprefix}","%{buildroot}%{octarchprefix}");pkg("global_list",fullfile("%{buildroot}%{octshareprefix}","octave_packages"));pkg("install","-nodeps","-verbose",glob("%{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}-*.tar.gz"){1,1});unlink(pkg("global_list")); \
if [ -e %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m ] \
then \
  mv %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m.orig \
fi \
echo "function on_uninstall (desc)" > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "  error ('Can not uninstall %s installed by the redhat package manager', desc.name);" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "endfunction" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
if [ -e %{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}/*.metainfo.xml ] \
then \
  echo "Found .metainfo.xml appdata file" \
  mkdir -p %{buildroot}/%{_metainfodir} \
  cp -p %{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}/*.metainfo.xml %{buildroot}/%{_metainfodir}/ \
  appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml \
else \
  echo "Did not find a .metainfo.xml appdata file" \
fi \
%{nil}

%global giturl  https://github.com/robol/MPSolve

Name:           mpsolve
Version:        3.2.1
Release:        24%{?dist}
Summary:        Multiprecision polynomial solver

License:        GPL-3.0-or-later
URL:            https://numpi.dm.unipi.it/software/mpsolve
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix mutex and condvar leaks
# https://github.com/robol/MPSolve/commit/a3f7bf39b4efdaab3fe6becb948b61c4e5ab390b
# https://github.com/robol/MPSolve/commit/1d073406146920b37d292357fdef5884d1670d67
Patch:          %{name}-mutex-leak.patch
# Fix configure.ac to work with autoconf 2.70+
# https://github.com/robol/MPSolve/commit/3a890878239717e1d5d23f574e4c0073a7249f7a
Patch:          %{name}-autoconf-2.70.patch
# Fix coefficient leaks
# https://github.com/robol/MPSolve/commit/2545de499edb272dbe7c4b03861d13e022d8b5d2
Patch:          %{name}-coefficient-leak.patch
# Updates for octave 6.x
# https://github.com/robol/MPSolve/pull/31
Patch:          %{name}-octave.patch
# Fix LTO warnings about mismatched types
Patch:          %{name}-lto.patch
# Fix configure tests with Modern C
# See https://fedoraproject.org/wiki/Changes/PortingToModernC
# https://github.com/robol/MPSolve/pull/33
Patch:          %{name}-modern-c.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bison
BuildRequires:  doxygen-latex
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(octave)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  python3-devel
BuildRequires:  tex(dvips)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _desc %{expand:
MPSolve stands for Multiprecision Polynomial SOLVEr.  It aims to provide
an easy to use universal blackbox for solving polynomials and secular
equations.

Its features include:
- Arbitrary precision approximation.
- Guaranteed inclusion radii for the results.
- Exploiting of polynomial structures: it can take advantage of sparsity
  as well as coefficients in a particular domain (i.e. integers or
  rationals).
- It can be specialized for specific classes of polynomials.  As an
  example, the roots of the Mandelbrot polynomial of degree 2,097,151
  were computed in about 10 days on a dual Xeon server.}

%description %_desc

This package contains command-line interfaces to %{name}.

%package        libs
Summary:        Multiprecision polynomial solver library

%description    libs %_desc

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc %_desc

This package contains developer documentation for %{name}.

%package        devel
Summary:        Headers and library links for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
This package contains header and library links for developing
applications that use %{name}.

%package     -n xmpsolve
Summary:        Qt GUI for mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}

%description -n xmpsolve %_desc

This package contains a Qt-based graphical interface to mpsolve.

%package     -n python3-mpsolve
Summary:        Python 3 interface to mpsolve
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-mpsolve %_desc

This package contains a python 3 interface to mpsolve.

%global octpkg  %{name}

%package     -n octave-mpsolve
Summary:        Octave interface to mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{?octave_api}%{!?octave_api:0}
Requires(post): octave
Requires(postun): octave

%description -n octave-mpsolve %_desc

This package contains an octave interface to mpsolve.

%prep
%autosetup -n MPSolve-%{version} -p1

%conf
# Fix the version number in the octave interface
sed -i 's/3\.1\.7/%{version}/' examples/octave/DESCRIPTION
cp -p examples/octave/DESCRIPTION examples/matlab

# Octave wants the COPYING file
cp -p COPYING examples/matlab

# We do not need both HTML and PDF documentation
sed -i '/GENERATE_LATEX/s/YES/NO/' doc/Doxyfile.in

# Doxygen wants the CSS file up one level
cp -p doc/doxygen/doxygen.css doc

# Invoke python3, not python
sed -i 's,%{_bindir}/env python,%{python3},' examples/python/tests/*.py

# Do not force use of -fomit-frame-pointer
sed -i '/-fomit-frame-pointer/d' configure.ac

# Generate the configure script
autoreconf -fi .

%build
%configure --disable-static --disable-debug --enable-qml-ui LIBS=-lpthread

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Work around https://bugs.ghostscript.com/show_bug.cgi?id=702024
export GS_OPTIONS=-dNOSAFER

%make_build

# Build the octave package the Fedora way
cd examples/matlab
mkdir -p MPSolve-%{version}/src
mkoctfile -I../../include -c -o mps_interp.o mps_interp.c
mkoctfile -I../../include -c -o mps_kostlan.o mps_kostlan.c
mkoctfile -I../../include -c -o mps_option_parser.o mps_option_parser.c
mkoctfile -I../../include -c -o mps_roots_double.o mps_roots_double.c
mkoctfile -I../../include -c -o mps_roots_string.o mps_roots_string.c
mkoctfile -o MPSolve-%{version}/src/mps_interp.oct -L../../src/libmps/.libs mps_interp.o -lmps -lmpfr
mkoctfile -o MPSolve-%{version}/src/mps_kostlan.oct -L../../src/libmps/.libs mps_kostlan.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_option_parser.oct -L../../src/libmps/.libs mps_option_parser.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_roots_double.oct -L../../src/libmps/.libs mps_roots_double.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_roots_string.oct -L../../src/libmps/.libs mps_roots_string.o -lmps
cp -p *.m MPSolve-%{version}/src
cp -p COPYING DESCRIPTION MPSolve-%{version}
tar cf mpsolve-%{version}-any-none.tar MPSolve-%{version}
gzip -9v mpsolve-%{version}-any-none.tar
cd -

%install
%make_install

# We do not want the libtool files
rm -f %{buildroot}%{_libdir}/*.la

# Move the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
mv %{buildroot}%{_datadir}/icons/xmpsolve.png \
   %{buildroot}%{_datadir}/icons/hicolor/192x192/apps

# Generate more icon sizes
for sz in 16 22 24 32 36 48 64 72 96 128 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  convert src/xmpsolve/xmpsolve.png -resize ${sz}x${sz} \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/xmpsolve.png
done

# Install the octave package the Fedora way
%my_octave_pkg_install

%check
make check

%post        -n octave-mpsolve
%octave_cmd pkg rebuild

%preun       -n octave-mpsolve
%octave_pkg_preun

%postun      -n octave-mpsolve
%octave_cmd pkg rebuild

%files
%{_bindir}/mandelbrot-solver
%{_bindir}/mpsolve
%{_bindir}/quadratic-solver
%{_bindir}/root_of_unity
%{_bindir}/secular
%{_mandir}/man1/mandelbrot-solver.1*
%{_mandir}/man1/mpsolve.1*
%{_mandir}/man1/quadratic-solver.1*

%files          libs
%doc AUTHORS README
%license COPYING
%{_libdir}/libmps.so.3*
%{_libdir}/libmps-fortran.so.0*

%files          doc
%doc doc/html/*
%license COPYING

%files          devel
%doc ChangeLog
%{_includedir}/mps/
%{_libdir}/libmps.so
%{_libdir}/libmps-fortran.so

%files       -n xmpsolve
%{_bindir}/xmpsolve
%{_datadir}/applications/xmpsolve.desktop
%{_datadir}/icons/hicolor/*/apps/xmpsolve.png
%{_datadir}/mime/packages/mpsolve.xml
%{_datadir}/mime-info/mpsolve.mime
%{_mandir}/man1/xmpsolve.1*

%files       -n python3-mpsolve
%{python3_sitelib}/mpsolve.py
%{python3_sitelib}/__pycache__/mpsolve.*

%files       -n octave-mpsolve
%{octpkglibdir}/
%dir %{octpkgdir}/
%{octpkgdir}/mps_chebroots.m
%{octpkgdir}/mps_roots.m
%{octpkgdir}/packinfo/
%doc %{octpkgdir}/doc-cache

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Jerry James <loganjerry@gmail.com> - 3.2.1-23
- Rebuild for octave 9.2.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jerry James <loganjerry@gmail.com> - 3.2.1-21
- Update %%my_octave_pkg_install for recent rpm changes

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.1-21
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 3.2.1-18
- Stop building for 32-bit x86

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 3.2.1-17
- Validate metainfo with appstream-util

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.2.1-17
- Rebuilt for Python 3.12

* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 3.2.1-16
- Rebuild for octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 3.2.1-14
- Add modern-c patch
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.1-12
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 3.2.1-11
- Rebuild for octave 7.1

* Tue May 24 2022 Jerry James <loganjerry@gmail.com> - 3.2.1-10
- Fix FTBFS with octave 7.1 (rhbz#2083937)
- Add -coefficient-leak patch to plug another memory leak

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Jerry James <loganjerry@gmail.com> - 3.2.1-8
- Rebuild for octave 6.3.0
- Add -octave and -lto patches to fix build issues

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.1-6
- Rebuilt for Python 3.10

* Thu Mar 25 2021 Jerry James <loganjerry@gmail.com> - 3.2.1-5
- Add -autoconf-2.70 patch (bz 1943108)
- Add -mutex-leak patch
- Upstream suggests building the matlab interface with octave in preference to
  the unmaintained octave interface

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-1
- Version 3.2.1
- The formerly missing files are now included in the tarball

* Thu Jun 11 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- Version 3.2.0
- Drop upstreamed patches: -strict-aliasing and -mpq-canonicalize

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 3.1.8-1
- Initial RPM
