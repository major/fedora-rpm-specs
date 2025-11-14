Name:          ufs-utils
Version:       7.14.12
Release:       %autorelease
Summary:       Universal Flash Storage host controller utilities

License:       GPL-2.0-only
URL:           https://github.com/SanDisk-Open-Source/ufs-utils
Source0:       %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
The UFS Tool project have been created to allow access UFS device from
user space, and perform basic set of UFS operations: Read and write UFS
device configuration (flags, attributes, descriptors), FFU, etc... The
set of UFS Tool features is co-existing and updated beside BSG and SG
infrastructure in Linux Kernel.

%prep
%autosetup -p1
chmod 644 COPYING

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" %make_build

%install
install -D -p ufs-utils %{buildroot}/%{_bindir}/ufs-utils

%files
%license COPYING
%doc README.md
%{_bindir}/ufs-utils

%changelog
%autochangelog
