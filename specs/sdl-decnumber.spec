%global srcname decNumber
%global forgeurl https://github.com/SDL-Hercules-390/%{srcname}
%global commit 3aa2f4531b5fcbd0478ecbaf72ccc47079c67280
%forgemeta

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
The decNumber library implements the General Decimal Arithmetic Specification
in ANSI C. This specification defines a decimal arithmetic which meets the
requirements of commercial, financial, and human-oriented applications. It
also matches the decimal arithmetic in the IEEE 754 Standard for Floating
Point Arithmetic.

The library fully implements the specification, and hence supports integer,
fixed-point, and floating-point decimal numbers directly, including infinite,
NaN (Not a Number), and subnormal values. Both arbitrary-precision and
fixed-size representations are supported.

This version is a fork by SoftDevLabs (SDL) to support the SDL-Hercules-390
emulator.}

Name:           sdl-decnumber
Version:        3.68.0
Release:        12%{?dist}
Summary:        ANSI C General Decimal Arithmetic Library (SDL version)

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Renamed from decnumber, remove once f40 and el8 are EOL
Provides:       decnumber-devel%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-devel < 1.0.0-11
Provides:       decnumber-static%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-static < 1.0.0-11

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
# Renamed from decnumber, remove once f40 and el8 are EOL
Provides:       decnumber-doc = %{version}-%{release}
Obsoletes:      decnumber-doc < 1.0.0-11

%description    doc
The %{name}-doc package contains documentation and examples for %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-doc:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-doc/decnumber.ICU-license.html .

%files devel
%license decnumber.ICU-license.html
%doc README.md
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%files doc
%license decnumber.ICU-license.html
%doc %{_docdir}/%{name}-doc/decnumber.*
%doc examples

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-11
- Properly obsolete the old decnumber package

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-5.20220328git3aa2f45
- Rename to sdl-decnumber (RHBZ#2068621)
- Update summary and description to make it clear this is a fork
- Update to 3aa2f45 git snapshot
- Drop f32 logic and tidy up the specfile

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-4.20210321gitda66509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-3.20210321gitda66509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-2.20210321gitda66509
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-1.20210321gitda66509
- Initial package
