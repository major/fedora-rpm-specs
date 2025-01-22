%global commit0 509d3b21a1084b4f492b50cced8835f4cd591c4a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20211013

Name:           libva-vdpau-driver
Version:        0.7.4
Release:        208.%{date0}%{?dist}
Summary:        HW video decode support for VDPAU platforms
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/xuanruiqi/vdpau-va-driver-vp9
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: libtool
BuildRequires:  gcc
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  mesa-libGL-devel
BuildRequires: make

Requires:       mesa-dri-filesystem

%description
VDPAU Backend for Video Acceleration (VA) API.

%prep
%setup -q -n vdpau-va-driver-vp9-%{commit0}


%build
autoreconf -vif
%configure \
  --disable-silent-rules \
  --enable-glx

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete


%files
%doc AUTHORS NEWS README.md
%license COPYING LICENSE
%{_libdir}/dri/*.so
%exclude %{_libdir}/dri/nvidia_drv_video.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-208.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.4-207.20211013
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-206.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-205.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-204.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-203.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-202.20211013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-201.20211013
- Swich upstream
- Exclude nvidia_drv_video to prevent conflicts

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-112
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-111
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-106
- Fix FTBFS - rhbz#1736054
- Bump to replace _copr_hellbangerkarna (uneeded anymore).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-23
- Add patch needed for vaapi enabled chromium - Akarshan Biswas
- spec file clean-up

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-20
- Rebuilt for libva-2.0.0

* Tue Sep 19 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-19
- Add patch for https://bugs.freedesktop.org/58836

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-16
- Rebuild for vaapi 0.40

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-13
- Revert symlinks - should be handled by mesa rhbz#1271842

* Thu Sep 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-12
- Add symlinks for radeonsi,r600,nouveau - rhbz#1264499

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-10
- Fix build with newer libva

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-7
- Drop conditional source inclusion
- Adjust patch for RHEL >= 7

* Wed Jul 31 2013 Simone Caronni <negativo17@gmail.com> - 0.7.4-6
- Drop H.264 specific VA buffer types only on Fedora 20+.

* Wed Jul 31 2013 Simone Caronni <negativo17@gmail.com> - 0.7.4-5
- Add patch to drop H.264 specific VA buffer types.
- Clean up spec file a bit.

* Thu Jun 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-4
- Rebuilt for vaapi 0.34

* Mon Feb 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-3
- Add --disable-silent-rules
- Clean-up spec

* Fri Jan 11 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-2
- Fix build with recent mesa

* Sun Oct 07 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Mon Jan 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-2
- Rename to libva-vdpau-driver

* Wed Mar 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Sun Jan 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.2.pre4
- Update to 0.7.3 pre4

* Wed Dec 15 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.1.pre2
- Update to 0.7.3.pre2
- Switch to vdpau-video-freeworld

* Mon Mar 15 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.5-1
- new release

* Thu Jan 21 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.2-1
- new release

* Thu Jan 14 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.1-1
- new release

* Thu Dec 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.6.0-1
- new release

* Tue Nov 17 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.2-1
- new release

* Wed Oct 7 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.0-1
- new release

* Thu Sep 10 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.1-1
- new release

* Thu Sep 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.0-1
- initial package
