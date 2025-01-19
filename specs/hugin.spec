Summary: A panoramic photo stitcher and more
Name: hugin
Version: 2024.0.0
Release: 2%{?dist}
License: GPL-2.0-or-later
Source: https://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
URL: http://hugin.sourceforge.net/
Requires: shared-mime-info
Requires: webclient
Requires: %{name}-base = %{version}-%{release}
BuildRequires: gcc-c++
BuildRequires: libpano13-devel zlib-devel libtiff-devel libjpeg-devel
BuildRequires: libpng-devel gettext-devel wxGTK-devel boost-devel freeglut-devel
BuildRequires: cmake desktop-file-utils OpenEXR-devel exiv2-devel glew-devel
BuildRequires: python3-devel swig flann-devel perl-Image-ExifTool
BuildRequires: mesa-libGLU-devel libXmu-devel sqlite-devel vigra-devel
BuildRequires: perl-podlators fftw-devel lcms2-devel
# contains deprecated distutils
BuildRequires: python-setuptools

%description
hugin can be used to stitch multiple images together. The resulting image can
span 360 degrees. Another common use is the creation of very high resolution
pictures by combining multiple images. It uses the Panorama Tools as back-end
to create high quality images

%package base
Summary: Command-line tools and libraries required by hugin
Requires: enblend perl-Image-ExifTool

%description base
Command-line tools used to generate panoramic images, install this package
separately from hugin if you want to batch-process hugin projects on a machine
without a GUI environment.

