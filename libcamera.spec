Name:    libcamera
Version: 0.0.4
Release: 1%{?dist}
Summary: A library to support complex camera ISPs
# Library is LGPLv2.1+ and the cam tool is GPLv2
License: LGPLv2+ and GPLv2
URL:     http://libcamera.org/

# libcamera is not expected to be used in these architectures
ExcludeArch: s390x ppc64le

# Upstream is still under development and does not release tarballs,
# but they do tag releases (https://git.linuxtv.org/libcamera.git).
#
# For use the following to do generate a tarball from a git tag:
#
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{version} | xz > %%{name}-%%{version}.tar.xz
Source0: %{name}-%{version}.tar.xz
Source1: qcam.desktop
Source2: qcam.metainfo.xml

Patch0001:	0001-cam-fix-compilation-with-gcc-13.patch

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: openssl
BuildRequires: ninja-build
BuildRequires: python3-jinja2
BuildRequires: python3-ply
BuildRequires: python3-pyyaml
BuildRequires: python3-sphinx
BuildRequires: boost-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gnutls-devel
BuildRequires: libatomic
BuildRequires: libevent-devel
BuildRequires: libtiff-devel
BuildRequires: libyaml-devel
BuildRequires: lttng-ust-devel
BuildRequires: systemd-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)

%description
libcamera is a library that deals with heavy hardware image processing
operations of complex camera devices that are shared between the linux
host all while allowing offload of certain aspects to the control of
complex camera hardware such as ISPs.

Hardware support includes USB UVC cameras, libv4l cameras as well as more
complex ISPs (Image Signal Processor).

%package     devel
Summary:     Development package for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package     doc
Summary:     Documentation for %{name}
BuildArch:   noarch

%description doc
HTML based documentation for %{name} including getting started and API.

%package     ipa
Summary:     ISP Image Processing Algorithm Plugins for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description ipa
Image Processing Algorithms plugins for interfacing with device
ISPs for %{name}

%package     tools
Summary:     Tools for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools for %{name}

%package     qcam
Summary:     Graphical QCam application for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description qcam
Graphical QCam application for %{name}

%package     gstreamer
Summary:     GSTreamer plugin for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description gstreamer
GSTreamer plugins for %{name}

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# cam/qcam crash with LTO
%global _lto_cflags %{nil}
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations"

%ifarch ppc64le
# 64-bit POWER LE does not use the IEEE long double ABI but
# instead a custom one by default. This leads to libcamera
# failing to build, use IEEE long double ABI to prevent it.
#
# https://bugzilla.redhat.com/show_bug.cgi?id=1538817
export CFLAGS="${CFLAGS} -mabi=ieeelongdouble"
export CXXFLAGS="${CXXFLAGS} -mabi=ieeelongdouble"
%endif

%meson
%meson_build

%install
%meson_install

# Install Desktop Entry file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE1

# Install AppStream metainfo file
mkdir -p %{buildroot}/%{_metainfodir}/
cp -a %SOURCE2 %{buildroot}/%{_metainfodir}/

# Remove the Sphinx build leftovers
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-*/html/.buildinfo
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-*/html/.doctrees

%files
%license COPYING.rst LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libcamera*.so.0.0.4

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcamera*.so
%{_libdir}/pkgconfig/libcamera-base.pc
%{_libdir}/pkgconfig/libcamera.pc

%files doc
%doc %{_docdir}/%{name}-*/

%files ipa
%{_datadir}/libcamera/
%{_libdir}/libcamera/
%{_libexecdir}/libcamera/

%files gstreamer
%{_libdir}/gstreamer-1.0/libgstlibcamera.so

%files qcam
%{_bindir}/qcam
%{_datadir}/applications/qcam.desktop
%{_metainfodir}/qcam.metainfo.xml

%files tools
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/cam
%{_bindir}/lc-compliance

%changelog
* Wed Feb 01 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.0.4-1
- Update to version 0.0.4
- Add ExcludeArch tag to avoid building libcamera for s390x and ppc64le.

* Tue Jan 24 2023 Wim Taymans <wtaymans@redhat.com> - 0.0.3-3
- Rebuild for gtest .so bump rhbz#2161870
- Add patch for gcc13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.3-1
- Update to version 0.0.3

* Thu Dec 01 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.2-1
- Update to version 0.0.2

* Wed Aug 31 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220831.68683d3-1
- Update to snapshot 68683d3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0~git.20220126.bb84fc6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.0~git.20220126.bb84fc6-4
- Rebuild for new gtest

* Thu Jun 23 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220623.bb84fc6-1
- Update to snapshot bb84fc6

* Wed Feb 02 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220128.7ea52d2-3
- Re-enable lc-compliance build

* Wed Feb 02 2022 Eric Curtin <ecurtin@redhat.com> - 0.0.0~git.20220128.7ea52d2-2
- Build with lc-compliance disabled

* Fri Jan 28 2022 Eric Curtin <ecurtin@redhat.com> - 0.0.0~git.20220128.7ea52d2-1
- Update to snapshot 7ea52d2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0~git.20210928.e00149f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.0~git.20210928.e00149f-2
- rebuild against new liblttng-ust

* Tue Sep 28 2021 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20210928.e00149f-1
- Update to snapshot e00149f

* Wed Sep 08 2021 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20210908.39c2d5d-1
- Update to snapshot 39c2d5d
- Add snapshot date information to follow the Fedora packaging guidelines
- Use correct license short names to follow the Fedora licensing guidelines
- Remove %%ldconfig_scriptlets that are not needed
- Add a downstream SONAME versioning
- Use %%global instead of %%define
- Fix ppc64le build error caused by not using the IEEE long double ABI
- Remove the Sphinx build leftovers
- Add only the needed license files instead of the whole LICENSE dir
- Ship only the .so.0.n and the .so in the devel sub-package
- Add Desktop and AppStream metainfo files
- Rename docs sub-package to libcamera-doc to silence a package review warning

* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.0-0.1.76a5861
- Update to snapshot 76a5861
- Enable gstreamer plugin and QCam tool
- More granular packaging

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.0-0.1.36d6229
- Initial package
