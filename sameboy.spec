
Name:           sameboy
Version:        0.15.8
Release:        2%{?dist}
Summary:        Game Boy and Game Boy Color emulator written in C

License:        MIT
URL:            https://github.com/LIJI32/SameBoy
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rgbds
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  desktop-file-utils

%description
SameBoy is an open source Game Boy (DMG) and Game Boy Color (CGB) emulator,
written in portable C. It has a native Cocoa front-end for MacOS,
an SDL front-end for other operating systems, and a libretro core.
It also includes a text-based debugger with expression evaluation.

%prep
%autosetup -n SameBoy-%{version}

%build
%set_build_flags
%make_build sdl DATA_DIR=%{_datadir}/%{name}/


%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}

%make_install FREEDESKTOP=true \
              PREFIX=%{_prefix} \
              DATA_DIR=%{_datadir}/%{name}/

cd FreeDesktop

cp %{name}.desktop %{name}-terminal.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install \
    --set-key=Name --set-value='SameBoy (Terminal)' \
    --set-key=Terminal --set-value='true' \
    --dir=%{buildroot}/%{_datadir}/applications \
    %{name}-terminal.desktop

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
%{_datadir}/applications/%{name}-terminal.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/x-gameboy*rom.png
%license LICENSE
%doc README.md


%changelog
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
