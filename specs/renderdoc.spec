%global vswig   modified-7
Name:           renderdoc
Version:        1.35
Release:        2%{?dist}
Summary:        A stand-alone graphics debugging tool

License:        MIT
URL:            https://renderdoc.org
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-%{vswig}/swig-%{vswig}.tar.gz
Patch0:         renderdoc-swig-pcre2-1.patch
Patch1:         renderdoc-swig-pcre2-2.patch

# renderdoc is officially only supported on x86_64.
# however, it also builds on aarch64
ExclusiveArch: x86_64 aarch64

# for the local swig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre2-devel

# for the renderdoc itself
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  bison
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(xcb-keysyms)
Requires:       hicolor-icon-theme

%description
A free MIT licensed stand-alone graphics debugger that allows quick
and easy single-frame capture and detailed introspection of any
application using Vulkan, OpenGL.

%package devel
Summary: Development files for renderdoc
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains headers and other files that are
required to develop applications that want to integrate with
renderdoc.

%prep
%setup -q -b 1
%patch -p1 -d %{_builddir}/swig-renderdoc-%{vswig} 0
%patch -p1 -d %{_builddir}/swig-renderdoc-%{vswig} 1

%build
# renderdoc does not allow in-source builds. out-of-source builds
# are the default starting with F33, but for anything below the
# __cmake_in_source_build macro needs to be undefined.
%undefine __cmake_in_source_build

# compiling renderdoc with lto currently leads to crashes
# https://github.com/baldurk/renderdoc/issues/2373
%define _lto_cflags %{nil}

%cmake -DQMAKE_QT5_COMMAND=qmake-qt5 \
       -DRENDERDOC_SWIG_PACKAGE=%{_builddir}/swig-renderdoc-%{vswig} \
       -DENABLE_GL=ON \
       -DENABLE_VULKAN=ON \
       -DENABLE_WAYLAND=ON \
       -DENABLE_RENDERDOCCMD=ON \
       -DENABLE_QRENDERDOC=ON \
       -DBUILD_VERSION_STABLE=ON \
       -DBUILD_VERSION_DIST_NAME="fedora" \
       -DBUILD_DISTRIBUTION_VERSION="%{version}-%{release}" \
       -DBUILD_VERSION_DIST_CONTACT="https://bugzilla.redhat.com" \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DLIB_SUBFOLDER=renderdoc \
       -DVULKAN_LAYER_FOLDER=/usr/share/vulkan/implicit_layer.d \
       -DCMAKE_BUILD_TYPE=Release \
       %{nil}

%cmake_build

%install
%cmake_install
rm %{buildroot}/%{_datadir}/menu/renderdoc

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE.md
%{_bindir}/qrenderdoc
%{_bindir}/renderdoccmd
%{_datadir}/applications/%{name}.desktop
%dir %{_libdir}/renderdoc
%{_libdir}/renderdoc/lib%{name}.so
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/icons/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%{_datadir}/mime/packages/renderdoc-capture.xml
%{_datadir}/pixmaps/%{name}-icon-*.xpm
%doc %{_docdir}/%{name}/
%{_datadir}/vulkan/implicit_layer.d/%{name}_capture.json

