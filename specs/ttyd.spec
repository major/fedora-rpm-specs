Name:           ttyd
Version:        1.7.7
Release:        %autorelease
Summary:        Share your terminal over HTTP
License:        MIT
URL:            https://github.com/tsl0922/ttyd
Source:         https://github.com/tsl0922/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libuv-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconf
BuildRequires:  zlib-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web, inspired
by GoTTY.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*
%license LICENSE

%changelog
%autochangelog
