Name:           atomic-queue
Version:        1.0
Release:        %autorelease
Summary:        C++ lockless queue

# SPDX
License:        MIT
URL:            https://github.com/max0x7ba/atomic_queue
Source0:        %{url}/archive/v%{version}/atomic_queue-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  boost-devel

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
C++14 multiple-producer-multiple-consumer lockless queues based on circular
buffer with std::atomic.

The main design principle these queues follow is minimalism: the bare minimum
of atomic operations, fixed size buffer, value semantics.

These qualities are also limitations:

  • The maximum queue size must be set at compile time or construction time.
    The circular buffer side-steps the memory reclamation problem inherent in
    linked-list based queues for the price of fixed buffer size. See Effective
    memory reclamation for lock-free data structures in C++ for more details.
    Fixed buffer size may not be that much of a limitation, since once the
    queue gets larger than the maximum expected size that indicates a problem
    that elements aren’t processed fast enough, and if the queue keeps growing
    it may eventually consume all available memory which may affect the entire
    system, rather than the problematic process only. The only apparent
    inconvenience is that one has to do an upfront back-of-the-envelope
    calculation on what would be the largest expected/acceptable queue size.
  • There are no OS-blocking push/pop functions. This queue is designed for
    ultra-low-latency scenarios and using an OS blocking primitive would be
    sacrificing push-to-pop latency. For lowest possible latency one cannot
    afford blocking in the OS kernel because the wake-up latency of a blocked
    thread is about 1-3 microseconds, whereas this queue’s round-trip time can
    be as low as 150 nanoseconds.

Ultra-low-latency applications need just that and nothing more. The minimalism
pays off, see the throughput and latency benchmarks.

Available containers are:

  • AtomicQueue - a fixed size ring-buffer for atomic elements.
  • OptimistAtomicQueue - a faster fixed size ring-buffer for atomic elements
    which busy-waits when empty or full.
  • AtomicQueue2 - a fixed size ring-buffer for non-atomic elements.
  • OptimistAtomicQueue2 - a faster fixed size ring-buffer for non-atomic
    elements which busy-waits when empty or full.

These containers have corresponding AtomicQueueB, OptimistAtomicQueueB,
AtomicQueueB2, OptimistAtomicQueueB2 versions where the buffer size is
specified as an argument to the constructor.

Totally ordered mode is supported. In this mode consumers receive messages in
the same FIFO order the messages were posted. This mode is supported for push
and pop functions, but for not the try_ versions. On Intel x86 the totally
ordered mode has 0 cost, as of 2019.

Single-producer-single-consumer mode is supported. In this mode, no
read-modify-write instructions are necessary, only the atomic loads and stores.
That improves queue throughput significantly.}

%description %{common_description}


%package devel
Summary:        Development files for %{name}
BuildArch:      noarch

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n atomic_queue-%{version}


%build
%meson -Dbenchmarks=false
%meson_build


%install
# Upstream does not install with meson. Just copy the headers.
install -d '%{buildroot}%{_includedir}'
cp -rvp include/atomic_queue '%{buildroot}%{_includedir}/'


%check
%meson_test --verbose
%{_vpath_builddir}/example


%files devel
%license LICENSE
%doc README.md
# We do NOT package “html”, which contains benchmark results, because it loads
# a Google Analytics script.

%{_includedir}/atomic_queue/


%changelog
%autochangelog
