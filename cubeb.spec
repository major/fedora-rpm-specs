%global commit 28c8aa4a9c3568187e16e3a47a0d16371d1c5d33
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20220915
%global fgittag %{gitdate}.git%{shortcommit}

Name:           cubeb
Version:        0.2
Release:        10%{?fgittag:.%{fgittag}}%{?dist}
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
License:        ISC and BSD and MIT
URL:            https://github.com/mozilla/cubeb
Source0:        https://github.com/mozilla/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

#Taken from the mozilla blog:
#https://blog.mozilla.org/webrtc/firefoxs-audio-backend/
#Which is licensed CC-BY-SA 3.0
%description
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
%cmake . -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=OFF -DUSE_SANITIZERS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libcubeb.a
%{_bindir}/%{name}-test
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_docdir}/%{name}

%changelog
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
