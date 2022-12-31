Name:           4ti2
Version:        1.6.9
Release:        13%{?dist}
Summary:        Algebraic, geometric and combinatorial problems on linear spaces

%global relver %(tr . _ <<< %{version})

# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in the PDF manual.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later
URL:            https://4ti2.github.io/
Source0:        https://github.com/4ti2/4ti2/releases/download/Release_%{relver}/%{name}-%{version}.tar.gz
Source1:        4ti2.module.in
# Deal with a boolean variable that can somehow hold the value 2
Patch0:         %{name}-maxnorm.patch
Patch1:         %{name}-missing-include.patch

BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(epic.sty)

# 4ti2 contains a copy of gnulib, which has been granted a bundling exception:
# https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(gnulib)

Requires:       4ti2-libs%{?_isa} = %{version}-%{release}
Requires:       environment(modules)

%description
A software package for algebraic, geometric and combinatorial problems
on linear spaces.

This package uses Environment Modules.  Prior to invoking the binaries,
you must run "module load 4ti2-%{_arch}" to modify your PATH.

%package devel
Summary:        Headers needed to develop software that uses 4ti2
Requires:       4ti2-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Headers and library files needed to develop software that uses 4ti2.

%package libs
Summary:        Library for problems on linear spaces

%description libs
A library for algebraic, geometric and combinatorial problems on linear
spaces.

%prep
%autosetup -p0

# Add a missing executable bit
chmod a+x ltmain.sh

# Fix encodings
iconv -f ISO8859-1 -t UTF-8 NEWS > NEWS.utf8
touch -r NEWS NEWS.utf8
mv -f NEWS.utf8 NEWS

# Update the C++ standard
sed -i 's/c++0x/c++11/g' configure

# Silence "egrep is obsolescent" warnings
for f in $(grep -Frl egrep src/groebner test); do
  sed -i.orig 's/egrep/grep -E/g' $f
  touch -r $f.orig $f
  rm $f.orig
done

%build
%configure --enable-shared --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Build the manual
export LD_LIBRARY_PATH=$PWD/src/4ti2/.libs:$PWD/src/fiber/.libs:$PWD/src/groebner/.libs:$PWD/src/ppi/.libs:$PWD/src/util/.libs:$PWD/src/zsolve/.libs
pushd doc
make update-manual
bibtex 4ti2_manual
pdflatex -interaction=batchmode 4ti2_manual
pdflatex -interaction=batchmode 4ti2_manual
popd

%install
%make_install

# Move the include files into a private directory
mkdir -p %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/{4ti2,groebner,util,zsolve} \
   %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/tmp %{buildroot}%{_includedir}/4ti2

# Move the 4ti2 binaries
mkdir -p %{buildroot}%{_libdir}/4ti2
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/4ti2

# Make the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#'%{_libdir}/4ti2'#g;' < %SOURCE1 >%{buildroot}%{_modulesdir}/4ti2-%{_arch}

# We don't need or want libtool files
rm -f %{buildroot}%{_libdir}/*.la

# We don't want documentation in _datadir
rm -fr %{buildroot}%{_datadir}/4ti2/doc

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check

%files
%doc doc/4ti2_manual.pdf
%{_libdir}/4ti2/
%{_modulesdir}/4ti2-%{_arch}

%files devel
%{_includedir}/4ti2/
%{_libdir}/lib4ti2*.so
%{_libdir}/libzsolve*.so

%files libs
%doc NEWS README THANKS TODO
%license COPYING
%{_libdir}/lib4ti2*.so.0*
%{_libdir}/libzsolve*.so.0*

%changelog
* Wed Dec 29 2022 Jeff Law <jlaw@ventanamicro.com> - 1.6.9-13
- Add missing #include for gcc-13

* Wed Nov 16 2022 Jerry James <loganjerry@gmail.com> - 1.6.9-12
- Silence "egrep is obsolescent" warnings from the scripts
- Update license to reflect embedded fonts in the PDF manual

* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 1.6.9-11
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.6.9-6
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  9 2019 Jerry James <loganjerry@gmail.com> - 1.6.9-4
- Fix the location of the module file (bz 1773348)
- Do not build the empty fiber library

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Jerry James <loganjerry@gmail.com> - 1.6.9-1
- Split back out of latte-integrale
