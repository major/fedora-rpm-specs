%define _legacy_common_support 1
Name:           fatsort
Version:        1.6.5.640
Release:        %autorelease
Summary:        FAT sorter for FAT16 and FAT32 filesystems

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://fatsort.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
# FIXME: Cannot run tests, because bbe is not available


%description
Fatsort is a utility written in C to sort FAT16 and FAT32 filesystems. It is
needed to sort files on cheap mp3 players that display files not sorted by
their name but by the order they appear in the file allocation table (FAT).


%prep
%autosetup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install
%make_install SBINDIR=%{_sbindir} MANDIR=%{_mandir}/man1


%files
%license LICENSE.txt
%doc CHANGES.md README
%{_mandir}/man1/fatsort.1*
%{_sbindir}/fatsort


%changelog
%autochangelog
