Name:       mako
Version:    1.9.0
Release:    3%{?dist}
Summary:    Lightweight Wayland notification daemon
Provides:   desktop-notification-daemon

License:    MIT
URL:        https://github.com/emersion/%{name}
Source0:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:    https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

Patch0: add-systemd-service-dbus.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.60.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus
Recommends:     jq
%{?systemd_requires}

%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson \
    -Dwerror=false \
    -Dsd-bus-provider=libsystemd \
    -Dbash-completions=true \
    -Dfish-completions=true \
    -Dzsh-completions=true
%meson_build

%install
%meson_install

# Install dbus-activated systemd unit
install -m0644 -Dt %{buildroot}%{_userunitdir}/ contrib/systemd/mako.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1*
%{_mandir}/man5/mako.5*
%{_mandir}/man1/makoctl.1*
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/fr.emersion.mako.service
%{bash_completions_dir}/mako*
%{fish_completions_dir}/mako*.fish
%{zsh_completions_dir}/_mako*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 02 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 03 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0 (#2211755)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1 (#2105115)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6-1
- Update to 1.6
- Install fish completions

* Tue May 04 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5-1
- Update to 1.5
- Sync BuildRequires with meson.build
- Use upstream service file
- Verify source signature

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 2020 Stefano Figura <stefano@figura.im> - 1.4.1-1
- Upstream 1.4.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Jeff Peeler <jpeeler@redhat.com> - 1.4-1
- Upstream 1.4 release
- Removed D-Bus service file as it is upstream now

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Jeff Peeler <jpeeler@redhat.com> - 1.3-1
- Upstream 1.3 release

* Thu Apr 04 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-2
- Fix location of systemd service file

* Sun Mar 17 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-1
- Let there be package
