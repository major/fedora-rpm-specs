Name:    engauge-digitizer
Summary: Convert graphs or map files into numbers
Version: 12.1
Release: 17%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://markummitchell.github.io/%{name}/
Source0: https://github.com/markummitchell/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Epoch: 1

## Proposed in https://bugzilla.redhat.com/show_bug.cgi?id=1182409
Source1: %{name}.appdata.xml
Source2: %{name}.svg
Source3: %{name}-with-name.svg

## Fix variables for using correctly pkgconfig
Patch0: %{name}-fix_path_variables.patch

## Main building
BuildRequires: gcc, gcc-c++
BuildRequires: fftw-devel, log4cpp-devel, desktop-file-utils
BuildRequires: qt5-qtbase-devel, qt5-qttools-devel
%{?fedora:BuildRequires: pkgconf-pkg-config}
%{?rhel:BuildRequires: pkgconfig}

%if 0%{?fedora}
BuildRequires: libappstream-glib
BuildRequires: openjpeg2-devel
BuildRequires: poppler-qt5-devel
%endif

%description
The Engauge Digitizer tool accepts image files
(like PNG, JPEG and TIFF) containing graphs,
and recovers the data points from those graphs.
The resulting data points are usually used as input
to other software applications.
Conceptually, Engauge Digitizer is the opposite of
a graphing tool that converts data points to graphs.
The process is shown below - an image file is imported,
digitized within Engauge, and exported as a table of
numeric data to a text file.
Work can be saved into an Engauge DIG file.

New features already added to Engauge:

-  Grid lines are displayed for fine adjustments of the axis points
   that define the coordinate systems
-  Automated line and point extraction rapidly digitizes data
-  Image processing for separating important details from background information
-  Undo/redo of all operations means recovering from mistakes and experimenting
   with options is painless
-  Installers for Windows and OSX operating systems, and repository packages for
   Linux make installation easy
-  Wizard provides an interactive tutorial to explain the basic steps
-  Wizard creates a checklist guide to interactively leads user through steps from
   file import to file export
-  Cubic spline interpolation between points gives more accurate curves with
   fewer points
-  Axes Checker briefly highlights the axes when they are defined or modified,
   to reveal entry mistakes
-  Graph coordinates can be specified as date and time values, or as degrees,
   minutes and seconds
-  File import and data export by drag-and-drop and copy/paste
-  Test suite for regression testing minimizes code breakage as
   new features are added
-  Multiple coordinate systems in the same image can be digitized in
   advanced mode
-  Axes with only one known coordinate (floating axes) can be digitized in
   advanced mode
-  Geometry Window displays geometric information about the selected curve
-  Curve Fitting Window fits a polynomial function to the selected curve


