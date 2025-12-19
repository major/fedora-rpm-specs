# Upstream has not yet tagged any releases, so build from git for now
%global commit      30f2951d1e90e47afa821bdd1b12b82246656c42
%global shortcommit %{sub %{commit} 1 7}
%global gitdate     20251029
%global giturl      https://github.com/scipopt/vipr

Name:           vipr
Version:        1.1^%{gitdate}.%{shortcommit}
Release:        %autorelease
Summary:        Verifying Integer Programming Results

# MIT: the project as a whole
# LGPL-3.0-or-later: code/CMakeConfig.hpp.in
License:        MIT AND LGPL-3.0-or-later
URL:            https://scipopt.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# The Fedora SoPlex build requires zlib-ng, not zlib
Patch:          %{name}-zlib-ng.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(soplex)
BuildRequires:  cmake(tbb)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib-ng)

%description
VIPR is a software project to verify, in exact rational arithmetic, the
correctness of results computed by mixed-integer linear programming solvers.
It is based on an elementary file format for LP-based branch-and-cut
certificates.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
cd code
%cmake
%cmake_build

# For some reason, viprincomp is linked with libsoplex, even though
# -Wl,-as-needed is in the link flags.  Relink to drop that dependency.
cd %{_vpath_builddir}
g++ %{build_cxxflags} %{build_ldflags} \
    -Wl,--dependency-file=CMakeFiles/viprincomp.dir/link.d \
    CMakeFiles/viprincomp.dir/incompletify.cpp.o \
    -o viprincomp -lmpfr -lgmp
cd ../..

%install
#%%cmake_install does nothing, so install by hand
mkdir -p %{buildroot}%{_bindir}
cp -p code/%{_vpath_builddir}/vipr* %{buildroot}%{_bindir}

%check
#%%ctest does nothing, so run some examples
code/%{_vpath_builddir}/viprchk examples/IPCO_eg3.vipr
code/%{_vpath_builddir}/viprchk_parallel examples/cg.vipr
code/%{_vpath_builddir}/viprchk_parallel examples/infeasbb.vipr

%files
%doc README.md cert_spec_v1_0.md cert_spec_v1_1.md
%{_bindir}/vipr2html
%{_bindir}/viprchk
%{_bindir}/viprchk_parallel
%{_bindir}/viprcomp
%{_bindir}/viprincomp
%{_bindir}/viprttn

%changelog
%autochangelog
