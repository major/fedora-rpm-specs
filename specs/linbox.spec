%global giturl  https://github.com/linbox-team/linbox

Name:           linbox
Version:        1.7.1
%global so_version 0
Release:        %autorelease
Summary:        C++ Library for High-Performance Exact Linear Algebra

License:        LGPL-2.1-or-later
URL:            https://linalg.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix failure to build the OpenCL tests
Patch:          %{giturl}/pull/326.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  expat-devel
BuildRequires:  fflas-ffpack-devel
BuildRequires:  flexiblas-devel
BuildRequires:  flint-devel
BuildRequires:  givaro-devel
BuildRequires:  iml-devel
BuildRequires:  libfplll-devel
BuildRequires:  mpfr-devel
BuildRequires:  ntl-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  saclib-devel
BuildRequires:  tinyxml2-devel

# This can be removed when F43 reaches EOL
Obsoletes:      linbox-doc < 1.7.0-1

%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.


%package        devel
Summary:        Development libraries/headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fflas-ffpack-devel%{?_isa}
Requires:       iml-devel%{?_isa}
Requires:       libfplll-devel%{?_isa}
Requires:       ntl-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}


%description    devel
Headers and libraries for development with %{name}.


%package        doc
Summary:        Documentation for %{name}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -p1


%conf
# Adapt to the way saclib is packaged in Fedora
sed -e 's,include/saclib,&/saclib,' \
    -e '/saclib\.h/,+1s/__GNU_MP_VERSION < 3/SACMAJVERS < 2/' \
    -i macros/saclib-check.m4

# Remove spurious executable bits
find -O3 . \( -name \*.h -o -name \*.inl \) -perm /0111 -exec chmod a-x {} +


%build
# Regenerate configure after monkeying with m4 macros
autoreconf -fi

export CPPFLAGS='-I%{_includedir}/saclib'
%configure --disable-silent-rules \
  --disable-static \
  --with-ocl=yes \
  --with-saclib=yes \
  --without-archnative
chmod -v a+x linbox-config

# Remove hardcoded rpaths; workaround libtool reordering -Wl,--as-needed after
# all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Don't try to optimize the tests; the build takes gargantuan amounts of memory
sed -i 's|-O2|-Og|g' tests/Makefile

%make_build


%install
%make_install

# We don't want libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# Documentation is installed in the wrong place
rm -vrf '%{buildroot}%{_prefix}/doc'


%check
# Do not test in parallel, leads to duplicated work
LD_LIBRARY_PATH=$PWD/linbox/.libs %make_build check -j1


%files
%doc AUTHORS ChangeLog README.md
%license COPYING COPYING.LESSER
%{_libdir}/lib%{name}.so.%{so_version}
%{_libdir}/lib%{name}.so.%{so_version}.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1*


%changelog
%autochangelog
