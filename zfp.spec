%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:           zfp
Version:        0.5.5
Release:        5%{?dist}
Summary:        Library for compressed numerical arrays with high throughput R/W random access

License:        BSD
URL:            https://computation.llnl.gov/projects/floating-point-compression
Source0:        https://github.com/LLNL/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++

%description
This is zfp, an open source C/C++ library for compressed numerical arrays
that support high throughput read and write random access. zfp was written by
Peter Lindstrom at Lawrence Livermore National Laboratory, and is loosely
based on the algorithm described in the following paper:

Peter Lindstrom
"Fixed-Rate Compressed Floating-Point Arrays"
IEEE Transactions on Visualization and Computer Graphics,
  20(12):2674-2683, December 2014
doi:10.1109/TVCG.2014.2346458

zfp was originally designed for floating-point data only, but has been
extended to also support integer data, and could for instance be used to
compress images and quantized volumetric data. To achieve high compression
ratios, zfp uses lossy but optionally error-bounded compression. Although
bit-for-bit lossless compression of floating-point data is not always
possible, zfp is usually accurate to within machine epsilon in near-lossless
mode.

zfp works best for 2D and 3D arrays that exhibit spatial coherence, such as
smooth fields from physics simulations, images, regularly sampled terrain
surfaces, etc. Although zfp also provides a 1D array class that can be used
for 1D signals such as audio, or even unstructured floating-point streams,
the compression scheme has not been well optimized for this use case, and
rate and quality may not be competitive with floating-point compressors
designed specifically for 1D streams.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%ldconfig_scriptlets


%files
%doc README.md VERSIONS.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/zfp/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Orion Poplawski <orion@nwra.com> - 0.5.5-1
- Update to 0.5.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Orion Poplawski <orion@nwra.com> - 0.5.4-1
- Update to 0.5.4

* Tue May 9 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.1-1
- Initial Fedora package
