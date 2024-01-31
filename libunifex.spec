%global forgeurl https://github.com/facebookexperimental/libunifex
Version:        0.4.0
%forgemeta

Name:           libunifex
Release:        %autorelease
Summary:        A prototype implementation of the C++ sender/receiver async programming model
License:        Apache-2.0 WITH LLVM-exception
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         https://github.com/facebookexperimental/libunifex/pull/588.patch

# https://koji.fedoraproject.org/koji/taskinfo?taskID=110446313
# https://kojipkgs.fedoraproject.org//work/tasks/6375/110446375/build.log
ExcludeArch:    i686

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
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
export CXXFLAGS="%{optflags} -Wno-error=maybe-uninitialized"
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUNIFEX_USE_SYSTEM_GTEST=ON \
    -DCMAKE_CXX_STANDARD=20 \

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
