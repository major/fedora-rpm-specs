Name:           mathic
Version:        1.6
Release:        %autorelease
Summary:        Data structures for Groebner basis computations

License:        LGPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathic
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DBUILD_TESTING:BOOL=ON
BuildOption(conf): -DCMAKE_SKIP_RPATH:BOOL=ON
BuildOption(conf): -Denable_divsim:BOOL=ON
BuildOption(conf): -Denable_pqsim:BOOL=ON

BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
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
%autosetup

%install -a
# Install the tools
mkdir -p %{buildroot}%{_bindir}
cp -p %{_vpath_builddir}/{divsim,pqsim} %{buildroot}%{_bindir}

# We install these files in a different place
rm -fr %{buildroot}%{_docdir}/%{name}

%check
%{_vpath_builddir}/src/mathic-unit-tests

%files
%doc README.md
%license lgpl-2.0.txt lgpl-2.1.txt lgpl-3.0.txt
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/divsim
%{_bindir}/pqsim

%changelog
%autochangelog
