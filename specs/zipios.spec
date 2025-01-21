%undefine __cmake_in_source_build

# Avoid architecture-specific name of build-dir to fix per-arch reproducibility with doxygen
%global _vpath_builddir %{_vendor}-%{_target_os}-build

Name:           zipios
Version:        2.2.5.0
Release:        11%{?dist}
# Most of the project is under LGPLv2+ but two source filesa are GPLv2+ so the
# combined work is GPLv2+.
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        C++ library for reading and writing Zip files

URL:            https://snapwebsites.org/project/zipios
Source0:        https://github.com/Zipios/Zipios/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++ libstdc++-devel
BuildRequires:  catch1-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  cppunit-devel
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  doxygen
# For man page generation
BuildRequires:  help2man


%description
Zipios is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

Note: This is nearly a complete rewrite of the 1.x series by a new upstream.
The previous version is depreciated but still supported as zipios++.


%package devel
Summary:        Header files for zipios
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       zlib-devel
Requires:       cmake

%description devel
The header files are only needed for development of programs using %{name}.

Note: This is nearly a complete rewrite of the 1.x series by a new upstream.
The previous version is depreciated but still supported as zipios++.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Developer documentation for %{name}.


%prep
%autosetup -n Zipios-%{version}
sed -i "s/\-std=c++11//g" CMakeLists.txt


%build
%cmake -DCATCH_INCLUDE_DIR=%{_includedir}/catch \
       -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \
       -DBUILD_ZIPIOS_TESTS=TRUE \
       %{nil}
%cmake_build


%install
%cmake_install
# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
for bin in appendzip dosdatetime zipios; do
    help2man -s 1 -N %{_vpath_builddir}/tools/$bin > %{buildroot}%{_mandir}/man1/$bin.1
done


%check
# Catch based testing is broken on gcc 6
# https://sourceforge.net/p/zipios/bugs/9/
# Test executable no longer compiles with gcc 7
# https://bugzilla.redhat.com/show_bug.cgi?id=1424569
# https://sourceforge.net/p/zipios/bugs/10/
# Still broken, gcc 10.2.1
# https://github.com/Zipios/Zipios/issues/4
#pushd %{_vpath_builddir}
#make run_zipios_tests


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%exclude %{_pkgdocdir}/html/
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*.1*

%files devel
%{_libdir}/*.so
%{_datadir}/cmake/ZipIos/
%{_includedir}/%{name}
%{_mandir}/man3/*

%files doc
%{_pkgdocdir}/html/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.5.0-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.5.0-1
- Update to 2.2.5.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-4
- catch → catch1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Update to latest upstream release.
- Disable unit testing until catch works with gcc 6.

* Mon Oct 19 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-5
- Use system catch now that it's available.

* Wed Sep 16 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-4
- Add cmake as requirement to devel subpackage.
- Fix references to documentation for directory ownership.
- Fix documentation install to be compliant with the packaging guidelines.
- Make doc subpackage only require the main package.
- Add help2man to build requirements to generate man pages.
- Update %%{_pkgdocdir} in %%files to fix directory ownership.

* Fri Aug 28 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-2
- Update license tag to GPLv2+.
- Fix dist tag.
- Add note to description how this package differs from zipios++.

* Mon May 11 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-1
- Initial packaging.
