Name:       orocos-bfl
%global commit cf72962177bc8287eb9dab19d6aea61b9212b04b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout 20190423git%{shortcommit}
Version:    0.8.99
Release:    29.%{checkout}%{?dist}
Summary:    A framework for inference in Dynamic Bayesian Networks

# Explanation from upstream for multiple licenses:
# "The technical reason we could not longer use the LGPL license for RTT/BFL
# software was that the LGPL is not compatible with C++ templates, which are
# used extensively in the RTT/BFL libraries. The 'runtime exception' says
# explicitly that using the C++ templates (or any other function) of the RTT
# software does not make your derived work GPL. The derived work may be
# distributed under any license you see fit."
# see http://www.orocos.org/orocos/license
License:    GPLv2 with exceptions and LGPLv2+
URL:        http://www.orocos.org/bfl/
Source0:    https://github.com/toeklk/orocos-bayesian-filtering/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  ginac-devel

%description
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters, etc.  These algorithms can, for
example, be run on top of the Realtime Services, or be used for estimation in
Kinematics & Dynamics applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel, ginac-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%setup -q -n orocos-bayesian-filtering-%{commit}/orocos_bfl

%build
export LDFLAGS='-ldl'
%cmake \
  -DGINAC_SUPPORT:BOOL=ON \
  -DLIBRARY_TYPE:STRING="shared"
%cmake_build

%cmake_build --target docs

%check
%cmake_build --target check


%install
%cmake_install

# tests are installed here, remove them
rm -rf %{buildroot}%{_bindir}/bfl

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%doc %{_vpath_builddir}/doc/html
%license COPYING


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-29.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-28.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-27.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-26.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.99-25.20190423gitcf72962
- Rebuild for ginac ginac-1.8.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-24.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.8.99-23.20190423gitcf72962
- Adapt to cmake out-of-source builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-22.20190423gitcf72962
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-21.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-20.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-19.20190423gitcf72962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.8.99-18.20190423gitcf72962
- Update to latest upstream snapshot
- Remove upstreamed patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-17.20180529git3d0d149
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-16.20180529git3d0d149
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.8.99-15.20180529git3d0d149
- Add patch to fix build error on i686
- Re-enable all arches, as all build issues are fixed
- Update to latest github master
- Remove doxygen include paths to make doc sub-package truly noarch

* Tue May 29 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.8.99-14.20180529git0950663
- Update to latest github master

* Fri May 25 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.8.99-13.20180525gitddcf55e
- Switch to github upstream source
- Update to latest github master

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-12.20160503gitc1b18e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-11.20160503gitc1b18e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-10.20160503gitc1b18e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8.99-9.20160503gitc1b18e3
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.99-8.20160503gitc1b18e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Dan Horák <dan[at]danny.cz> - 0.8.99-7.20160503gitc1b18e3
- Switch to ExclusiveArch, the unit test fails on ppc64/ppc64le/s390x too

* Mon Oct 03 2016 Till Hofmann <till.hofmann@posteo.de> - 0.8.99-6.20160503gitc1b18e3
- Exclude aarch64, the error is the same as on arm
- Add -ldl to the linker flags

* Wed May 04 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.99-5.20160503gitc1b18e3
- Add COPYING file to doc subpackage
- Fix license and add explanation for multiple licenses
- Improve documentation

* Tue May 03 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.99-4.20160503gitc1b18e3
- Update to latest commit

* Mon Jan 04 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.99-3.20150905git927874e
- Change license to "LGPLv2+ and LGPLv2+ with exceptions and GPLv2+"

* Sun Oct 18 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.99-2.20150905git927874e
- Change devel package's dependency to fully versioned dependency
- Make doc package noarch

* Sat Sep 05 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.99-1.20150905git927874e
- Switch to new upstream source: gitlab snapshots
- Remove upstreamed patches

* Thu Jun 18 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.0-5
- Do not execute unit tests on i686 due to a bug in test_pdf

* Thu Jun 18 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.0-4
- Add patch 'link-against-ginac' to fix issues with undefined non-weak symbols

* Tue Jun 02 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.0-3
- Build unit tests, add BuildRequires: cppunit-devel
- ExcludeArch: arm

* Tue May 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8.0-2
- Split documentation into separate package
- Build and run tests
- Clean up and split patch

* Wed Apr 22 2015 Sebastian Reuter <sebastian.reuter@rwth-aachen.de> - 0.8.0-1
- Initial package
