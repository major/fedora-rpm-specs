Name:		kealib
Version:	1.6.2
Release:	1%{?dist}
Summary:	HDF5 Based Raster File Format as a GDAL plugin

License:	MIT
URL:		http://kealib.org/
Source0:	https://github.com/ubarsc/kealib/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

# Fix cmake config files install dir
Patch0:         kealib-cmakedir.patch
# Fix build against gdal-3.12
# https://github.com/ubarsc/kealib/commit/791a57c0ddf6274e2a6b264b2e712e00b812b4ff
# https://github.com/ubarsc/kealib/commit/14556e2f8ae66b6b8662a6fbd2b16fd04b9d9e0e
# https://github.com/ubarsc/kealib/commit/db4a900d42babb81d2ac2c397df11ac4eaf46a5a
# https://github.com/ubarsc/kealib/commit/b9cf5d48c0968698d4443d06b080be6e011d6779
Patch1:         kealib-gdal312.patch

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	ccache
BuildRequires:	gdal-devel
BuildRequires:	proj-devel
BuildRequires:	hdf5-devel
Requires:	gdal

%description
KEALib is a project to provide an implementation of the GDAL
specification within the the HDF5 file format. Specifically, the format
will support raster attribute tables (commonly not included within
other formats), image pyramids, GDAL meta-data, in-built statistics
while also providing large file handling with compression used
throughout the file.

%package devel
Summary:     KEA development headers
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
KEA development headers

%prep
%autosetup -p1

# fix wrong lib entry
sed -i 's+set (PROJECT_LIBRARY_DIR lib)+set (PROJECT_LIBRARY_DIR %{_lib})+g' %{_builddir}/%{name}-%{version}/CMakeLists.txt

%build
# compile with kealib as a GDAL plugin (LIBKEA_WITH_GDAL:BOOL=ON)
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="Release" \
    -DGDAL_INCLUDE_DIR:PATH=%{_includedir}/gdal \
    -DGDAL_LIB_PATH:PATH=%{_libdir} \
    -DHDF5_INCLUDE_DIR:PATH=%{_includedir} \
    -DHDF5_LIB_PATH:PATH=%{_libdir} \
    -DHDF5_STATIC_LIBS:BOOL=OFF \
    -DLIBKEA_WITH_GDAL:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .

%cmake_build

%install
%cmake_install

%ifnarch %ix86
# needed since libkea insists on using /usr/lib/ target nontheless sed above
mkdir -p %{buildroot}%{_libdir}/ %{buildroot}%{_libdir}/gdalplugins/
mv %{buildroot}%{_prefix}/lib/libkea* %{buildroot}%{_libdir}/
mv %{buildroot}%{_prefix}/lib/gdalplugins/* %{buildroot}%{_libdir}/gdalplugins/
%endif

%files
%{_libdir}/libkea.so.1*
%{_libdir}/gdalplugins/gdal_KEA.so
%doc Changes.txt README.md
%license LICENSE.txt

%files devel
%{_bindir}/kea-config
%{_libdir}/libkea.so
%{_libdir}/cmake/Kealib/
%{_libdir}/cmake/libkea/
%{_includedir}/libkea

%changelog
* Sun Nov 23 2025 Sandro Mani <manisandro@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Sun Nov 23 2025 Sandro Mani <manisandro@gmail.com> - 1.5.0-15
- Rebuild (gdal)

* Tue Jul 29 2025 Sandro Mani <manisandro@gmail.com> - 1.5.0-14
- Rebuild (gdal)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 1.5.0-11
- Rebuild (gdal)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.5.0-10
- Rebuild for hdf5 1.14.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 1.5.0-8
- Rebuild (gdal)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.5.0-5
- Rebuild (gdal)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 1.5.0-3
- Rebuild (gdal)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Markus Neteler <neteler@mundialis.de> - 1.5.0-1
- New upstream version kealib 1.5.0 with GDAL 3.6.0 support

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 1.4.15-3
- Rebuild (gdal)

* Fri Nov 04 2022 Markus Neteler <neteler@mundialis.de> - 1.4.15-2
- fix i386/i686 compilation

* Fri Nov 04 2022 Markus Neteler <neteler@mundialis.de> - 1.4.15-1
- new upstream version

* Wed Dec 22 2021 Markus Neteler <neteler@mundialis.de> - 1.4.14-1
- new upstream version

* Tue Oct 06 2020 Markus Neteler <neteler@mundialis.de> - 1.4.13-3
- updated after package review RHBZ#1876864

* Wed Sep 16 2020 Markus Neteler <neteler@mundialis.de> - 1.4.13-2
- updated after package review RHBZ#1876864

* Wed Aug 19 2020 Markus Neteler <neteler@mundialis.de> - 1.4.13-1
- new upstream version

* Thu Sep 14 2017 Markus Neteler <neteler@mundialis.de> - 1.4.6-1
- initial packaging
