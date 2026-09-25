Name:           mint-themes
Epoch:          1
Version:        2.4.1
Release:        %autorelease
Summary:        Mint themes

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         switch_to_sassc.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  sassc

Recommends:     mint-x-icons

%description
A collection of mint themes.

%package -n     mint-y-theme
Summary:        The Mint-Y theme
Recommends:     mint-y-icons

%description -n	mint-y-theme
The Mint-Y theme.  This theme is based on the Arc theme.

%package -n     mint-themes-gtk3
Summary:        Mint themes for GTK3
Recommends:     mint-themes = %{epoch}:%{version}
Recommends:     mint-y-theme = %{epoch}:%{version}


%description -n	mint-themes-gtk3
A collection of mint themes for GTK3.

%package -n     mint-themes-gtk4
Summary:        Mint themes for GTK4
Recommends:     mint-themes = %{epoch}:%{version}
Recommends:     mint-y-theme = %{epoch}:%{version}

%description -n	mint-themes-gtk4
A collection of mint themes for GTK4.

%package -n	cinnamon-themes
Summary:        Mint themes for GTK3
Requires:       filesystem
Requires:       mint-themes-gtk3 = %{epoch}:%{version}
Requires:       mint-themes-gtk4 = %{epoch}:%{version}

%description -n	cinnamon-themes
Collection of the best themes available for Cinnamon


%prep
%autosetup -p1

%build
make

%install
%{__cp} -pr usr/ %{buildroot}
%fdupes -s %{buildroot}

%files
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/
%exclude %{_datadir}/themes/Mint-X*/gtk-3.0/*
%exclude %{_datadir}/themes/Mint-X*/gtk-4.0/*
%exclude %{_datadir}/themes/Mint-X*/cinnamon/

%files -n mint-y-theme
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-Y*/
%exclude %{_datadir}/themes/Mint-Y*/gtk-3.0/*
%exclude %{_datadir}/themes/Mint-Y*/gtk-4.0/*
%exclude %{_datadir}/themes/Mint-Y*/cinnamon/

%files -n mint-themes-gtk3
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/gtk-3.0/*
%{_datadir}/themes/Mint-Y*/gtk-3.0/*

%files -n mint-themes-gtk4
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/gtk-4.0/*
%{_datadir}/themes/Mint-Y*/gtk-4.0/*

%files -n cinnamon-themes
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/cinnamon/
%{_datadir}/themes/Mint-Y*/cinnamon/

%changelog
%autochangelog