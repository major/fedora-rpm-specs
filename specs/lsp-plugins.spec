Name:           lsp-plugins
Version:        1.2.19
Release:        2%{?dist}
Summary:        Linux Studio Plugins

License:        LGPL-3.0-or-later and Zlib
URL:            https://lsp-plug.in/
Source0:        https://github.com/sadko4u/%{name}/releases/download/%{version}/%{name}-src-%{version}.tar.gz

# Fixed atomic operations for AArch64
# https://github.com/lsp-plugins/lsp-common-lib/commit/156be4d61c57d805745b85d7fadb781a4bc581b0
Patch0:         156be4d61c57d805745b85d7fadb781a4bc581b0.patch

ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libstdc++-devel >= 4.7
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pipewire-jack-audio-connection-kit
%else
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.5
%endif
BuildRequires:  lv2-devel >= 1.10
BuildRequires:  ladspa-devel >= 1.13
BuildRequires:  expat-devel >= 2.1
BuildRequires:  libsndfile-devel >= 1.0.25
BuildRequires:  cairo-devel >= 1.14
BuildRequires:  php >= 5.5.14
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libGL-devel
BuildRequires:  php-cli
BuildRequires:  desktop-file-utils
BuildRequires:  libXrandr-devel
BuildRequires:  pkgconfig(gstreamer-audio-1.0)

Requires:       redhat-menus
Requires:       hicolor-icon-theme

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
compatible with LADSPA, LV2, LinuxVST formats and Standalone (using Jack).

%package -n liblsp-r3d-glx
Summary:        liblsp-r3d-glx plugin

%description -n liblsp-r3d-glx
Library liblsp-r3d-glx plugin.

%package -n liblsp-r3d-glx-devel
Summary:        liblsp-r3d-glx plugin development
Requires:       liblsp-r3d-glx%{?_isa} = %{version}-%{release}

%description -n liblsp-r3d-glx-devel
Library liblsp-r3d-glx plugin development.


%package doc
Summary:        Linux Studio Plugins documentation
BuildArch:      noarch

%description doc
Documentation for Linux Studio Plugins

%package ladspa
Summary:        Linux Studio Plugins LADSPA format
Requires:       ladspa%{?_isa}

%description ladspa
Linux Studio Plugins (LSP) compatible with the obsolete LADSPA format.

%package lv2
Summary:        Linux Studio Plugins LV2 format
Requires:       lv2%{?_isa}

%description lv2
Linux Studio Plugins (LSP) compatible with the LV2 format (recommended format).

%package vst
Summary:        Linux Studio Plugins VST format
Requires:       Carla-vst%{?_isa}

%description vst
Linux Studio Plugins (LSP) and UIs for Steinberg's VST 2.4 format ported on GNU/Linux Platform.

%package vst3
Summary:        Linux Studio Plugins VST 3 format
#Requires:       Carla-vst%{?_isa}

%description vst3
Linux Studio Plugins (LSP) and UIs for Steinberg's VST 3 format ported on GNU/Linux Platform.

%package jack
Summary:        Linux Studio Plugins JACK format

%description jack
Linux Studio Plugins (LSP) standalone versions for JACK Audio connection Kit with UI

%package clap
Summary:        Linux Studio Plugins CLAP format

%description clap
Linux Studio Plugins (LSP) compatible with the CLAP format.

%package gstreamer
Summary:        Linux Studio Plugins gstreamer format

%description gstreamer
Linux Studio Plugins (LSP) compatible with the gstreamer format.

%prep
%autosetup -p1 -n %{name}
rm -rf include/3rdparty/ladspa
sed -i "s|\$\(LDFLAGS_EXT\) -r|\$\(LDFLAGS_EXT\) -r %{build_ldflags}|" make/tools.mk
# sed -i 's|march=i586|march=i686|' make/system.mk
# sed -i 's|gst/|gstreamer-1.0/gst/|' modules/lsp-plugin-fw/include/lsp-plug.in/plug-fw/wrap/gstreamer/defs.h


%build
%ifarch %ix86
%global optflags %{optflags} -DLSP_PROFILING

%endif
%{set_build_flags}
make config ADD_FEATURES=xdg \
  PREFIX=%{_prefix} LIBDIR=%{_libdir} ETCDIR=%{_sysconfdir} \
  CFLAGS_EXT="%optflags" CXXFLAGS_EXT="%optflags"
