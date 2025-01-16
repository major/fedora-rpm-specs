%global giturl  https://github.com/Normaliz/Normaliz

Name:           normaliz
Version:        3.10.4
Release:        %autorelease
Summary:        A tool for discrete convex geometry

# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# Bera: Bitstream-Vera
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# DoubleStroke: LicenseRef-DoubleStroke
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Bitstream-Vera AND Knuth-CTAN AND GPL-1.0-or-later AND LicenseRef-DoubleStroke AND AGPL-3.0-only AND LicenseRef-Rsfs
URL:            https://www.normaliz.uni-osnabrueck.de/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use libcrypto from openssl instead of the (unpackaged) hash-library
Patch:          %{name}-hash-library.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cocoalib-devel
BuildRequires:  e-antic-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libnauty)

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
Normaliz is a tool for computations in affine monoids, vector
configurations, rational polyhedra, and rational cones.  Normaliz now
computes rational and algebraic polyhedra, i.e., polyhedra defined over
real algebraic extensions of QQ.

Documentation and examples can be found in %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}},
in particular you may find Normaliz%{version}Documentation.pdf useful.  

%package -n libnormaliz
License:        GPL-3.0-or-later
Summary:        Normaliz internals as a library

%description -n libnormaliz
This package contains the normaliz internals as a library, often called
libnormaliz.

%package -n libnormaliz-devel
License:        GPL-3.0-or-later
Summary:        Developer files for libnormaliz
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       cocoalib-devel%{?_isa}
Requires:       e-antic-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description -n libnormaliz-devel
Header files and library links to develop applications that use the
Normaliz internals as a library (libnormaliz).

%prep
%autosetup -p0 -n Normaliz-%{version}

%conf
# Update the configuration for Fedora
sed -e 's|-funroll-loops|%{build_cxxflags} -I%{_includedir}/gfanlib|' \
    -e 's|-O3|-O2|' \
    -e 's|STRIP_FLAGS = .*|CXXFLAGS += -g|' \
    -i source/Makefile.configuration

# Do not strip the binary
sed -i 's|AM_LDFLAGS = -Wl,-s|AM_CXXFLAGS += -g|' source/Makefile.am

# Generate configure
autoreconf -fi .

%build
export CPPFLAGS="-I%{_includedir}/arb -I%{_includedir}/gfanlib"
%configure \
  --disable-silent-rules \
  --disable-static \
  --with-cocoalib=%{_prefix} \
  --with-hashlibrary=%{_prefix}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
mkdir -p docs/example

# Correct the end of line encodings for use on Linux
pushd example
for file in *.in
do
    sed 's/\r//' "$file" > "../docs/example/$file"
    touch -r "$file" "../docs/example/$file"
done
popd

# Generate the man page
export LD_LIBRARY_PATH=$PWD/source/.libs
help2man -s 1 -o normaliz.1 -N -n 'A tool for discrete convex geometry' \
  source/.libs/normaliz

%install
# Install the library, binary, and headers
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p normaliz.1 %{buildroot}%{_mandir}/man1

%check
# Temporarily disable tests on s390x
# See https://github.com/Normaliz/Normaliz/issues/407
%ifnarch s390x
LD_LIBRARY_PATH=$PWD/source/.libs make check
%endif

%files
%doc CHANGELOG docs/* doc/Normaliz.pdf
%{_bindir}/normaliz
%{_mandir}/man1/normaliz.1*

%files -n libnormaliz
%license COPYING
%{_libdir}/libnormaliz.so.3
%{_libdir}/libnormaliz.so.3.*

%files -n libnormaliz-devel
%doc source/libnormaliz/README
%{_libdir}/libnormaliz.so
%{_includedir}/libnormaliz/

%changelog
%autochangelog
