# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

# Disable LTO because it breaks EFI binary build
%global _lto_cflags %{nil}

%global commit 496ae8501f244e38e812f234968121bb809e248b
%global commitdate 20240824
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           btrfs-efi
Version:        20230328^git%{commitdate}.%{shortcommit}
Release:        3%{?dist}
Summary:        EFI driver to enable Btrfs support

License:        LGPL-2.1-or-later
URL:            https://github.com/maharmstone/btrfs-efi
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Fix with native GCC
## Proposed upstream: https://github.com/maharmstone/btrfs-efi/pull/5
Patch:          0001-cmake-Refactor-to-use-an-EFI-building-module.patch
# Drop dupe memcpy and memset
Patch:          0002-Drop-duplicate-memcpy-and-memset-functions.patch

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
Provides:       bundled(zlib) = 1.2.11
Provides:       bundled(zstd)

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


%build
%cmake
%cmake_build


%install
%cmake_install


%changelog
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
