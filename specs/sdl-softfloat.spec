%global srcname SoftFloat
%global forgeurl https://github.com/SDL-Hercules-390/%{srcname}
%global commit c114c53e672d92671e0971cfbf8fe2bed3d5ae9e
%forgemeta

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Berkeley SoftFloat is a software implementation of binary floating-point that
conforms to the IEEE Standard for Floating-Point Arithmetic. The current
release supports five binary formats: 16-bit half-precision, 32-bit
single-precision, 64-bit double-precision, 80-bit double-extended- precision,
and 128-bit quadruple-precision.

This version is a fork by SoftDevLabs (SDL) to support the SDL-Hercules-390
emulator.}

Name:           sdl-softfloat
Version:        3.5.0
Release:        12%{?dist}
Summary:        Berkeley IEEE Binary Floating-Point Library (SDL version)

License:        BSD-3-Clause
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Renamed from softfloat, remove once f40 and el8 are EOL
Provides:       softfloat-devel%{?_isa} = %{version}-%{release}
Obsoletes:      softfloat-devel < 3.5.0-11
Provides:       softfloat-static%{?_isa} = %{version}-%{release}
Obsoletes:      softfloat-static < 3.5.0-11

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt \
  -e 's:DESTINATION  .:DESTINATION share/doc/%{name}-devel:g' \
  -e 's:DESTINATION doc:DESTINATION share/doc/%{name}-devel:g' \

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/softfloat.LICENSE.txt .

%files devel
%license softfloat.LICENSE.txt
%doc README.md CHANGELOG.txt
%doc %{_docdir}/%{name}-devel/softfloat.README.*
%doc %{_docdir}/%{name}-devel/%{srcname}*.html
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%changelog
* Thu Dec 26 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-12
- Update to c114c53 git snapshot

* Wed Jul 31 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-11
- Properly obsolete the old softfloat package
- Convert license tag to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-5
- Rename to sdl-softloat (RHBZ#2068621)
- Update summary and description to make it clear this is a fork
- Update to 4b0c326 git snapshot
- Drop f32 logic and tidy up the specfile

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-2.20210321git42f2f99
- Fix build on f32 and epel8

* Sun Mar 21 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-1.20210321git42f2f99
- Initial package
