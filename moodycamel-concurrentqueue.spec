%bcond_without check

# header-only package
%global debug_package %{nil}

%global project concurrentqueue

Name:           moodycamel-%{project}
Version:        1.0.4
Release:        %autorelease
Summary:        An industrial-strength lock-free queue for C++

# main software is dual BSD-2-Clause or BSL-1.0
# lightweightesmaphore.h is Zlib
# tests:
# - we don't include CDSChecker
# - Relacy is BSD-3-Clause (used only in tests)
# ^ not currently running those two but probably not worth stripping out
License:        (BSD-2-Clause OR BSL-1.0) AND BSD-3-Clause AND Zlib
URL:            https://github.com/cameron314/%{project}
Source:         %{url}/archive//v%{version}/%{name}-%{version}.tar.gz
# install to %%{_datadir}/cmake not %%{_libdir}/cmake
Patch:          %{project}-install-noarch-to-share.diff

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
License:        (BSD-2-Clause OR BSL-1.0) AND Zlib
# this is noarch, but we want to force tests to run on all platforms
BuildArch:      noarch
Requires:       cmake-filesystem

%description    devel %{_description}

The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.


%prep
%autosetup -p1 -n %{project}-%{version}
# fix wrong-file-end-of-line-encoding
touch -r README.md README.md.tstamp
sed -i 's/\r$//' README.md
touch -r README.md.tstamp README.md


%build
%cmake


%install
%cmake_install


%if %{with check}
%check
%make_build -C tests/unittests
./build/bin/unittests --disable-prompt
%endif


%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/%{project}/
%{_datadir}/cmake/concurrentqueue


%changelog
%autochangelog
