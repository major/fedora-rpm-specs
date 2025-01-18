%global commit 48689ae7a73caeb747953f9ed664dc71d2f918d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230517
%global fgittag %{gitdate}.git%{shortcommit}

Name:           cubeb
Version:        0.2
Release:        17%{?fgittag:.%{fgittag}}%{?dist}
Summary:        A cross platform audio library

#cubeb is ISC, sanitizers-cmake is MIT
#excluding the following files which are BSD 3-clause:
#/src/speex/arch.h
#/src/speex/fixed_generic.h
#/src/speex/resample.c
#/src/speex/resample_neon.h
#/src/speex/resample_sse.h
#/src/speex/speex_resampler.h
#/src/speex/stack_alloc.h
# Automatically converted from old format: ISC and BSD and MIT - review is highly recommended.
License:        ISC AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/mozilla/cubeb
Source0:        https://github.com/mozilla/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel

#Taken from the mozilla blog:
#https://blog.mozilla.org/webrtc/firefoxs-audio-backend/
#Which is licensed CC-BY-SA 3.0
%description
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package devel
Summary:        A cross platform audio library
Provides:       %{name}-static = %{version}-%{release}

%description devel
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%prep
%autosetup -p1 -n %{name}-%{commit}
#Clean up Android files
rm -rf src/android

#Clean up the README.md, we don't need building information:
sed -i -e "/^\[!/d" -e "/INSTALL.md/d" README.md

%build
%cmake . -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=ON -DUSE_SANITIZERS=OFF
%cmake_build

%install
%cmake_install

%check
#Run only the tests known to work in mock/chroot:
%ctest -R "(record|resampler|duplex|triple_buffer|ring_array|utils|ring_buffer|device_changed_callback)"

%files devel
%doc README.md
%license LICENSE
%{_libdir}/libcubeb.a
%{_bindir}/%{name}-test
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_docdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17.20230517.git48689ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2-16.20230517.git48689ae
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15.20230517.git48689ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14.20230517.git48689ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13.20230517.git48689ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.20230517.git48689ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.2-11.20230517.git48689ae
- Update to newer git
- fix up packaging a bit
- enable some tests

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10.20220915.git28c8aa4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.2-9.20220915.git28c8aa4
- Build as static

* Thu Nov 10 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.2-8.20220915.git28c8aa4
- Update to latest git
- Drop sanitizer (not necessary)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7.20200409.git9caa5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6.20200409.git9caa5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5.20200409.git9caa5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4.20200409.git9caa5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3.20200409.git9caa5b1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2.20200409.git9caa5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Jeremy Newton <alexjnewt AT hotmail DOT com>
- Add breakdown for a few BSD-licensed files
- Clean up android files

* Mon Apr 20 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.2-1.20200409.git9caa5b1
- Initial Package
