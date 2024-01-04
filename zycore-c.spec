%global sover 1.4

Name:           zycore-c
Version:        1.4.1
Release:        %autorelease
Summary:        Zyan Core Library for C

License:        MIT
URL:            https://github.com/zyantific/zycore-c
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/zyantific/zycore-c/issues/59
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gtest-devel
BuildRequires:  doxygen

%description
The Zyan Core Library for C is an internal library providing platform
independent types, macros and a fallback for environments without LibC.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DZYCORE_BUILD_SHARED_LIB=ON \
    -DZYCORE_BUILD_TESTS=ON \
    -DZYCORE_BUILD_EXAMPLES=ON \
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libZycore.so.%{sover}*

%files devel
%{_includedir}/Zycore/
%{_libdir}/cmake/zycore/
%{_libdir}/libZycore.so

%files doc
%license LICENSE
%{_docdir}/Zycore/

%changelog
%autochangelog
