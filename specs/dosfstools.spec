Name: dosfstools
Version: 4.2
Release: %autorelease
Summary: Utilities for making and checking MS-DOS FAT filesystems on Linux
License: GPL-3.0-or-later
Source0: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch:   https://github.com/dosfstools/dosfstools/commit/8da7bc93315c.patch
URL: https://github.com/dosfstools/dosfstools

BuildRequires: gcc
BuildRequires: make
# For tests
BuildRequires: xxd
# rhbz#2021638
Recommends: glibc-gconv-extra

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/mkfs.vfat
%endif

%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT filesystems on hard
drives or on floppies.

%prep
%autosetup -p1

%build
%configure --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing"

%install
%make_install PREFIX=%{_prefix}

# license file is in the licenses dir, drop ancient/duplicate docs
rm -f %{buildroot}%{_docdir}/%{name}/*

%check
make check

%files
%license COPYING
%doc NEWS README
%{_sbindir}/*
%{_mandir}/man8/*


%changelog
%autochangelog
