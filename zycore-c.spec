%global sover 1.4

Name:           zycore-c
Version:        1.4.1
Release:        %autorelease
Summary:        Zyan Core Library for C

License:        MIT
URL:            https://github.com/zyantific/zycore-c
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Set DOXYGEN_GENERATE_MAN config option to generate manpages
Patch0:         https://github.com/zyantific/zycore-c/pull/65.patch

# https://github.com/zyantific/zycore-c/issues/59
ExcludeArch:    s390x

BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
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
%dir %{_includedir}/Zycore
%dir %{_includedir}/Zycore/API
%dir %{_includedir}/Zycore/Internal
%{_includedir}/Zycore/*.h
%{_includedir}/Zycore/API/*.h
%{_includedir}/Zycore/Internal/*.h
%dir %{_libdir}/cmake/zycore
%{_libdir}/cmake/zycore/*.cmake
%{_libdir}/libZycore.so
%{_mandir}/man3/*

%files doc
%license LICENSE
%dir %{_datadir}/doc/Zycore
%dir %{_datadir}/doc/Zycore/api
%dir %{_datadir}/doc/Zycore/api/search
%{_datadir}/doc/Zycore/api/*.css
%{_datadir}/doc/Zycore/api/*.png
%{_datadir}/doc/Zycore/api/*.html
%{_datadir}/doc/Zycore/api/*.map
%{_datadir}/doc/Zycore/api/*.md5
%{_datadir}/doc/Zycore/api/*.js
%{_datadir}/doc/Zycore/api/*.svg
%{_datadir}/doc/Zycore/api/search/*.js
%{_datadir}/doc/Zycore/api/search/*.svg
%{_datadir}/doc/Zycore/api/search/*.css

%changelog
%autochangelog
