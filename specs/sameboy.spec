
Name:           sameboy
Version:        1.0
Release:        1%{?dist}
Summary:        Game Boy and Game Boy Color emulator written in C

License:        MIT
URL:            https://github.com/LIJI32/SameBoy
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/LIJI32/SameBoy/pull/681
# 1.0 made some changes that install the mimetype to the wrong location
Patch0:         0001-correct-mimetype-location-to-follow-the-shared-mime-.patch
# https://github.com/LIJI32/SameBoy/pull/682
# 1.0 made some changes that strips the build unconditionally
Patch1:         0001-strip-thumbnailer-on-release-builds-don-t-strip-on-i.patch
# https://github.com/LIJI32/SameBoy/pull/683
# Needed to fix builds for GCC 15
Patch2:         0001-add-missing-include-for-toupper-and-isxdigit.patch

Requires:       hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rgbds
BuildRequires:  desktop-file-utils
# SDL
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(gl)
# xdg-thumbnailer
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

%description
SameBoy is an open source Game Boy (DMG) and Game Boy Color (CGB) emulator,
written in portable C. It has a native Cocoa front-end for MacOS,
an SDL front-end for other operating systems, and a libretro core.
It also includes a text-based debugger with expression evaluation.

%package thumbnailer
Summary:        Thumbnailer for Game Boy and Game Boy Color games

%description thumbnailer
Thumbnailer for Game Boy and Game Boy Color games

%prep
%autosetup -n SameBoy-%{version} -p1

%build
%set_build_flags
%make_build \
    xdg-thumbnailer sdl \
    DATA_DIR=%{_datadir}/%{name}/


%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}

%make_install \
    PREFIX=%{_prefix} \
    DATA_DIR=%{_datadir}/%{name}/ \
    FREEDESKTOP=true \
    CONF=debug

cd FreeDesktop

cp %{name}.desktop %{name}-terminal.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.sym
%{_datadir}/%{name}/background.bmp
%dir %{_datadir}/%{name}/Shaders
%{_datadir}/%{name}/Shaders/*.fsh
%{_datadir}/%{name}/Palettes/*.sbp
%{_datadir}/%{name}/LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/x-gameboy*rom.png
%license LICENSE
%doc README.md

%files thumbnailer
%{_bindir}/sameboy-thumbnailer
%{_datadir}/thumbnailers/sameboy.thumbnailer

%changelog
* Thu Jan 23 2025 Jan200101 <sentrycraft123@gmail.com> - 1.0-1
- Update to 1.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Jan200101 <sentrycraft123@gmail.com> - 0.16.6-1
- Update to 0.16.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 0.16-1
- Update to 0.16

* Fri Sep 08 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.8-4
- remove terminal desktop entry

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.8-1
- Update to 0.15.8

* Mon Sep 26 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.6-1
- Update to 0.15.6

* Thu Aug 25 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.5-1
- Update to 0.15.5

* Tue Aug 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.4-1
- Update to 0.15.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Sun Jul 03 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.15-1
- Update to 0.15

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.14.7-1
- Update to 0.14.7

* Fri Oct 22 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.14.6-1
- Update to 0.14.6

* Sun Aug 01 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.14.5-1
- Update to 0.14.5

* Sun Aug 01 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.14.4-1
- Update to 0.14.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.14.3-1
- Initial spec
