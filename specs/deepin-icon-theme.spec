%global themes bloom bloom-dark bloom-classic bloom-classic-dark Sea vintage
%global start_logo start-here

Name:           deepin-icon-theme
Version:        2025.03.27
Release:        %autorelease
Summary:        Icons for the Deepin Desktop Environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/python
BuildRequires:  make
BuildRequires:  gtk-update-icon-cache
BuildRequires:  xcursorgen
BuildRequires:  fedora-logos

Requires:       papirus-icon-theme
Requires:       fedora-logos

%description
%{summary}.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install
cp -a ./Sea ./usr/share/icons/hicolor %{buildroot}%{_datadir}/icons
for theme in %{themes}; do
    for dir in %{buildroot}%{_datadir}/icons/$theme/places/*; do
        size=$(basename $dir)
        if [ -f %{_datadir}/icons/hicolor/${size}x${size}/places/%{start_logo}.png ]; then
            ln -sf ../../../hicolor/${size}x${size}/places/%{start_logo}.png $dir
        elif [ -f %{_datadir}/icons/hicolor/${size}/places/%{start_logo}.svg ]; then
            ln -sf ../../../hicolor/${size}/places/%{start_logo}.svg $dir
        fi
    done
    touch %{buildroot}%{_datadir}/icons/$theme/icon-theme.cache
done

%post
for theme in %{themes}; do
  touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
  for theme in %{themes}; do
    touch --no-create %{_datadir}/icons/$theme &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$theme &>/dev/null || :
  done
fi

%posttrans
for theme in %{themes}; do
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$theme &>/dev/null || :
done

%files
%license LICENSE
%{_datadir}/icons/hicolor/*/status/*.svg
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/bloom-dark/
%{_datadir}/icons/bloom/
%{_datadir}/icons/bloom-classic/
%{_datadir}/icons/bloom-classic-dark/
%{_datadir}/icons/Sea/
%{_datadir}/icons/vintage/
%ghost %{_datadir}/icons/*/icon-theme.cache

%changelog
%autochangelog
