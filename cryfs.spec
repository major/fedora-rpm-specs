# The shared libraries are useless
%global _cmake_shared_libs %{nil}

Name:           cryfs
Version:        0.11.2
Release:        5%{?dist}
Summary:        Cryptographic filesystem for the cloud
License:        LGPLv3
URL:            https://www.cryfs.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         unversioned_python.patch
# fmt-9 formatter change
Patch1:         cryfs-0.11.2-fmt9-formatter.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  boost-devel

BuildRequires:  cryptopp-devel

BuildRequires:  python3
BuildRequires:  python3-versioneer

BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)

# Required library doesn't exist
ExcludeArch: i686

%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
%autosetup -p1

%build
%cmake \
    -G Ninja \
    -DDEPENDENCY_CONFIG=./cmake-utils/DependenciesFromLocalSystem.cmake \
    -DBUILD_TESTING=OFF \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCRYFS_UPDATE_CHECKS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DBoost_USE_STATIC_LIBS=OFF


%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md ChangeLog.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-unmount
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.2-4
- Patch for fmt-9

* Sun May 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.2-3
- Rebuilt for Spdlog #2088633

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.11.2-2
- Rebuilt for Boost 1.78

* Sun Mar 27 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.2-1
- Version update: 0.11.2

* Sun Feb 06 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-3
- ExcludeArch: i686

* Sat Feb 05 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.11.1-2
- Disable building useless internal shared libraries

* Sat Jan 22 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.11.1-1
- initial package
