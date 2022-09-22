# dependency from rpmfusion; disabled by default
%bcond_with     libheif

Name:           imv
Version:        4.3.1
Release:        4%{?dist}
Summary:        Image viewer for X11 and Wayland

License:        MIT
URL:            https://sr.ht/~exec64/imv/
Source0:        https://git.sr.ht/~exec64/imv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
%if %{with libheif}
BuildRequires:  pkgconfig(libheif)
%endif
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44
BuildRequires:  pkgconfig(libturbojpeg)

%description
imv is a command line image viewer intended for use with tiling window managers.
Features:
 - Native Wayland and X11 support
 - Support for dozens of image formats including: PNG, JPEG, animated GIFs, SVG,
    TIFF, various RAW formats, Photoshop PSD files
 - Configurable key bindings and behavior
 - Highly scriptable with IPC via imv-msg


%prep
%autosetup -n %{name}-v%{version}


%build
%meson \
    -Dlibheif=%[%{with libheif}?"en":"dis"]abled \
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
    %{buildroot}/%{_datadir}/applications/imv-folder.desktop


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}_config
%{_bindir}/%{name}
%{_bindir}/%{name}-folder
%{_bindir}/%{name}-msg
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-x11
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-folder.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*

%changelog
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
