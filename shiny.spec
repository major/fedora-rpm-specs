%global commit 411ac43426e76066a45077276c5832c9f4d62a9c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           shiny
Version:        0.3
Release:        37.git%{shortcommit}%{?dist}
Summary:        Shader and material management library for OGRE

License:        MIT
URL:            https://github.com/scrawl/shiny/
Source0:        https://github.com/scrawl/shiny/archive/%{commit}/%{name}-%{version}-%{shortcommit}.zip
# https://github.com/scrawl/shiny/pull/25
Patch0:         0001-Revert-shiny.OgrePlatform.so-should-be-installed-in-.patch
Patch1:         0002-now-we-have-working-example-CMake-module.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ogre-devel
Requires:       ogre

%description
Shader and material management library for OGRE.

%package devel
Summary:        Development Files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ogre-devel

%description devel
Development files for shader and material management library for OGRE.

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1
%patch1 -p1


%build
LDFLAGS="$LDFLAGS -Wl,--as-needed"; export LDFLAGS
%cmake
%cmake_build


%install
%cmake_install

%ldconfig_scriptlets


%files
%doc License.txt Readme.txt
%{_libdir}/lib%{name}.so.*
%{_libdir}/OGRE/lib%{name}.OgrePlatform.so

%files devel
%doc example/FindSHINY.cmake
%{_includedir}/shiny/
%{_libdir}/lib%{name}.so

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-37.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.3-36.git411ac43
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-35.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Jonathan Wakely <jwakely@redhat.com> - 0.3-34.git411ac43
- Rebuilt for Boost 1.76

* Tue Aug 10 2021 Richard Shaw <hobbes1069@gmail.com> - 0.3-33.git411ac43
- Rebuild for boost 1.75.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-32.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-31.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.3-30.git411ac43
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-29.git411ac43
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-28.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.3-27.git411ac43
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 0.3-23.git411ac43
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.3-18.git411ac43
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3-16.git411ac43
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.3-14.git411ac43
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.3-12.git411ac43
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3-10.git411ac43
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.3-9.git411ac43
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7.git411ac43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-6.git411ac43
- Rebuild for boost 1.55.0

* Sat May 24 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-5.git411ac43
- revert OgrePlatform to libdir/OGRE
- add example cmake file

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 0.3-4.git411ac43
- Rebuild for boost 1.55.0

* Fri May 23 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-3.git411ac43
- Rebuild for boost 1.55.0

* Sat May 17 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-2.git411ac43
- Update to latest master (install OgrePlatform.so to libdir)

* Thu May 15 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-1.gitdc53364
- Update to latest master

* Wed May 14 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-3.gitf41178f
- don't ignore old LDFLAGS

* Wed May 14 2014 Richard Shaw <hobbes1069@gmail.com> - 0.2-2.gitf41178f
- Add patch to set soversion, install targets, and linking with Boost.
- Add LDFLAG option to prevent uncessary linking.

* Wed May 14 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1.gitf41178f
- Initial package
