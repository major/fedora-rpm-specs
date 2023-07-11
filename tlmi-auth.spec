Name:     tlmi-auth
Version:  1.0.1
Release:  %autorelease
Summary:  Utility function for certificate based authentication on Lenovo platforms
License:  GPL-2.0-or-later
URL:      https://www.github.com/lenovo/tlmi-auth/
Source:   %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: gcc
BuildRequires: meson
BuildRequires: openssl-devel

%description
%{summary}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files 
%license COPYING
%{_bindir}/tlmi-auth
%doc README.md

%check
%meson_test

%changelog
%autochangelog
