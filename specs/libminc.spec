%global upver release-%{version}

Name:           libminc
Version:        2.4.03
Release:        %{autorelease}
Summary:        Core library and API of the MINC toolkit

License:        MIT
URL:            https://github.com/BIC-MNI/libminc
Source0:        https://github.com/BIC-MNI/libminc/archive/%{upver}/%{name}-%{version}.tar.gz
Patch0:         0001-install-cmake-files-in-private-directory.patch
# Fix building with GCC15 as C23
# https://github.com/BIC-MNI/libminc/pull/129
Patch1:         %{url}/pull/129.patch

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
%autochangelog
