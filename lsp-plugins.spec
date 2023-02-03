Name:           lsp-plugins
Version:        1.2.5
Release:        1%{?dist}
Summary:        Linux Studio Plugins

License:        LGPL-3.0-or-later and Zlib
URL:            https://lsp-plug.in/
Source0:        https://github.com/sadko4u/%{name}/releases/download/%{version}/%{name}-src-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libstdc++-devel >= 4.7
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.5
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

Requires:       redhat-menus
Requires:       hicolor-icon-theme

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
compatibles with LADSPA, LV2, LinuxVST formats and Standalone (using Jack).

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

%package jack
Summary:        Linux Studio Plugins JACK format

%description jack
Linux Studio Plugins (LSP) standalone versions for JACK Audio connection Kit with UI

%package clap
Summary:        Linux Studio Plugins CLAP format

%description clap
Linux Studio Plugins (LSP) compatible with the CLAP format.

%prep
%autosetup -p1 -n %{name}
rm -rf include/3rdparty/ladspa
sed -i "s|\$\(LDFLAGS_EXT\) -r|\$\(LDFLAGS_EXT\) -r %{build_ldflags}|" make/tools.mk
# sed -i 's|march=i586|march=i686|' make/system.mk


%build
%ifarch %ix86
%global optflags %{optflags} -DLSP_PROFILING

%endif
%{set_build_flags}
make config ADD_FEATURES=xdg PREFIX=%{_prefix} LIBDIR=%{_libdir} \
CFLAGS_EXT="%optflags" CXXFLAGS_EXT="%optflags"
%make_build


%install
%make_install
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
%{_libdir}/liblsp-r3d-glx-lib-1.0.8.so

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

%files jack
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/%{name}

%files clap
%dir %{_libdir}/clap
%{_libdir}/clap/%{name}-clap-%{version}.clap

%changelog
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
