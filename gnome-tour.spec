# Use bundled deps as we don't ship the exact right versions for all the
# required rust libraries
%global bundled_rust_deps 0

%global tarball_version %%(echo %{version} | tr '~' '.')

%if 0%{?bundled_rust_deps}
%global debug_package %{nil}
%endif

Name:           gnome-tour
Version:        43.0
Release:        5%{?dist}
Summary:        GNOME Tour and Greeter

# * gnome-tour source code is GPLv3+
# * welcome-fedora.svg is CC-BY-SA
# * bundled rust crates all include either MIT or GPLv3+ as one of the possible
#   licenses, which when compiled into gnome-tour binary together with GPLv3+
#   gnome-tour source code results in effective GPLv3+ for the resulting binary
License:        GPLv3+ and CC-BY-SA
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/gnome-tour/43/gnome-tour-%{tarball_version}.tar.xz
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

%if 0%{?bundled_rust_deps}
BuildRequires:  cargo
BuildRequires:  rust
%else
BuildRequires:  rust-packaging
%endif

%if 0%{?bundled_rust_deps}
# bundled crates list updated for gnome-tour 42.beta
Provides: bundled(crate(aho-corasick/default)) = 0.7.18
Provides: bundled(crate(anyhow/default)) = 1.0.53
Provides: bundled(crate(atty/default)) = 0.2.14
Provides: bundled(crate(autocfg/default)) = 1.0.1
Provides: bundled(crate(bitflags/default)) = 1.3.2
Provides: bundled(crate(block/default)) = 0.1.6
Provides: bundled(crate(cairo-rs/default)) = 0.15.1
Provides: bundled(crate(cairo-sys-rs/default)) = 0.15.1
Provides: bundled(crate(cc/default)) = 1.0.72
Provides: bundled(crate(cfg-expr/default)) = 0.9.0
Provides: bundled(crate(cfg-if/default)) = 1.0.0
Provides: bundled(crate(env_logger/default)) = 0.7.1
Provides: bundled(crate(field-offset/default)) = 0.3.4
Provides: bundled(crate(futures-channel/default)) = 0.3.19
Provides: bundled(crate(futures-core/default)) = 0.3.19
Provides: bundled(crate(futures-executor/default)) = 0.3.19
Provides: bundled(crate(futures-io/default)) = 0.3.19
Provides: bundled(crate(futures-task/default)) = 0.3.19
Provides: bundled(crate(futures-util/default)) = 0.3.19
Provides: bundled(crate(gdk4/default)) = 0.4.4
Provides: bundled(crate(gdk-pixbuf/default)) = 0.15.1
Provides: bundled(crate(gdk-pixbuf-sys/default)) = 0.15.1
Provides: bundled(crate(gdk4-sys/default)) = 0.4.2
Provides: bundled(crate(gettext-rs/default)) = 0.7.0
Provides: bundled(crate(gettext-sys/default)) = 0.21.2
Provides: bundled(crate(gio/default)) = 0.15.3
Provides: bundled(crate(gio-sys/default)) = 0.15.1
Provides: bundled(crate(glib/default)) = 0.15.3
Provides: bundled(crate(glib-macros/default)) = 0.15.3
Provides: bundled(crate(glib-sys/default)) = 0.15.1
Provides: bundled(crate(gobject-sys/default)) = 0.15.1
Provides: bundled(crate(graphene-rs/default)) = 0.15.1
Provides: bundled(crate(graphene-sys/default)) = 0.15.1
Provides: bundled(crate(gsk4/default)) = 0.4.4
Provides: bundled(crate(gsk4-sys/default)) = 0.4.2
Provides: bundled(crate(gtk4/default)) = 0.4.5
Provides: bundled(crate(gtk4-macros/default)) = 0.4.3
Provides: bundled(crate(gtk4-sys/default)) = 0.4.5
Provides: bundled(crate(heck/default)) = 0.3.3
Provides: bundled(crate(heck/default)) = 0.4.0
Provides: bundled(crate(humantime/default)) = 1.3.0
Provides: bundled(crate(lazy_static/default)) = 1.4.0
Provides: bundled(crate(libc/default)) = 0.2.74
Provides: bundled(crate(libadwaita/default)) = 0.1.0
Provides: bundled(crate(libadwaita-sys/default)) = 0.1.0
Provides: bundled(crate(libc/default)) = 0.2.114
Provides: bundled(crate(locale_config/default)) = 0.3.0
Provides: bundled(crate(log/default)) = 0.4.14
Provides: bundled(crate(malloc_buf/default)) = 0.0.6
Provides: bundled(crate(memchr/default)) = 2.4.1
Provides: bundled(crate(memoffset/default)) = 0.6.5
Provides: bundled(crate(objc/default)) = 0.2.7
Provides: bundled(crate(objc-foundation/default)) = 0.1.1
Provides: bundled(crate(objc_id/default)) = 0.1.1
Provides: bundled(crate(pango/default)) = 0.15.2
Provides: bundled(crate(pango-sys/default)) = 0.15.1
Provides: bundled(crate(pest/default)) = 2.1.3
Provides: bundled(crate(pin-project-lite/default)) = 0.2.8
Provides: bundled(crate(pin-utils/default)) = 0.1.0
Provides: bundled(crate(pkg-config/default)) = 0.3.24
Provides: bundled(crate(pretty_env_logger/default)) = 0.4.0
Provides: bundled(crate(proc-macro-crate/default)) = 1.1.0
Provides: bundled(crate(proc-macro-error/default)) = 1.0.4
Provides: bundled(crate(proc-macro-error-attr/default)) = 1.0.4
Provides: bundled(crate(proc-macro2/default)) = 1.0.36
Provides: bundled(crate(quick-error/default)) = 1.2.3
Provides: bundled(crate(quote/default)) = 1.0.15
Provides: bundled(crate(regex/default)) = 1.5.4
Provides: bundled(crate(regex-syntax/default)) = 0.6.25
Provides: bundled(crate(rustc_version/default)) = 0.3.3
Provides: bundled(crate(semver/default)) = 0.11.0
Provides: bundled(crate(semver-parser/default)) = 0.10.2
Provides: bundled(crate(serde/default)) = 1.0.136
Provides: bundled(crate(slab/default)) = 0.4.5
Provides: bundled(crate(smallvec/default)) = 1.8.0
Provides: bundled(crate(syn/default)) = 1.0.86
Provides: bundled(crate(system-deps/default)) = 6.0.0
Provides: bundled(crate(temp-dir/default)) = 0.1.11
Provides: bundled(crate(termcolor/default)) = 1.1.2
Provides: bundled(crate(thiserror/default)) = 1.0.30
Provides: bundled(crate(thiserror-impl/default)) = 1.0.30
Provides: bundled(crate(toml/default)) = 0.5.8
Provides: bundled(crate(ucd-trie/default)) = 0.1.3
Provides: bundled(crate(unicode-segmentation/default)) = 1.8.0
Provides: bundled(crate(unicode-xid/default)) = 0.2.2
Provides: bundled(crate(version-compare/default)) = 0.1.0
Provides: bundled(crate(version_check/default)) = 0.9.4
%endif

