Name:           atomic-queue
Version:        1.6.7
Release:        %autorelease
Summary:        C++ lockless queue

# SPDX
License:        MIT
URL:            https://github.com/max0x7ba/atomic_queue
Source:         %{url}/archive/v%{version}/atomic_queue-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  boost-devel

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
C++14 multiple-producer-multiple-consumer lock-free queues based on circular
buffers and std::atomic.

Designed with a goal to minimize the latency between one thread pushing an
element into a queue and another thread popping it from the queue.}

%description %{common_description}


%package devel
Summary:        Development files for atomic-queue

# Header-only library
Provides:       atomic-queue-static = %{version}-%{release}

%description devel %{common_description}

The atomic-queue-devel package contains libraries and header files for
developing applications that use atomic-queue.


%prep
%autosetup -n atomic_queue-%{version}


%conf
%meson -Dbenchmarks=false


%build
%meson_build


%install
%meson_install


%check
%meson_test --verbose


%files devel
%license LICENSE
%doc README.md
# We do NOT package “html”, which contains benchmark results, because it loads
# a Google Analytics script.

%{_includedir}/atomic_queue/
%{_libdir}/pkgconfig/atomic_queue.pc


%changelog
%autochangelog
