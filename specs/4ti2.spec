%global giturl  https://github.com/4ti2/4ti2

Name:           4ti2
Version:        1.6.10
Release:        %autorelease
Summary:        Algebraic, geometric and combinatorial problems on linear spaces

%global relver %(tr . _ <<< %{version})

# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in the PDF manual.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:            https://4ti2.github.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/Release_%{relver}/%{name}-%{version}.tar.gz
Source1:        4ti2.module.in

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

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
License:        GPL-2.0-or-later
Requires:       4ti2-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Headers and library files needed to develop software that uses 4ti2.

%package libs
Summary:        Library for problems on linear spaces
License:        GPL-2.0-or-later

%description libs
A library for algebraic, geometric and combinatorial problems on linear
spaces.

%prep
%autosetup

%conf
# Add a missing executable bit
chmod a+x ltmain.sh

# Fix encodings
iconv -f ISO8859-1 -t UTF-8 NEWS > NEWS.utf8
touch -r NEWS NEWS.utf8
mv -f NEWS.utf8 NEWS

# Update the C++ standard
sed -i 's/c++0x/c++11/g' configure

# Do not override Fedora compiler flags
sed -e 's|-O3 -fomit-frame-pointer|%{build_cflags}|' \
    -e 's/-march=\$arch -mcpu=\$arch -m\$arch//' \
    -e 's/-mtune=\$arch//' \
    -i configure

%configure --enable-shared --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%build
%make_build

# Build the manual
export LD_LIBRARY_PATH=$PWD/src/4ti2/.libs:$PWD/src/fiber/.libs:$PWD/src/groebner/.libs:$PWD/src/ppi/.libs:$PWD/src/util/.libs:$PWD/src/zsolve/.libs
pushd doc
make update-manual
bibtex 4ti2_manual
pdflatex 4ti2_manual
pdflatex 4ti2_manual
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
%autochangelog
