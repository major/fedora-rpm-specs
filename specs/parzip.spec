Name:           parzip
Version:        1.4.0
Release:        %autorelease
Summary:        High performance parallel PKZIP implementation
License:        GPL-3.0-or-later
URL:            https://github.com/jpakkane/parzip
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)

%description
A command line utility to pack and unpack zip archives using multiple threads.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/parzip
%{_bindir}/parunzip
%{_mandir}/man1/parzip.1*
%{_mandir}/man1/parunzip.1*

%changelog
%autochangelog
