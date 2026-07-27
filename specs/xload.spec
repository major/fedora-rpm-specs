Name:       xload
Version:    1.2.1
Release:    %autorelease
Summary:    Tool to display system load average

License:    X11
URL:        https://www.x.org
Source0:    https://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.xz
Source1:    https://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg
Patch0:     xload-1.2.1-setgroups.patch
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)

%description
xload displays a periodically updating histogram of the system load average.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_bindir}/xload
%{_mandir}/man1/xload.1*
%{_datadir}/X11/app-defaults/XLoad

%changelog
%autochangelog

