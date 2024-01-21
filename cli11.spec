# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

# Install documentation with the devel package documentation
%global _docdir_fmt %{name}-devel

Name:           cli11
Version:        2.3.2
Release:        5%{?dist}
Summary:        Command line parser for C++11

License:        BSD-3-Clause
URL:            https://github.com/CLIUtils/CLI11
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel

%description
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set with a simple and intuitive interface.

%package devel
Summary:        Command line parser for C++11
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set with a simple and intuitive interface.

%package        docs
# Doxygen adds files with licenses other than BSD-3-Clause.
# GPL-1.0-or-later: bc_s*.png, bdwn.png, closed.png, doc.png, doxygen.css,
#     doxygen.svg, folderclosed.png, folderopen.png, nav_*.png, open.png,
#     search/close.svg, search/mag*.svg, search/search.css, splitbar*.png,
#     sync_off.png, sync_on.png, tab_*.png, tabs.css
# MIT: dynsections.js, jquery.js, menu.js, menudata.js, search/search.js
License:        BSD-3-Clause AND GPL-1.0-or-later AND MIT
Summary:        Documentation for CLI11
BuildArch:      noarch

%description    docs
Documentation for CLI11.

%prep
%autosetup -p1 -n CLI11-%{version}

# Alter the icon path in README.md for the installed paths
sed -i.orig 's,\./docs,.,' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build
CXXFLAGS='%{build_cxxflags} -DCLI11_OPTIONAL -DCLI11_STD_OPTIONAL=1'
%cmake \
    -DCLI11_BUILD_DOCS:BOOL=TRUE \
    -DCLI11_BUILD_TESTS:BOOL=TRUE \
    -DCMAKE_CXX_STANDARD=17
%cmake_build

# Build the documentation
%cmake_build --target docs

%install
%cmake_install

%check
%ctest

%files devel
%doc CHANGELOG.md README.md docs/CLI11_300.png
%license LICENSE
%{_includedir}/CLI/
%{_datadir}/cmake/CLI11/
%{_datadir}/pkgconfig/CLI11.pc

%files docs
%doc %{_vpath_builddir}/docs/html
%doc docs/CLI11.svg docs/CLI11_100.png

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar  8 2023 Jerry James <loganjerry@gmail.com> - 2.3.2-3
- Header-only parent packages must not be noarch
- Update the catch2-devel dependency

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- Version 2.3.2

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1

* Wed Oct 12 2022 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- Version 2.3.0
- Further clarify license of the docs subpackage

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Convert License field to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 2.1.2-1
- Version 2.1.2
- Drop the -catch patch, no longer necessary

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1

* Tue Sep 21 2021 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0

* Thu Jul 29 2021 Ryan Curtin <ryan@ratml.org> - 2.0.0-1
- Upgrade to latest stable version.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jerry James <loganjerry@gmail.com> - 1.9.1-2
- Adapt to cmake changes in Rawhide

* Sun Jun 21 2020 Jerry James <loganjerry@gmail.com> - 1.9.1-1
- Version 1.9.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Jerry James <loganjerry@gmail.com> - 1.9.0-1
- Version 1.9.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Jerry James <loganjerry@gmail.com> - 1.8.0-1
- Initial RPM
