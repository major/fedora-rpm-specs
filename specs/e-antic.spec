%global giturl  https://github.com/flatsurf/e-antic

Name:           e-antic
Version:        2.1.0
Release:        %autorelease
Summary:        Real Embedded Algebraic Number Theory In C

License:        LGPL-3.0-or-later
URL:            https://flatsurf.github.io/e-antic/libeantic/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
# The e-antic sources contain patches to flint, but those patches have already
# been incorporated into the Fedora versions.  Make e-antic skip attempts to
# build the patched files.
Patch:          %{name}-unpatch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  catch2-devel
BuildRequires:  cereal-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)

# Missing dependencies to build docs:
# - byexample: https://github.com/byexamples/byexample
# - standardese: https://github.com/standardese/standardese

# The python interface, pyeantic, requires cppyy, which is currently not
# available in Fedora.

%description
E-ANTIC is a C/C++ library to deal with real embedded number fields, built on
top of ANTIC.  Its aim is to have as fast as possible exact arithmetic
operations and comparisons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       cereal-devel%{?_isa}
Requires:       flint-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%conf
# Upstream does not generate the configure script
autoreconf -fi .

# Make catch2 available for testing
mkdir -p libeantic/test/external/catch2/single_include
ln -s %{_includedir}/catch2 libeantic/test/external/catch2/single_include

# Make cereal available for testing
rmdir libeantic/test/external/cereal
ln -s %{_includedir}/cereal libeantic/test/external/cereal

%build
%configure \
  --disable-static \
  --disable-silent-rules \
  --without-doc \
  --without-pyeantic

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libeantic/libtool

%make_build

%install
%make_install

# Documentation is installed below
rm -fr %{buildroot}%{_docdir}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check

%files
%doc AUTHORS README.md
%license COPYING COPYING.LESSER
%{_libdir}/libeantic.so.3{,.*}
%{_libdir}/libeanticxx.so.3{,.*}

%files          devel
%{_includedir}/%{name}/
%{_includedir}/libeantic/
%{_libdir}/libeantic.so
%{_libdir}/libeanticxx.so

%changelog
%autochangelog
