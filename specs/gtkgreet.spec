Name:           gtkgreet
Version:        0.8
Release:        5%{?dist}
Summary:        GTK based greeter for greetd

License:        GPL-3.0-only
URL:            https://git.sr.ht/~kennylevinsen/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Desktop session file support - https://todo.sr.ht/~kennylevinsen/gtkgreet/8
Source100:      %{name}-update-environments
Source101:      %{name}.css
Source102:      %{name}-sway.conf
Source103:      %{name}-wayfire.ini
Source104:      %{name}-river-init

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(scdoc) >= 1.9.7

Requires:       greetd >= 0.6
Provides:       greetd-greeter = 0.6
Provides:       greetd-%{name} = %{version}
# upgrade path for copr builds
Obsoletes:      greetd-%{name} < 0.7-2

# gtkgreet requires a wayland compositor
Requires:       (sway or wayfire or river or cage)
Suggests:       sway

# Default background in the example configs
Recommends:     desktop-backgrounds-compat
# and the utility to display the background
Recommends:     swaybg
# Terminates the compositor once the greeter is done
Recommends:     wayland-logout

%description
%{summary}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}

install -D -m755 -vp %{SOURCE100} %{buildroot}%{_libexecdir}/gtkgreet-update-environments
install -D -m644 -vp %{SOURCE101} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet.css
install -D -m644 -vp %{SOURCE102} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-sway.conf
install -D -m644 -vp %{SOURCE103} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-wayfire.ini
# River config is an executable that talks with river via riverctl or wayland
# protocol and starts the apps
install -D -m755 -vp %{SOURCE104} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-river-init

mkdir -p %{buildroot}%{_sysconfdir}/greetd
touch %{buildroot}%{_sysconfdir}/greetd/environments


%post
# initialize list of session commands
if [ ! -f %{_sysconfdir}/greetd/environments ]; then
    %{_libexecdir}/gtkgreet-update-environments -w %{_sysconfdir}/greetd/environments
fi
exit 0


%files -f %{name}.lang
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/gtkgreet
%ghost %config(noreplace) %{_sysconfdir}/greetd/environments
%config(noreplace) %{_sysconfdir}/gtkgreet/gtkgreet.css
%config(noreplace) %{_sysconfdir}/gtkgreet/gtkgreet-sway.conf
%config(noreplace) %{_sysconfdir}/gtkgreet/gtkgreet-wayfire.ini
%config(noreplace) %{_sysconfdir}/gtkgreet/gtkgreet-river-init
%{_bindir}/gtkgreet
%{_libexecdir}/gtkgreet-update-environments
%{_mandir}/man1/gtkgreet.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.8-1
- Initial import (#2080706)