%package samples
Summary: Sample files for %{name}
BuildArch: noarch
%description samples
This package contains several sample image files that may be imported into
Engauge Digitizer (http://digitizer.sourceforge.net).

These files are listed below, with comments:

 - corners.png - Graph that lots of corners that would be painful
   to digitize manually
 - gridlines.gif - Graph with gridlines that are easily removed by Engauge
 - gridlines_log.gif - Another graph with gridlines that are easily
   removed by Engauge
 - gridlines_log.src - Creates gridlines_log.gif in gnuplot using 'load'
   command (not an image!)
 - inverse.jpg - Image of y/x function
 - inverse.png - Same as inverse.jpg but in png format
 - linlog.jpg - Graph with linear/logarithmic coordinates
 - linlog.png - Same as linlog.jpg but in png format
 - loglin.png - Graph with logarithmic/linear coordinates
 - loglog.png - Graph with logarithmic/logarithmic coordinates
 - normdist.jpg - Graph of normal distribution
 - normdist.png - Same as normdist.jpg but in png format
 - pointmatch.jpg - Graph with fuzzy points for playing with Point Match
   feature of Engauge
 - pointplot.bmp - Graph with points that are easily captured by Point Match
   feature of Engauge, if the Discretize settings are set to
   "Intensity 90 to 99"
   for the triangles, and "Intensity 10 to 50" for the diamonds
 - polarcircles.jpg - Polar plot for experimenting. No coordinates are
   displayed, so not very useful
 - polarplot.jpg - Polar plot with cardioid pattern
 - polarplot.png - Same as polarplot.jpg but in png format
 - testcase.jpg - Simple graph that serves as an excellent starting point
   for the new user
 - testcase.png - Same as testcase.jpg but in png format
 - testcoords.jpg - Advanced graph used by developers to check the affine
   transformations in Engauge
 - testcoords.sxd - Open Office document used to create testcoords.jpg
   (not an image!)
 - usgs.png - Fictional map loosely based on U.S. Geological Survey
   topographic maps

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
BuildRequires: texlive-epstopdf, ghostscript
BuildRequires: doxygen
BuildRequires: make
%description doc
HTML documentation of %{name}.

%prep
%autosetup -p0 -n %{name}-%{version}

## Remove default -O1 optimization
sed -e 's|-O1||g' -i engauge.pro

## Set fftw library link-path
sed -e 's|-L/$$(FFTW_HOME)/lib|-L$$(FFTW_HOME)/%{_libdir}|g' -i engauge.pro

## Remove post-link task
sed --in-place '/QMAKE_POST_LINK/d' engauge.pro

## Remove rpath link
sed --in-place '/QMAKE_LFLAGS/d' engauge.pro

## Remove spurious executable permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.cpp" -exec chmod 0644 '{}' \;

%build
export ENGAUGE_RELEASE=1
%if 0%{?fedora}
export OPENJPEG_INCLUDE=`pkg-config --cflags libopenjp2 | sed 's/-I//'`
export OPENJPEG_LIB=%{_libdir}
export POPPLER_INCLUDE=`pkg-config --cflags poppler-qt5 | sed 's/-I//'`
export POPPLER_LIB=%{_libdir}
%{qmake_qt5} engauge.pro "CONFIG+=pdf jpeg2000" QT_SELECT=qt5 \
%else
%{qmake_qt5} engauge.pro "CONFIG+=log4cpp_null" QT_SELECT=qt5 \
%endif
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS -pie -Wl,-z,now" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS -pie -Wl,-z,now" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS -pie -Wl,-z,now" \
 DEFINES+=HELPDIR=%{_datadir}/doc/%{name}/help
%make_build

## Build HELP files
pushd help
qcollectiongenerator-qt5 engauge.qhcp -o engauge.qhc
rm -f build build.*
rm -rf .gitignore
popd

## Build HTML/Latex documentation files
pushd src
doxygen
popd

%install
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}/samples
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}/img
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_metainfodir}
mkdir -p %{buildroot}%{_bindir}

install -p -m 755 bin/engauge %{buildroot}%{_bindir}

pushd samples
install -p -m 644 *.gif *.jp* *.png *.bmp %{buildroot}%{_datadir}/%{name}-%{version}/samples
popd

