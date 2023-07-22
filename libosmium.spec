%global gdalcpp_version 1.3.0
%global protozero_version 1.6.3

%global testcommit ecfdeb0d5ffcfcb60939651d517d5d7d1bb041a3

%define debug_package %{nil}

Name:           libosmium
Version:        2.19.0
Release:        3%{?dist}
Summary:        Fast and flexible C++ library for working with OpenStreetMap data

License:        BSL-1.0
URL:            http://osmcode.org/libosmium/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/osmcode/osm-testdata/archive/%{testcommit}/osm-testdata-%{testcommit}.tar.gz
# https://github.com/osmcode/libosmium/issues/319
Patch0:         libosmium-tag-list.patch

BuildRequires:  cmake make gcc-c++
BuildRequires:  doxygen graphviz xmlstarlet
BuildRequires:  ruby rubygems spatialite-tools

BuildRequires:  catch2-devel
BuildRequires:  boost-devel
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  gdalcpp-devel >= %{gdalcpp_version}
BuildRequires:  expat-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  sparsehash-devel
BuildRequires:  gdal-devel
BuildRequires:  geos-devel

BuildRequires:  catch2-static
BuildRequires:  protozero-static
BuildRequires:  gdalcpp-static

%description
A fast and flexible C++ library for working with OpenStreetMap data.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       boost-devel
Requires:       protozero-devel >= %{protozero_version}
Requires:       gdalcpp-devel >= %{gdalcpp_version}
Requires:       expat-devel
Requires:       zlib-devel
Requires:       bzip2-devel
Requires:       lz4-devel
Requires:       sparsehash-devel
Requires:       gdal-devel
Requires:       geos-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for developing
applications that use %{name}.


%prep
%setup -q -c -T -a 0 -a 1
%patch0 -p 1 -d %{name}-%{version}
mv %{name}-%{version} %{name}
mv osm-testdata-%{testcommit} osm-testdata
rm -rf libosmium/include/gdalcpp.h libosmium/test/catch
ln -sf /usr/include/catch2 libosmium/test/catch
sed -i -e 's/-O3 -g//' libosmium/CMakeLists.txt


%build
cd libosmium
rm include/osmium/geom/projection.hpp
%cmake -DBUILD_HEADERS=ON -DBUILD_DATA_TESTS=ON
%cmake_build
%cmake_build --target doc


%install
cd libosmium
%cmake_install
rm -rf %{buildroot}%{_docdir}


%check
cd libosmium
%ctest


%files devel
%doc libosmium/README.md libosmium/CHANGELOG.md
%license libosmium/LICENSE
%{_includedir}/osmium


