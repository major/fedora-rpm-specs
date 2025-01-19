%global commit abeb3e9156b553d2e8f5ebbc8b3df833f531ce0f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20181215

Name:           lv2-fabla
Version:        1.3.2
Release:        0.13.%{prerelease}git%{shortcommit}%{?dist}
Summary:        An LV2 drum sequencer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://openavproductions.com/fabla/
Source0:        https://github.com/harryhaaren/openAV-Fabla/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-lv2.patch

BuildRequires:  faust
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(ntk)
BuildRequires:  pkgconfig(sndfile)
# This package uses cairo directly; cairo is a public dependency of ntk, so the
# following line is not strictly required. It serves to document the direct
# dependency.
BuildRequires:  pkgconfig(cairo)
# Contrary to the README, which says cairomm-1.0 is required, only the cairo C
# api is used, and only pkgconfig(cairo)/cairo-devel is required to build this
# package.
BuildRequires:  cmake
Requires:       lv2

%description
%{name} is a drum sampler plugin instrument. It is ideal for loading up your
favorite sampled sounds and bashing away on a MIDI controller. Or if it’s 
crafty beat programming your after that’s cool too! The ADSR envelope allows
the shaping of hi-hats and kicks while the compressor beefs up the sound for 
those thumping kicks!
Additional presets can be found at:
   https://github.com/harryhaaren/openAV-presets

%prep
%autosetup -p1 -n openAV-Fabla-%{commit}
sed -i -e  's|lib/|%{_lib}/|g'  -e 's|\-Wall|%{optflags}|g' \
  -e 's|-Wl,-z,nodelete -Wl,--no-undefined|%{__global_ldflags}|g' CMakeLists.txt
%ifnarch %{ix86} x86_64
sed -i -e 's|-msse2 -mfpmath=sse||g' CMakeLists.txt
%endif

%build
%cmake .
%cmake_build

%install
mkdir -p %{buildroot}/%{_libdir}/lv2
%cmake_install

%files
%doc README.md CHANGELOG
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.13.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.2-0.12.20181215gitabeb3e9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.11.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.10.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.9.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.8.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.7.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.6.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.5.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-0.4.20181215gitabeb3e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.2-0.3.20181215gitabeb3e9
- Add a direct dependency on pkgconfig(cairo) for documentation purposes
- Add a comment about the non-dependency on pkgconfig(caromm-1.0)

* Fri Feb 12 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.2-0.2.20181215gitabeb3e9
- Switch to pkgconfig() BRs, removing -devel BRs that are not required directly

* Wed Jan 27 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.2-0.1.20181215gitabeb3e9
- Update to 1.3.2
- Fix FTBFS with latest LV2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.17.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.3-0.16.20150303gitcfbd4b3
- Change to new cmake macros
- Resolves: rhbz #1864102

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.15.20150303gitcfbd4b3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.14.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.11.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.3-0.10.20150303gitcfbd4b3
- Append curdir to CMake invokation. (#1668512)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.9.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.8.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.7.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.6.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.5.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.4.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3-0.3.20150303gitcfbd4b3
- Disable SSE on all non x86(-64) architectures - rhbz#1220294
- Change order of CMakeLists.txt mangling to keep /usr/lib for hardening rules file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.2.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Brendan Jones <brendan.jones.it@gmail.com> 1.3-0.1.gitcfbd4b36
- Update to latest git 

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-4.3.20131003git5f2cb26
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.3.20131003git5f2cb26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2.3.20131003git5f2cb26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.3.20131003git5f2cb26
- Remove additional presets, update description

* Fri Oct 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.2.20101003git5f2cb26
- Remove durtySouth kit

* Sun Oct 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.1.20131003git5f2cb26
- Clean up git URLs and sources
- Split presets into separate package

* Tue Sep 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.1.gite8fb937
- Initial package

