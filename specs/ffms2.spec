%global git 0
%global gittag 5.0-RC3

Name:           ffms2
Version:        5.0
Release:        5%{?dist}
# src/index/vsutf16.h is LGPL-2.1-or-later
# the rest is MIT-licensed
License:        MIT AND LGPL-2.1-or-later
Summary:        Video source library for easy frame accurate access
URL:            https://github.com/FFMS/ffms2
%if 0%{?git}
Source0:        %{url}/archive/%{gittag}/ffms2-%{gittag}.tar.gz
# run ffms2-samples.sh to fetch samples from upstream
%else
Source0:        %{url}/archive/%{version}/ffms2-%{version}.tar.gz
%endif
Source1:        ffms2-samples.tar.gz
Source2:        ffms2-samples.sh
Patch:          ffms2-use-latest-stdc.patch
Patch:          ffms2-use-system-vapoursynth.patch
Patch:          ffms2-use-system-gtest.patch
Patch:          ffms2-skip-unsupported-codec-tests.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  gtest-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  zlib-devel

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around FFmpeg. It gives you an easy, convenient way to say "open and
decompress this media file for me, I don't care how you do it" and get frame-
and sample-accurate access (usually), without having to bother with the
sometimes less than straightforward and less than perfectly documented FFmpeg
API.

%package devel
Summary:        Development package for ffms2
Requires:       ffms2%{?_isa} = %{version}-%{release}

%description devel
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper 
library around FFmpeg.

This package contains the headers and development files.

%prep
%if 0%{?git}
%autosetup -p1 -n ffms2-%{gittag} -a 1
%else
%autosetup -p1 -a 1
%endif
rm -rv src/vapoursynth/V*.h
mkdir -p src/config
autoreconf -vfi

%build
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
rm -v %{buildroot}%{_libdir}/libffms2.la
rm -rv %{buildroot}%{_docdir}

%check
# HDR test uses unsupported H.265 codec samples, so run only the other two tests
CPPFLAGS=-I/usr/include/ffmpeg make -C test SAMPLES_DIR=$(pwd)/test/samples TESTS="indexer display_matrix" run

%files
%license COPYING
%doc README.md
%{_bindir}/ffmsindex
%{_libdir}/libffms2.so.5{,.*}

%files devel
%doc doc/*
%{_libdir}/libffms2.so
%{_includedir}/ffms{,compat}.h
%{_libdir}/pkgconfig/ffms2.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Dominik Mierzejewski <dominik@greysector.net> - 5.0-4
- Rebuilt for FFmpeg 7

* Fri Sep 20 2024 Dominik Mierzejewski <dominik@greysector.net> - 5.0-3
- fix unused-direct-shlib-dependency rpmlint error

* Fri Sep 06 2024 Dominik Mierzejewski <dominik@greysector.net> - 5.0-2
- correct license tag
- fix unused-direct-shlib-dependency rpmlint error
- fix tests
- use latest C++ standard

* Sun Jun 09 2024 Dominik Mierzejewski <dominik@greysector.net> - 5.0-1
- update to 5.0

* Wed Apr 10 2024 Dominik Mierzejewski <dominik@greysector.net> - 5.0~rc3-1
- update to 5.0-RC3
- drop obsolete patches
- unbundle vapoursynth
- run tests (using system gtest)

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 2.40-9
- Rebuild for new ffmpeg

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 2.40-6
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 24 2021 Leigh Scott <leigh123linux@gmail.com> - 2.40-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 2.40-2
- Rebuilt for new ffmpeg snapshot

* Sun Nov  1 2020 Leigh Scott <leigh123linux@gmail.com> - 2.40-1
- Update to 2.40

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Leigh Scott <leigh123linux@gmail.com> - 2.23-16
- Remove libavresample dependency (rfbz#5349)

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.23-15
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 2.23-13
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.23-11
- Rebuild for ffmpeg-3.4.5 on el7
- Use ldconfig_scriptlets macros

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.23-9
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.23-7
- Rebuilt for ffmpeg-3.5 git

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.23-6
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.23-3
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.23-1
- Update to 2.23

* Tue Aug 30 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.22-3
- Couple of trivial fixes

* Tue Jun 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 2.2-2
- rebuilt against new ffmpeg

* Wed Nov 04 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.22-1
- Update to 2.22

* Sun Jun 28 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.21-1
- Update to 2.21

* Mon Jan  5 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.20-1
- Update to 2.20

* Fri Mar 28 2014 Ivan Epifanov <isage.dna@gmail.com> - 2.19-1
- Initial spec for Fedora
