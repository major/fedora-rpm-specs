%global _vpath_srcdir src
%undefine __cmake_in_source_dir

Name:           voro++
Version:        0.4.6
Release:        30%{?dist}
Summary:        Library for 3D computations of the Voronoi tessellation

License:        BSD-3-Clause-LBNL
URL:            http://math.lbl.gov/voro++/
Source0:        http://math.lbl.gov/voro++/download/dir/%{name}-%{version}.tar.gz
Source1:        CMakeLists.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

# Make base class destructors virtual
Patch0:         voro++_virtual-destructor.patch
# Fix manpage formatting
Patch1:         voro++_man.patch

%description
Voro++ is a software library for carrying out three-dimensional computations
of the Voronoi tessellation. A distinguishing feature of the Voro++ library
is that it carries out cell-based calculations, computing the Voronoi cell for
each particle individually. It is particularly well-suited for applications
that rely on cell-based statistics, where features of Voronoi cells (e.g.
volume, centroid, number of faces) can be used to analyze a system of particles.


%package devel
Summary:        %{name} headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for %{name}.


%package doc
Summary:        %{name} documentation
BuildArch:      noarch

%description doc
Documentation for %{name}.


%prep
%autosetup -p1

cp -a %{SOURCE1} src


%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 man/voro++.1 %{buildroot}%{_mandir}/man1/voro++.1

# Fix path in examples
find examples -name "*.cc" -exec sed -i 's/"voro++.hh"/<voro++\/voro++.hh>/g' '{}' \;
cp config.mk examples/
find examples -name "Makefile" -exec sed -i 's/..\/..\/config.mk/..\/config.mk/g' '{}' \;


%ldconfig_scriptlets


%files
%doc LICENSE README NEWS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%files doc
%doc LICENSE
%doc html/
%doc examples/
%doc scripts/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 0.4.6-16
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.6-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 0.4.6-6
- Fix license
- doc subpackage
- Fix manpage formatting

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 0.4.6-5
- Merge libs subpackage into main package

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 0.4.6-4
- Add missing -libs requires for main package

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 0.4.6-3
- Build proper versioned shared libraries

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 0.4.6-2
- Spec cleanup
- Add voro++_virtual-destructor.patch

* Fri Feb 14 2014 Alexey Vasyukov <vasyukov@gmail.com> - 0.4.6-1
- Initial package for Fedora
