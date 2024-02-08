%global commit0 9b891540183ddc834a02b2bd81b31afae71b2153
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20200212

%bcond_with check

# lto broken
%define _lto_cflags %{nil}

Summary:        A deep learning framework
Name:           caffe
License:        BSD-2-Clause
Version:        1.0^git%{date0}.%{shortcommit0}
Release:        10%{?dist}

ExclusiveArch:  x86_64 aarch64 ppc64le
URL:            http://caffe.berkeleyvision.org/
Source0:        https://github.com/BVLC/caffe/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/BVLC/caffe/pull/7065
Patch0:         0001-rename-CV_LOAD_IMAGE_-enums.patch
# misc changes to make scripts compliant with Fedora
Patch1:         0002-fedora-script-changes.patch
# unsafe yaml call fixed
Patch2:         0003-Use-yaml-safe_load.patch
# cuda warning
Patch3:         0004-cuda-11-update.patch
# protobuf error, deprecated function
Patch4:         0005-protobuf-3.14-update.patch
# cmake files install to /usr/lib64/cmake/
Patch5:         0006-change-cmake-files-install-location.patch
# allow rebuilding of examples
Patch6:         0007-examples-standalone-CMakeLists.patch
# convert libcaffeproto.a to libcaffproto.so
Patch7:         0008-convert-libcaffeeproto-to-shared.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gflags-devel
BuildRequires: glog-devel
BuildRequires: hdf5-devel
BuildRequires: leveldb-devel
BuildRequires: lmdb-devel
BuildRequires: make
BuildRequires: openblas-devel
BuildRequires: opencv-devel
BuildRequires: protobuf-devel
BuildRequires: snappy-devel

%description
Caffe is a deep learning framework made with expression, speed,
and modularity in mind. It is developed by Berkeley AI Research
(BAIR) and by community contributors. Yangqing Jia created the
project during his PhD at UC Berkeley.

%package devel
Summary: A deep learning framework

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake
Requires: gcc-c++
Requires: gflags-devel
Requires: glog-devel
Requires: opencv-devel
Requires: protobuf-devel
# Needed to fetch the samples' data files
Requires: gzip
Requires: tar
Requires: wget

%description devel
Caffe is a deep learning framework made with expression, speed,
and modularity in mind. It is developed by Berkeley AI Research
(BAIR) and by community contributors. Yangqing Jia created the
project during his PhD at UC Berkeley.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
# Not worth trying to get old python to run
%cmake -DBLAS=open \
       -DBUILD_python=OFF
       
%cmake_build

%if %{with check}
%check
%cmake_build --target runtest
%endif


%install
mkdir -p %{buildroot}%{_datadir}/Caffe/docs
mkdir -p %{buildroot}%{_datadir}/Caffe/data
mkdir -p %{buildroot}%{_datadir}/Caffe/examples
mkdir -p %{buildroot}%{_datadir}/Caffe/models
mkdir -p %{buildroot}%{_datadir}/Caffe/scripts
cp -p -r docs/* %{buildroot}%{_datadir}/Caffe/docs
cp -p -r data/* %{buildroot}%{_datadir}/Caffe/data
cp -p -r examples/* %{buildroot}%{_datadir}/Caffe/examples
# Use standalone cmakelist
mv %{buildroot}%{_datadir}/Caffe/examples/CMakeLists.txt.standalone %{buildroot}%{_datadir}/Caffe/examples/CMakeLists.txt
cp -p -r models/* %{buildroot}%{_datadir}/Caffe/models
cp -p -r scripts/upload* %{buildroot}%{_datadir}/Caffe/scripts
cp -p -r scripts/download* %{buildroot}%{_datadir}/Caffe/scripts

# Some gitignores got copied over
find %{buildroot} -name .gitignore -delete

%cmake_install

# lingering python
rm -r %{buildroot}/usr/python

%files
%dir %{_datadir}/Caffe
%license LICENSE
%doc README.md
%{_bindir}/caffe
%{_bindir}/classification
%{_bindir}/compute_image_mean
%{_bindir}/convert_cifar_data
%{_bindir}/convert_imageset
%{_bindir}/convert_mnist_data
%{_bindir}/convert_mnist_siamese_data
%{_bindir}/extract_features
%{_bindir}/upgrade_net_proto_binary
%{_bindir}/upgrade_net_proto_text
%{_bindir}/upgrade_solver_proto_text
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}proto.so.*

%files devel
%doc %{_datadir}/Caffe/docs/
%{_datadir}/Caffe/data
%{_datadir}/Caffe/examples
%{_datadir}/Caffe/models
%{_datadir}/Caffe/scripts
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}proto.so
%{_libdir}/cmake/Caffe/

%changelog
* Tue Feb 06 2024 Sérgio Basto <sergio@serjux.com> - 1.0^git20200212.9b89154-10
- Rebuild for opencv 4.9.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^git20200212.9b89154-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^git20200212.9b89154-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.0^git20200212.9b89154-7
- Rebuilt for Boost 1.83

* Thu Sep 07 2023 Tom Rix <trix@redhat.com> - 1.0^git20200212.9b89154-6
- Disable broken arches

* Wed Sep 06 2023 Tom Rix <trix@redhat.com> - 1.0^git20200212.9b89154-5
- Address review comments

* Sun Sep 03 2023 Tom Rix <trix@redhat.com> - 1.0^git20200212.9b89154-4
- Address review comments

* Thu Aug 17 2023 Tom Rix <trix@redhat.com> - 1.0^git20200212.9b89154-3
- Address review comments

* Sat May 20 2023 Tom Rix <trix@redhat.com> - 1.0.20200212git9b89154-2
- Address review comments
-  spdx for bsd clause 2
-  improve snapshot release name
-  drop Group tag
-  drop ExclusiveArch
-  run testing with --target runtest
-  change libcaffeeproto.a to *.so
- Remove cuda conditional
- Check all the time
- Add some requires for running devel scripts

* Sat Nov 26 2022 Tom Rix <trix@redhat.com> - 1.0-1.20200212git9b89154
- Initial release
