Name:          zsync
Summary:       a file transfer program using the same algorithm as rsync over HTTP
URL:           http://zsync.moria.org.uk/
License:       Artistic-2.0 and Zlib and NTP and LicenseRef-Fedora-Public-Domain
               # Zlib: zlib/*
               # NTP: base64.c
               # PD: librcksum/*
Version:       0.6.2
Release:       %autorelease

Source0:       http://zsync.moria.org.uk/download/%{name}-%{version}.tar.bz2

# https://sources.debian.org/data/main/z/zsync/0.6.2-7/debian/patches/fix-build-with-gcc-14.patch
Patch1:        fix-build-with-gcc-14.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake

# "zsync uses a large part of zlib [...]. This code contains local changes by
#  me that are not compatible with and not available in standard zlib [...]."
Provides:      bundled(zlib)

%description
zsync is a file transfer program. It allows you to download a file from a
remote server, where you have a copy of an older version of the file on your
computer already. zsync downloads only the new parts of the file. It uses the
same algorithm as rsync. However, where rsync is designed for synchronising
data from one computer to another within an organisation, zsync is designed for
file distribution, with one file on a server to be distributed to thousands of
downloaders. zsync requires no special server software - just a web server to
host the files - and imposes no extra load on the server, making it ideal for
large scale file distribution.

%prep
%autosetup -p1
sed -i '/^doc_DATA/s/COPYING//' Makefile.am # avoid duplicating license file

%build
autoreconf -if
%configure
%make_build CFLAGS+="-Wno-old-style-definition -D_DEFAULT_SOURCE"
# bundled zlib uses old-style function definition, ignore.
# zsync uses deprecated _BSD_SOURCE in places, also define replacement.

%install
%make_install

%check
./check-zsyncmake

%files
%license COPYING
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}make
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
