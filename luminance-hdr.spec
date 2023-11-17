Name:           luminance-hdr
Version:        2.6.1.1
Release:        %autorelease
Summary:        GUI that provides a complete workflow for HDR imaging

# The entire source is GPL-2.0-or-later, except:
#
# GPL-2.0-only:
#   src/HelpBrowser/schelptreemodel.{cpp,h} (before patching)
#   src/HelpBrowser/treeitem.{cpp,h} (before patching)
#   src/HelpBrowser/treemodel.{cpp,h} (before patching)
#
#   These files are patched with changes from upstream PR#250, after which they
#   are BSD-3-Clause instead of GPL-2.0-only. This resolves the license
#   incompatibility with GPLv3+
#   (https://github.com/LuminanceHDR/LuminanceHDR/issues/247). Without the
#   patches, we would need to remove these files in %%prep and patch out the
#   help browser.
#
# GPL-3.0-or-later:
#   src/StopWatch.h
#   src/gauss.h
#   src/mytime.h
#   src/noncopyable.h
#   src/opthelper.h
#   src/Libpfs/rt_algo.{cpp,h}
#   src/MainCli/ezETAProgressBar.hpp
#
# LGPL-2.1-or-later:
#   src/HdrCreation/fusionoperator.{cpp,h}
#   src/HdrCreation/weights.h
#   src/Libpfs/array2d.{hxx,h}
#   src/Libpfs/channel.{cpp,h}
#   src/Libpfs/fixedstrideiterator.h
#   src/Libpfs/frame.{cpp,h}
#   src/Libpfs/pfs.h
#   src/Libpfs/strideiterator.h
#   src/Libpfs/tag.{cpp,h}
#   src/Libpfs/colorspace/colorspace.{cpp,h}
#   src/Libpfs/exif/exifdata.{cpp,hpp}
#   src/Libpfs/manip/shift.{cpp,hxx,h}
#   src/Libpfs/utils/dotproduct.{hxx,h}
#   src/Libpfs/utils/minmax.{hxx,h}
#   src/Libpfs/utils/numeric.{hxx,h}
#
# BSD-3-Clause:
#   src/HelpBrowser/schelptreemodel.{cpp,h} (after patching)
#   src/HelpBrowser/treeitem.{cpp,h} (after patching)
#   src/HelpBrowser/treemodel.{cpp,h} (after patching)
#   src/UI/FlowLayout.cpp
#
# MIT:
#   src/contrib/qtwaitingspinner/QtWaitingSpinner.{cpp,h}
#
# BSL-1.0: (see https://github.com/LuminanceHDR/LuminanceHDR/issues/239)
#   src/helpersse2.h
#   src/sleef.c
#   src/sleefsseavx.c
#
# CC0-1.0:
#   net.sourceforge.qtpfsgui.LuminanceHDR.appdata.xml
#
# Note that CC0-1.0 is allowed only for content, such as this AppData XML file.
License:        %{shrink:
                GPL-2.0-only AND
                GPL-3.0-or-later AND
                LGPL-2.1-or-later AND
                BSD-3-Clause AND
                MIT AND
                BSL-1.0 AND
                CC0-1.0
                }
# Additionally, the following are only build system files and do not contribute
# to the License field:
#
# BSL-1.0:
#   build_files/Modules/GetGitRevisionDescription.cmake{,.in}
URL:            http://qtpfsgui.sourceforge.net/
%global forgeurl https://github.com/LuminanceHDR/LuminanceHDR/
Source0:        %{forgeurl}/archive/v.%{version}/luminance-hdr-%{version}.tar.gz
# https://github.com/LuminanceHDR/LuminanceHDR/issues/242
Source1:        luminance-hdr.1
Source2:        luminance-hdr-cli.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# https://github.com/LuminanceHDR/LuminanceHDR/issues/239
Patch:          luminance-hdr-2.6.1.1-sleef-boost-license.patch

# https://github.com/LuminanceHDR/LuminanceHDR/issues/240
Patch:          luminance-hdr-2.6.1.1-external-librtprocess.patch

# This patch series is a backport of upstream PR#250
# (https://github.com/LuminanceHDR/LuminanceHDR/pull/250). It resolves the
# following issue, allowing us to avoid removing the help browser:
#
# License incompatibility
# https://github.com/LuminanceHDR/LuminanceHDR/issues/247
Patch:          0001-Update-help-tree-files-from-Scribus-SVN-24770.patch
Patch:          0002-Fix-an-include-path-in-schelptreemodel.h.patch
Patch:          0003-Comment-out-Q_OBJECT-in-ScHelpTreeModel-and-TreeMode.patch

