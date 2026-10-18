Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        15.0
Release:        %autorelease
# snapraid itself is GPL-3.0-or-later but uses other source codes, breakdown:
# Apache-2.0 AND GPL-3.0-or-later: cmdline/metro.c
# BSD-2-Clause: tommyds/*
# GPL-2.0-or-later: raid/*
# GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain: cmdline/murmur3.c
# LGPL-2.0-or-later: cmdline/fnmatch.[ch]
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause

URL:            https://www.snapraid.it/
Source0:        https://github.com/amadvance/snapraid/releases/download/v%{version}/snapraid-%{version}.tar.gz

BuildRequires:  gcc make libblkid-devel

%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep
%setup -q

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%license COPYING LICENSES/*
%doc AUTHORS HISTORY README
%{_bindir}/snapraid
%{_mandir}/man1/snapraid*
%{_mandir}/*/man1/snapraid*

%changelog
%autochangelog

