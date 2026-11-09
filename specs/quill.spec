# This is a header-only package
%global debug_package %{nil}

Name:           quill
Version:        13.1.0
Release:        2%{?dist}
Summary:        Ultra-low-latency asynchronous C++17 logging and metrics library

License:        MIT
URL:            https://quillcpp.readthedocs.io/
Source:         https://github.com/odygrd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    cmake
BuildRequires:  gcc-c++

%if 0%{?fedora} && 0%{?fedora} < 44
BuildRequires:  ninja-build
BuildOption:    -GNinja
%endif

BuildOption:    -DCMAKE_CXX_STANDARD=20
#BuildOption:    -DQUILL_BUILD_EXAMPLES=BOOL:ON
BuildOption:    -DQUILL_BUILD_MODULE=BOOL:ON
BuildOption:    -DQUILL_BUILD_TESTS=BOOL:ON
BuildOption:    -DQUILL_ENABLE_EXTENSIVE_TESTS=BOOL:ON

%description
Quill is an asynchronous logging and metrics library for C++17 and later.
It keeps formatting and I/O away from latency-sensitive application threads
by encoding log arguments on the frontend and processing them on a dedicated
backend worker.

%dnl ---------------------------------------------------------------

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
Quill is an asynchronous logging and metrics library for C++17 and later.
It keeps formatting and I/O away from latency-sensitive application threads
by encoding log arguments on the frontend and processing them on a dedicated
backend worker.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%doc README.md examples
%license LICENSE
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%dnl ---------------------------------------------------------------


%prep
%autosetup -C -p1


%changelog
* Sun Nov 08 2026 Neal Gompa <ngompa@fedoraproject.org> - 13.1.0-2
- Force ninja for Fedora releases older than 44

* Sun Nov 08 2026 Neal Gompa <ngompa@fedoraproject.org> - 13.1.0-1
- Initial packaging
