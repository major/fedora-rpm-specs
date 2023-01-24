%global app_id  com.github.tchx84.Flatseal

Name:           flatseal
Version:        1.8.1
Release:        1%{?dist}
Summary:        Manage Flatpak permissions

License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/Flatseal
Source0:        %{url}/archive/v%{version}/Flatseal-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  gjs
BuildRequires:  libhandy-devel >= 1.5
BuildRequires:  meson >= 0.59.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# loaded by imports.gi
Requires:       gtk3
Requires:       libappstream-glib
Requires:       libhandy
Requires:       webkit2gtk4.1

BuildArch:      noarch

%description
Flatseal is a graphical utility to review and modify permissions from your
Flatpak applications.


%prep
%autosetup -n Flatseal-%{version}
# disable gnome.post_install steps
sed -i -e 's/true/false/' meson.build


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc CHANGELOG.md DOCUMENTATION.md README.md
%{_bindir}/%{app_id}
%{_datadir}/%{name}
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}*
%{_datadir}/icons/hicolor/*/*/%{app_id}*


%changelog
* Sun Jan 22 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.1-1
- Initial build
