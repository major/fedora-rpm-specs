%global commit 1e9524ffd759841789dadb4ca19fb5d4ac5820e7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%ifarch x86_64
%global niarch x64
%endif
%ifarch %{ix86}
%global niarch x86
%endif
%ifarch %arm
%global niarch Arm
%endif


Name:           openni
Version:        1.5.7.10
Release:        36%{?dist}
Summary:        Library for human-machine Natural Interaction

# Automatically converted from old format: ASL 2.0 and BSD - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            http://www.openni.org
# To reproduce tarball (adapt version and shortcommit):
# wget https://github.com/OpenNI/OpenNI/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# tar xvf openni-%{version}-%{shortcommit}.tar.gz
# cd OpenNI-%{commit}
# rm -rf Platform/Win32 Platform/Android Platform/ARC
# cd ..
# tar czf openni-%{version}-%{shortcommit}-fedora.tar.gz OpenNI-%{commit}
Source0:        openni-%{version}-%{shortcommit}-fedora.tar.gz
Source1:        libopenni.pc
Patch0:         openni-1.5.7.10-willow.patch
Patch1:         openni-1.5.7.10-fedora.patch
Patch2:         openni-1.5.2.23-disable-sse.patch
Patch3:         openni-1.3.2.1-silence-assert.patch
Patch4:         openni-1.3.2.1-fedora-java.patch
Patch5:         openni-1.5.2.23-disable-softfloat.patch
Patch6:         openni-1.5.2.23-armsamples.patch
Patch7:         openni-1.5.7.10-rename-equivalent-for-gcc6.patch
Patch8:         openni-freeglut.patch
# Fix compilation with -ansi or -std options
# https://github.com/OpenNI/OpenNI/commit/ca99f6181234c682bba42a6ba988cc10cee894d7
Patch9:         openni-ansi.patch

Patch10:        python3.patch

ExclusiveArch:  x86_64 %{arm}

BuildRequires:  gcc-c++, make
BuildRequires:  freeglut-devel, tinyxml-devel, libjpeg-devel, dos2unix, libusb1-devel
BuildRequires:  python3, doxygen, graphviz

%description
OpenNI (Open Natural Interaction) is a multi-language, cross-platform
framework that defines APIs for writing applications utilizing Natural
Interaction. OpenNI APIs are composed of a set of interfaces for writing NI
applications. The main purpose of OpenNI is to form a standard API that
enables communication with both:
 * Vision and audio sensors
 * Vision and audio perception middleware


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        java
Summary:        %{name} Java library
Requires:       %{name} = %{version}-%{release}
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java-headless
Requires:       jpackage-utils

%description    java
The %{name}-java package contains a Java JNI library for
developing applications that use %{name} in Java.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the automatically generated API documentation
for OpenNI.


%package        examples
Summary:        Sample programs for %{name}
Requires:       %{name} = %{version}-%{release}

%description    examples
The %{name}-examples package contains example programs for OpenNI.

