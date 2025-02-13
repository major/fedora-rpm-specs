%{?mingw_package_header}

%global pkgname opencv

Name:          mingw-%{pkgname}
Version:       4.11.0
Release:       1%{?dist}
Summary:       MinGW Windows OpenCV library

BuildArch:     noarch
License:       BSD-3-Clause AND Apache-2.0 AND ISC
URL:           https://opencv.org
# RUN opencv-clean.sh TO PREPARE TARBALLS FOR FEDORA
#
# Need to remove copyrighted lena.jpg images from tarball (rhbz#1295173)
# and SIFT/SURF from tarball, due to legal concerns.
#
Source0:       %{pkgname}-clean-%{version}.tar.gz
Source1:       %{pkgname}_contrib-clean-%{version}.tar.gz
Source2:       %{pkgname}-clean.sh

# Don't build bundled libraries
Patch0:        opencv_unbundle.patch
# Pass -mbig-obj to linker when linking python module, to prevent "too many sections" failure
Patch1:        opencv_bigobj.patch


BuildRequires: make
BuildRequires: cmake
BuildRequires: swig
BuildRequires: protobuf-compiler

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-eigen3
# BuildRequires: mingw32-flatbuffers
BuildRequires: mingw32-freetype
BuildRequires: mingw32-gdal
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw32-harfbuzz
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtheora
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libvorbis
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-openexr
BuildRequires: mingw32-openjpeg2-tools
BuildRequires: mingw32-protobuf
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-numpy
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-tesseract
BuildRequires: mingw32-vulkan-headers
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-eigen3
# BuildRequires: mingw64-flatbuffers
BuildRequires: mingw64-freetype
BuildRequires: mingw64-gdal
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw64-gstreamer1-plugins-base
BuildRequires: mingw64-harfbuzz
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtheora
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libvorbis
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-openexr
BuildRequires: mingw64-openjpeg2-tools
BuildRequires: mingw64-protobuf
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-numpy
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-tesseract
BuildRequires: mingw64-vulkan-headers
BuildRequires: mingw64-zlib



%description
MinGW Windows OpenCV library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows OpenCV library

%description -n mingw32-%{pkgname}
MinGW Windows OpenCV library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 OpenCV bindings
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 OpenCV bindings.


%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows OpenCV library tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
MinGW Windows OpenCV library tools.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows OpenCV library

%description -n mingw64-%{pkgname}
MinGW Windows OpenCV library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 OpenCV bindings
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 OpenCV bindings.


%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows OpenCV library tools
Requires:      mingw64-%{pkgname} = %{version}-%{release}


%description -n mingw64-%{pkgname}-tools
MinGW Windows OpenCV library tools.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version} -a1
# we don't use pre-built contribs except quirc and flatbuffers
mv 3rdparty/quirc/ .
mv 3rdparty/flatbuffers/ .
rm -r 3rdparty/
mkdir 3rdparty/
mv quirc/ 3rdparty/
mv flatbuffers/ 3rdparty/


%build

# rgbd module disabled
# https://github.com/opencv/opencv_contrib/pull/2161#issuecomment-560155630
MINGW32_CMAKE_ARGS="\
    -DOPENCV_CONFIG_INSTALL_PATH=%{mingw32_libdir}/cmake/OpenCV \
    -DVULKAN_INCLUDE_DIRS=%{mingw32_includedir}/vulkan \
    -DPYTHON3_INCLUDE_PATH=%{mingw32_includedir}/python%{mingw32_python3_version} \
    -DPYTHON3_NUMPY_INCLUDE_DIRS=%{mingw32_includedir}/numpy/ " \
MINGW64_CMAKE_ARGS="\
    -DOPENCV_CONFIG_INSTALL_PATH=%{mingw64_libdir}/cmake/OpenCV \
    -DVULKAN_INCLUDE_DIRS=%{mingw64_includedir}/vulkan \
    -DPYTHON3_INCLUDE_PATH=%{mingw64_includedir}/python%{mingw64_python3_version} \
    -DPYTHON3_NUMPY_INCLUDE_DIRS=%{mingw64_includedir}/numpy/ " \
%mingw_cmake \
 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo \
 -DWITH_IPP=OFF \
 -DWITH_ITT=OFF \
 -DWITH_QT=ON \
 -DWITH_OPENGL=ON \
 -DWITH_GDAL=ON \
 -DWITH_UNICAP=ON \
 -DWITH_CAROTENE=OFF \
 -DENABLE_PRECOMPILED_HEADERS=OFF \
 -DBUILD_opencv_java=OFF \
 -DWITH_FFMPEG=OFF \
 -DWITH_XINE=OFF \
 -DPYTHON2_EXECUTABLE=false \
 -DWITH_OPENCL=OFF \
 -DOPENCV_SKIP_PYTHON_LOADER=ON \
 -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-%{version}/modules \
 -DWITH_OPENMP=ON \
 -DBUILD_PERF_TESTS=OFF \
 -DBUILD_TESTS=OFF \
 -DBUILD_PROTOBUF=OFF \
 -DPROTOBUF_UPDATE_FILES=ON \
 -DBUILD_opencv_rgbd=OFF \
 -DWITH_OBSENSOR=OFF

