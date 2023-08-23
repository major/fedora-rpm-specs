%global md5() {$(echo -n %1 | md5sum | awk '{print$1}')}
%if 0%{?fedora} >= 38
%global fedora_release_name f38
%else
%global fedora_release_name f%{?fedora}
%endif

Name:           deepin-wallpapers
Version:        1.7.7
Release:        %autorelease
Summary:        Deepin Wallpapers provides wallpapers of DDE
# SPDX migration
License:        GPL-3.0-only
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  deepin-api
# convert default Fedora wallpaper to jpg format
BuildRequires:  /usr/bin/convert
# for the current default wallpaper
BuildRequires:  %{fedora_release_name}-backgrounds-base
BuildRequires:  make
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
mv deepin/desktop.jpg deepin/deepin-desktop.jpg
convert %{_datadir}/backgrounds/%{fedora_release_name}/default/%{fedora_release_name}-01-day.png \
        deepin/desktop.jpg
%make_build

%install
install -d %{buildroot}%{_datadir}/wallpapers/deepin/
cp deepin/* deepin-private/* deepin-community/* %{buildroot}%{_datadir}/wallpapers/deepin/

install -d %{buildroot}%{_var}/cache/
cp -ar image-blur %{buildroot}%{_var}/cache/

install -d %{buildroot}%{_datadir}/backgrounds/deepin/
ln -sv ../../wallpapers/deepin/Hummingbird_by_Shu_Le.jpg \
  %{buildroot}%{_datadir}/backgrounds/deepin/desktop.jpg
ln -sv %{md5 %{_datadir}/wallpapers/deepin/Hummingbird_by_Shu_Le.jpg}.jpg \
  %{buildroot}%{_var}/cache/image-blur/%{md5 %{_datadir}/backgrounds/deepin/desktop.jpg}.jpg

touch %{buildroot}%{_datadir}/backgrounds/default_background.jpg

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_datadir}/backgrounds/default_background.jpg \
    deepin-default-background %{_datadir}/wallpapers/deepin/desktop.jpg 50
fi

%postun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove deepin-default-background %{_datadir}/wallpapers/deepin/desktop.jpg
fi

%files
%doc README.md
%license LICENSE
%ghost %{_datadir}/backgrounds/default_background.jpg
%{_datadir}/backgrounds/deepin/
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
%autochangelog
