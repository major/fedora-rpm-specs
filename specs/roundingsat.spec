# Upstream's git tags do not follow any versioning scheme
# Build from git commits for now
%global commit      d4edbf7908a9bb951fd181940919e0f3ac7ab1ee
%global shortcommit %{sub %{commit} 1 7}
%global gitdate     20260303
%global giturl      https://gitlab.com/MIAOresearch/software/roundingsat

Name:           roundingsat
Summary:        Pseudo-boolean solver powered by proof complexity
Version:        0~%{gitdate}.%{shortcommit}
Release:        %autorelease

# The code in src/used_licenses claims that several licenses apply.
# MIT: this project and the code copied from minisat
# Apache-2.0: soplex, which we link with but do not bundle
# BSL-1.0: the Boost library, which we link with but do not bundle
# LGPL-3.0: GMP, which we do not use to build
License:        MIT
URL:            https://roundingsat.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Do not invoke git to get the git branch and commit
Patch:          %{name}-git-commit.patch
# Do not attempt to download and build soplex
Patch:          %{name}-no-downloads.patch
# Build a shared library for use by papilo
Patch:          %{name}-shared.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo

BuildRequires:  boost-devel
BuildRequires:  cmake(soplex)
BuildRequires:  gcc-c++
BuildRequires:  help2man

%description
RoundingSat solves decision and optimization problems formulated as 0-1
integer linear programs.  Features:

- Native conflict analysis over 0-1 integer linear constraints, constructing
  full-blown cutting planes proofs.
- Highly efficient watched propagation routines.
- Seamless use of multiple precision arithmetic.
- Optional integration with the SoPlex LP solver.
- Linear and core-guided optimization.
- Certified unsatisfiability and optimality.

All of these combine to make RoundingSat the world's fastest pseudo-Boolean
solver.

%package        devel
Summary:        Header files and library links for roundingsat
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for building projects that use %{name}.

%prep
%autosetup -n %{name}-%{commit} -p1

# Do not invoke git to get the git commit
sed -i 's/%%COMMIT%%/%{commit}/' CMakeLists.txt

%conf -p
%ifarch %{power64}
# Avoid error due to clashing "long double" and "float128" definitions
export CFLAGS='%{build_cflags} -DBOOST_MP_BITS_OF_FLOAT128_DEFINED'
export CXXFLAGS='%{build_cxxflags} -DBOOST_MP_BITS_OF_FLOAT128_DEFINED'
%endif

%build -p
# Single file gcc compiles reach about 4.5G RSS on x86_64, so limit parallelism
%constrain_build -m 5120

%install -a
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -n roundingsat --version-string='%{gitdate}' \
    -o %{buildroot}%{_mandir}/man1/roundingsat.1 \
    %{buildroot}%{_bindir}/roundingsat

# The tests require /usr/bin/veripb; see https://veripb.org/.  Once that is
# packaged, do this:
#%%check
#%%cmake_build --target testruns

%files
%doc InputFormats.md README.md
%license LICENSE src/used_licenses/MIT.txt
%{_bindir}/roundingsat
%{_libdir}/libroundingsat.so.0{,.*}
%{_mandir}/man1/roundingsat.1*

%files devel
%{_includedir}/roundingsat/
%{_libdir}/libroundingsat.so

%changelog
%autochangelog
