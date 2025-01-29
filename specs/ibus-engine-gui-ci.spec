Name:           ibus-engine-gui-ci
Version:        1.0.0.20220118
Release:        %autorelease
Summary:        GUI CI for IBus engines
License:        LGPL-2.0-or-later
URL:            https://github.com/fujiwarat/ibus-engine-gui-ci
Source0:        https://github.com/fujiwarat/ibus-engine-gui-ci/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2
BuildRequires:  ibus-devel
BuildRequires:  json-glib-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gtk3-devel
Requires:       ibus
Recommends:     ibus-desktop-testing

%description
GUI CI can run with ibus-desktop-testing-runner and engines get
focus events with the window manager.

%prep
%autosetup -S git

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%doc AUTHORS README
%license COPYING
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}

%changelog
%autochangelog
