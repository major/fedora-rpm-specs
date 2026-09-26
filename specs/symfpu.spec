Name:           symfpu
Version:        1.2.0
Release:        %autorelease
Summary:        An implementation of IEEE-754 / SMT-LIB floating-point 

# See LICENSE for the choice between GPL-3.0-or-later and BSD-3-Clause
License:        GPL-3.0-or-later OR BSD-3-Clause
URL:            https://github.com/martin-cs/symfpu
VCS:            git:%{url}.git
Source:         %{url}/archive/%{name}-%{version}-dual-license.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc-c++

%description
SymFPU is an implementation of the SMT-LIB / IEEE-754 operations in terms of
bit-vector operations.  It is templated in terms of the bit-vectors,
propositions, floating-point formats and rounding mode types used.  This
allows the same code to be executed as an arbitrary precision "SoftFloat"
library (although it's performance would not be good) or to be used to build
symbolic representations of floating-point operations suitable for use in
"bit-blasting" SMT solvers (you could also generate circuits from them but
again, performance will likely not be good).

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch

%description devel
This package contains header files and library links for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}-dual-license

# The build expects to be done in a directory named symfpu
ln -s %{name}-%{name}-%{version}-dual-license ../symfpu

# Turn off x86-specific build flags for other architectures
%ifnarch %{x86_64}
sed -i 's/ -msse2 -mfpmath=sse//;s/ -mfma -mno-fma4//' flags
%endif

%build
# The source dereferences type-punned pointers
export CFLAGS='%{build_cflags} -fno-strict-aliasing'
export CXXFLAGS='%{build_cxxflags} -fno-strict-aliasing'
# Parallel build almost always leads to an error
make

# Build a shared library instead of a static library, and give it an soname
flags=$(sed 's/CXXFLAGS+=//' flags)
cd baseTypes
g++ $CXXFLAGS $flags -fPIC -I../../ -c simpleExecutable.cpp \
    -o simpleExecutable.o
g++ %{build_ldflags} -shared -Wl,-h,libsymfpu.so.0 -o ../libsymfpu.so.0.0.0 \
    simpleExecutable.o
cd -

%install
# Install the header files
mkdir -p %{buildroot}%{_includedir}/%{name}/baseTypes
cp -p baseTypes/*.h %{buildroot}%{_includedir}/%{name}/baseTypes
cp -a core utils %{buildroot}%{_includedir}/%{name}
rm %{buildroot}%{_includedir}/%{name}/{core,utils}/Makefile

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p libsymfpu.so.0.0.0 %{buildroot}%{_libdir}
ln -s libsymfpu.so.0.0.0 %{buildroot}%{_libdir}/libsymfpu.so.0
ln -s libsymfpu.so.0 %{buildroot}%{_libdir}/libsymfpu.so

# The test executable always exits with error code 1, which isn't super helpful
#%%check
#./test --allTests

%files
%doc README.md
%license LICENSE
%{_libdir}/libsymfpu.so.0{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsymfpu.so

%changelog
%autochangelog
