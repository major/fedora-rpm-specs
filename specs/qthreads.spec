# Use commit to enable builds on ppc64le and add soname
%global commit       cedb1fc6f725ea1a51dc9f5bbdc1ec6ec00e33d7
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate   20251007

Name:           qthreads
Version:        1.22^%{commitdate}git%{shortcommit}
Release:        %{autorelease}
Summary:        Lightweight locality-aware user-level threading runtime

# Breakdown of licenses is documented in COPYING
License:        BSD-3-Clause AND MIT AND dtoa
URL:            https://www.sandia.gov/qthreads/
Source:         https://github.com/sandialabs/qthreads/archive/%{commit}/qthreads-%{shortcommit}.tar.gz
# This library relies on some low-level platform-specific code, so it can
# only be expected to work on explicitly-supported architectures, and it only
# compiles on architectures that upstream has attempted to support. See:
#
# https://github.com/sandialabs/qthreads/blob/1.22/README.md#compatibility
# https://github.com/sandialabs/qthreads/blob/1.22/include/qthread/common.h#L44-L58.
#
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86} s390x

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel

%description
The Qthreads API is designed to make using large numbers of threads convenient
and easy. The Qthreads API also provides access to full/empty-bit (FEB)
semantics, where every word of memory can be marked either full or empty, and a
thread can wait for any word to attain either state.

Qthreads is essentially a library for spawning and controlling stackful
coroutines: threads with small (4-8k) stacks. The exposed user API resembles
OS threads, however the threads are entirely in user-space and use their
locked/unlocked status as part of their scheduling.

The library's metaphor is that there are many Qthreads and several "shepherds".
Shepherds generally map to specific processors or memory regions, but this is
not an explicit part of the API. Qthreads are assigned to specific shepherds
and are only allowed to migrate when running on a scheduler that supports work
stealing or when migration is explicitly triggered via user APIs.

The API includes utility functions for making threaded loops, sorting, and
similar operations convenient.


%package devel
Summary:   Development files for qthreads library
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for qthreads library.

%prep
%autosetup -p1 -n qthreads-%{commit}

# Remove bundled HPGCC, only for benchmarks, to show it is unused
# and its LGPL license does not contribute to the built software
rm -rv test/benchmarks/mantevo/hpccg/

%build
# Fast context swap is broken on ppc64le
#https://github.com/sandialabs/qthreads/issues/371#issuecomment-3378502168
%ifarch ppc64le
%cmake -DQTHREADS_CONTEXT_SWAP_IMPL=system
%else
%cmake
%endif
%cmake_build


%install
%cmake_install
install -t '%{buildroot}%{_mandir}/man3' -p -m 0644 -D man/man3/*.3
rm %{buildroot}%{_includedir}/qthread/.gitignore

%check
%ctest

%files
%license COPYING
%doc AUTHORS
%doc NEWS
%doc README.md
%doc README.affinity
%doc SCHEDULING
%{_libdir}/libqthread.so.1{,.*}

%files devel
%{_includedir}/qthread.h
%dir %{_includedir}/qthread
%{_includedir}/qthread/*.h
%{_includedir}/qthread/*.hpp
%dir %{_libdir}/cmake/qthread
%{_libdir}/cmake/qthread/*.cmake
%{_libdir}/libqthread.so
%{_mandir}/man3/q*.3*

%changelog
%autochangelog