install -p -m 644 src/img/* %{buildroot}%{_datadir}/%{name}-%{version}/img
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/
%if 0%{?fedora}
install -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
%endif

## Make a .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Engauge Digitizer %{version}
Type=Application
Comment=Extract data from graphs
TryExec=engauge
Exec=engauge
MimeType=text/plain
Categories=Education;Science;DataVisualization;
Icon=/usr/share/pixmaps/engauge-digitizer.xpm
Keywords=Analog-Digital Converter;
EOF

%if 0%{?fedora}
desktop-file-edit \
 --set-icon=%{name}-with-name \
 --set-key=Keywords --set-value="analog;digital;converter;" %{buildroot}%{_datadir}/applications/%{name}.desktop
%else

sed -e \
 's|Icon=%{_datadir}/pixmaps/%{name}.xpm|Icon=%{name}-with-name|g' \
 -i %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -e \
 's|Keywords=Analog-Digital Converter;|Keywords=analog;digital;converter;|g' \
 -i %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%files
%doc README.md help
%license LICENSE
%{_bindir}/engauge
%{_datadir}/pixmaps/%{name}*.svg
%if 0%{?fedora}
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-%{version}/
%exclude %{_datadir}/%{name}-%{version}/samples

%files samples
%doc samples/README
%license LICENSE
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/samples

%files doc
%doc README.md doc/doxygen/html
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:12.1-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1:12.1-9
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 1:12.1-4
- Drop bogus runtime dependency (rhbz#1797268)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1:12.1-2
- Rebuild for poppler-0.84.0

* Sat Nov 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:12.1-1
- Release 12.1

* Sat Aug 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:12-2
- SPEC file enhancements

* Fri Aug 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:12-1
- Release 12.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:11.3-1
- Release 11.3

* Thu May 02 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:11.2-1
- Release 11.2

* Thu Mar 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:10.12-1
- Release 10.12

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:10.11-1
- Update to 10.11

* Mon Aug 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:10.9-1
- Update to 10.9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:10.7-1
- Update to 10.7

* Sat May 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:10.6-1
- Update to 10.6

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:10.4-4
- Add gcc gcc-c++ BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:10.4-2
- Appdata file moved into metainfo data directory

* Sat Oct 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:10.4-1
- Update to 10.4

* Mon Aug 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:10.2-1
- Update to 10.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:10.1-1
- Update to 10.1

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Apr 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:10.0-1
- Update to 10.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Antonio Trande <sagitterATfedoraproject.org> 1:9.8-2
- Conformed to new rules for scriptlets

* Sun Dec 11 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.8-1
- Update to 9.8

* Thu Dec 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.7-1
- Update to 9.7
- qgnomeplatform required on f25+

* Tue Nov 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.6-1
- Update to 9.6

* Mon Oct 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.5-1
- Update to 9.5

* Sat Oct 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.4-1
- Update to 9.4

* Tue Sep 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.3-1
- Update to 9.3

* Sun Aug 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.2-1
- Update to 9.2

* Sun Jul 31 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.1-1
- Update to 9.1

* Tue Jul 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.0-2
- Fix appdata file's tags

* Tue Jul 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:9.0-1
- Update to 9.0

* Thu Jun 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:8.2-1
- Update to 8.2

* Tue May 31 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1-1
- Update to 8.1

* Mon Apr 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:7.2-1
- Update to 7.2

* Thu Mar 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:7.1-1
- Update to 7.1

* Sun Mar 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:7.0-2
- Update of appdata file

* Sun Mar 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:7.0-1
- Update to 7.0

* Thu Feb 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 1:6.2-4.20160204gitb6ad5b
- Update to commit #b6ad5b

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1:6.2-2
- use %%qmake_qt5 macro (instead of settings flags by hand)

* Tue Dec 01 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6.2-1
- Update to 6.2

* Sun Nov 08 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6.1-2
- Excluding PPC arch on EPEL6 because of missing BR packages (log4cpp)

* Sat Oct 31 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6.1-1
- Update to 6.1

* Sat Oct 24 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6.0-1
- First release
- Build release version
- Activated jpeg200 support

* Wed Oct 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6-0.4.20151011git77e64e
- Commit #77e64e
- Old Transpose tool obsoleted

* Tue Sep 29 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6-0.3.20150928git4b8703
- Commit #4b8703

* Mon Sep 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6-0.2.20150928gita25102
- Commit #a25102
- Built HTML docs
- Tests performed

* Thu Sep 24 2015 Antonio Trande <sagitter@fedoraproject.org> - 1:6-0.1.20150921git4f0c92
- Bump to the new Engauge6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-10.20150115git28de7d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.2-9.20150115git28de7d
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.2-8.20150115git28de7d
- Fixed Keywords key in .desktop file

* Thu Jan 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.2-7.20150115git28de7d
- Included files proposed in bz#1182409

* Thu Jan 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.2-6.20150115git28de7d
- Update to commit 28de7d
- Package appdata and SVG files
- data sub-package incorporated in the main one
- Used the new macro %%license

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Antonio Trande <sagitter@fedoraproject.org> 5.2-3
- Data files splitted into a noarch -data subpackage
- .h/.cpp files not packaged anymore

* Tue Nov 12 2013 Antonio Trande <sagitter@fedoraproject.org> 5.2-2
- Fix 'src/pointset.cpp' compilation error in EPEL
- Defined Qt3/Qt4 qmake
- Fix BR Qt4 for EPEL
- RPM_OPT_FLAGS fixed without patches 

* Sun Nov 10 2013 Antonio Trande <sagitter@fedoraproject.org> 5.2-1
- First package
