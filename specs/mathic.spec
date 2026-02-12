Name:           mathic
Version:        1.2
Release:        %autorelease
Summary:        Data structures for Groebner basis computations

License:        LGPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathic
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(memtailor)

%description
Mathic is a C++ library of fast data structures designed for use in Groebner
basis computation.  This includes data structures for ordering S-pairs,
performing divisor queries and ordering polynomial terms during polynomial
reduction.

With Mathic you get to use highly optimized code with little effort so that
you can focus more of your time on whatever part of your Groebner basis
implementation that you are interested in.  The data structures use templates
to allow you to use them with whatever representation of monomials/terms and
coefficients that your code uses.  In fact the only places where Mathic
defines its own monomials/terms is in the test code and example code.
Currently only dense representations of terms/monomials are suitable since
Mathic will frequently ask "what is the exponent of variable number x in this
term/monomial?".

%package devel
Summary:        Development files for mathic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       memtailor-devel%{?_isa}

%description devel
Files for developing applications that use mathic.

%package tools
Summary:        Mathic-based tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Mathic-based tools.  Currently this contains:
- divsim: divisor query simulation
- pqsim: priority queue simulation

%prep
%autosetup -p1

%conf
# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/mathic.pc.in

# Upstream doesn't generate the configure script
autoreconf -fi .

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes GTEST_LIBS=-lgtest

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build
%make_build divsim pqsim

%install
%make_install

# Install the tools
mkdir -p %{buildroot}%{_bindir}
cp -p .libs/{divsim,pqsim} %{buildroot}%{_bindir}

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md
%license lgpl-2.0.txt lgpl-2.1.txt lgpl-3.0.txt
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/divsim
%{_bindir}/pqsim

%changelog
%autochangelog
