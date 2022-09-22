%bcond_without check

# header-only package
%global debug_package %{nil}

%global project concurrentqueue

Name:           moodycamel-%{project}
Version:        1.0.3
Release:        %autorelease
Summary:        An industrial-strength lock-free queue for C++

# main software is dual BSD or Boost
# lightweightesmaphore.h is zlib
# tests:
# - we don't include CDSChecker
# - Relacy is BSD (used only in tests)
# ^ not currently running those two but probably not worth stripping out
# lightweightesmaphore.h is zlib
License:        (BSD or Boost) and BSD and zlib
URL:            https://github.com/cameron314/%{project}
Source0:        %{url}/archive//v%{version}/%{name}-%{version}.tar.gz
# fix C API: MOODYCAMEL_EXPORT undefined on non-Windows platforms
Patch0:         https://github.com/cameron314/concurrentqueue/commit/e6fec438e8639221d43dae4b2ddf133e20580fdd.patch#/%{name}-1.0.3-fix-moodycamel-export.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%global _description %{expand:
An industrial-strength lock-free queue for C++.

Features:
- Knock-your-socks-off blazing fast performance
- Single-header implementation. Just drop it in your project
- Fully thread-safe lock-free queue. Use concurrently from any number of threads
- C++11 implementation -- elements are moved (instead of copied) where possible
- Templated, obviating the need to deal exclusively with pointers -- memory is
  managed for you
- No artificial limitations on element types or maximum count
- Memory can be allocated once up-front, or dynamically as needed
- Fully portable (no assembly; all is done through standard C++11 primitives)
- Supports super-fast bulk operations
- Includes a low-overhead blocking version (BlockingConcurrentQueue)
- Exception safe}

%description    %{_description}


%package        devel
Summary:        Development files for %{name}
License:        (BSD or Boost) and zlib
# this is noarch, but we want to force tests to run on all platforms
BuildArch:      noarch

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{project}-%{version}


%build
%cmake


%install
%cmake_install
# duplicate
rm %{buildroot}%{_includedir}/%{project}/LICENSE.md


%if %{with check}
%check
%make_build -C tests/unittests
./build/bin/unittests --disable-prompt
%endif


%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/%{project}/


%changelog
%autochangelog
