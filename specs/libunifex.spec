%global date 20260109
%global commit d2058fd1d4800203e1ded1cfad74fa73fdbf622a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libunifex
Version:        0.4.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        A prototype implementation of the C++ sender/receiver async programming model
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/facebookexperimental/libunifex
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel

%description
The 'libunifex' project is a prototype implementation of the C++ sender/receiver
async programming model that is currently being considered for standardisation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -C

%build
export CXXFLAGS="%{optflags} -Wno-error=maybe-uninitialized -Wno-error=template-body"
%cmake \
    -GNinja \
    -DUNIFEX_USE_SYSTEM_GTEST=ON \
    -DCMAKE_CXX_STANDARD=20
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libunifex.so.0*

%files devel
%{_includedir}/unifex/
%{_libdir}/libunifex.so
%{_libdir}/cmake/unifex/
%{_libdir}/pkgconfig/unifex.pc

%changelog
%autochangelog
