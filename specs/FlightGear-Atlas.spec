%define snapshot .cvs20141002

Name:           FlightGear-Atlas
Summary:        Flightgear map tools
Version:        0.5.0
Release:        0.90%{snapshot}%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        Atlas-%{version}%{snapshot}.tar.bz2
Source1:        Atlas-0.5.0-default-maps.tar.bz2
Patch0:         Atlas-0.5.0-fix-unused-but-set-variable-warning.patch
Patch1:         Atlas-0.5.0-fix-narrowing-conversion-from-int-to-char-error.patch
Patch2:         Atlas-0.5.0-fix-operator-should-have-been-declared-inside-namespace-error.patch
Patch3:         Atlas-0.5.0-fix-removal-of-deprecated-function-in-sgtime.patch
Patch4:         Atlas-0.5.0-add-material-from-corine-landcover-classes.patch
Patch5:         Atlas-0.5.0-remove-assert-about-matching-navaids.patch
Patch6:         Atlas-0.5.0-fix-sgpath-api-change.patch 
URL:            http://atlas.sourceforge.net
BuildRequires:  gcc-c++
BuildRequires:  freeglut-devel, curl-devel, libpng-devel, glew-devel, boost-devel
BuildRequires:  SimGear-devel >= 2.6.0, OpenSceneGraph-devel, mesa-libEGL-devel
BuildRequires:  automake autoconf intltool libtool
BuildRequires: make
Requires:       FlightGear-data
Obsoletes:      fgfs-Atlas < 0.3.1-10

%description
Atlas aims to produce and display high quality charts of the world for
users of FlightGear, an open source flight simulator. This is achieved
through two main parts: The map creator (simply called Map) and the
Atlas viewer

%prep
%autosetup -p0 -n Atlas
find -type f -name '*.[hc]xx' -exec chmod a-x {} \;

%build
./autogen.sh
%configure CXXFLAGS="$RPM_OPT_FLAGS -fPIC" \
        --with-fgbase=%{_datadir}/flightgear \
        --datadir=%{_datadir}/flightgear \
        --enable-simgear-shared
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear
tar jxf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/flightgear

# the palette file must be installed
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Palettes
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Fonts

