Name:    engauge-digitizer
Summary: Convert graphs or map files into numbers
Version: 12.9.1
Release: %autorelease
License: GPL-2.0-or-later
URL:     https://akhuettel.github.io/%{name}/
Source0: https://github.com/markummitchell/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Epoch:   1

## Proposed in https://bugzilla.redhat.com/show_bug.cgi?id=1182409
Source1: %{name}.metainfo.xml
Source2: %{name}.svg
Source3: %{name}-with-name.svg

## Fix variables for using correctly pkgconfig
Patch0: %{name}-fix_path_variables.patch

## Main building
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: fftw-devel
BuildRequires: log4cpp-devel
BuildRequires: desktop-file-utils
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-doctools

%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires: libappstream-glib
BuildRequires: openjpeg2-devel
BuildRequires: poppler-qt6-devel
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
Requires: %{name}%{?_isa} = 1:%{version}-%{release}

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
BuildRequires: texlive-epstopdf
BuildRequires: ghostscript
BuildRequires: doxygen

%description doc
HTML documentation of %{name}.

%prep
%autosetup -N -n %{name}-%{version}
%patch -P 0 -p1 -b .backup

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
%if 0%{?fedora} || 0%{?rhel} > 9
export OPENJPEG_INCLUDE=`pkg-config --cflags libopenjp2 | sed 's/-I//'`
export OPENJPEG_LIB=%{_libdir}
export POPPLER_INCLUDE=`pkg-config --cflags poppler-qt6 | sed 's/-I//'`
export POPPLER_LIB=%{_libdir}
%{qmake_qt6} engauge.pro "CONFIG+=pdf jpeg2000" QT_SELECT=qt6 \
%else
%{qmake_qt5} engauge.pro "CONFIG+=log4cpp_null" QT_SELECT=qt5 \
%endif
 DEFINES+=HELPDIR=%{_datadir}/doc/%{name}/help
%make_build

## Build HELP files
pushd help
%{_libdir}/qt6/libexec/qhelpgenerator engauge.qhcp -o engauge.qhc
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

install -p -m 755 bin/Engauge %{buildroot}%{_bindir}

pushd samples
install -p -m 644 *.gif *.jp* *.png *.bmp %{buildroot}%{_datadir}/%{name}-%{version}/samples/
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
Exec=Engauge
MimeType=text/plain
Categories=Science;DataVisualization;
Icon=/usr/share/pixmaps/engauge-digitizer.xpm
Keywords=Analog-Digital Converter;
EOF

%if 0%{?fedora}
desktop-file-edit \
 --set-icon=%{name}-with-name --set-key=Exec --set-value=Engauge \
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
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%endif

%files
%doc README.md help
%license LICENSE
%{_bindir}/Engauge
%{_datadir}/pixmaps/%{name}*.svg
%if 0%{?fedora}
%{_metainfodir}/*.metainfo.xml
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-%{version}/
%exclude %{_datadir}/%{name}-%{version}/samples

%files samples
%doc samples/README
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/samples

%files doc
%doc README.md doc/doxygen/html
%license LICENSE

%changelog
%autochangelog
