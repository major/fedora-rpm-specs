# -*-Mode: rpm-spec -*-
# Use 0 for release and 1 for git
%global   git 1
Version:  0.3.1
%global   forgeurl https://github.com/ammen99/wf-recorder
%if %{?git}
%global   commit a9725f75dd3469e1434c99e32607ad2b7ef62ace
%global   date 20221225
%endif
%forgemeta

Name:     wf-recorder
Summary:  Screen recorder for wlroots-based compositors eg swaywm
Release:  0.1%{?dist}
License:  MIT
URL:      %{forgeurl}
Source0:  %{forgesource}

%ifarch ppc64le
# fix compilation on ppc64le (gcc#58241)
%global configure_flags -Dcpp_std=gnu++11
%endif

BuildRequires: gcc-c++
BuildRequires: ffmpeg-free-devel
BuildRequires: meson
BuildRequires: ocl-icd-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
wf-recorder is a utility program for screen recording of wlroots-based
compositors (more specifically, those that support wlr-screencopy-v1
and xdg-output).

%prep
%forgesetup -a

%build
%meson %{?configure_flags}
%meson_build

%install
%meson_install

%files
%{_bindir}/wf-recorder*

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
* Thu Dec 22 2022 Bob Hepple <bob.hepple@gmail.com> - 0.3.1-0.1.20221222git3933ab2
- moving to rawhide/f38 - retire from fusion now that ffmpeg-free is available
- merge https://github.com/ammen99/wf-recorder/pull/198:
- change the default for wf-recorder to use only royalty-free codecs (libvpx-vp9) by default.
- merge https://github.com/ammen99/wf-recorder/pull/197:
- a minimal set of options to enable realtime encoding.

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Fri Jun 17 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.3.0-3
- rebuilt

* Thu Jun 16 2022 Bob Hepple <bob.hepple@gmail.com> - 0.3.0-1
- new version

* Sun Feb 06 2022 Leigh Scott <leigh123linux@gmail.com> - 0.2.2-0.1.20220129git9b9b471
- Update to git snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.1-3
- Rebuilt for new ffmpeg snapshot

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2.1-1
- new release

* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-3
- fixed release tag

* Tue Feb 25 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-2
- fix ppc64le compile error ref. https://bugzilla.rpmfusion.org/show_bug.cgi?id=5527

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-1
- fix release string

* Wed Feb 12 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-1
- Initial version of the package
