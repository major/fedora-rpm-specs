%global commit b6e81a0b1e8abdcfdf321569a61524a3a01c8cc4
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           casync
Version:        2.git%{shortcommit}
Release:        %autorelease
Summary:        Content Addressable Data Synchronizer

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/casync
%if %{defined commit}
Source0:        https://github.com/keszybz/casync/archive/%{?commit}/casync-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/systemd/casync/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

Patch:          0001-casync-drop-kernel-includes.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liblzma) >= 5.1.0
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl) >= 7.32.0
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  libacl-devel
# for rpm macros
BuildRequires:  systemd
# for tests
BuildRequires:  rsync
# for the man page
BuildRequires:  python3-sphinx

%description
casync provides a way to efficiently transfer files which change over
time over the internet. It will split a given set into a git-inspired
content-addressable set of smaller compressed chunks, which can then
be conveniently transferred using HTTP. On the receiving side those
chunks will be uncompressed and merged together to recreate the
original data. When the original data is modified, only the new chunks
have to be transferred during an update.

%prep
%autosetup -p1 %{?commit:-n %{name}-%{commit}}

%build
%meson
%meson_build

%check
%meson_test \
%ifarch ppc64le
|| :
%endif

%install
%meson_install

%files
%license LICENSE.LGPL2.1
%doc README.md TODO
%_bindir/casync
%dir %_prefix/lib/casync
%dir %_prefix/lib/casync/protocols
%_prefix/lib/casync/protocols/casync-ftp
%_prefix/lib/casync/protocols/casync-http
%_prefix/lib/casync/protocols/casync-https
%_prefix/lib/casync/protocols/casync-sftp
%_mandir/man1/casync.1*
%_udevrulesdir/75-casync.rules
/usr/share/bash-completion/completions/casync

%changelog
%autochangelog