# In 2.6.1.1, wrong include in src/Common/init_fftw.h
# https://github.com/LuminanceHDR/LuminanceHDR/issues/252
# Fix include for std::mutex in init_fftw.h
# https://github.com/LuminanceHDR/LuminanceHDR/pull/253
Patch:          %{forgeurl}/pull/253.patch

# Fix deprecated top-level developer_name in AppData XML
# https://github.com/LuminanceHDR/LuminanceHDR/pull/277
Patch:          %{forgeurl}/pull/277.patch

# Fix build with >=exiv2-0.28.0, raise minimum to 0.27.0
# https://github.com/LuminanceHDR/LuminanceHDR/pull/279
Patch:          0001-Fix-build-with-exiv2-0.28.0-raise-minimum-to-0.27.0.patch

BuildRequires:  cmake
# We choose to use the ninja backend instead of the make backend. Either works.
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  desktop-file-utils
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

# INSTALL.md:
# To compile Luminance HDR your system will need a set of tools and code
# libraries called "dependencies". The following is a list of dependencies
# needed to compile the latest version of Luminance HDR:
# - [Qt5](https://www.qt.io/), the widget toolkit used by the graphical user
#   interface (GUI).
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  qt5-qtwebengine-devel
%else
BuildRequires:  qt5-qtwebkit-devel
%endif
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
# - [Exiv2](https://www.exiv2.org/), used to read and write image metadata
#   (Exif, IPTC, XMP).
BuildRequires:  exiv2-devel
# - [Little CMS](http://www.littlecms.com/), LCMS2 is used for color
#   management.
BuildRequires:  lcms2-devel
# - [libjpeg-turbo](https://libjpeg-turbo.org/) (or libjpeg), used to read and
#   write JPEG files.
BuildRequires:  libjpeg-devel
# - [LibTIFF](http://www.libtiff.org/), used to read and write TIFF files.
BuildRequires:  libtiff-devel
# - [libpng](http://www.libpng.org/pub/png/libpng.html), used to read and write
#   PNG files.
BuildRequires:  libpng-devel
# - [LibRaw](https://www.libraw.org/), used to read raw files.
BuildRequires:  LibRaw-devel
# - [OpenEXR](http://www.openexr.com/), used to read and write high dynamic
#   range EXR files. Some distributions refer to the package as `ilmbase`.
#
#   Upstream does not support OpenEXR 3.x, and a nontrivial patch may be
#   required. See https://bugzilla.redhat.com/show_bug.cgi?id=1968167 and
#   https://github.com/LuminanceHDR/LuminanceHDR/issues/244. For now, we must
#   use the OpenEXR 2.x compatibility package. (In the long term, this package
#   will risk retirement if upstream does not resume active development.)
BuildRequires:  openexr2-devel
# - [CFITSIO](https://heasarc.gsfc.nasa.gov/fitsio/), an optional library for
#   reading and writing FITS files, commonly used by the astrophotographer
#   community.
BuildRequires:  cfitsio-devel
# - [FFTW](www.fftw.org), used for computing discrete Fourier transforms.
#   Luminance HDR requires the single-precision "float" version of FFTW3,
#   usually called `fftw3f` or `fftw-3-single` on MacPorts.
BuildRequires:  fftw-devel
# - [Boost](https://www.boost.org/), a set of C++ support libraries.
BuildRequires:  boost-devel
# - [GNU Scientific Library](https://www.gnu.org/software/gsl/), GSL is used by
#   the Mantiuk08 tone mapping operator.
BuildRequires:  gsl-devel
# - [Eigen3](http://eigen.tuxfamily.org/), a C++ template library required by
#   by the Lischinski tone mapping operator.
BuildRequires:  eigen3-devel

BuildRequires:  librtprocess-devel

BuildRequires:  gtest-devel

Obsoletes:      qtpfsgui < 2.2.0
Provides:       qtpfsgui = %{version}-%{release}

# https://github.com/LuminanceHDR/LuminanceHDR/issues/241
# Original version is unclear
Provides:       bundled(pfstools)
# Version based on searching commit messages for “pfstmo”; could be out of
# date.
Provides:       bundled(pfstmo) = 2.0.5

# A few routines from sleef are included; cannot build with upstream/system
# sleef as there are downstream modifications. It is not clear which version of
# sleef was used as the basis for the fork.
Provides:       bundled(sleef)

Requires:       luminance-hdr-data = %{version}-%{release}

%global app_id net.sourceforge.qtpfsgui.LuminanceHDR

%description
Luminance HDR is a graphical user interface (based on the Qt5 toolkit) that
provides a complete workflow for HDR imaging.

Supported HDR formats:

  • OpenEXR (extension: exr)
  • Radiance RGBE (extension: hdr)
  • Tiff formats: 16bit, 32bit (float) and LogLuv (extension: tiff)
  • Raw image formats (extension: various)
  • PFS native format (extension: pfs)

