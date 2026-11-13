%global appstream_minver 1.2.0
%global glib2_minver 2.80

%global asgen_jsdir %{_datadir}/appstream/templates/default/static/js

Name:           appstream-generator
Version:        1.0.0
Release:        1%{?dist}
Summary:        Fast AppStream metadata generator

License:        LGPL-3.0-or-later AND MIT
URL:            https://github.com/ximion/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
## Fix with libfyaml 0.9.6
Patch0:         https://github.com/ximion/appstream-generator/commit/0e63c36a321bd715ea92f9227910822b40545135.patch
## Fix tests
Patch1:         https://github.com/ximion/appstream-generator/commit/13b25cd209d47e42c8df96691dfbdb6648be6845.patch
Patch2:         https://github.com/ximion/appstream-generator/commit/069ccce39dc5c849e16d832e2d5964eca94b4db5.patch

BuildSystem:    meson

BuildRequires:  gcc-c++ >= 14.0
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(appstream) >= %{appstream_minver}
BuildRequires:  pkgconfig(appstream-compose) >= %{appstream_minver}
BuildRequires:  pkgconfig(lmdb) >= 0.9.22
BuildRequires:  pkgconfig(libarchive) >= 3.2
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libfyaml) >= 0.9.6
BuildRequires:  pkgconfig(quill) >= 11.1
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(inja) >= 3.5.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  meson >= 1.6
# For man pages
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl

# For tests
BuildRequires:  ffmpeg-free
BuildRequires:  optipng

# Included in the source tarball
Provides:       bundled(js-highlight) = 11.12.0
Provides:       bundled(js-uplot) = 1.6.32

Recommends:     ffmpeg-free
Recommends:     optipng

# We don't need to build for 32-bit architectures...
ExcludeArch:    %{ix86} %{arm32}

%description
appstream-generator is a tool to generate distribution metadata
from package repositories. It will extract icons, download
screenshots, validate and transform the metadata, and return
XML or YAML files that can be read by AppStream clients,
such as software centers. It will also generate issue reports
as JSON documents and HTML pages.

%prep
%autosetup -C -p1


%files
%license LICENSE
%doc MAINTAINERS NEWS README.md TODO
%{_bindir}/appstream-generator
%{_mandir}/man1/appstream-generator.1*
%{_datadir}/appstream/
%{_datadir}/metainfo/org.freedesktop.appstream.generator.metainfo.xml


%changelog
* Thu Nov 12 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.0.0-1
- Rebase to 1.0.0
- Modernize spec file

* Thu Sep 10 2026 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.1-5
- Rebuilt for libxml-2.5.4

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Nov 03 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.10.1-1
- Rebase to 0.10.1

* Sun Oct 26 2025 Kalev Lember <klember@redhat.com> - 0.9.1-9
- Rebuilt for ldc 1.41

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 0.9.1-6
- Rebuilt for ldc 1.40

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 0.9.1-5
- Rebuilt for ldc 1.39

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 final

* Tue Nov 07 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1~git20231008.4d2ebc3-1
- Bump to 0.9.1 git snapshot for AppStream 1.0 compatibility

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 0.8.8-2
- Rebuilt for ldc 1.30

* Wed Jul 27 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.8.8-1
- Update to 0.8.8

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 16 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.8.7-1
- Update to 0.8.7

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5

* Wed Aug 18 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4 (#1924378)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 0.8.2-3
- Use ldc_arches macro rather than hardcoding supported arches
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Neal Gompa <ngompa13@gmail.com> - 0.8.2-1
- Update to 0.8.2 (#1834975)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Neal Gompa <ngompa13@gmail.com> - 0.8.1-1
- Rebase to 0.8.1 (#1755095)
- Vendor JavaScript components and declare as bundled

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.7-1
- Update to 0.7.7 (#1674286)

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 0.7.4-2
- Rebuilt for ldc 1.14

* Sat Feb 02 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.4-1
- Rebase to 0.7.4 (#1563877)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 0.6.8-2
- Rebuilt for ldc 1.11

* Wed Feb 21 2018 Neal Gompa <ngompa13@gmail.com> - 0.6.8-1
- Update to 0.6.8 (#1544598)

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 0.6.7-3
- Rebuilt for ldc 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct  8 2017 Neal Gompa <ngompa13@gmail.com> - 0.6.7-1
- Initial packaging for Fedora (#1498468)
