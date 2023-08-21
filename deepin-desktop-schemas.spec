Name:           deepin-desktop-schemas
Version:        6.0.2
Release:        %autorelease
Summary:        GSettings deepin desktop-wide schemas
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  glib2
#add jzy
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang(github.com/linuxdeepin/go-lib/keyfile)
BuildRequires:  make
ExclusiveArch:  %{go_arches}

Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-sound-theme
Obsoletes:      deepin-artwork-themes <= 15.12.4

%description
%{summary}.

%prep
%autosetup -p1

# fix default background url
sed -i '/picture-uri/s|default_background.jpg|default.png|' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
sed -i 's|python|python3|' Makefile tools/overrides.py
# connectivity check uri copy from /usr/lib/NetworkManager/conf.d/20-connectivity-fedora.conf
sed -i "s#'http://detect.uniontech.com', 'http://detectportal.deepin.com'#'http://fedoraproject.org/static/hotspot.txt'#" \
    schemas/com.deepin.dde.network-utils.gschema.xml
grep uniontech schemas/com.deepin.dde.network-utils.gschema.xml && exit 1 || :

%build
GOPATH=%{gopath} %make_build ARCH=x86

%install
%make_install PREFIX=%{_prefix}

%check
make test

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/deepin-appstore/
%{_datadir}/deepin-app-store/
%{_datadir}/%{name}/


%changelog
%autochangelog
