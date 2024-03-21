Name:           deepin-gtk-theme
Version:        23.11.23
Release:        %autorelease
Summary:        Deepin GTK Theme
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

%description
%{summary}.

%prep
%autosetup -p1

%build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
%autochangelog
