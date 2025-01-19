Name:           imv
Version:        4.5.0
Release:        4%{?dist}
Summary:        Image viewer for X11 and Wayland

License:        MIT
URL:            https://sr.ht/~exec64/imv/
Source:         https://git.sr.ht/~exec64/imv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://lists.sr.ht/~exec64/imv-devel/patches/41580
Patch:          imv-4.4.0-libheif-support-fixes.patch

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xkbcommon)
# wayland
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
# x11
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
# backends
BuildRequires:  freeimage-devel
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libjxl)

%description
imv is a command line image viewer intended for use with tiling window managers.
Features:
 - Native Wayland and X11 support
 - Support for dozens of image formats including: PNG, JPEG, animated GIFs, SVG,
    TIFF, various RAW formats, Photoshop PSD files
 - Configurable key bindings and behavior
 - Highly scriptable with IPC via imv-msg


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%meson \
    -Dlibnsgif=disabled \
    -Dlibpng=disabled  \
    -Dlibtiff=disabled
%meson_build


%install
%meson_install
# install platform-specific manuals
for manfile in %{name}-wayland.1 %{name}-x11.1; do
    ln -sf %{name}.1 %{buildroot}%{_mandir}/man1/$manfile
done


%check
%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/imv.desktop \
    %{buildroot}/%{_datadir}/applications/imv-dir.desktop


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}_config
%{_bindir}/%{name}
%{_bindir}/%{name}-dir
%{_bindir}/%{name}-msg
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-x11
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 13 2024 Sérgio Basto <sergio@serjux.com> - 4.5.0-2
- Rebuild for jpegxl (libjxl) 0.10.2

* Tue Feb 20 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0 (#2265221)

* Tue Feb 06 2024 František Zatloukal <fzatlouk@redhat.com> - 4.4.0-8
- Rebuilt for turbojpeg 3.0.2

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 4.4.0-7
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 4.4.0-3
- Rebuilt for ICU 73.2

* Fri Jun 02 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.4.0-2
- Enable libheif backend

* Wed Jan 18 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0 (#2162162)
- Convert License tag to SPDX

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 4.3.1-5
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.3.1-4
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1 (#2032268)

* Fri Aug 06 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 4.2.0-3
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-2
- Rebuild for ICU 67

* Wed Mar 25 2020 Aleksei Bavshin <alebastr89@gmail.com> - 4.1.0-1
- Initial package (#1812761)
