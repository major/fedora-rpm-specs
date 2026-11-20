Name:           CSFML2
Summary:        C Interface for SFML, version 2
License:        Zlib

Version:        2.6.1
Release:        1%{?dist}

URL:            https://www.sfml-dev.org/download/csfml/
Source0:        https://github.com/SFML/CSFML/archive/%{version}/CSFML-%{version}.tar.gz

# Use install paths from GNUInstallDirs
# Cherr-picked from: https://github.com/SFML/CSFML/pull/398.patch
Patch0:         CSFML-2.6.1-Use_GNUInstallDirs.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SFML2-devel

# Prevent users from trying to install this alongside old versions of regular CSFML package
Conflicts: (CSFML >= 2.0.0 with CSFML < 3.0.0)

%description
CSFML2 is the official C interface for the SFML2 library (written in C++),
allowing to develop applications using C instead of C++.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

# This will conflict with any CSFML-devel version because they all
# provide a "libcsfml-system.so" file (and -audio, -graphics, etc)
Conflicts:      CSFML-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains developer documentation (in HTML format) for %{name}.


%prep
%autosetup -p1 -n CSFML-%{version}


%build
%cmake -DCSFML_BUILD_DOC=TRUE
%cmake_build


%install
%cmake_install

# Fix documentation being installed in wrong directory
install -m 755 -d %{buildroot}%{_datadir}/doc
mv \
	%{buildroot}%{_datadir}/CSFML/doc \
	%{buildroot}%{_datadir}/doc/%{name}

# Remove license.txt and readme.txt - rely on %%license and %%doc macros
rm %{buildroot}%{_datadir}/CSFML/license.md
rm %{buildroot}%{_datadir}/CSFML/readme.md


%ldconfig_scriptlets


%files
%license license.md
%doc readme.md
%{_libdir}/libcsfml-*.so.2*

%files devel
%{_includedir}/SFML/
%{_libdir}/libcsfml-*.so
%{_libdir}/pkgconfig/csfml*.pc

%files doc
%license license.md
%doc %{_datadir}/doc/%{name}/


%changelog
* Thu Nov 19 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.6.1-1
- Rename to CSFML2

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 15 2025 Cristian Le <git@lecris.dev> - 2.6.1-4
- Use default install paths from GNUInstallDirs

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.6.1-1
- Update to v2.6.1

* Mon Feb 05 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.6.0-1
- Update to v2.6.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 2.5.2-3
- Rebuild for SFML-2.6.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.2-1
- Update to v2.5.2
- Switch to downloading sources from GitHub (no v2.5.2 download available on sfml-dev.org)
- Convert License tag to SPDX

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-6
- Fix CMake-related FTBFS

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-3
- Do not install multiple copies of license.txt and readme.txt

* Thu Aug 12 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-2
- Change wildcard for .so files to protect against SONAME changes
- Fix license file not being installed properly
- Fix documentation being installed under wrong path
- Move documentation to -doc subpackage

* Mon Aug 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-1
- Update to v2.5.1

* Fri Jul 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5-1
- Initial packaging