install -m 0644 src/data/Fonts/*.txf \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Fonts
install -m 0644 src/data/Palettes/*.ap \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Palettes
install -m 0644 src/data/background.jpg \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas
install -m 0644 src/data/airplane_image.png \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/flightgear/Atlas

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.90.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-0.89.cvs20141002
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.88.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.87.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.86.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.85.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.84.cvs20141002
- rebuild with newer SimGear

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.83.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.82.cvs20141002
- rebuild with newer SimGear

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.81.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.80.cvs20141002
- rebuild with newer SimGear

* Thu Oct 20 2022 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.79.cvs20141002
- rebuild with newer SimGear

* Mon Oct 03 2022 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.78.cvs20141002
- rebuild with newer SimGear

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.77.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.76.cvs20141002
- rebuild with newer SimGear

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.5.0-0.75.cvs20141002
- Rebuild for glew 2.2

* Fri Feb 04 2022 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.74.cvs20141002
- rebuild with newer SimGear

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.73.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.72.cvs20141002
- rebuild with newer SimGear

* Mon Jul 26 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.71.cvs20141002
- rebuild with newer SimGear

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.70.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.69.cvs20141002
- rebuild with newer SimGear

* Tue Mar 30 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.68.cvs20141002
- rebuild with newer SimGear

* Mon Mar 22 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.67.cvs20141002
- rebuild with newer SimGear

* Tue Jan 26 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.66.cvs20141002
- rebuild with newer SimGear

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.65.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.64.cvs20141002
- rebuild with newer SimGear

* Tue Dec 01 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.63.cvs20141002
- rebuild with newer SimGear

* Sun Nov 29 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.62.cvs20141002
- rebuild with newer SimGear

* Mon Nov 09 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.61.cvs20141002
- rebuild with newer SimGear

* Fri Oct 30 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.60.cvs20141002
- rebuild with newer SimGear

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.59.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.58.cvs20141002
- rebuild with newer SimGear

* Sat May 23 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.57.cvs20141002
- rebuild with newer SimGear

* Tue May 12 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.56.cvs20141002
- rebuild with newer SimGear

* Mon Feb 10 2020 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.55.cvs20141002
- newer freeglut doesn't require a dedicated patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.54.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.5.0-0.53.cvs20141002
- Rebuilt for new freeglut

* Mon Jul 29 2019 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.52.cvs20141002
- rebuild with newer SimGear

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.51.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.50.cvs20141002
- rebuild with newer SimGear

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.49.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.48.cvs20141002
- rebuild with newer SimGear

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-0.47.cvs20141002
- Rebuilt for glew 2.1.0

* Sun Jul 15 2018 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.46.cvs20141002
- BR: gcc-c++

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.45.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.44.cvs20141002
- rebuild with newer SimGear

* Thu May 24 2018 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.43.cvs20141002
- rebuild with newer SimGear

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.42.cvs20141002
- rebuild with newer SimGear

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.41.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.40.cvs20141002
- bump and rebuild

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.39.cvs20141002
- rebuild with newer SimGear

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.38.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.37.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.36.cvs20141002
- rebuild with newer SimGear

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.35.cvs20141002
- rebuild with newer SimGear

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.34.cvs20141002
- rebuild with newer SimGear

* Fri Feb 24 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.33.cvs20141002
- rebuild with newer SimGear

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.32.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-0.31.cvs20141002
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.0-0.30.cvs20141002
- Rebuild for glew 2.0.0

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.29.cvs20141002
- rebuild with newer SimGear

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.28.cvs20141002
- rebuild with newer SimGear

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.27.cvs20141002
- rebuild with newer SimGear

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.26.cvs20141002
- rebuild with newer SimGear

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.25.cvs20141002
- rebuild with newer SimGear
- fix for SGPath API change

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.24.cvs20141002
- rebuild with newer SimGear

* Wed May 11 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.23.cvs20141002
- rebuild with newer SimGear

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.22.cvs20141002
- Add material from CORINE landcover classes
- Remove assert about matching navaids

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.21.cvs20141002
- rebuild with newer SimGear
- fix the removal of deprecated function in sgtime

* Mon Feb 15 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.20.cvs20141002
- updated the patch to fix the operator should have been declared
  inside namespace error

* Sun Feb 14 2016 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.19.cvs20141002
- rebuild for updated simgear
- fix unused-but-set-variable warning
- fix narrowing conversion from int to char error
- fix operator should have been declared inside namespace error

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.18.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-0.17.cvs20141002
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.5.0-0.16.cvs20141002
- Rebuild for glew 1.13

* Sat Sep 12 2015 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.15.cvs20141002
- rebuilt with newer SimGear

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-0.14.cvs20141002
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-0.13.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.5.0-0.12.cvs20141002
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-0.11.cvs20141002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-0.10.cvs20141002
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.9.cvs20141002
- rebuilt with newer SimGear

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.5.0-0.8.cvs20141002
- Rebuild for boost 1.57.0

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.7.cvs20141002
- rebuilt with newer SimGear

* Thu Oct 02 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.6.cvs20141002
- new snapshot, drop local patches
- regenerate defaults maps around KSFO using scenery version 2

* Tue Sep 23 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.5.cvs20140918
- Dont compute elevation via GL_SELECT render mode while scrolling with 
  the mouse, as this is an expensive operation.

* Mon Sep 22 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.4.cvs20140918
- Disable live bucket intersection computation, to restore some smoothness
  while scrolling, because drawing with glRenderMode set to GL_SELECT is 
  expensive.

* Thu Sep 18 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.3.cvs20140918
- new snapshot

* Mon Sep 15 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.2.cvs20140914
- Fix missing GL/glew.h include file in Subbucket.cxx

* Sun Sep 14 2014 Fabrice Bellet <fabrice@bellet.info> - 0.5.0-0.1.cvs20140914
- new snapshot

* Fri Sep 12 2014 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.19.cvs20140320
- rebuilt with newer SimGear

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-0.21.cvs20140320
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.4.9-0.20.cvs20140320
- Rebuild for OSG-3.2.1.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-0.19.cvs20140320
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.18.cvs20140320
- new snapshot

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.17.cvs20131203
- rebuilt with newer SimGear
- temporary fix to use FlightGear-data-2.12 airports and navaids files
  until upstream supports the new versions of these files as shipped in
  FlightGear-data-3.0

* Wed Dec 11 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.16.cvs20131203
- new snapshot to gracefully handle scenery v2.0 generation from terrasync

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.4.9-0.15.cvs20130922
- rebuilt for GLEW 1.10

* Mon Sep 30 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.14.cvs20130922
- add the default maps source file back

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.13.cvs20130922
- new snapshot

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-0.12.cvs20120911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.11.cvs20120911
- libpthread link patch is no longer needed (rh#918003)

* Wed Mar 06 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.10.cvs20120911
- add libpthread to link Atlas

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.9.cvs20120911
- rebuilt with newer SimGear

* Sun Feb 17 2013 Fabrice Bellet <fabrice@bellet.info> - 0.4.9-0.8.cvs20120911
- init _renderConfirmDialog

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-0.7.cvs20120911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.4.9-0.6.cvs20120911
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.4.9-0.5.cvs20120911
- Rebuild for glew 1.9.0

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 0.4.9-0.4.cvs20120911
- rebuilt with newer SimGear

* Mon Jul 30 2012 Fabrice Bellet <fabrice@bellet.info> 0.4.9-0.3.cvs20120219
- Rebuilt for new glew

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-0.2.cvs20120219
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Fabrice Bellet <fabrice@bellet.info> 0.4.9-0.1.cvs20120219
- new snapshot

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-0.6.cvs20110905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.8-0.5.cvs20110905
- Rebuild for new libpng

* Tue Sep 06 2011 Fabrice Bellet <fabrice@bellet.info> 0.4.8-0.4.cvs20110905
- add the default maps source file back

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 0.4.8-0.3.cvs20110905
- new snapshot
- the FlightGear data directory name is now in lowercase

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-0.2.cvs20100719
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Fabrice Bellet <fabrice@bellet.info> 0.4.8-0.1.cvs20100719
- new cvs snapshot
- fix some segmentation faults

* Thu Mar 11 2010 Fabrice Bellet <fabrice@bellet.info> 0.4.0-0.5.cvs20100226
- Fix graph axis formatting bug, by avoiding negative values in the
  format string

* Sat Feb 27 2010 Fabrice Bellet <fabrice@bellet.info> 0.4.0-0.4.cvs20100226
- Rebuild with missing librt library

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 0.4.0-0.3.cvs20100226
- Prepare for release 0.4.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Fabrice Bellet <fabrice@bellet.info> 0.3.1-11
- rebuild with newer SimGear

* Tue Jan 06 2009 Fabrice Bellet <fabrice@bellet.info> 0.3.1-10
- new build fixes for newer SimGear

* Tue May 13 2008 Fabrice Bellet <fabrice@bellet.info> 0.3.1-9
- rebuild with newer plib

* Mon Feb  4 2008 Fabrice Bellet <fabrice@bellet.info> 0.3.1-8
- fix gcc43 build

* Mon Jan  7 2008 Fabrice Bellet <fabrice@bellet.info> 0.3.1-7
- rebuild with newer SimGear

* Sun Sep 23 2007 Fabrice Bellet <fabrice@bellet.info> 0.3.1-6
- update License tag

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.3.1-5
- Rebuild for selinux ppc32 issue.

* Wed Jun 27 2007 Fabrice Bellet <fabrice@bellet.info> 0.3.1-4
- Rebuild with newer version of SimGear
- Add the missing Palette file to the package
- Remove the buildmaps.sh script (the functionnality provided
  by this script is now part of the Atlas program)

* Mon Apr  2 2007 Fabrice Bellet <fabrice@bellet.info> 0.3.1-3
- Fixed duplicate BuildRequires

* Sun Apr  1 2007 Fabrice Bellet <fabrice@bellet.info> 0.3.1-2
- Rebuild with new SimGear

* Tue Mar 20 2007 Fabrice Bellet <fabrice@bellet.info> 0.3.1-1
- Initial packaging
