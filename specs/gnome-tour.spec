%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-tour
Version:        47.0
Release:        2%{?dist}
Summary:        GNOME Tour and Greeter

# * gnome-tour source code is GPL-3.0-or-later
# * welcome-fedora.svg is CC-BY-SA-3.0
# * rust crate dependencies are:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND MIT AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz
# https://pagure.io/fedora-workstation/issue/175
Source1:        welcome-fedora.svg

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif

%description
A guided tour and greeter for GNOME.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%if 0%{?fedora}
# Install Fedora branding
install -p %{SOURCE1} data/resources/assets/welcome.svg
%endif

%if 0%{?bundled_rust_deps}
%cargo_prep -v vendor
%else
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install

%find_lang gnome-tour


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Tour.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tour.desktop


%files -f gnome-tour.lang
%license LICENSE.md
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc NEWS README.md
%{_bindir}/gnome-tour
%{_datadir}/gnome-tour/
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tour.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
%{_metainfodir}/org.gnome.Tour.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Fabio Valentini <decathorpe@gmail.com> - 46.0-2
- Rebuild with Rust 1.78 to fix incomplete debuginfo and backtraces.

* Sun Apr 07 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Feb 07 2024 Kalev Lember <klember@redhat.com> - 45.0-5
- Drop downstream patch that downgraded pretty_env_logger dep to 0.4
- Don't use both meson and cargo for building
- Migrate to SPDX license

* Thu Feb 01 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 45.0-4
- Update Rust macro usage

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0
- Downgrade pretty_env_logger dep to 0.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 44.0-2
- Enable bundled deps in RHEL builds
- Update bundled provides
- Only use Fedora branding in Fedora builds

* Tue Mar 21 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Mon Mar 06 2023 Kalev Lember <klember@redhat.com> - 43.0-5
- Rebuilt for rust-gtk4 0.4.9

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 43.0-4
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Kalev Lember <klember@redhat.com> - 43.0-2
- Switch to packaged rust deps

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41~rc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Kalev Lember <klember@redhat.com> - 40.0-2
- Add missing obsoletes for gnome-getting-started-docs-hu (#1954117)

* Tue Mar 23 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Wed Mar 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-5
- Update the fedora logo in welcome image (#1940041)

* Tue Feb 23 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 40~beta-4
- Obsolete all language-specific gnome-getting-started-docs subpackages

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~beta-3
- Obsolete gnome-getting-started-docs

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-2
- New welcome image for Fedora branding (thanks, jimmac!)

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Kalev Lember <klember@redhat.com> - 3.38.0-2
- Add missing gstreamer1-plugins-good-gtk dep (#1889657)

* Wed Sep 16 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.37.92-2
- Use a lower res video to improve the layout (thanks jimmac!)

* Tue Sep 08 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Thu Aug 27 2020 Kalev Lember <klember@redhat.com> - 3.37.91-2
- Add provides for bundled rust crates (#1873108)
- Clarify licensing for bundled rust crates (#1873108)

* Thu Aug 27 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Initial Fedora packaging
