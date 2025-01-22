# Force out of source build
%undefine __cmake_in_source_build

Name:           liborigin
Version:        3.0.3
Release:        4%{?dist}
Epoch:          1
Summary:        Library for reading OriginLab OPJ project files

License:        GPL-3.0-only
URL:            https://sourceforge.net/projects/liborigin/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

Provides:       liborigin2 = 2.0.0-21
Obsoletes:      liborigin2 < 2.0.0-21

%description
A library for reading OriginLab OPJ project files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       liborigin2-devel = 2.0.0-21
Obsoletes:      liborigin2-devel < 2.0.0-21

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DBUILD_STATIC_LIBS=off
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.3*
%{_bindir}/opj2dat
%exclude %{_docdir}/%{name}/html
# We have license in different location and FORMAT in -doc
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/FORMAT

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc FORMAT README
%license COPYING
%{_docdir}/%{name}/html/

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.3-1
- Update to 3.0.3 (#2295679)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.2-2
- Fix source URL

* Fri Jul 28 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.2-1
- Update to 3.0.2 (#2227374)

* Mon Jul 24 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.1-6
- Really remove the path

* Sat Jul 23 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.1-5
- Remove source path after cmake macro

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 11 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.1-1
- New release
- Drop unneeded patches
- Use new cmake options

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-10
- Fix for https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1:3.0.0-4
- Append curdir to CMake invokation. (#1668512)

* Fri Nov 23 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-3
- Build opj2dat against shared library - patch by Miquel Garriga
- Move unversioned shared library to devel subpackage

* Wed Nov 21 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-2
- Disable static library generation
- Add patch for exit calls - bug #24, patch by Miquel Garriga

* Sun Nov 18 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:3.0.0-1
- First v3.0.0 release
- Remove obsolete code from spec file
- Clean up the changelog
- Use epoch to provide an upgrade path from the old version
