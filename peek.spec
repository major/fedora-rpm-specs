%global uuid    com.uploadedlobster.%{name}

Name:           peek
Version:        1.5.1
Release:        7%{?dist}
Summary:        Animated GIF screen recorder with an easy to use interface
# The entire source code is GPLv3+ except:
# * MIT:        print-description.py
License:        GPLv3+ and MIT
URL:            https://github.com/phw/peek
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gzip
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python
BuildRequires:  txt2man
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(keybinder-3.0)

Requires:       dbus-common
Requires:       gstreamer1-plugins-good >= 1.2
Requires:       hicolor-icon-theme
# Available in RPM Fusion
# * https://rpmfusion.org/Configuration
#Recommends:     ffmpeg >= 3
#Recommends:     gstreamer1-plugins-ugly

# TODO: Rust package
#Recommends:     gifski

%description
Peek makes it easy to create short screencasts of a screen area. It was built
for the specific use case of recording screen areas, e.g. for easily showing UI
features of your own apps or for showing a bug in bug reports. With Peek, you
simply place the Peek window over the area you want to record and press
"Record". Peek is optimized for generating animated GIFs, but you can also
directly record to WebM or MP4 if you prefer.

Peek is not a general purpose screencast app with extended features but rather
focuses on the single task of creating small, silent screencasts of an area of
the screen for creating GIF animations or silent WebM or MP4 videos.

Peek runs on X11 or inside a GNOME Shell Wayland session using XWayland. Support
for more Wayland desktops might be added in the future.

Peek requires FFmpeg or running GNOME Shell session. FFmpeg avaliable in RPM
Fusion repo. Enabling the RPM Fusion repositories:

* RPM Fusion
  - https://rpmfusion.org/Configuration
  - https://rpmfusion.org/Howto/Multimedia


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}
# Don't show desktop entry for non-GNOME environment. Works only with:
# * gnome-shell and GNOME session
# * ffpmpeg (RPM Fusion)
# * gstreamer1-plugins-ugly (RPM Fusion)
# - https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SOUYWF72MZSEH27PBJB6FI5YBR4SXPVT/
# - https://github.com/phw/peek/issues/539
#
# Disable temporary in favour of proper upstream fix
%dnl sed -i  '/Desktop Entry/a OnlyShowIn=GNOME' \
%dnl         %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/man/man1/*.1*
%{_metainfodir}/*.xml


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-5
- fix: Add BR: python | python-unversioned-command required to fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Tue Feb 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Sun Feb 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-4
- Build with upstream patch:
  Show error dialog if recording backend is unavailable

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-2
- Drop weak deps which is not avaliable in official repo
- Don't show desktop entry for non-GNOME environment
- Cosmetic spec file fixes

* Tue Sep 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7.20190616gitaeb190d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-6.20190616gitaeb190d
- Update to 1.3.1-6.20190616gitaeb190d

* Wed Apr 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-5.20190508git6e76e30
- Initial package
