%global srcname crypto
%global forgeurl https://github.com/SDL-Hercules-390/%{srcname}
%global commit a5096e5dd79f46b568806240c0824cd8cb2fcda2
%forgemeta

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Crypto provides a simple implementation of the Rijndael (now AES) and DES
encryption algorithms as well as the SHA1 and SHA2 hashing algorithms. The
library is almost a verbatim copy of the code from OpenBSD and PuTTY for use by
the SDL-Hercules-390 emulator.}

Name:           sdl-crypto
Version:        1.0.0
Release:        12%{?dist}
Summary:        Simple AES/DES encryption and SHA1/SHA2 hashing library

# The Public Domain declarations are under review:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/550
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/551
License:        LicenseRef-Fedora-Public-Domain AND MIT AND BSD-3-Clause
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
# both packages install /usr/include/sha2.h
Conflicts:      sha2-devel
# Renamed from crypto, remove once f40 and el8 are EOL
Provides:       crypto-devel%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-devel < 1.0.0-11
Provides:       crypto-static%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-static < 1.0.0-11

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-devel:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/%{srcname}.LICENSE.txt .

%files devel
%license %{srcname}.LICENSE.txt
%doc README.md
%doc %{_docdir}/%{name}-devel/%{srcname}.README.txt
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-11
- Properly obsolete the old crypto package
- Convert license tag to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-5.20220328gita5096e5
- Rename to sdl-crypto (RHBZ#2068621)
- Update summary and description to make it clear this is a fork
- Update to a5096e5 git snapshot
- Drop f32 logic and tidy up the specfile

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20210321git837705e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20210321git837705e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-2.20210321git837705e
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1.20210321git837705e
- Initial package