%files doc
%doc libosmium/%{__cmake_builddir}/doc/html/*
%license libosmium/LICENSE


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 Tom Hughes <tom@compton.nu> - 2.19.0-2
- Require catch2-devel instead of catch-devel

* Thu Jan 19 2023 Tom Hughes <tom@compton.nu> - 2.19.0-1
- Update to 2.19.0 upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  8 2022 Tom Hughes <tom@compton.nu> - 2.18.0-1
- Update to 2.18.0 upstream release

* Thu Jan 20 2022 Tom Hughes <tom@compton.nu> - 2.17.3-1
- Update to 2.17.3 upstream release

* Fri Dec 17 2021 Tom Hughes <tom@compton.nu> - 2.17.2-1
- Update to 2.17.2 upstream release

* Tue Oct  5 2021 Tom Hughes <tom@compton.nu> - 2.17.1-1
- Update to 2.17.1 upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Tom Hughes <tom@compton.nu> - 2.17.0-1
- Update to 2.17.0 upstream release

* Wed Mar 24 2021 Tom Hughes <tom@compton.nu> - 2.16.0-3
- Drop generic projection support

* Fri Feb 19 2021 Tom Hughes <tom@compton.nu> - 2.16.0-2
- Unbundle catch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Tom Hughes <tom@compton.nu> - 2.16.0-1
- Update to 2.16.0 upstream release

* Mon Nov 16 2020 Tom Hughes <tom@compton.nu> - 2.15.6-4
- Add patch for intermittent test failures

* Thu Nov 12 01:41:40 CET 2020 Sandro Mani <manisandro@gmail.com> - 2.15.6-3
- Rebuild (proj, gdal)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Tom Hughes <tom@compton.nu> - 2.15.6-1
- Update to 2.15.6 upstream release

* Tue Apr 21 2020 Tom Hughes <tom@compton.nu> - 2.15.5-1
- Update to 2.15.5 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Tom Hughes <tom@compton.nu> - 2.15.4-1
- Update to 2.15.4 upstream release

* Wed Oct 23 2019 Tom Hughes <tom@compton.nu> - 2.15.3-2
- Drop utf8cpp dependency

* Mon Sep 16 2019 Tom Hughes <tom@compton.nu> - 2.15.3-1
- Update to 2.15.3 upstream release

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 2.15.2-1
- Update to 2.15.2 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Tom Hughes <tom@compton.nu> - 2.15.1-1
- Update to 2.15.1 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec  8 2018 Tom Hughes <tom@compton.nu> - 2.15.0-1
- Update to 2.15.0 upstream release

* Tue Jul 24 2018 Tom Hughes <tom@compton.nu> - 2.14.2-1
- Update to 2.14.2 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  1 2018 Tom Hughes <tom@compton.nu> - 2.14.0-1
- Update to 2.14.0 upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 2.13.1-3
- Add patch for protozero 1.6.x support
- Ensure we build with Fedora optimisation options

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 2.13.1-2
- Drop the explicit dependnecy on rubypick.

* Fri Aug 25 2017 Tom Hughes <tom@compton.nu> - 2.13.1-1
- Update to 2.13.1 upstream release

* Wed Aug 16 2017 Tom Hughes <tom@compton.nu> - 2.13.0-2
- Re-enable test with upstream patch

* Tue Aug 15 2017 Tom Hughes <tom@compton.nu> - 2.13.0-1
- Update to 2.13.0 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Tom Hughes <tom@compton.nu> - 2.12.2-1
- Update to 2.12.2 upstream release

* Mon Apr 10 2017 Tom Hughes <tom@compton.nu> - 2.12.1-1
- Update to 2.12.1 upstream release

* Tue Mar  7 2017 Tom Hughes <tom@compton.nu> - 2.12.0-1
- Update to 2.12.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Tom Hughes <tom@compton.nu> - 2.11.0-1
- Update to 2.11.0 upstream release

* Wed Nov 16 2016 Tom Hughes <tom@compton.nu> - 2.10.2-1
- Update to 2.10.2 upstream release
- Exclude ppc64le as the tests fail

* Thu Sep 15 2016 Tom Hughes <tom@compton.nu> - 2.9.0-1
- Update to 2.9.0 upstream release
- Exclude aarch64 as the tests fail

* Thu Aug  4 2016 Tom Hughes <tom@compton.nu> - 2.8.0-1
- Update to 2.8.0 upstream release

* Sat Jun 11 2016 Tom Hughes <tom@compton.nu> - 2.7.2-1
- Update to 2.7.2 upstream release

* Wed Jun  1 2016 Tom Hughes <tom@compton.nu> - 2.7.1-1
- Update to 2.7.1 upstream release

* Mon Feb 22 2016 Tom Hughes <tom@compton.nu> - 2.6.1-1
- Update to 2.6.1 upstream release

* Fri Feb 19 2016 Tom Hughes <tom@compton.nu> - 2.6.0-3
- Add patch for newer protozero

* Thu Feb 18 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.6.0-2
- Add ruby deps

* Sat Feb  6 2016 Tom Hughes <tom@compton.nu> - 2.6.0-1
- Update to 2.6.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Jonathan Wakely <jwakely@redhat.com> - 2.5.4-2
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 2.5.4-1
- Update to 2.5.4 upstream release

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 2.5.3-2
- Add patches for test failures

* Wed Nov 18 2015 Tom Hughes <tom@compton.nu> - 2.5.3-1
- Update to 2.5.3 upstream release

* Mon Nov  9 2015 Tom Hughes <tom@compton.nu> - 2.5.2-1
- Update to 2.5.2 upstream release

* Fri Sep 18 2015 Tom Hughes <tom@compton.nu> - 2.2.0-11
- Revert unathorised bundling of gdalcpp

* Fri Sep 18 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.2.0-10
- added few backports to fix ftbfs

* Sat Jul 25 2015 Tom Hughes <tom@compton.nu> - 2.2.0-9
- Rebuild for boost 1.58.0

* Sat Jul 25 2015 Tom Hughes <tom@compton.nu> - 2.2.0-8
- Disable empty debuginfo package

* Tue Jul 21 2015 Tom Hughes <tom@compton.nu> - 2.2.0-7
- Rebuild for boost 1.58.0

* Tue Jul 21 2015 Tom Hughes <tom@compton.nu> - 2.2.0-6
- Enable data tests

* Sat Jul 18 2015 Tom Hughes <tom@compton.nu> - 2.2.0-5
- Add license to doc subpackage

* Thu Jul 16 2015 Tom Hughes <tom@compton.nu> - 2.2.0-4
- Remove bundled header

* Thu Jul 16 2015 Tom Hughes <tom@compton.nu> - 2.2.0-3
- Use %%cmake

* Wed Jul 15 2015 Tom Hughes <tom@compton.nu> - 2.2.0-2
- Make devel subpackage an arched package
- Move documentation to doc subpackage

* Sun Jul 12 2015 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Mon Jun  8 2015 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Initial build
