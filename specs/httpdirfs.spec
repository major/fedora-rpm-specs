Name:           httpdirfs
Version:        1.3.3
Release:        %autorelease
Summary:        Mount HTTP directory listings as a virtual filesystem

License:        GPL-3.0-or-later WITH sqlitestudio-OpenSSL-exception
URL:            https://github.com/fangfufu/httpdirfs
Source0:        %{url}/archive/%{version}/httpdirfs-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(expat)
BuildRequires:  help2man

%description
HTTPDirFS is a FUSE filesystem that allows you to mount HTTP directory
listings, with a built-in persistent cache. It also supports
Airsonic/Subsonic servers. It uses libcurl for HTTP transfers, Gumbo for
HTML parsing, and FUSE3 for filesystem presentation.

%prep
%autosetup
# Tests require the Unity framework as a meson subproject download;
# disable them for the RPM build.
sed -i "/subdir('tests')/d" meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md USAGE.md
%{_bindir}/httpdirfs
%{_mandir}/man1/httpdirfs.1*

%changelog
%autochangelog
