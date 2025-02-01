Name:           ethos
Version:        0.1.1
Release:        %autorelease
Summary:        Flexible and efficient proof checker for SMT solvers

License:        BSD-3-Clause
URL:            https://github.com/cvc5/ethos
VCS:            git:%{url}.git
Source:         %{url}/archive/%{name}-%{version}.tar.gz
# Explicitly include cstdint.h; fixes FTBFS with GCC 15
Patch:          %{url}/pull/111.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
The Ethos checker is an efficient and extensible tool for checking proofs of
Satisfiability Modulo Theories (SMT) solvers.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

# We want to know about use of deprecated interfaces
sed -i '/Wno-deprecated/d' CMakeLists.txt

# Make sure the bundled copy of drat-trim is not used in the build
rm -fr contrib/drat_trim

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{_vpath_builddir}/src/ethos %{buildroot}%{_bindir}

%check
%ctest

%files
%doc NEWS.md README.md user_manual.md
%license COPYING
%{_bindir}/ethos

%changelog
%autochangelog
