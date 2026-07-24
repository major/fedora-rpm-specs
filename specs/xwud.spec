Name:       xwud
Version:    1.0.8
Release:    %autorelease
Summary:    Tool to display an X window image

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto) >= 7.0.25

%description
xwud allows X users to display in a window an image saved in a specially
formatted dump file, such as produced by xwd.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
%doc README.md ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