%prep
%autosetup -p1
sed -i 's^/usr/bin/env python3^/usr/bin/python3^' \
src/hugin_script_interface/plugins-dev/*.py \
src/hugin_script_interface/*.py \
src/hugin_script_interface/plugins/*.py

%build
%cmake -DBUILD_HSI=1 -DUSE_GDKBACKEND_X11=ON
%cmake_build

%install
%cmake_install

%if 0%{?flatpak}
# pyinstalldir is not configurable
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_usr}/%{_lib}/python%{python3_version}/site-packages/* %{buildroot}%{python3_sitearch}
%endif

desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/PTBatcherGUI.desktop
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/pto_gen.desktop
%find_lang %{name}

# Merge applications into one software center item
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
cat > $RPM_BUILD_ROOT%{_datadir}/metainfo/calibrate_lens_gui.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>calibrate_lens_gui.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">hugin.desktop</value>
  </metadata>
</component>
EOF

%ldconfig_scriptlets base

%files -f %{name}.lang
%{_bindir}/PTBatcherGUI
%{_bindir}/hugin
%{_bindir}/hugin_stitch_project
%{_bindir}/icpfind
%{_bindir}/calibrate_lens_gui
%{_bindir}/hugin_executor
%{_libdir}/%{name}/libhuginbasewx.so*
%{_libdir}/%{name}/libicpfindlib.so*
%{_datadir}/%{name}/xrc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/PTBatcherGUI.desktop
%{_datadir}/applications/calibrate_lens_gui.desktop
%{_datadir}/applications/pto_gen.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/PTBatcherGUI.appdata.xml
%{_datadir}/metainfo/calibrate_lens_gui.appdata.xml
%{_datadir}/metainfo/hugin.appdata.xml
%{_mandir}/man1/PTBatcherGUI.*
%{_mandir}/man1/calibrate_lens_gui.*
%{_mandir}/man1/hugin.*
%{_mandir}/man1/hugin_stitch_project.*
%{_mandir}/man1/icpfind.*
%{_mandir}/man1/hugin_executor.*
%{_mandir}/man1/hugin_stacker.*

%doc AUTHORS README TODO src/celeste/LICENCE_LIBSVM doc/nona.txt doc/fulla.html doc/executor_file_format.txt src/hugin1/hugin/xrc/data/help_en_EN/LICENCE.manual
%license COPYING.txt

%files base
%{_bindir}/align_image_stack
%{_bindir}/autooptimiser
%{_bindir}/celeste_standalone
%{_bindir}/fulla
%{_bindir}/hugin_hdrmerge
%{_bindir}/nona
%{_bindir}/tca_correct
%{_bindir}/vig_optimize
%{_bindir}/cpclean
%{_bindir}/deghosting_mask
%{_bindir}/pano_trafo
%{_bindir}/pano_modify
%{_bindir}/pto_merge
%{_bindir}/checkpto
%{_bindir}/cpfind
%{_bindir}/linefind
%{_bindir}/pto_gen
%{_bindir}/pto_lensstack
%{_bindir}/pto_var
%{_bindir}/geocpset
%{_bindir}/pto_mask
%{_bindir}/pto_move
%{_bindir}/pto_template
%{_bindir}/verdandi
%{_bindir}/hugin_lensdb
%{_bindir}/hugin_stacker

%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/libhuginbase.so*
%{_libdir}/%{name}/libceleste.so*
%{_libdir}/%{name}/liblocalfeatures.so*
%{_libdir}/%{name}/libhugin_python_interface.so*
%{python3_sitearch}/_hsi.so
%{python3_sitearch}/hsi.py*
%{python3_sitearch}/hpi.py*
%{python3_sitearch}/__pycache__/*

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/data

%{_mandir}/man1/align_image_stack.*
%{_mandir}/man1/autooptimiser.*
%{_mandir}/man1/cpclean.*
%{_mandir}/man1/celeste_standalone.*
%{_mandir}/man1/fulla.*
%{_mandir}/man1/hugin_hdrmerge.*
%{_mandir}/man1/nona.*
%{_mandir}/man1/tca_correct.*
%{_mandir}/man1/vig_optimize.*
%{_mandir}/man1/deghosting_mask.*
%{_mandir}/man1/pano_trafo.*
%{_mandir}/man1/pano_modify.*
%{_mandir}/man1/pto_merge.*
%{_mandir}/man1/checkpto.*
%{_mandir}/man1/cpfind.*
%{_mandir}/man1/linefind.*
%{_mandir}/man1/pto_gen.*
%{_mandir}/man1/pto_lensstack.*
%{_mandir}/man1/pto_var.*
%{_mandir}/man1/geocpset.*
%{_mandir}/man1/pto_mask.*
%{_mandir}/man1/pto_move.*
%{_mandir}/man1/pto_template.*
%{_mandir}/man1/verdandi.*
%{_mandir}/man1/hugin_lensdb.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Bruno Postle <bruno@postle.net> - 2024.0.0-1
- stable release

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Robert-André Mauchin <zebob.m@gmail.com> - 2023.0.0-10
- Rebuilt for exiv2 0.28.2

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2023.0.0-9
- Rebuilt for Python 3.13

* Sun May 19 2024 Bruno Postle <bruno@postle.net> - 2023.0.0-8
- own {_libdir}/hugin and {_datadir}/hugin folders bug #2280163
- migrated to SPDX license

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2023.0.0-7
- Rebuilt for openexr 3.2.4

* Fri Mar 15 2024 Bruno Postle <bruno@postle.net> - 2023.0.0-6
- Support flatpak python install dir (yselkowitz)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2023.0.0-3
- Rebuilt for Boost 1.83

* Tue Dec 05 2023 Bruno Postle <bruno@postle.net> - 2023.0.0-2
- build without lz4 workarounds see bug #2240334

* Sat Nov 11 2023 Bruno Postle <bruno@postle.net> - 2023.0.0-1
- 2023.0.0 stable release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2022.0.0-4
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2022.0.0-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Bruno Postle <bruno@postle.net> - 2022.0.0-1
- Upstream stable release

* Wed Dec 14 2022 Scott Talbert <swt@techie.net> - 2021.0.0-10
- Rebuild with X11 backend due to wxGL now not supporting Wayland

* Wed Dec 14 2022 Scott Talbert <swt@techie.net> - 2021.0.0-9
- Fix crash with wxWidgets 3.2 (#2152749)

* Sun Nov 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2021.0.0-8
- Rebuild due to wxGLCanvas ABI change

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2021.0.0-7
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2021.0.0-5
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2021.0.0-4
- Rebuilt for Boost 1.78

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2021.0.0-3
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Bruno Postle <bruno@postle.net> - 2021.0.0-1
- upstream stable release

* Sat Aug 21 2021 Richard Shaw <hobbes1069@gmail.com> - 2020.0.0-12
- Rebuild for OpenEXR/Imath 3.1.

* Tue Aug 10 2021 Richard Shaw <hobbes1069@gmail.com> - 2020.0.0-11
- Rebuild for OpenEXR 3.

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.0.0-10
- Rebuilt for Boost 1.76

* Mon Aug 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2020.0.0-9
- Rebuild for OpenEXR/Imath 3.

* Thu Jul 29 2021 Bruno Postle <bruno@postle.net> - 2020.0.0-8
- Rebuilt

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.0.0-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.0.0-4
- Rebuilt for Boost 1.75

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2020.0.0-3
- rebuild against New OpenEXR again

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2020.0.0-2
- Rebuild for OpenEXR 2.5.3.

* Sat Dec 12 2020 Bruno Postle <bruno@postle.net> - 2020.0.0-1
- stable release
- remove -DUSE_GDKBACKEND_X11=1 wayland workaround as WX now carries a patch for this directly

* Sat Aug 08 2020 Rich Mattes <richmattes@gmail.com> - 2019.2.0-7
- Rebuild for flann-1.9.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Bruno Postle <bruno@postle.net> - 2019.2.0-5
- cmake macros have changed, rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 2019.2.0-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.2.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Bruno Postle <bruno@postle.net> - 2019.2.0-1
- stable release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.0.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.0.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Bruno Postle <bruno@postle.net> - 2019.0.0-2
- Patch to fix breakage caused by exiv2-0.27.1

* Sat Apr 13 2019 Bruno Postle <bruno@postle.net> - 2019.0.0-1
- Stable release, still built with configure option to force X11 backend on Wayland

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2018.0.0-11
- Rebuild for OpenEXR 2.3.0.

* Sat Mar 23 2019 Bruno Postle <bruno@postle.net> - 2018.0.0-10
- upstream fix for cmake 3.14 changes

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 2018.0.0-9
- Rebuilt for Boost 1.69

* Wed Jan 30 2019 Bruno Postle <bruno@postle.net> - 2018.0.0-8
- fix for exiv2 0.27

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2018.0.0-7
- rebuild (exiv2)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2018.0.0-6
- Rebuilt for Boost 1.69

* Tue Sep 18 2018 Bruno Postle <bruno@postle.net> - 2018.0.0-5
- remove ambiguous /usr/bin/env python

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2018.0.0-4
- Rebuilt for glew 2.1.0
- Fix build switch to python3
- Spec file clean-up

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Bruno Postle <bruno@postle.net> - 2018.0.0-1
- stable release, built with configure option to force X11 backend on Wayland

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2017.0.0-8
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.0.0-7
- Remove obsolete scriptlets

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2017.0.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2017.0.0-4
- rebuilt

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 2017.0.0-2
- Rebuilt for Boost 1.64

* Tue Jul 04 2017 Bruno Postle <bruno@postle.net> - 2017.0.0-1
- stable release, built with configure option to force X11 backend on Wayland

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2016.2.0-4
- rebuild (exiv2)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2016.2.0-2
- Rebuild for glew 2.0.0

* Sun Sep 18 2016 Bruno Postle <bruno@postle.net> - 2016.2.0-1
- stable release, built with GTK2

* Wed Apr 13 2016 Bruno Postle <bruno@postle.net> - 2016.0.0-1
- stable release

* Wed Aug 19 2015 Bruno Postle <bruno@postle.net> - 2015.0.0-1
- upstream release

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2014.0.0-9
- rebuild for Boost 1.58

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2014.0.0-8
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Nils Philippsen <nils@redhat.com> - 2014.0.0-6
- rebuild for lensfun-0.3.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2014.0.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2014.0.0-4
- Add an AppData file for the software center

* Tue Feb 03 2015 Petr Machata <pmachata@redhat.com> - 2014.0.0-3
- Rebuild for boost 1.57.0
- Apply an upstream patch that ports expression parser to
  Boost.Phoenix V3 (hugin-2013.0.0-boost-phoenix3.patch)

* Mon Feb 02 2015 Bruno Postle <bruno@postle.net> - 2014.0.0-2
- Upstream release

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2013.0.0-12
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 2013.0.0-11
- FTBFS against lensfun-0.3 (#1168239)

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 2013.0.0-10
- rebuild (openexr)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2013.0.0-8
- update icon/mime scriptlets

* Sat Jun 07 2014 Bruno Postle <bruno@postle.net> - 2013.0.0-7
- Rebuild for rebuilt libpano13

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2013.0.0-6
- Rebuild for boost 1.55.0

* Sun Dec 15 2013 Bruno Postle <bruno@postle.net> - 2013.0.0-5
- fix to re-enable .pto file association

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 2013.0.0-4
- rebuild (exiv2)

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 2013.0.0-3
- rebuild (openexr)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2013.0.0-2
- rebuilt for GLEW 1.10

* Thu Oct 31 2013 Bruno Postle <bruno@postle.net> - 2013.0.0-1
- upstream stable release

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 2012.0.0-11
- rebuild (openexr)

* Mon Aug 26 2013 Rex Dieter <rdieter@fedoraproject.org> 2012.0.0-10
- fix FTBFS wrt perl pod encoding issue(s) (#991875)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 2012.0.0-8
- Rebuild for boost 1.54.0

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> 2012.0.0-7
- rebuild (openEXR)

* Wed Feb 13 2013 Bruno Postle 2012.0.0-6
- perl-podlators is now split from perl

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2012.0.0-5
- Rebuild for Boost-1.53.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2012.0.0-4
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 26 2012 Kevin Fenzi <kevin@scrye.com> 2012.0.0-3
- Rebuild for new libflann_cpp

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 2012.0.0-2
- Rebuild for glew 1.9.0

* Mon Nov 05 2012 Bruno Postle 2012.0.0-1
- Stable release, no longer contains a bundled flann

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> 2011.4.0-9
- Rebuild for new boost

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> 2011.4.0-8
- Rebuild for new glew

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Bruno Postle - 2011.4.0-6
- backported fix for bug that prevented python plugin 'Actions' menu appearing

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2011.4.0-5
- rebuild (exiv2)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.4.0-4
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Bruno Postle 2011.4.0-3
- Patch to build with gcc-4.7.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Bruno Postle 2011.4.0-1
- upstream release

* Sun Nov 20 2011 Thomas <thomas.spura@googlemail.com> - 2011.2.0-4
- rebuild for https://fedoraproject.org/wiki/Features/F17Boost148

* Sun Oct 30 2011 Bruno Postle 2011.2.0-3
- remove tclap patch since tclap is now in fedora

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 2011.2.0-2
- rebuild (exiv2)

* Fri Sep 30 2011 Bruno Postle 2011.2.0-1
- upstream release. tclap patch ported forward from 2011.0.0, see bug #683591

* Sun Jul 24 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2011.0.0-3
- Rebuilt for boost 1.47.0 soname bump

* Mon Jun 20 2011 ajax@redhat.com - 2011.0.0-2
- Rebuild for new glew soname

* Mon May 30 2011 Bruno Postle 2011.0.0-1
- upstream release

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 2010.4.0-5
- Rebuilt for boost 1.46.1 soname bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2010.4.0-3
- Rebuild for new Boost

* Fri Feb 04 2011 Bruno Postle <bruno@postle.net> - 2010.4.0-2
- Backport gcc-4.6.0 patch from upstream

* Wed Jan 12 2011 Bruno Postle <bruno@postle.net> - 2010.4.0-1
- Upstream release (2010.4.0)

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 2010.2.0-2
- rebuild (exiv2)

* Sun Nov 07 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2010.2.0-1
- Upstream release (2010.2.0)

* Mon Aug 23 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2010.0.0-5
- The xorg-x11-devel package is not available on Fedora. So,
   removed it.

* Wed Aug 04 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 2010.0.0-4
- Rebuild for Boost soname bump
- Update to match current guidelines and drop obsolete ifdefs

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2010.0.0-3
- rebuilt against wxGTK-2.8.11-2

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 2010.0.0-2
- rebuild (exiv2)

* Tue Mar 23 2010 Bruno Postle <bruno@postle.net> 2010.0.0-1
- 2010.0.0 release
- Thanks to Terry Duell for updated .spec

* Fri Feb 05 2010 Bruno Postle <bruno@postle.net> 2009.4.0-1
- Fixes for push to fedora

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 2009.2.0-2
- Rebuild for Boost soname bump

* Tue Oct 20 2009 Bruno Postle <bruno@postle.net> 2009.2.0-1
- 2009.2.0 release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Bruno Postle <bruno@postle.net> 0.8.0-1
- 0.8.0 release

* Thu May 28 2009 Bruno Postle <bruno@postle.net> - 0.7.0-7
- Rebuild for libpano13 soname change

* Fri May 22 2009 Bruno Postle <bruno@postle.net> - 0.7.0-6
- Rebuild for boost soname change.
- Remove trademark from summary, remove .desktop vendor.

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 0.7.0-5
- include stdio.h for snprintf and cstdio for std::sprintf

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.7.0-3
- respin (eviv2)

* Thu Dec 18 2008 Petr Machata <pmachata@redhat.com> - 0.7.0-2
- rebuild for new boost

* Tue Oct 07 2008 Bruno Postle <bruno@postle.net> 0.7.0-1
- 0.7.0 release

* Thu Jun 26 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.4.20080528svn
- rawhide rebuild for updated libexiv2

* Wed May 28 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.3.20080528svn
- SVN snapshot, 0.7 beta. New tools matchpoint tca_correct

* Mon Feb 18 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.3.20080218svn
- SVN snapshot, 0.7 beta, gcc-4.3.0 fixes

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.0-0.3.20080216svn
- Autorebuild for GCC 4.3

* Tue Feb 05 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.2.20080205svn
- SVN snapshot, 0.7 beta.

* Tue Jan 22 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.2.20080121svn
- SVN snapshot, 0.7 beta. move cli dependencies to hugin-base package

* Mon Jan 21 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.1.20080121svn
- SVN snapshot, add LICENCE.manual

* Sat Jan 19 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.1.20080119svn
- SVN snapshot, split to hugin and hugin-base packages

* Wed Jan 16 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.1.20080116svn
- remove autopano-sift-C dependency, use autopano-noop.sh instead
- delete devel .so symlinks

* Mon Jan 14 2008 Bruno Postle <bruno@postle.net> 0.7.0-0.1.20080112svn
- SVN snapshot, switch to fedora naming scheme, add exiftool dependency

* Sat Oct 27 2007 Bruno Postle <bruno@postle.net> 0.7.0-0svn20071029
- revert to trunk
- ldconfig as we are installing libs
- libpano13-tools & make dependency

* Wed Oct 24 2007 Bruno Postle <bruno@postle.net> 0.7.0-0svn20071024
- lib64 issue should be fixed, lots of .so.0 files now, release has decremented

* Mon Oct 22 2007 Bruno Postle <bruno@postle.net> 0.7.1-0svn20071022
- ippei branch, switch to cmake

* Mon Apr 16 2007 Bruno Postle <bruno@postle.net> 0.7.0_beta5-0cvs20070416
- CVS snapshot
- add shared-mime-info, desktop-file-utils dependencies
- use desktop-file-install for .desktop file

* Mon Jan 29 2007 Bruno Postle <bruno@postle.net> 0.7.0_beta3-2cvs20070129
- CVS snapshot of 0.7 beta, switch to libpano13

* Sun Sep 17 2006 Bruno Postle <bruno@postle.net> 0.6.1-4
- Fix spec typos and cruft, use find_lang, post and postun fixes

* Fri Sep 15 2006 Bruno Postle <bruno@postle.net> 0.6.1-2
- replace mono autopanog patch with sed

* Thu Aug 24 2006 Bruno Postle <bruno@postle.net> 0.6.1-1
- 0.6.1 release

* Mon Jul 24 2006 Bruno Postle <bruno@postle.net> 0.6-4
- 0.6 release, tidy spec file, add post-release autopano-sift patch

* Mon Jul 24 2006 Bruno Postle <bruno@postle.net> 0.6-3
- 0.6 release

* Mon Jun 19 2006 Bruno postle <bruno@postle.net> 0.6-2cvs20060611
- Recompile to link to libpano12-2.8.4. use find_lang macro. remove repo tag. use dist tag

* Wed Apr 19 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot + gcc 4.1 hack.
- batch processing for fulla.
- requires latest pano12 > 2.8.0 for direct access to optimiser

* Thu Mar 09 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot + hack to fix charset of cs_CZ translation

* Thu Mar 09 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot. new vignetting/aberation/lens correction tool: fulla

* Tue Mar 07 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot, add missing docs

* Thu Jan 12 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot. Philippe Thomins color correction tool. fix for ptoptimizer

* Mon Jan 09 2006 Bruno Postle <bruno@postle.net>
- 0.6 CVS snapshot. nona vignetting correction

* Mon Nov 14 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. included ca_ES catalan translation

* Thu Nov 10 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. included hu hungarian translation

* Fri Sep 16 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. includes zh_CN Chinese translation

* Fri Sep 16 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. includes nl dutch translation

* Wed Aug 17 2005 Bruno Postle <bruno@postle.net>
- new build from CVS.
- Remove patch that turns off enblend compression, as compression
  is now disabled by default.

* Thu Mar 10 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. This is approximately hugin 0.5 beta3

* Mon Feb 28 2005 Bruno Postle <bruno@postle.net>
- new build from CVS. Removed fftw dependency

* Mon Nov 22 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs. patch to call enblend without compression.
  patch to call autopanog.exe via mono.

* Thu Oct 21 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Should fix bug where fov can't be optimised

* Wed Oct 20 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Updated French translation.
  add enblend dependency.

* Thu Oct 14 2004 Bruno Postle  <bruno@postle.net>
- New build for fedora fc2.
  Now uses automake/autoconf
  Switch dependency from panorama-tools to libpano12 & libpano12-devel

* Thu Sep 09 2004 Bruno Postle <bruno@postle.net>
- new build from cvs.  point picker can do rotation matching, various bugfixes.
  panoviewer doesn't get built anymore.

* Tue Aug 31 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Should fix bug where enblend isn't executed from the gui.

* Fri Jul 23 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, removed vigra dependency.

* Tue Jul 13 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, still requires vigra, though the vigra stuff is now
  in the hugin tree. Installs utilities: mergepto pta2hugin.py run-autopano-sift.sh

* Fri Jul 02 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, needs a newer patched vigra
- install various (nonworking?) tools automatch autooptimiser panosifter
  autopano_old

* Tue Jun 15 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, requires a vigra with 16bit unsigned tiff support
     remove: autopano_old, automatch, autooptimiser, panosifter

* Sun Apr 04 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, new features:
     autopano integration
     delete control points between selected images
     reset positions of all selected images

* Sun Mar 14 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs, this is post 0.4b release with nona_gui

* Sun Feb 08 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Now doesn't depend on vigra

* Wed Feb 04 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Now depends on vigra

* Tue Feb 03 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  Two new tools autooptimiser and panosifter

* Thu Jan 15 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs. now includes automatch

* Sat Jan 03 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  This is the 0.4pre release

* Thu Jan 01 2004 Bruno Postle  <bruno@postle.net>
- new build from cvs.  autopano now requires fftw.

* Sun Nov 30 2003 Bruno Postle <bruno@postle.net>
- The vigra library when compiled with shared libraries isn't actually
  necessary to run nona, so it's now only a build requirement.  The
  panorama-tools package is now split with the nonfree package now
  required to run hugin.

* Sat Nov 29 2003  Bruno Postle  <bruno@postle.net>
- new build from cvs; stitcher is now called nona

* Mon Nov 24 2003 Bruno Postle  <bruno@postle.net>
- new build from cvs; add vigra dependency for stitcher

* Sun Nov 16 2003 Bruno Postle <bruno@postle.net>
- new build from cvs; patch to build with gtk2

* Sun Nov 09 2003 Bruno Postle <bruno@postle.net>
- new build from cvs; first build with fedora1

* Mon Oct 27 2003 Bruno Postle <bruno@postle.net>
- new build from cvs, added manual.html to doc and [de] translation to .desktop

* Mon Oct 13 2003 Bruno Postle <bruno@postle.net>
- build of hugin-0-3-beta release, sorry no time to fix numbering.

* Sat Oct 04 2003 Bruno Postle <bruno@postle.net>
- new build from cvs, patch0 adds a shortcut to gnome/kde menu

* Thu Sep 25 2003 Bruno Postle <bruno@postle.net>
- build now requires panorama tools include headers.

* Wed Aug 06 2003 Bruno Postle <bruno@postle.net>
- new build from cvs. po/mo files still not getting built

* Sat Aug 02 2003 Bruno Postle <bruno@postle.net>
- new build from cvs, panoviewer now gets built by default. removed
  useless .po installation.

* Sat Jul 26 2003 Bruno Postle <bruno@postle.net>
- new build from cvs, panoviewer built as well

* Sat May 24 2003 Bruno Postle <bruno@postle.net>
- build of wxGTK version

* Sat May 10 2003 Bruno Postle
- Initial RPM release.
