%bcond check 1

Name:           phrog
Version:        0.50.0
Release:        %autorelease
Summary:        Mobile-friendly greeter for greetd
# phrog itself is licensed under GPL-3.0.
# (plus some test-only assets that are CC-BY-SA-4.0)
SourceLicense:  GPL-3.0-only AND CC-BY-SA-4.0
# The License tag reflects statically linked, vendored Rust dependencies:
License:        %{shrink:
    ((MIT OR Apache-2.0) AND Unicode-3.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    GPL-3.0-only AND
    LGPL-2.1-only AND
    MIT AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (Unlicense OR MIT)
}
# (taken from cargo_license_summary output and placed above)
URL:            https://github.com/samcday/phrog
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# To regenerate vendor tarball:
# dir="$(mktemp -d)"; version="$(cat phrog.spec| grep ^Version: | awk '{print $2}')"; tar -C $dir --strip-components=1 -xvf phrog-$version.tar.gz && (cd $dir && cargo vendor --locked --versioned-dirs $dir/vendor) && tar -C $dir -cvzf vendor-$version.tar.gz vendor/
Source:         vendor-%{version}.tar.gz

ExcludeArch:    %{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2426735
ExcludeArch:    ppc64le
# phrog is intended for mobile devices, s390x is a mainframe arch
ExcludeArch:    s390x

BuildRequires:  cargo-rpm-macros >= 25

%if %{with check}
# for dbus-run-session
BuildRequires:  dbus-daemon
# for desktop-file-validate
BuildRequires:  desktop-file-utils
# for xvfb-run
BuildRequires:  xorg-x11-server-Xvfb
# first-run test
BuildRequires:  foot
%endif

BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libphosh-0.45)

Requires:       accountsservice
Requires:       gnome-session
Requires:       greetd
Requires:       phoc
Requires:       phosh-osk = 1.0

%description
Phrog uses Phosh and greetd to provide a graphical login manager.

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0644 data/mobi.phosh.Phrog.service -t %{buildroot}%{_userunitdir}/
install -Dpm 0644 data/mobi.phosh.Phrog.target -t %{buildroot}%{_userunitdir}/
install -Dpm 0644 data/mobi.phosh.phrog.gschema.xml -t %{buildroot}%{_datadir}/glib-2.0/schemas/
install -Dpm 0644 data/phrog.session -t %{buildroot}%{_datadir}/gnome-session/sessions/
install -Dpm 0644 data/mobi.phosh.Phrog.desktop -t %{buildroot}%{_datadir}/applications/
install -Dpm 0644 dist/fedora/greetd-config.toml -t %{buildroot}%{_sysconfdir}/phrog/
install -Dpm 0644 dist/fedora/phrog.service -t %{buildroot}%{_unitdir}/
install -Dpm 0644 data/systemd-session.conf -T %{buildroot}%{_userunitdir}/gnome-session@phrog.target.d/session.conf
install -Dpm 0755 data/phrog-greetd-session -t %{buildroot}%{_libexecdir}/
install -d %{buildroot}%{_datadir}/phrog/autostart
install -d %{buildroot}%{_sysconfdir}/phrog/autostart
install -Dpm 0755 target/rpm/phrog -t %{buildroot}%{_bindir}/

%if %{with check}
%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/mobi.phosh.Phrog.desktop
# tests need a writable XDG_RUNTIME_DIR
export XDG_RUNTIME_DIR=/tmp/runtime-dir
mkdir -p ${XDG_RUNTIME_DIR}
chmod 0700 ${XDG_RUNTIME_DIR}
export G_MESSAGES_DEBUG=all
%{shrink:dbus-run-session xvfb-run -a -s -noreset phoc -S -E "%cargo_test"}
%endif

%post
%systemd_post phrog.service

%preun
%systemd_preun phrog.service

%postun
%systemd_postun_with_restart phrog.service

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/phrog
%{_datadir}/applications/mobi.phosh.Phrog.desktop
%{_datadir}/glib-2.0/schemas/mobi.phosh.phrog.gschema.xml
%{_datadir}/gnome-session/sessions/phrog.session
%dir %{_datadir}/phrog
%dir %{_datadir}/phrog/autostart
%{_libexecdir}/phrog-greetd-session
%dir %{_sysconfdir}/phrog
%dir %{_sysconfdir}/phrog/autostart
%config(noreplace) %{_sysconfdir}/phrog/greetd-config.toml
%{_unitdir}/phrog.service
%dir %{_userunitdir}/gnome-session@phrog.target.d
%{_userunitdir}/gnome-session@phrog.target.d/session.conf
%{_userunitdir}/mobi.phosh.Phrog.service
%{_userunitdir}/mobi.phosh.Phrog.target

%changelog
%autochangelog
