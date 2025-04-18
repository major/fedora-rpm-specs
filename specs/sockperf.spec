Name:           sockperf
Version:        3.10
Release:        %autorelease
Summary:        Network benchmarking utility for testing latency and throughput
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Mellanox/%{name}
Source0:        https://github.com/Mellanox/%{name}/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  autoconf automake
BuildRequires:  doxygen
BuildRequires:  libtool

%description
sockperf is a network benchmarking utility over socket API that was designed
for testing performance (latency and throughput) of high-performance systems
(it is also good for testing performance of regular networking systems as
well). It covers most of the socket API calls and options.

Specifically, in addition to the standard throughput tests, sockperf, does the
following:

* Measure latency of each discrete packet at sub-nanosecond resolution (using
  TSC register that counts CPU ticks with very low overhead).

* Does the above for both ping-pong mode and for latency under load mode. This
  means that we measure latency of single packets even under load of millions
  Packets Per Second (without waiting for reply of packet before sending
  subsequent packet on time)

* Enable spike analysis by providing histogram, with various percentiles of the
  packets’ latencies (for example: median, min, max, 99%% percentile, and more),
  (this is in addition to average and standard deviation). Also, sockperf
  provides full log with all packet’s tx/rx times that can be further analyzed
  with external tools, such as MS-Excel or matplotlib - All this without
  affecting the benchmark itself.

* Support MANY optional settings for good coverage of socket API and network
  configurations, while still keeping very low overhead in the fast path to
  allow cleanest results.

%prep
%autosetup -p1

%build
./autogen.sh
# Upstream wants and defaults to "-O3 --param inline-unit-growth=200".
# The Fedora optflags would override the former, so let's put it back.
# Avner wrote:
# > I reached that in the past after fine tuning the performance of sockperf.
# > We used sockperf for measuring latency of extremely fast networks.
# > Sometimes at sub microsecond resolution. This parameter helps us keeping
# > the entire fast path of the application as "one big function" with no
# > calls to other functions because it helps the compiler to respect all our
# > "inline" directive for other functions that we call (while still keeping
# > the "one big function" at a reasonable size for good performance at run
# > time).
export CXXFLAGS='%{optflags} -O3'
%configure --enable-doc
# --enable-tool --enable-test
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/sockperf
%{_mandir}/man3/sockperf.3.*
%{_pkgdocdir}

%changelog
%autochangelog