%prep
%setup -q -n OpenNI-%{commit}
%patch -P0 -p1 -b .willow
%patch -P1 -p1 -b .fedora
%patch -P2 -p1 -b .disable-sse
%patch -P3 -p1 -b .silence-assert
%patch -P4 -p1 -b .fedora-java
%patch -P5 -p1 -b .disable-softfloat
%patch -P6 -p1 -b .armsamples
%patch -P7 -p1 -b .rename-equivalent-for-gcc6
%patch -P8 -p0 -b .freeglut
%patch -P9 -p1 -b .ansi
dos2unix Platform/Linux/CreateRedist/Redist_OpenNi.py
%patch -P10 -p1 -b python3
rm -rf Source/External
rm -rf Platform/Linux/Build/Prerequisites/*
find Samples -name GL -prune -exec rm -rf {} \;
find Samples -name Libs -prune -exec rm -rf {} \;

for ext in c cpp; do
  find Samples -name "*.$ext" -exec \
    sed -i -e 's|#define SAMPLE_XML_PATH "../../../../Data/SamplesConfig.xml"|#define SAMPLE_XML_PATH "%{_sysconfdir}/%{name}/SamplesConfig.xml"|' {} \;
done

sed -i 's|python|python3|' Platform/Linux/CreateRedist/RedistMaker
sed -i 's|if (os.path.exists("/usr/bin/gmcs"))|if (0)|' Platform/Linux/CreateRedist/Redist_OpenNi.py

dos2unix README
dos2unix LICENSE

%build
cd Platform/Linux/CreateRedist
# {?_smp_mflags} omitted, not supported by OpenNI Makefiles
chmod +x RedistMaker RedistMaker.Arm

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DEBUG=1 \
%ifarch %arm
./RedistMaker.Arm || cat Output/BuildOpenNI.txt
%else
./RedistMaker
%endif
cat Output/BuildOpenNI.txt


%install
rm -rf $RPM_BUILD_ROOT
pushd Platform/Linux/Redist/OpenNI-Bin-Dev-Linux-%{niarch}-v%{version}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/ni \
INSTALL_VAR=$RPM_BUILD_ROOT%{_var}/lib/ni \
INSTALL_JAR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
./install.sh -n

install -m 0755 Samples/Bin/%{niarch}-Release/libSample-NiSampleModule.so $RPM_BUILD_ROOT%{_libdir}/libNiSampleModule.so
install -m 0755 Samples/Bin/%{niarch}-Release/NiViewer $RPM_BUILD_ROOT%{_bindir}
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiAudioSample $RPM_BUILD_ROOT%{_bindir}/NiAudioSample
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiBackRecorder $RPM_BUILD_ROOT%{_bindir}/NiBackRecorder
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiConvertXToONI $RPM_BUILD_ROOT%{_bindir}/NiConvertXToONI
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiCRead $RPM_BUILD_ROOT%{_bindir}/NiCRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiRecordSynthetic $RPM_BUILD_ROOT%{_bindir}/NiRecordSynthetic
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleCreate $RPM_BUILD_ROOT%{_bindir}/NiSimpleCreate
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleRead $RPM_BUILD_ROOT%{_bindir}/NiSimpleRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleViewer $RPM_BUILD_ROOT%{_bindir}/NiSimpleViewer
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiUserTracker $RPM_BUILD_ROOT%{_bindir}/NiUserTracker

popd

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 0644 Data/SamplesConfig.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/ni
touch $RPM_BUILD_ROOT%{_var}/lib/ni/modules.xml

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
    -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
    -e 's![@]libdir[@]!%{_libdir}!g' \
    -e 's![@]includedir[@]!%{_includedir}!g' \
    -e 's![@]version[@]!%{version}!g' \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/libopenni.pc



%post
%{?ldconfig}
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libnimMockNodes.so
  niReg -r %{_libdir}/libnimCodecs.so
  niReg -r %{_libdir}/libnimRecorder.so
fi


%preun
if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libnimMockNodes.so
  niReg -u %{_libdir}/libnimCodecs.so
  niReg -u %{_libdir}/libnimRecorder.so
fi


%ldconfig_postun


%files
%doc LICENSE README NOTICE CHANGES
%dir %{_sysconfdir}/%{name}
%dir %{_var}/lib/ni
%ghost %{_var}/lib/ni/modules.xml
%{_libdir}/*.so
%{_bindir}/ni*

%files devel
%doc Documentation/OpenNI_UserGuide.pdf
%{_includedir}/*
%{_libdir}/pkgconfig/libopenni.pc

%files java
%{_libdir}/%{name}

%files examples
%config(noreplace) %{_sysconfdir}/%{name}/SamplesConfig.xml
%{_bindir}/Ni*
# not packaging any .desktop files for the sample applications. The
# applications will print relevant to the console and hence they are
# intended to be run on the console, not from the menu

%files doc
%doc Source/DoxyGen/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.7.10-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.5.7.10-33
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Till Hofmann <thofmann@fedoraproject.org> - 1.5.7.10-29
- Do not build on i686

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.7.10-26
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 14 21:22:42 CET 2021 Petr Viktorin <pviktori@redhat.com> - 1.5.7.10-23
- Build with Python 3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.5.7.10-20
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 01 2020 Orion Poplawski <orion@nwra.com> - 1.5.7.10-19
- Add upstream patch to fix compilation with -ansi or -std

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.5.7.10-17
- Rebuilt for new freeglut

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.7.10-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 17 2016 Scott K Logan <logans@cottsay.net> - 1.5.7.10-8
- Add patch for building with gcc6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.7.10-5
- Rebuild for gcc-5.0 (RHBZ#1211467).

* Mon Jan 05 2015 Rich Mattes <richmattes@gmail.com> - 1.5.7.10-4
- Fix ownership of modules.xml

* Mon Jan 05 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.7.10-4
- Rework openni-1.5.7.10-willow.patch (RHBZ#1178545).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <richmattes@gmail.com> - 1.5.7.10-1
- Update to release 1.5.7.10

* Sun Jun 01 2014 Rich Mattes <richmattes@gmail.com> - 1.5.2.23-1
- Update to release 1.5.2.23

* Fri Apr 04 2014 Scott K Logan <logans@cottsay.net> - 1.3.2.1-11
- Fix wrong pkgconfig path

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.2.1-10
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 26 2014 Scott K Logan <logans@cottsay.net> - 1.3.2.1-9
- Added patch and changed spec for arm support
- Added a simple pkgconfig

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.3.2.1-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.3.2.1-5
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Tim Niemueller <tim@niemueller.de> 1.3.2.1-2
- Add BR graphviz

* Thu Dec 22 2011 Tim Niemueller <tim@niemueller.de> 1.3.2.1-1
- Remove git suffix, we package the stable version
- Add Willow Garage and assertion silencing patches

* Sun Dec 04 2011 Tim Niemueller <tim@niemueller.de> 1.3.2.1-0.3.gitf8467404
- Mark modules.xml as config file, fixes deregistering of modules on upgrade

* Wed Oct 12 2011 Tim Niemueller <tim@niemueller.de> 1.3.2.1-0.2.gitf8467404
- Fix passing of opt cflags, fixes bz #735594

* Tue Aug 30 2011 Tim Niemueller <tim@niemueller.de> 1.3.2.1-0.1.gitf8467404
- Update to stable 1.3.2.1 based on patch by Anders Blomdell

* Mon Jun 27 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.0.25-0.5.git4c9ff978
- ExclusiveArch: %%ix86 x86_64 (#709718)

* Fri Feb 11 2011 Tim Niemueller <tim@niemueller.de> - 1.0.0.25-0.4.git4c9ff978
- Exclude ppc64, it is not supported by OpenNI

* Tue Feb 08 2011 Tim Niemueller <tim@niemueller.de> - 1.0.0.25-0.3.git4c9ff978
- Rename samples subpackage to examples 
- Remove bundled libraries and headers in prep stage
- Create empty modules.xml in install stage
- Do not package GPL.txt, all code is LGPL 

* Tue Feb 01 2011 Tim Niemueller <tim@niemueller.de> - 1.0.0.25-0.2.git4c9ff978
- Incorporate review suggestions

* Thu Jan 20 2011 Tim Niemueller <tim@niemueller.de> - 1.0.0.25-0.1.git4c9ff978
- Initial revision

