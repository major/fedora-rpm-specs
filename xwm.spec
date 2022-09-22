Name:           xwm
Version:        0.1.9
Release:        %autorelease
Summary:        Tiny XCB floating window manager

License:        MIT
URL:            https://github.com/mcpcpc/xwm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

Recommends:     dmenu
Recommends:     st
Recommends:     surf
Suggests:       ImageMagick

%description
xwm is a tiny XCB floating window manager. It is a minimal viable solution
that was developed with single-monitor workflows in mind. Despite the small
footprint, xwm maintains extensibility and can be customized to enhance the
user experience.

%prep
%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xwm
%{_mandir}/man1/xwm.1*

%changelog
%autochangelog
