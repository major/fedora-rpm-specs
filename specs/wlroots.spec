# Version of the .so library
%global abi_ver 0.19
# libliftoff does not bump soname on API changes
%global liftoff_ver 0.5.0
%global tag     0.19.0

Name:           wlroots
Version:        0.19.0
Release:        2%{?dist}
Summary:        A modular Wayland compositor library

# Source files/overall project licensed as MIT, but
# - HPND-sell-variant
#   * protocol/drm.xml
#   * protocol/wlr-data-control-unstable-v1.xml
#   * protocol/wlr-foreign-toplevel-management-unstable-v1.xml
#   * protocol/wlr-gamma-control-unstable-v1.xml
#   * protocol/wlr-input-inhibitor-unstable-v1.xml
#   * protocol/wlr-layer-shell-unstable-v1.xml
#   * protocol/wlr-output-management-unstable-v1.xml
# - LGPL-2.1-or-later
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        %{url}/-/releases/%{tag}/downloads/%{name}-%{tag}.tar.gz
Source1:        %{url}/-/releases/%{tag}/downloads/%{name}-%{tag}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

# this file is a modification of examples/meson.build so as to:
# - make it self-contained
# - only has targets for examples known to compile well (cf. "examples) global)
Source3:        examples.meson.build

# Upstream patches

# Fedora patches
# Following patch is required for phoc.
Patch:          Revert-layer-shell-error-on-0-dimension-without-anch.patch

BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 1.3

BuildRequires:  (pkgconfig(libdisplay-info) >= 0.1.1 with pkgconfig(libdisplay-info) < 0.3)
BuildRequires:  (pkgconfig(libliftoff) >= %{liftoff_ver} with pkgconfig(libliftoff) < 0.6)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.122
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1) >= 0.43.0
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.23.1
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
# libliftoff does not bump soname on API changes
Requires:       libliftoff%{?_isa} >= %{liftoff_ver}

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# not required per se, so not picked up automatically by RPM
Recommends:     pkgconfig(xcb-icccm)
# for examples
Suggests:       gcc
Suggests:       meson >= 0.58.0
Suggests:       pkgconfig(wayland-egl)

%description    devel
Development files for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -n %{name}-%{tag}
# apply unconditional patches (0..99)
%autopatch -p1 -M99
# apply conditional patches (100..)


%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
)

%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}


%install
%{meson_install}
install -pm0644 -D '%{SOURCE3}' '%{buildroot}/%{_pkgdocdir}/examples/meson.build'


%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%{_libdir}/libwlroots-%{abi_ver}.so


