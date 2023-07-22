%global upver release-%{version}

Name:           libminc
Version:        2.4.03
Release:        16%{?dist}
Summary:        Core library and API of the MINC toolkit

License:        MIT
URL:            https://github.com/BIC-MNI/libminc
Source0:        https://github.com/BIC-MNI/libminc/archive/%{upver}/%{name}-%{version}.tar.gz
Patch0:         0001-install-cmake-files-in-private-directory.patch

BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  nifticlib-devel
BuildRequires:  netcdf-devel
BuildRequires:  hdf5-devel

%description
The MINC file format is a highly flexible medical image file format
built on the HDF5 generalized data format. The format is
simple, self-describing, extensible, portable and N-dimensional, with
programming interfaces for both low-level data access and high-level
volume manipulation. On top of the libraries is a suite of generic
image-file manipulation tools. The format, libraries and tools are
designed for use in a medical-imaging research environment : they are
simple and powerful and make no attempt to provide a pretty interface
to users.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nifticlib-devel%{?_isa}
Requires:       netcdf-devel%{?_isa}
Requires:       zlib-devel%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       cmake%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{upver} -S git
rm -rf build/
sed -i -e '/SET (LIBMINC_INSTALL_INCLUDE_DIR/s/include/include\/%{name}/' CMakeLists.txt
sed -i -e '/CMAKE_INSTALL_RPATH/d' CMakeLists.txt

%build
%cmake ../ \
-DLIBMINC_BUILD_SHARED_LIBS=ON \
-DLIBMINC_USE_SYSTEM_NIFTI=ON \
-DLIBMINC_MINC1_SUPPORT=ON \
-DLIBMINC_BUILD_EZMINC=ON
%cmake_build

%install
%cmake_install

%check
%ctest || :

%files
%license COPYING
%doc README README.release doc/ NEWS ChangeLog AUTHORS
%{_libdir}/%{name}*.so.*

%files devel
%doc volume_io/example/*.c ezminc/examples/*.cpp ezminc/examples/Example_CMakeLists.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/LIBMINC/
%{_libdir}/%{name}*.so

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 2.4.03-12
- Rebuild for hdf5 1.12.1

* Wed Aug 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4.03-11
- Bump and rebuild: koschei says FTBFS

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.4.03-10
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4.03-7
- Fix build using correct cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.4.03-4
- Rebuild for hdf5 1.10.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.03-1
- Skip tests on s390x (#1688972)

* Wed Mar 13 2019 Orion Poplawski <orion@nwra.com> - 2.4.03-1
- Update to 2.4.03

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.00-6
- Rebuild for hdf5 1.8.18

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.00-5
- Rebuild for hdf5 1.8.17

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.00-3
- Rebuild for netcdf 4.4.0

* Wed Dec 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.00-2
- Apply patch to fix endian tests (RHBZ #1287015)

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.00-1
- Initial package
