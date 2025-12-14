%global _vpath_srcdir ..

%global common_desc							\
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and	\
Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments	\
like Gnome, Cinnamon, Budgie, Pantheon, XFCE, Mate, etc.


Name:		arc-theme
Version:	20221218
Release:	%autorelease
Summary:	Flat theme with transparent elements

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/jnsh/%{name}
Source0:	%{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk3-devel
BuildRequires:	gtk4-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:	cinnamon
BuildRequires:	make
BuildRequires:	meson
BuildRequires:	gnome-shell

Requires:	filesystem
Requires:	gtk-murrine-engine
#Requires:	gnome-themes-extra

%description
%{common_desc}


%package plank
Summary:	Arc-theme for Plank dock

Requires:	%{name} == %{version}-%{release}

%if 0%{?fedora}
Requires:	plank
Supplements:	(%{name} and plank)
%endif

%description plank
%{common_desc}

This package contains the %{summary}.


%prep
%autosetup -p 1

%build
%{__mkdir} -p regular solid

pushd regular
%meson -Dthemes=cinnamon,gnome-shell,gtk2,gtk3,gtk4,metacity,plank,xfwm
%meson_build
popd

pushd solid
%meson -Dthemes=cinnamon,gnome-shell,gtk2,gtk3,gtk4,metacity,plank,xfwm -Dtransparency=false
%meson_build
popd

%install
pushd regular
%meson_install
popd

pushd solid
%meson_install
popd

# Install Plank-theme.
%{__mkdir} -p %{buildroot}/%{_datadir}/plank/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker-solid/

# cleanup plank theme files from main package
rm -fvr %{buildroot}/%{_datadir}/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}/plank

%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*

%files plank
%if 0%{?fedora}
%{_datadir}/plank/themes/*
%else
%{_datadir}/plank
%endif


%changelog
%autochangelog