%files devel
%{_includedir}/%{name}_app.h


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.35-1
- Update to 1.35 (#2315525)

* Mon Aug 05 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.34-1
- Update to 1.34 (#2302961)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.33-2
- Rebuilt for Python 3.13

* Sun Jun 02 2024 kb1000 <fedora@kb1000.de> - 1.33-1
- Update to 1.33 (#2284206)
- Remove Python 3.13 compatibility patch that was upstreamed

* Sat Apr 06 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.32-1
- Update to 1.32 (#2273742)

* Sun Feb 18 2024 kb1000 <fedora@kb1000.de> - 1.31-2
- Fix compatibility with Python 3.13

* Sun Feb 11 2024 kb1000 <fedora@kb1000.de> - 1.31-1
- Update to version 1.31
  Resolves: rhbz#2045957

* Mon Jan 22 2024 kb1000 <fedora@kb1000.de> - 1.30-3
- Build for aarch64

* Thu Dec 21 2023 kb1000 <fedora@kb1000.de> - 1.30-2
- Move the custom SWIG to PCRE2

* Wed Dec 13 2023 kb1000 <fedora@kb1000.de> - 1.30-1~kb1000
- Update to version 1.30

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.17-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.17-1
- Update to version 1.17
  Resolves: rhbz#2027030

* Sat Nov 06 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.16-1
- Update to version 1.16
  Resolves: #1902340
- Disable LTO to fix crashes
  Resolves: #1955122

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Christian Kellner <christian@kellner.me> - 1.10-1
- New upstream release (1.10)
- Only build on x86_64, which is the only officially supported archiecture.
  https://github.com/baldurk/renderdoc/issues/1991#issuecomment-663840783
- Drop cmake patch (no needed anymore)

* Fri Aug  7 2020 Christian Kellner <christian@kellner.me> - 1.8-4
- Use cmake macros for out-of-source build
  Resolves: rhbz#1865372

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Christian Kellner <christian@kellner.me> - 1.8-1
- New upstream release (1.8)
- Drop gcc-libsdc-10.patch, included in the upstream release.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6-2
- Rebuilt for Python 3.9

* Wed Feb  5 2020 Christian Kellner <ckellner@redhat.com> - 1.6-1
- New upstream release (1.6)
  Resolves: rhbz#1792068
- Include patch to fix compilation on gcc10
  https://github.com/baldurk/renderdoc/commit/29403836c60fd8d61325e9972d3a56d8b0ff0178

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Christian Kellner <ckellner@redhat.com> - 1.5-1
- renderdoc 1.5 (new upstream release)
  Resolves: rhbz#1760976
- Drop swig patch (got upstreamed)
- Adjust CMake patch (drop the swig part)
- Move capture layer config from /etc to /usr/share
  Resolves: rhbz#1762274

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Christian Kellner <ckellner@redhat.com> - 1.4-2
- Patches to add upport for python 3.8
  Resolves: rhbz#1705450

* Wed May 15 2019 Christian Kellner <ckellner@redhat.com> - 1.4-1
- renderdoc 1.4 (new upstream release)
  Resolves: rhbz#1703666
- Fixes FTBFS by using a new upstream release that supports python 3.8
  Resolves: rhbz#1705450
- Remove README.md as we ship the user-directed README of the docs dir
- Remove CODE_OF_CONDUCT.md as this is developer oriented

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  1 2018 Christian Kellner <ckellner@redhat.com> - 1.1-1
- renderdoc 1.1 (new upstream stable)
- Drop swig-i386.patch (now upstream)
- Change BUILD_VERSION_DIST_CONTACT to point to RH bugzilla
- Resolves: #1608619

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Christian Kellner <ckellner@redhat.com> - 1.0-1
- renderdoc 1.0 (new upstream stable)
- Update swig modified source to version 5
- Drop Patch0 (lib subfolder), it is upstream now
- Add patch to build on i386

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.91-7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.91-5
- Remove obsolete scriptlets

* Wed Sep 27 2017 Christian Kellner <ckellner@redhat.com> - 0.91-4
- Remove ldconfig calls

* Wed Sep 27 2017 Christian Kellner <ckellner@redhat.com> - 0.91-3
- Split out devel package
- Address review comments

* Mon Sep 18 2017 Christian Kellner <ckellner@redhat.com> - 0.91-2
- Restrict archs to x86

* Mon Sep 18 2017 Christian Kellner <ckellner@redhat.com> - 0.91-1
- New upstream version
- Dropped patches, replaced by cmake options.

* Mon Jun 19 2017 Christian Kellner <ckellner@redhat.com>
- Initial packaging
