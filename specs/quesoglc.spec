Name:           quesoglc
Version:        0.7.2
Release:        42%{?dist}
Summary:        The OpenGL Character Renderer

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://quesoglc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-free.tar.bz2
Patch0:         quesoglc-0.7.2-drop-glewContext.patch
Patch1:         quesoglc-0.7.2-doxyfile.patch
Patch2:         fribidi.build.patch
Patch3:         quesoglc-0.7.2-wayland.patch
Patch4:         quesoglc-0.7.2-buildfix.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fontconfig-devel
BuildRequires:  freeglut-devel
BuildRequires:  fribidi-devel
BuildRequires:  glew-devel
BuildRequires:  libSM-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  libXi-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  texlive-dvips-bin
BuildRequires:  ghostscript-core

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel
Requires:       pkgconfig

%description
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%description devel
This package provides the libraries, include files, and other resources needed
for developing GLC applications.


%prep
%autosetup -p1
rm -f include/GL/{glxew,wglew,glew}.h
rm -f src/glew.c
ln -s %{_includedir}/GL/{glxew,wglew,glew}.h include/GL/
rm -rf src/fribidi/


%build
%configure --disable-static 
%make_build
cd docs
doxygen
cd ../


%install
%make_install
rm %{buildroot}%{_libdir}/libGLC.la

%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_libdir}/libGLC.so.*

%files devel
%doc docs/html
%{_includedir}/GL/glc.h
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.2-41
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Hans de Goede <hdegoede@redhat.com> - 0.7.2-38
- Fix FTBFS due to https://fedoraproject.org/wiki/Changes/PortingToModernC

* Sat Jan 20 2024 Hans de Goede <hdegoede@redhat.com> - 0.7.2-37
- Fix quesoglc not working under Wayland
- Resolves: rhbz#2169654
- Resolves: rhbz#2258142

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.7.2-33
- Rebuild for glew 2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.2-24
- Modernization of the spec file
- Add missing buildrequires (#1606062)

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.7.2-23
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 28 2018 Caolán McNamara <caolanm@redhat.com> - 0.7.2-21
- Fix building with fribidi 1.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Hans de Goede <hdegoede@redhat.com> - 0.7.2-16
- Fix building with glew 2.0.0

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.7.2-15
- Rebuild for glew 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> 0.7.2-13
- Rebuild for glew 1.13

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.7.2-9
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.7.2-6
- Rebuild for glew 1.9.0

* Sat Jul 28 2012 Hans de Goede <hdegoede@redhat.com> - 0.7.2-5
- Fix FTBFS (rhbz#716030)
- Fix multilib conflict (rhbz#831438)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Karol Trzcionka <karlikt at gmail.com> - 0.7.2-1
- Update to v0.7.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 22 2008 Karol Trzcionka <karlikt at gmail.com> - 0.7.1-1
- Update to v0.7.1
- Using original tarball
* Sat Feb 23 2008 Karol Trzcionka <karlikt at gmail.com> - 0.7.0-1
- Update to v0.7.0
* Sat Feb 09 2008 Karol Trzcionka <karlikt at gmail.com> - 0.6.5-5
- Rebuild for gcc43
- Fix typo in patch
* Thu Dec 27 2007 Karol Trzcionka <karlikt at gmail.com> - 0.6.5-4
- Delete %%check
* Sun Dec 23 2007 Karol Trzcionka <karlikt at gmail.com> - 0.6.5-3
- Add %%check section
- Remove redundant BuildRequires
* Sat Dec 22 2007 Karol Trzcionka <karlikt at gmail.com> - 0.6.5-2
- Remove freeB and GLXPL files
- Add html docs
- Add Requires for subpackage -devel
- Fix BuildRequires
* Sat Dec 01 2007 Karol Trzcionka <karlikt at gmail.com> - 0.6.5-1
- Initial release
