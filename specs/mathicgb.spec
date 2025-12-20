Name:           mathicgb
Version:        1.1
Release:        %autorelease
Summary:        Groebner basis computations

License:        GPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathicgb
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(mathic)
BuildRequires:  pkgconfig(tbb)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Mathicgb is a program for computing Groebner basis and signature Groebner
bases.  Mathicgb is based on the fast data structures from mathic.

%package devel
Summary:        Development files for mathicgb
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use mathicgb.

%package libs
Summary:        Mathicgb libraries

%description libs
Library interface to mathicgb.

%prep
%autosetup

%conf
# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/description.txt
touch -r doc/description.txt.orig doc/description.txt
rm -f doc/description.txt.orig

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
%configure --disable-static --enable-shared --with-gtest=yes

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
sed -i 's|g++$|& -Wl,--as-needed|' Makefile

%make_build

%install
%make_install

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md doc/description.txt doc/slides.pdf
%{_bindir}/mgb
%{_mandir}/man1/mgb.1*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.0*

%changelog
%autochangelog
