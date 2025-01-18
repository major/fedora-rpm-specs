Name:           easyeffects
Version:        7.2.3
Release:        3%{?dist}
Summary:        Audio effects for PipeWire applications

License:        GPL-3.0-or-later
Url:            https://github.com/wwmm/easyeffects
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Provides:       pulseeffects = 6.1.1-1
Obsoletes:      pulseeffects < 6.1.1-1

BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  boost-devel >= 1.70
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  zita-convolver-devel >= 3.1.0
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  cmake
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  ladspa-devel

Requires:       hicolor-icon-theme
Requires:       dbus-common

Recommends:     lv2-calf-plugins
Recommends:     lv2-mdala-plugins
Recommends:     lsp-plugins-lv2
Recommends:     lv2-zam-plugins


%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PipeWire applications.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
--dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}
%find_lang %{name}-news
cat %{name}-news.lang >> %{name}.lang

# Change absolute symlinks to relative
# https://github.com/wwmm/pulseeffects/issues/590
find %{buildroot}%{_datadir}/help/ -type l -exec bash -c 'ln -sf ../../../C/easyeffects/figures/$(basename {}) {}' \;


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.wwmm.%{name}-symbolic.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%{_datadir}/help/*
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 7.2.3-2
- Rebuilt for rubberband 4

* Thu Jan 09 2025 Vasiliy N. Glazov <vascom2@gmail.com> - 7.2.3-1
- Update to 7.2.3

* Wed Jan 08 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 7.1.9-3
- Update plugin dependencies

* Mon Oct 07 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.9-2
- Update to 7.1.9
- Make lv2-calf-plugins weak dependency (#2313553)

* Mon Jul 22 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.7-1
- Update to 7.1.7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 01 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.6-1
- Update to 7.1.6

* Mon Mar 25 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.5-1
- Update to 7.1.5

* Tue Feb 06 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.4-1
- Update to 7.1.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 7.1.3-2
- Rebuilt for TBB 2021.11

* Thu Nov 09 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.3-1
- Update to 7.1.3

* Mon Oct 30 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.1-1
- Update to 7.1.1

* Tue Sep 12 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.0-1
- Update to 7.1.0

* Thu Aug 31 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.8-1
- Update to 7.0.8

* Mon Aug 14 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.7-1
- Update to 7.0.7

* Tue Aug 01 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.6-1
- Update to 7.0.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 7.0.5-2
- Rebuilt due to fmt 10 update.

* Wed Jun 28 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.5-1
- Update to 7.0.5

* Tue May 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.4-1
- Update to 7.0.4

* Sat Apr 08 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.3-1
- Update to 7.0.3

* Sun Feb 26 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.1-1
- Update to 7.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Mon Sep 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Mon Aug 01 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.8-1
- Update to 6.2.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.7-1
- Update to 6.2.7

* Sun Jul 17 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.6-2
- Rebuild for new fmt

* Mon Jun 27 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.6-1
- Update to 6.2.6

* Thu May 05 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.5-1
- Update to 6.2.5

* Mon Mar 14 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.4-1
- Update to 6.2.4

* Mon Jan 31 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Nov 25 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.2-2
- Fix obsoleting pulseeffects

* Tue Sep 21 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Sun Sep 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.1-1
- Initial packaging
