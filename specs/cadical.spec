%global giturl  https://github.com/arminbiere/cadical

Name:           cadical
Epoch:          1
Version:        2.2.1
Release:        %autorelease
Summary:        Simplified SAT solver

License:        MIT
URL:            http://fmv.jku.at/cadical/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/rel-%{version}/%{name}-%{version}.tar.gz
# Based on the cryptominisat version
Source1:        %{name}-cmakelists.txt
# Extra functionality needed by cryptominisat
Patch:          %{name}-cryptominisat.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  zlib-devel

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description
CaDiCaL is a simplified Satisfiability solver.  The goal of the development of
CaDiCaL is to obtain a CDCL solver, which is easy to understand and change,
while at the same time not being much slower than other state-of-the-art CDCL
solvers.

%package libs
Summary:        Simplified SAT solver library

%description libs
This package contains the CaDiCaL simplified Satisfiability solver as a
library, for use in applications that need a SAT solver.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Library links and header files for developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-rel-%{version}

%conf
sed 's/%%version%%/%{version}/' %{SOURCE1} > CMakeLists.txt
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON

%build
%cmake_build

# Make man pages for the command line interface
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}
help2man --version-string=%{version} -N -o cadical.1 \
  -n 'Simplified SAT solver' %{_vpath_builddir}/cadical
help2man --version-string=%{version} -N -o mobical.1 -h -h \
  -n 'Model Based Tester for CaDiCaL' %{_vpath_builddir}/mobical

%install
%cmake_install

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1

%check
# Prevent rebuilding the library while testing
sed -i '/make -C \$CADICALBUILD/d;/^make$/d' test/*/run.sh

## Make the test scripts happy
# Give them a makefile
sed -e 's/@CXX@/g++/' \
    -e "s|@CXXFLAGS@|%{build_cxxflags} -DNBUILD -DNCLOSEFROM -DNCONTRACTS -DNDEBUG -DNTRACING -DNUNLOCKED -Dcadical_EXPORTS -I$PWD/src|" \
    -e 's/@CC@/gcc/' \
    -e "s|@CFLAGS@|%{build_cflags} -DNBUILD -DNCLOSEFROM -DNCONTRACTS -DNDEBUG -DNTRACING -DNUNLOCKED -Dcadical_EXPORTS -I$PWD/src|" \
    makefile.in > %{_vpath_builddir}/makefile
# Give them what appears to be a static library
ln -s libcadical.so %{_vpath_builddir}/libcadical.a
# Give them a bogus config file
cat > %{_vpath_builddir}/config.h << EOF
#define VERSION "%{version}"
#define COMPILE "gcc %{build_cflags}"
EOF
# Make them see the bogus config file
sed -i 's/cc -O/& -I./' test/cnf/run.sh
# Give them a bogus build directory
ln -s %{_vpath_builddir} build

export LD_LIBRARY_PATH="$PWD/%{_vpath_builddir}"
export CADICALBUILD='../%{_vpath_builddir}'
%ctest
rm %{_vpath_builddir}/{config.h,libcadical.a} build

%files
%{_bindir}/cadical
%{_bindir}/mobical
%{_mandir}/man1/cadical.1*
%{_mandir}/man1/mobical.1*

%files libs
%license LICENSE
%doc NEWS.md README.md
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