# Removed in F34
Obsoletes: gnome-getting-started-docs < 3.38.1-2
Obsoletes: gnome-getting-started-docs-cs < 3.38.1-2
Obsoletes: gnome-getting-started-docs-de < 3.38.1-2
Obsoletes: gnome-getting-started-docs-es < 3.38.1-2
Obsoletes: gnome-getting-started-docs-fr < 3.38.1-2
Obsoletes: gnome-getting-started-docs-gl < 3.38.1-2
Obsoletes: gnome-getting-started-docs-hu < 3.38.1-2
Obsoletes: gnome-getting-started-docs-it < 3.38.1-2
Obsoletes: gnome-getting-started-docs-pl < 3.38.1-2
Obsoletes: gnome-getting-started-docs-pt_BR < 3.38.1-2
Obsoletes: gnome-getting-started-docs-ru < 3.38.1-2

%description
A guided tour and greeter for GNOME.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

# Install Fedora branding
cp -a %{SOURCE1} data/resources/assets/welcome.svg

%if ! 0%{?bundled_rust_deps}
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson
%meson_build

%if ! 0%{?bundled_rust_deps}
%cargo_build
%endif


%install
%meson_install

%if ! 0%{?bundled_rust_deps}
%cargo_install
%endif

%find_lang gnome-tour


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Tour.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tour.desktop


%files -f gnome-tour.lang
%license LICENSE.md
%doc NEWS README.md
%{_bindir}/gnome-tour
%{_datadir}/gnome-tour/
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tour.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
%{_metainfodir}/org.gnome.Tour.metainfo.xml


%changelog
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
