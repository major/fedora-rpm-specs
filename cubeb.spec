%global commit 9caa5b113a2a4faef8bd31894fc2d762b884a5cf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20200409
%global fgittag %{gitdate}.git%{shortcommit}

%global sanitizerscommit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
%global sanitizersshortcommit %(c=%{sanitizerscommit}; echo ${c:0:7})

Name:           cubeb
Version:        0.2
Release:        7%{?fgittag:.%{fgittag}}%{?dist}
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
URL:            https://github.com/kinetiknz/cubeb
Source0:        https://github.com/kinetiknz/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
#github doesn't support downloading gitsubmodules:
Source1:        https://github.com/arsenm/sanitizers-cmake/archive/%{sanitizerscommit}/sanitizers-cmake-%{sanitizersshortcommit}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
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
Summary:        Development files for cubeb
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for cubeb

%prep
%autosetup -p1 -n %{name}-%{commit} -a 1
#Clean up Android files
rm -rf src/android

#Link the sanitizer cmake files into the expected location
ln -s ../../sanitizers-cmake-%{sanitizerscommit}/cmake cmake/sanitizers-cmake

#Clean up the README.md, we don't need building information:
sed -i -e "/^\[!/d" -e "/INSTALL.md/d" README.md

#Upstream aims to distribute statically, so it doesn't set a SONAME
#We can define it ourselves to allow dynamic linking:
echo "set_target_properties(%{name} PROPERTIES SOVERSION 0)" >> CMakeLists.txt

%build
%cmake . -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libcubeb.so.*

%files devel
%{_libdir}/libcubeb.so
%{_bindir}/%{name}-test
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%changelog
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
