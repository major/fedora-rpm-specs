Name:           sockperf
Version:        3.8
Release:        2%{?dist}
Summary:        Network benchmarking utility for testing latency and throughput
License:        BSD
URL:            https://github.com/Mellanox/%{name}
Source0:        https://github.com/Mellanox/%{name}/archive/%{version}.tar.gz

BuildRequires: make
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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 30 2022 Izabela Bakollari <izabela.bakollari@gmail.com> - 3.8-1
- Upstream release 3.8.

* Wed Mar 09 2022 Izabela Bakollari <izabela.bakollari@gmail.com> - 3.7-1
- Upstream release 3.7.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Michal Schmidt <mschmidt@redhat.com> - 3.6-1
- Upstream release 3.6.
- Plus a couple of fixes from upstream git.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Michal Schmidt <mschmidt@redhat.com> - 3.5-1
- Upstream release 3.5.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Michal Schmidt <mschmidt@redhat.com> - 3.3-1
- Upstream release 3.3.
- BR: gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2.gitc1f3ca79bff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 09 2015 Michal Schmidt <mschmidt@redhat.com> - 2.6-1.gitc1f3ca79bff9
- Update to current upstream snapshot.
- Adjust for upstream move to github.
- Drop patches (upstreamed).
- Compile with -O3 as recommended by upstream.

* Thu Aug 27 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.5.244-4
- Modity 0001-Don-t-throw-away-Fedora-s-CXXFLAGS.patch to remove -Werror
  from configure.ac (Fix F23FTBFS, RHBZ#1240012).
- Run doxygen -u.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.244-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 04 2014 Dan Horák <dan[at]danny.cz> - 2.5.244-2
- Add s390(x) support

* Mon Sep 08 2014 Michal Schmidt <mschmidt@redhat.com> - 2.5.244-1
- Update to current upstream from SVN. Has aarch64 and ppc64 support.
- Simplify svnversion substitution.
- Build fix. Make sure config/m4 exists.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.241-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.5.241-5
- Added AArch64 support

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.241-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Michal Schmidt <mschmidt@redhat.com> - 2.5.241-3
- Adjust the CXXFLAGS patch to drop all optimization flags changing.
- Run autoreconf with -f to force regenerating config/aux.

* Tue Apr 08 2014 Michal Schmidt <mschmidt@redhat.com> - 2.5.241-2
- Use %%autosetup.

* Fri Mar 21 2014 Michal Schmidt <mschmidt@redhat.com> - 2.5.241-1
- Initial Fedora packaging.