%mingw_make_build


%install
%mingw_make_install

# Install licenses through %%license
mkdir install_licenses
mv %{buildroot}%{mingw32_datadir}/licenses/opencv4/* install_licenses/
rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses

# Remove stray files
rm -f %{buildroot}%{mingw32_prefix}/{LICENSE,setup_vars_opencv4.cmd}
rm -f %{buildroot}%{mingw64_prefix}/{LICENSE,setup_vars_opencv4.cmd}


%files -n mingw32-%{pkgname}
%license install_licenses/*
%{mingw32_bindir}/libopencv_*4110.dll
%{mingw32_includedir}/opencv4/
%{mingw32_libdir}/libopencv_*4110.dll.a
%{mingw32_libdir}/cmake/OpenCV/
%{mingw32_datadir}/opencv4


%files -n mingw32-python3-%{pkgname}
%{mingw32_python3_sitearch}/cv2.cpython-%{mingw32_python3_version_nodots}.dll

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license install_licenses/*
%{mingw64_bindir}/libopencv_*4110.dll
%{mingw64_includedir}/opencv4/
%{mingw64_libdir}/libopencv_*4110.dll.a
%{mingw64_libdir}/cmake/OpenCV/
%{mingw64_datadir}/opencv4

%files -n mingw64-python3-%{pkgname}
%{mingw64_python3_sitearch}/cv2.cpython-%{mingw64_python3_version_nodots}.dll

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Feb 11 2025 Sandro Mani <manisandro@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Sandro Mani <manisandro@gmail.com> - 4.10.0-4
- Rebuild (openexr)

* Thu Nov 14 2024 Sandro Mani <manisandro@gmail.com> - 4.10.0-3
- Rebuild (openexr)

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 4.10.0-2
- Rebuild (gdal)

* Sat Jul 27 2024 Sandro Mani <manisandro@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 4.7.0-9
- Rebuild (openexr)

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 4.7.0-8
- Rebuild (gdal)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 4.7.0-5
- Rebuild (gdal)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 4.7.0-3
- Rebuild (gdal)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Sandro Mani <manisandro@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 4.6.0-4
- Rebuild (gdal)

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 4.6.0-3
- Rebuild (python-3.11)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 4.5.5-6
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.5.5-5
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.5.5-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.5.5-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Sandro Mani <manisandro@gmail.com> - 4.5.5-1
- Update to 4.5.5

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 4.5.4-4
- Rebuild (gdal)

* Mon Nov 08 2021 Sandro Mani <manisandro@gmail.com> - 4.5.4-3
- Rebuild (protobuf)

* Wed Oct 27 2021 Sandro Mani <manisandro@gmail.com> - 4.5.4-2
- Rebuild (protobuf)

* Mon Oct 11 2021 Sandro Mani <manisandro@gmail.com> - 4.5.4-1
- Update to 4.5.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Sandro Mani <manisandro@gmail.com> - 4.5.3-1
- Update to 4.5.3

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 4.5.2-3
- Rebuild (python-3.10)

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 4.5.2-2
- Rebuild (gdal)

* Sun Apr 04 2021 Sandro Mani <manisandro@gmail.com> - 4.5.2-1
- Update to 4.5.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 13:20:12 CET 2021 Sandro Mani <manisandro@gmail.com> - 4.5.1-2
- Rebuild (protobuf)

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.com> - 4.5.1-1
- Update to 4.5.1

* Thu Dec 17 2020 Sandro Mani <manisandro@gmail.com> - 4.5.0-3
- Rebuild (openexr)

* Fri Nov 13 00:52:37 CET 2020 Sandro Mani <manisandro@gmail.com> - 4.5.0-2
- Rebuild (gdal)

* Fri Oct 23 2020 Sandro Mani <manisandro@gmail.com> - 4.5.0-1
- Update to 4.5.0

* Mon Sep 28 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-6
- Harden requires

* Mon Sep 28 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-5
- Rebuild (protobuf)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-3
- Add opencv-clean.sh to sources

* Sat Jun 27 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-2
- Use %%{mingw32,64_python3_version_nodots}

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Wed May 27 2020 Sandro Mani <manisandro@gmail.com> - 4.2.0-2
- Rebuild (gdal)

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Thu Oct 24 2019 Sandro Mani <manisandro@gmail.com> - 4.1.2-1
- Initial package
