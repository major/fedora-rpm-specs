Name:           efitools
Version:        1.9.2
Release:        %autorelease
Summary:        Tools to manipulate EFI secure boot keys and signatures
License:        GPL-2.0-only and LGPL-2.1-or-later and BSD-2-Clause

# call-to-mktemp:
# https://github.com/vathpela/efitools/issues/2
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:        %{url}/snapshot/%{name}-%{version}.tar.gz
Patch1:         makefile-enable-harden-local-files.patch
Patch2:         fix-deps.patch
Patch3:         allow-riscv64-build.patch
Patch4:         sbat-compat.patch
Patch5:         fix-ftbfs-lp2083030.patch
Patch6:         drop-engine-options.patch

# same as gnu-efi
ExclusiveArch:  %{efi}

BuildRequires:  pkgconfig(openssl)

BuildRequires:  gcc
BuildRequires:  gnu-efi-devel
BuildRequires:  help2man
BuildRequires:  openssl
BuildRequires:  perl-File-Slurp
BuildRequires:  sbsigntools

Requires:       coreutils
Requires:       mtools
Requires:       parted
Requires:       util-linux
Recommends:     sbsigntools

%description
This package installs a variety of tools for manipulating keys and binary
signatures on UEFI secure boot platforms. The tools provide access to the keys
and certificates stored in the secure variables of the UEFI firmware, usually
in the NVRAM area.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install DOCDIR=%{buildroot}%{_docdir}/%{name}/ CFLAGS="%{optflags}"

rm -v %{buildroot}%{_docdir}/%{name}/COPYING

%global efi_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*

%files
%doc README
%license COPYING
%efi_tool cert-to-efi-hash-list
%efi_tool cert-to-efi-sig-list
%efi_tool efi-readvar
%efi_tool efi-updatevar
%efi_tool hash-to-efi-sig-list
%efi_tool sig-list-to-certs
%efi_tool sign-efi-sig-list
%{_bindir}/flash-var
%{_bindir}/efitool-mkusb

%changelog
%autochangelog