%make_build


%install
%make_install GSTREAMER_INSTDIR=%{_libdir}/gstreamer-1.0
mv %{buildroot}%{_datadir}/doc .
rm %{buildroot}%{_libdir}/*.a

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_sysconfdir}/xdg/menus/applications-merged/%{name}.menu
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/%{name}.directory
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -n liblsp-r3d-glx
%license COPYING COPYING.LESSER
%{_libdir}/liblsp-r3d-glx-lib-1.0.21.so

%files -n liblsp-r3d-glx-devel
%{_libdir}/liblsp-r3d-glx-lib.so
%{_libdir}/pkgconfig/lsp-r3d-glx-lib.pc

%files doc
%license COPYING COPYING.LESSER
%doc doc/%{name}/*

%files ladspa
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/ladspa/%{name}*

%files lv2
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/lv2/%{name}*

%files vst
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/vst/%{name}*

%files vst3
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%dir %{_libdir}/vst3
%{_libdir}/vst3/%{name}*

%files jack
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/%{name}

%files clap
%dir %{_libdir}/clap
%{_libdir}/clap/%{name}.clap

%files gstreamer
%{_libdir}/gstreamer-1.0/libgstlsp-plugins*.so

%changelog
* Thu Nov 21 2024 Janne Grunau <janne-fdr@jannau.net> - 1.2.19-2
- Backport upstream aarch64 atomic_swap fix. Fixes rhbz#2327886

* Wed Nov 13 2024 Nikolas Nyby <nikolas@gnu.org> - 1.2.19-1
- Update to 1.2.19
- Switch to pipewire-jack-audio-connection-kit-devel where available

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Vasiliy Glazov <vascom2@gmail.com> - 1.2.16-1
- Update to 1.2.16

* Fri Apr 12 2024 Vasiliy Glazov <vascom2@gmail.com> - 1.2.15-2
- Disable i686 build

* Thu Mar 07 2024 Vasiliy Glazov <vascom2@gmail.com> - 1.2.15-1
- Update to 1.2.15

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 26 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.14-1
- Update to 1.2.14

* Thu Dec 14 2023 Hector Martin <marcan@fedoraproject.org> - 1.2.13-2
- Add patch to fix aarch64

* Mon Oct 30 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.13-1
- Update to 1.2.13

* Mon Oct 16 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.12-1
- Update to 1.2.12

* Mon Sep 11 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.11-1
- Update to 1.2.11

* Tue Aug 22 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.10-1
- Update to 1.2.10

* Fri Jul 21 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.8-1
- Update to 1.2.8

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.6-1
- Update to 1.2.6

* Mon Jan 30 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.2.5-1
- Update to 1.2.5
- Add CLAP plugin

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Vasiliy Glazov <vascom2@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Mon Sep 19 2022 Vasiliy Glazov <vascom2@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Vasiliy Glazov <vascom2@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Apr 05 2022 Vasiliy Glazov <vascom2@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Vasiliy Glazov <vascom2@gmail.com> - 1.1.31-1
- Update to 1.1.31

* Fri Oct 22 2021 Vasiliy Glazov <vascom2@gmail.com> - 1.1.30-3
- Makes doc not depend on main package

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Vasiliy Glazov <vascom2@gmail.com> - 1.1.30-1
- Update to 1.1.30

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Vasiliy Glazov <vascom2@gmail.com> - 1.1.29-1
- Update to 1.1.29

* Mon Dec 21 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.28-1
- Update to 1.1.28

* Thu Oct 01 2020 Jeff Law  <law@redhat.com> - 1.1.26-2
- Re-enable LTO

* Fri Sep 18 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.26-1
- Update to 1.1.26

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.24-1
- Update to 1.1.24

* Sun May 31 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.22-1
- Update to 1.1.22

* Thu Apr 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.19-1
- Update to 1.1.19

* Mon Apr 06 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.17-1
- Update to 1.1.17

* Sun Mar 29 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.15-1
- Update to 1.1.15

* Mon Mar 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.13-1
- Update to 1.1.13

* Mon Dec 23 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.11-1
- Update to 1.1.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.10-1
- Update to 1.1.10

* Thu Jun 27 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.9-2
- Corrected lisense
- Spec improvments

* Wed Jun 26 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.9-1
- Initial release
