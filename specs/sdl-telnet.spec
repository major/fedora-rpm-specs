%global srcname telnet
%global forgeurl https://github.com/SDL-Hercules-390/%{srcname}
%global commit e0e2a9150cb0c7cea8b27ea126e1367b3f03b17e
%forgemeta

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
libtelnet is a library for handling the TELNET protocol for use by the
SDL-Hercules-390 emulator. It includes routines for parsing incoming data from
a remote peer as well as formatting data to be sent to the remote peer.

libtelnet uses a callback-oriented API, allowing application-specific handling
of various events. The callback system is also used for buffering outgoing
protocol data, allowing the application to maintain control of the actual
socket connection.

Features supported include the full TELNET protocol, Q-method option
negotiation, and NEW-ENVIRON.}

Name:           sdl-telnet
Version:        1.0.0
Release:        11%{?dist}
Summary:        Simple RFC-compliant TELNET implementation for SDL-Hercules-390

License:        LicenseRef-Fedora-Public-Domain
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

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

* Mon Mar 28 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-5.20220328gite0e2a91
- Update summary and description to make it clear this is a fork
- Update to e0e2a91 git snapshot
- Drop f32 logic and tidy up the specfile

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20210321git2aca101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20210321git2aca101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-2.20210321git2aca101
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1.20210321git2aca101
- Initial package
