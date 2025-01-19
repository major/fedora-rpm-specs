# LuaJIT git snapshot
%global commit1 3f9389edc6cdf3f78a6896d550c236860aed62b2
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           howl
Version:        0.6
Release:        28%{?dist}
Summary:        Lightweight editor with a keyboard-centric minimalistic UI

# For a breakdown of the licensing, see LICENSE.md
# Automatically converted from old format: MIT and Public Domain and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD
URL:            https://howl.io
Source0:        https://github.com/howl-editor/howl/releases/download/%{version}/%{name}-%{version}.tgz
# newer git snapshot for LuaJIT for aarch64 support
Source1:        https://github.com/LuaJIT/LuaJIT/archive/%{commit1}/LuaJIT-%{shortcommit1}.tar.gz

# Bundled LuaJIT-2.1.0-beta3 failed to compile with this arches
ExcludeArch:    ppc64le s390x
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)

Obsoletes:      %{name}-data < 0.6-21

Requires:       hicolor-icon-theme

Recommends:     fontawesome-fonts

Provides:       bundled(luajit) = 2.1.0~beta3

# Filter out Python and Ruby requirements pulled in from examples
%global __requires_exclude_from ^%{_datadir}/howl/.*$

%global _description \
Howl is a general purpose editor that aims to be both lightweight and fully\
customizable. It's built on top of the very fast LuaJIT runtime, uses Gtk for\
its interface, and can be extended in either Lua or Moonscript. It's known to\
work on Linux, but should work on at least the *BSD's as well.

%description %{_description}

%prep
%autosetup -a1
%ifarch aarch64
rm -rf src/deps/LuaJIT-2.1.0-beta3
mv LuaJIT-%{commit1} src/deps/LuaJIT-2.1.0-beta3
%endif

%build
export HOST_CFLAGS="%{build_cflags}"
export HOST_LDFLAGS="%{build_ldflags}"
export TARGET_CFLAGS="%{build_cflags}"
export TARGET_LDFLAGS="%{build_ldflags}"
%make_build -C src

%install
%make_install -C src PREFIX=%{_prefix}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_avoid_bundling_of_fonts_in_other_packages
# We can install it in *Requires*
rm -r       %{buildroot}%{_datadir}/howl/fonts
# https://github.com/howl-editor/howl/pull/502
mv          %{buildroot}%{_datadir}/appdata %{buildroot}%{_metainfodir}
# https://github.com/howl-editor/howl/issues/501#issuecomment-484565885
find        %{buildroot}%{_datadir}/howl/bundles/python/misc/ -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@/usr/bin/python3@g' -i "{}" \;
find        %{buildroot}%{_datadir}/howl/bundles/ruby/misc/ -type f -name "*.rb" -exec sed -e 's@/usr/bin/env ruby@/usr/bin/ruby@g' -i "{}" \;

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/howl.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/howl.desktop

%files
%doc README.md Changelog.md
%license LICENSE.md
%{_bindir}/howl
%{_bindir}/howl-spec
%{_datadir}/applications/howl.desktop
%{_datadir}/howl/
%{_datadir}/icons/hicolor/scalable/apps/howl.svg
%{_metainfodir}/howl.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 03 2023 Pete Walter <pwalter@fedoraproject.org> - 0.6-22
- ExcludeArch i686 for https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Fri Feb 03 2023 Pete Walter <pwalter@fedoraproject.org> - 0.6-21
- Drop separate -data subpackage

* Thu Feb 02 2023 Pete Walter <pwalter@fedoraproject.org> - 0.6-20
- Update bundled LuaJIT for aarch64 support

* Thu Feb 02 2023 Pete Walter <pwalter@fedoraproject.org> - 0.6-19
- Fix FTBFS (rhbz#2045707)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-10
- Add ExcludeArch: aarch64 ppc64le s390x
- Remove Requires %{?_isa} from noarch package
- Remove fdupes

* Wed Apr 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-9
- Initial package
