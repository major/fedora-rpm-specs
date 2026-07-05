Name:     image-garden
Version:  0.6.3
Release:  %autorelease
Summary:  Tool for creating test virtual machines

License:  Apache-2.0
URL:      https://gitlab.com/zygoon/image-garden
Source:   %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:     noarch

BuildRequires: make
BuildRequires: shellcheck
BuildRequires: python3
BuildRequires: python3-mypy

Requires:      edk2-aarch64
Requires:      edk2-ovmf
Requires:      genisoimage
Requires:      make
Requires:      python3-mypy
Requires:      qemu-img
Requires:      qemu-system-aarch64-core
Requires:      qemu-system-x86-core
Requires:      wget
Requires:      whois
Requires:      xz

%description
Image Garden downloads, initializes and optionally operates virtual machine
images for popular operating systems. All the systems are designed for
testing and come configured with well-known username and password, usually
matching the name of the system.

%prep
%autosetup -n %{name}-v%{version}

%build
%make_build

%check
make check

%install
%make_install prefix=%{_prefix}

%files
%{_includedir}/image-garden.mk
%{_bindir}/image-garden
%{_mandir}/man1/image-garden.1.*
%license LICENSE
%doc README.md NEWS
# SPDX meta-data for the NEWS file is not worth installing.
%exclude %{_docdir}/%{name}/NEWS.license
# Don't install Docker-container and snap-package NEWS
%exclude %{_docdir}/%{name}/NEWS.docker*
%exclude %{_docdir}/%{name}/NEWS.snappy*

%changelog
%autochangelog