Supported LDR formats:

  • JPEG, PNG, PPM, PBM, TIFF, FITS

Supported features:

  • Create an HDR file from a set of images (JPEG, TIFF 8bit and 16bit, RAW) of
    the same scene taken at different exposure settings
  • Save and load HDR files
  • Rotate and resize HDR files
  • Tonemap HDR images
  • Projective Transformations
  • Copy EXIF data between sets of images
  • Supports internationalization

Raw image formats are supported - and treated as HDR - thanks to LibRAW.

The code is in part based on the existing open source packages:

  • “pfstools”, “pfstmo” and “pfscalibration” by Grzegorz Krawczyk and Rafal
    Mantiuk
  • “qpfstmo”, by Nicholas Phillips.

Without their contribution all of this would have not been possible.


%package data
Summary:        Architecture-independent data files for luminance-hdr
License:        GPL-2.0-or-later

BuildArch:      noarch

# For icon directory:
Requires:       hicolor-icon-theme
# For unbundled hdrhtml:
Requires:       pfstools

%description data
Architecture-independent data files for luminance-hdr, such as HTML help and
translations.


%prep
%autosetup -n LuminanceHDR-v.%{version} -p1

# Just in case the bundled librtprocess shows up in the tarball:
rm -rf librtprocess

# https://github.com/LuminanceHDR/LuminanceHDR/pull/236
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(TestPoissonSolver\b.*pfstmo)'\
'[[:blank:]]*$/\1 common/' \
    test/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/pull/237
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfstmo[[:blank:]]+)(Qt5::)/\1pfs \2/' \
     src/TonemappingOperators/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/issues/240
# https://github.com/LuminanceHDR/LuminanceHDR/pull/238
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfs[[:blank:]]+)(Qt5::)/\1rtprocess \2/' \
     src/Libpfs/CMakeLists.txt

# Remove bundled copy of hdrhtml from pfstools package; let the build system
# install an empty directory, then replace it with a symbolic link to the
# pfstools copy.
rm -rf hdrhtml/*


%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_UNIT_TEST:BOOL=ON -GNinja
%cmake_build


%install
%cmake_install

# Upstream installs AUTHORS, Changelog, LICENSE, and README.md. We install
# documentation and license files with the %%doc and %%license macros instead,
# putting them in the usual locations favored by Fedora.
rm -rvf '%{buildroot}%{_datadir}/luminance-hdr/doc'

# Install mimeinfo file
install -t '%{buildroot}/%{_datadir}/mime/packages' -D -p -m 0644 \
    luminance-hdr.xml

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications \
    %{app_id}.desktop

# We need to move the AppData file to the correct location. We also choose to
# rename the file from upstream using the legacy .appdata.xml name to the
# current .metainfo.xml used for AppData. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/.
install -d '%{buildroot}%{_metainfodir}'
mv -v '%{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml' \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE1}' '%{SOURCE2}'

%find_lang lang --with-qt

rm -rvf '%{buildroot}%{_datadir}/luminance-hdr/hdrhtml'
ln -s ../pfstools '%{buildroot}%{_datadir}/luminance-hdr/hdrhtml'


%check
# https://github.com/LuminanceHDR/LuminanceHDR/issues/154
x='Mantiuk06Pyramid'
%ifarch %{ix86}
# TestPoissonSolver sometimes hangs on this arch only. It exists only for
# multilib on x86_64 anyway, so there is very little reason to try to find a
# solution.
x="${x}|PoissonSolver"
%endif
%ctest --exclude-regex "^Test(${x})\$"


%files
%doc AUTHORS
%doc BUGS
%doc Changelog
%doc README.i18n
%doc README.md
%doc TODO

%{_bindir}/luminance-hdr
%{_bindir}/luminance-hdr-cli

# While the following are technically arch-independent data files, they have
# configuration-like functionality and should not be installed without the
# actual application, so they belong here instead of in -data.

# Shared directory ownership with shared-mime-info
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/luminance-hdr.xml

%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop


%files data -f lang.lang
%license LICENSE LICENSE.txt

%dir %{_datadir}/luminance-hdr

# Relative symbolic link to %%{_datadir}/pfstools
%{_datadir}/luminance-hdr/hdrhtml
# A backed-up bundled hdrhtml directory from a previous upgrade may be present:
%ghost %{_datadir}/luminance-hdr/hdrhtml.rpmmoved

%{_datadir}/luminance-hdr/help/

# Contents of this directory are listed by %%find_lang
%dir %{_datadir}/luminance-hdr/i18n

%{_datadir}/icons/hicolor/48x48/apps/luminance-hdr.png

%{_mandir}/man1/luminance-hdr.1*
%{_mandir}/man1/luminance-hdr-cli.1*


%changelog
%autochangelog
