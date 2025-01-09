Name:           gstreamer1-vaapi
Version:        1.24.11
Release:        1%{?dist}
Summary:        GStreamer plugins to use VA API video acceleration

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.40
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gstreamer1-plugins-bad-free-devel >= %{version}
BuildRequires:  libva-devel >= 1.1.0
BuildRequires:  libdrm-devel
BuildRequires:  libudev-devel
BuildRequires:  libGL-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  libvpx-devel
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  gtk3-devel

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  wayland-devel >= 1.11.0
BuildRequires:  wayland-protocols-devel >= 1.15
BuildRequires:  pkgconfig(wayland-client)  >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor)  >= 1.11.0
BuildRequires:  pkgconfig(wayland-egl)     >= 1.11.0
BuildRequires:  pkgconfig(wayland-server)  >= 1.11.0
%endif

%ifnarch s390x
Recommends:     mesa-va-drivers%{?_isa}
%endif

# We can't provide encoders or decoders unless we know what VA-API drivers
# are on the system. Just filter them out, so they're not suggested by
# PackageKit et al.
%global __provides_exclude gstreamer1\\(decoder|gstreamer1\\(encoder

%description
A collection of GStreamer plugins to let you make use of VA API video
acceleration from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package devel
Summary:        GStreamer VA API Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.


%package        devel-docs
Summary:        Developer documentation for GStreamer VA API video acceleration plugins
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

Provides:       gstreamer1-vaapi-devel = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi-devel < 0.6.1-3

%description	devel-docs
The %{name}-devel-docs package contains developer documentation
for the GStreamer VA API video acceleration plugins

%prep
%autosetup -p1 -n gstreamer-vaapi-%{version}

%build

%meson \
	-D doc=disabled

%meson_build

%install
%meson_install

%check
%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/*.so

%files devel

%files devel-docs
%doc AUTHORS NEWS README
%if 0
%doc %{_datadir}/gtk-doc
%endif

%changelog
* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.24.11-1
- 1.24.11

* Wed Dec 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.10-1
- 1.24.10

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.9-1
- 1.24.9

* Thu Sep 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.8-1
- 1.24.8

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.24.7-2
- convert license to SPDX

* Wed Aug 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.7-1
- 1.24.7

* Mon Jul 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.6-1
- 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.5-1
- 1.24.5

* Wed May 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.4-1
- 1.24.4

* Tue Apr 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.3-1
- 1.24.3

* Tue Mar 05 2024 Wim Taymans <wtaymans@redhat.com> - 1.24.0-1
- Update to 1.24.0

* Thu Jan 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.22.9-1
- 1.22.9

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.8-1
- 1.22.8

* Tue Nov 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.7-1
- 1.22.7

* Tue Sep 26 2023 Nicolas Chauvet <nchauvet@linagora.com> - 1.22.6-1
- Update to 1.22.6

* Fri Jul 21 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.5-1
- Update to 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.3-1
- Update to 1.22.3

* Thu Apr 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.2-1
- Update to 1.22.2

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 1.22.1-2
- Rebuilt for libva update

* Mon Mar 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.1-1
- Update to 1.22.1

* Tue Jan 24 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Fri Jan 20 2023 Wim Taymans <wtaymans@redhat.com> - 1.21.90-1
- Update to 1.21.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Wim Taymans <wtaymans@redhat.com> - 1.20.5-1
- Update to 1.20.5

* Fri Dec 02 2022 Nicolas Chauvet <kwizart@gmail.com> - 1.20.4-2
- Fix mesa-va-drivers no available on s390 - rhbz#2150324

* Thu Oct 13 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.4-1
- Update to 1.20.4

* Mon Oct 10 2022 Ray Strode <rstrode@redhat.com> - 1.20.3-3
- Add requires on mesa-va-drivers
  Related: #2123998

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.3-1
- Update to 1.20.3

* Fri Feb 4 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.0-1
- Update to 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.3-1
- Update to 1.19.3

* Thu Sep 23 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.2-1
- Update to 1.19.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.1-1
- Update to 1.19.1

* Tue Mar 16 2021 Wim Taymans <wtaymans@redhat.com> - 1.18.4-1
- Update to 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.2-1
- Update to 1.18.2

* Fri Oct 30 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.1-1
- Update to 1.18.1

* Tue Sep 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Fri Aug 21 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.90-1
- Update to 1.17.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 6 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-1
- Update to 1.17.2

* Mon Jun 22 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.1-1
- Update to 1.17.1

* Thu Feb 6 2020 Wim Taymans <wtaymans@redhat.com> - 1.16.2-1
- Update to 1.16.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.16.1-3
- Drop applied patch
- Switch to autosetup

* Fri Oct 4 2019 Simon Farnsworth <simon@farnz.org.uk> - 1.16.1-2
- Disable Mesa VAAPI drivers (https://bugzilla.redhat.com/show_bug.cgi?id=1749861)

* Tue Sep 24 2019 Wim Taymans <wtaymans@redhat.com> - 1.16.1-1
- Update to 1.16.1

* Mon Jul 29 2019 Phil Wyett <philwyett@kathenas.org> - 1.16.0-3
- Add python3-devel BuildRequires.
- Fix day of week in bad changelog entry.
- Update all build dependency requirements.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Wim Taymans <wtaymans@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Tue Apr 16 2019 Simon Farnsworth <simon@farnz.org.uk> - 1.15.2-2
- Fix Wayland support

* Fri Mar 01 2019 Wim Taymans <wtaymans@redhat.com> - 1.15.2-1
- Update to 1.15.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Wim Taymans <wtaymans@redhat.com> - 1.15.1-1
- Update to 1.15.1

* Wed Oct 03 2018 Taymans <wtaymans@redhat.com> - 1.14.4-1
- Update to 1.14.4

* Tue Sep 18 2018 Taymans <wtaymans@redhat.com> - 1.14.3-1
- Update to 1.14.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.1-2
- .spec cosmetics, use %%make_build, %%ldconfig_scriptlets, %%license, drop Group:
- --disable-silent-rules

* Mon May 21 2018 Taymans <wtaymans@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Tue Mar 20 2018 Taymans <wtaymans@redhat.com> - 1.14.0-1
- Update to 1.14.0

* Wed Mar 14 2018 Taymans <wtaymans@redhat.com> - 1.13.91-1
- Update to 1.13.91

* Mon Mar 05 2018 Taymans <wtaymans@redhat.com> - 1.13.90-1
- Update to 1.13.90

* Thu Feb 22 2018 Taymans <wtaymans@redhat.com> - 1.13.1-1
- Update to 1.13.1
- Disable warnings

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.4-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.12.4-2
- Rebuilt for libva-2.0.0

* Mon Dec 11 2017 Taymans <wtaymans@redhat.com> - 1.12.4-1
- Update to 1.12.4

* Tue Sep 19 2017 Taymans <wtaymans@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Taymans <wtaymans@redhat.com> - 1.12.2-1
- Update to 1.12.2

* Tue Jun 20 2017 Taymans <wtaymans@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Wed May 10 2017 Taymans <wtaymans@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Fri Apr 28 2017 Taymans <wtaymans@redhat.com> - 1.11.91-1
- Update to 1.11.91

* Tue Apr 11 2017 Taymans <wtaymans@redhat.com> - 1.11.90-1
- Update to 1.11.90

* Fri Feb 24 2017 Taymans <wtaymans@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Taymans <wtaymans@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Mon Dec 05 2016 Taymans <wtaymans@redhat.com> - 1.10.2-1
- Update to 1.10.2

* Mon Nov 28 2016 Taymans <wtaymans@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Thu Nov 03 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Sat Oct 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.90-1
- Update to 1.9.90

* Thu Sep 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Thu Jul 07 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Thu Jun 09 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Mon Apr 25 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Fri Apr 08 2016 Egor Zaharov <nexfwall@gmail.com> - 1.8.0-1
- Updated to 1.8.0
- Update URL to follow project, because they moved to freedesktop

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 18 2015 Francesco Frassinelli <fraph24@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr  7 2015 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 0.5.10-3
- Update URL to follow project after gitorious shutdown

* Sun Feb 15 2015 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 0.5.10-2
- Fix FTBFS on s390x due to header file not matching implementation

* Tue Feb  3 2015 Simon Farnsworth <simon@farnz.org.uk> - 0.5.10-1
- Update to 0.5.10 release
- Filter out encoder and decoder Provides

* Tue Nov 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.5.9-3
- Rebuilt for vaapi 0.36

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  1 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 0.5.9-1
- Update to 0.5.9 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  9 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 0.5.8-4
- Provide Wayland support now that libva includes it

* Fri Feb  7 2014 Simon Farnsworth <simon@farnz.org.uk> - 0.5.8-3
- Fix typo in spec file - Patch1 and %%patch0 don't go together

* Fri Feb  7 2014 Simon Farnsworth <simon@farnz.org.uk> - 0.5.8-2
- Fix vaapipostproc crash in live pipelines

* Wed Feb  5 2014 Simon Farnsworth <simon@farnz.org.uk> - 0.5.8-1
- initial release
