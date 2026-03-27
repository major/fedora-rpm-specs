# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

# Disable Linux build flags because it breaks EFI binary build
%undefine _auto_set_build_flags
%global set_build_flags %{nil}
%global _cmake_shared_libs %{nil}

%global commit a17333f691c39e48cc3eac2eb251cf5b2f67e399
%global commitdate 20251111
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global madler_zlib_ver 1.3.2
%global madler_zlib_tag v%{madler_zlib_ver}
%global zstd_ver 1.5.7
%global zstd_tag v%{zstd_ver}

Name:           btrfs-efi
Version:        20230328^git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        EFI driver to enable Btrfs support

License:        LGPL-2.1-or-later
URL:            https://github.com/maharmstone/btrfs-efi
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://github.com/madler/zlib/archive/%{madler_zlib_tag}/zlib-%{madler_zlib_ver}.tar.gz
Source2:        https://github.com/facebook/zstd/archive/%{zstd_tag}/zstd-%{zstd_ver}.tar.gz

# Fix with native GCC
## Proposed upstream: https://github.com/maharmstone/btrfs-efi/pull/5
Patch:          0001-cmake-Refactor-to-use-an-EFI-building-module.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnu-efi-devel >= 3.0.18
BuildRequires:  make

ExclusiveArch:  %{efi}

%description
%{summary}.

%dnl -------------------------------------------------------------

%package unsigned-%{efi_arch}
Summary:        EFI driver for %{efi_arch} to enable Btrfs support
License:        LGPL-2.1-or-later AND Zlib AND BSD-3-Clause AND BSD-2-Clause
Requires:       efi-filesystem
Provides:       %{name}-driver-%{efi_arch}
Conflicts:      %{name}-driver-%{efi_arch}
# Modified versions for building in the EFI driver
Provides:       bundled(lzo)
Provides:       bundled(xxhash)
Provides:       bundled(madler_zlib) = %{madler_zlib_ver}
Provides:       bundled(zstd) = %{zstd_ver}

BuildArch:      noarch

%description unsigned-%{efi_arch}
%{summary}.

%files unsigned-%{efi_arch}
%license LICENCE
%doc README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/btrfs%{efi_arch}.efi

%dnl -------------------------------------------------------------

%prep
%autosetup -n %{name}-%{commit} -S git_am
mkdir -p src/{zlib,zstd}
tar -C src/zlib --strip-components=1 -xf %{S:1}
tar -C src/zstd --strip-components=1 -xf %{S:2}


%conf
%cmake


%build
%cmake_build


%install
%cmake_install


%changelog
* Wed Mar 25 2026 Neal Gompa <ngompa@fedoraproject.org> - 20230328^git20251111.a17333f-1
- Bump to new git snapshot
- Refresh patch set

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 20230328^git20240824.496ae85-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 20230328^git20240824.496ae85-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Oct 17 2025 Michel Lind <salimma@fedoraproject.org> - 20230328^git20240824.496ae85-5
- aarch64: work around loading an RWX segment now being considered an error; Resolves: RHBZ#2384486

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230328^git20240824.496ae85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230328^git20240824.496ae85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 08 2024 Neal Gompa <ngompa@fedoraproject.org> - 20230328^git20240824.496ae85-2
- Fix patch to build properly as EFI driver

* Sun Sep 08 2024 Neal Gompa <ngompa@fedoraproject.org> - 20230328^git20240824.496ae85-1
- Bump to new snapshot
- Refresh patch set

* Mon Sep 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 20230328^git20240520.c134e61-2
- Specify minimum gnu-efi version

* Sat Aug 31 2024 Neal Gompa <ngompa@fedoraproject.org> - 20230328^git20240520.c134e61-1
- Initial package
