# -*-Mode: rpm-spec -*-

Name:     neatvnc
Version:  0.7.0
Release:  1%{?dist}
Summary:  a liberally licensed VNC server library
# main source is ISC
# include/sys/queue.h is BSD
# bundled miniz is MIT and Unlicense
License:  ISC and MIT and Unlicense and BSD

URL:      https://github.com/any1/neatvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(aml)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(zlib)
BuildRequires: turbojpeg-devel

%description

This is a liberally licensed VNC server library that's intended to be
fast and neat. Note: This is a beta release, so the interface is not
yet stable.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/lib%{name}.so.0*

%doc README.md

%license COPYING

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*

%changelog
* Fri Oct 06 2023 Bob Hepple <bob.hepple@gmail.com> - 0.7.0-1
- new version

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.6.0-2
- Rebuild for ffmpeg 6.0

* Tue Jan 31 2023 Bob Hepple <bob.hepple@gmail.com> - 0.6.0-1
- new version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 12 2022 Bob Hepple <bob.hepple@gmail.com> - 0.5.4-1
- new version

* Mon Aug 29 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.5.1-3
- Rebuild for ffmpeg 5.1 (#2121070)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Bob Hepple <bob.hepple@gmail.com> - 0.5.1-1
- new version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Bob Hepple <bob.hepple@gmail.com> - 0.4.0-1
- new version

* Mon Sep 28 2020 Bob Hepple <bob.hepple@gmail.com> - 0.3.2-1
- new version

* Tue Sep 22 2020 Bob Hepple <bob.hepple@gmail.com> - 0.3.0-1
- new version

* Tue Aug 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-3
- fixed spelling of Unlicense

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-2
- fixed per review RHBZ#1824016

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-1
- Initial version of the package
