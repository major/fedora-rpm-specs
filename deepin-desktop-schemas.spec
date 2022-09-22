Name:           deepin-desktop-schemas
Version:        5.10.6
Release:        %autorelease
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
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

%build
export GOPATH=%{gopath}
%make_build ARCH=x86

%install
%make_install PREFIX=%{_prefix}
cp %{buildroot}/usr/share/deepin-desktop-schemas/server-override %{buildroot}/usr/share/glib-2.0/schemas/91_deepin_product.gschema.override

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