%files  devel
%doc %{_pkgdocdir}/examples
%{_includedir}/wlroots-%{abi_ver}/wlr
%{_libdir}/pkgconfig/wlroots-%{abi_ver}.pc


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 16 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.19.0-1
- Update to 0.19.0 (#2359256)

* Sat Feb 15 2025 Sam Day <me@samcday.com> - 0.18.2-4
- Add wlroots!4985 patch needed by phoc 0.45.0

* Mon Feb 10 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.18.2-3
- Rebuild for libdisplay-info 0.2.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2 (#2331871)

* Fri Sep 20 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1 (#2313753)

* Thu Aug 08 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.18.0-1
- Update to 0.18.0 (#2297921)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.4-1
- Update to 0.17.4 (#2294793)

* Fri Apr 26 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.3-1
- Update to 0.17.3

* Mon Mar 11 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.2-1
- Update to 0.17.2 (#2269046)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1 (#2255547)

* Tue Nov 21 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0 (#2250885)
- Use xcb-errors util library
- Apply patches from 0.17.x bugfix branch

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.16.2-2
- Apply upstream patch to remove hardcoded Vulkan validation layers

* Fri Feb 10 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.16.2-1
- Update to 0.16.2 (#2168992)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.16.1-1
- Update to 0.16.1

* Fri Dec 02 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0 (#2142159)
- Add patch for compatibility with older libdrm
- Sync examples.meson.build with upstream, include all available examples

* Mon Nov 14 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-5
- Backport upstream crash fix (#2142447)
- Convert license to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-3
- Add patches required for phoc 0.20

* Wed Jun 01 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-2
- Drop patches for wayland 1.19 compatibility

* Sat Feb 05 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-1
- Update to 0.15.1 (#2050408)

* Tue Jan 25 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.0-3
- Backport fix for permission popups in Firefox

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0 (#2033651)
- Update upstream URL to gitlab.freedesktop.org
- Backport some patches from 0.15.1 milestone

* Mon Dec 13 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.14.1-3
- Add patch for disappearing cursor issue (#2027431)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.14.1-1
- Update to wlroots 0.14.1

* Wed Jul 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.14.0-2
- Add patch for a few more issues with cursors, multi-GPUs and nouveau

* Wed Jun 23 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0
- Add upstream patch for cursor issues on scaled outputs

* Tue Jun 01 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.13.0-2
- Enable libseat session backend

* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0 (#1947218)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.12.0-1
- Updated to version 0.12.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.11.0-1
- Updated to version 0.11.0

* Sat May 09 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.10.1-2
- Add patch from upstream #2167 to fix #1829212

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 0.10.1-1
- Updated to version 0.10.1 (https://github.com/swaywm/wlroots/releases/tag/0.10.1)

* Mon Feb 10 2020 Jan Staněk <jstanek@redhat.com> - 0.10.0-6
- Propagate mesa-libEGL-devel workaround to -devel requirements

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 0.10.0-5
- RDP backend is no longer in wlroots 0.10.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 0.10.0-4
- Rebuild for updated FreeRDP.

* Tue Feb 04 2020 Jan Staněk <jstanek@redhat.com> - 0.10.0-3
- Disable -Werror compilation flag on s390x
  (https://github.com/swaywm/wlroots/issues/2018)

* Wed Jan 29 2020 Jan Staněk <jstanek@redhat.com> - 0.10.0-2
- Backport fix for compilation with GCC 10

* Tue Jan 28 2020 Joe Walker <grumpey0@gmail.com> - 0.10.0
- Updated to version 0.10.0 (https://github.com/swaywm/wlroots/releases/tag/0.10.0)

Mon Jan 20 2020 Jan Staněk <jstanek@redhat.com> - 0.9.1-1
- Upgrade to version 0.9.1 (https://github.com/swaywm/wlroots/releases/tag/0.9.1)

* Thu Sep 12 2019 Jan Staněk <jstanek@redhat.com> - 0.7.0-2
- Spec file cleanup

* Thu Aug 29 2019 Jeff Peeler <jpeeler@redhat.com> - 0.7.0-1
- Updated to version 0.7.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.6.0-1
- Updated to version 0.6.0
  (see https://github.com/swaywm/wlroots/releases/tag/0.6.0)
- Overhaul dependencies and shipped examples in -devel

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.5.0-2
- Rebuild with Meson fix for #1699099

* Thu Mar 14 2019 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.5.0-1
- Updated to version 0.5.0 (0.2, 0.3, 0.4, 0.4.1 releases effectively skipped)
- Avoid building some parts that are not shipped in binary form, anyway
- Minor spec cleanup (clarify the licensing comment, licensecheck's NTP ~ MIT,
  ldconfig_scriptlets no longer relevant, arch-specific tweak no longer needed)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-4
- Fix Firefox crash around text selection/clipboard
  (https://github.com/swaywm/wlroots/pull/1380)

* Tue Nov 27 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-3
- Make Firefox run smoother (https://github.com/swaywm/wlroots/pull/1384)

* Wed Nov 07 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-2
- Fix incorrect "pkgconfig" version

* Wed Oct 31 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-1
- Updated to historically first official release
- Turned off implicit enablement of all 'auto' build features under Meson,
  since xcb-errors is not available at this time
- Added BR: libpng
- Expanding spec comment on source files not covered with MIT license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.9.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.8.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.7.20180106git03faf17
- Updated snapshot

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.6.20180102git767df15
- Initial import (#1529352)

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.5.20180102git767df15
- Updated snapshot

* Sun Dec 31 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.4.20171229git80ed4d4
- Add licensing clarification
- Add BR: gcc

* Sat Dec 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.3.20171229git80ed4d4
- Updated snapshot

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.2.20171227giteeb7cd8
- Optimize spec-file

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.1.20171227giteeb7cd8
- Initial rpm release (#1529352)
