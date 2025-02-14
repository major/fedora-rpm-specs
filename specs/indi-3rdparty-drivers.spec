%global aagcloudwatcher_ng_pkg indi-3rdparty-aagcloudwatcher-ng
%global ahpxc_pkg indi-3rdparty-ahp-xc
%global aok_pkg indi-3rdparty-aok
%global apogee_pkg indi-3rdparty-apogee
%global avalon_pkg indi-3rdparty-avalon
%global avalonud_pkg indi-3rdparty-avalonud
%global beefocus_pkg indi-3rdparty-beefocus
%global bresser_pkg indi-3rdparty-bresserexos2
%global caux_pkg indi-3rdparty-celestronaux
%global eqmod_pkg indi-3rdparty-eqmod
%global fli_pkg indi-3rdparty-fli
%global gphoto_pkg indi-3rdparty-gphoto
%global gpsd_pkg indi-3rdparty-gpsd
%global gpsnmea_pkg indi-3rdparty-gpsnmea
%global lunatico_pkg indi-3rdparty-armadillo-platypus
%global maxdome_pkg indi-3rdparty-maxdome
%global mgen_pkg indi-3rdparty-mgen
%global nexdome_pkg indi-3rdparty-nexdome
%global nightscape_pkg indi-3rdparty-nightscape
%global ocs_pkg indi-3rdparty-ocs
%global orion_pkg indi-3rdparty-orionssg3
%global rolloffino_pkg indi-3rdparty-rolloffino
%global rtklib_pkg indi-3rdparty-rtklib
%global shelyak_pkg indi-3rdparty-shelyak
%global starbook_pkg indi-3rdparty-starbook
%global starbookten_pkg indi-3rdparty-starbook-ten
%global sx_pkg indi-3rdparty-sx
%global talon6_pkg indi-3rdparty-talon6
%global webcam_pkg indi-3rdparty-webcam
%global weewx_pkg indi-3rdparty-weewx-json

%global indi_version 2.1.2

# Define boolean to quickly set option and dependencies for
# unit tests
%global build_tests 1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Name:           indi-3rdparty-drivers
Version:        %{indi_version}
Release:        %autorelease
Summary:        INDI 3rdparty drivers
License:        LGPL-2.1-or-later
URL:            http://indilib.org

# Tar is generated from the huge all-in-one tar from INDI
# by using ./generate-drivers-tarball.sh %%{version}
# The main source from upstream is at
# https://github.com/indilib/indi-3rdparty/archive/refs/tags/v%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.zst
Source1:        generate-drivers-tarball.sh

# Patch for building with libahp-xc >=1.4.4
Patch:          ahp-xc-1.4.4.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  indi-3rdparty-libapogee-devel = %{version}
BuildRequires:  indi-3rdparty-libfli-devel = %{version}
BuildRequires:  libnova-devel
BuildRequires:  libindi = %{indi_version}
BuildRequires:  websocketpp-devel
BuildRequires:  zlib-devel

BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libindi) = %{version}
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libusb-1.0)

%if 0%{?fedora}
%global system_jsonlib ON
BuildRequires: json-static
%else
%global system_jsonlib OFF
%endif

%if 0%{?build_tests}
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
%global tests ON
%else
%global tests OFF
%endif

# We want this metapackage to install all drivers at once.
# Just use weak dependencies to avoid possible errors.
Recommends:     %{aagcloudwatcher_ng_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{ahpxc_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{aok_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{apogee_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{avalon_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{avalonud_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{beefocus_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{bresser_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{caux_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{eqmod_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{fli_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{gphoto_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{gpsd_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{gpsnmea_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{lunatico_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{maxdome_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{mgen_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{nexdome_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{nightscape_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{ocs_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{orion_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{rolloffino_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{rtklib_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{shelyak_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{starbook_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{starbookten_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{sx_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{talon6_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{webcam_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{weewx_pkg}%{?_isa} = %{version}-%{release}


%description
This is a metapackage for installing all INDI 3rdparty drivers
at once. You probably don't want to install everything, but just pick
the drivers you need from the appropriate subpackage.

We currently ship the following drivers:
- %{aagcloudwatcher_ng_pkg}
- %{ahpxc_pkg}
- %{aok_pkg}
- %{apogee_pkg}
- %{avalon_pkg}
- %{avalonud_pkg}
- %{beefocus_pkg}
- %{bresser_pkg}
- %{caux_pkg}
- %{eqmod_pkg}
- %{fli_pkg}
- %{gphoto_pkg}
- %{gpsd_pkg}
- %{gpsnmea_pkg}
- %{lunatico_pkg}
- %{maxdome_pkg}
- %{mgen_pkg}
- %{nexdome_pkg}
- %{nightscape_pkg}
- %{ocs_pkg}
- %{orion_pkg}
- %{rolloffino_pkg}
- %{rtklib_pkg}
- %{shelyak_pkg}
- %{starbook_pkg}
- %{starbookten_pkg}
- %{sx_pkg}
- %{talon6_pkg}
- %{webcam_pkg}
- %{weewx_pkg}


%package -n %{aagcloudwatcher_ng_pkg}
License:        GPL-3.0-or-later
Summary:        INDI driver for the AAG Cloud Watcher NG

Requires:       libindi = %{indi_version}

Provides:       indi-aagcloudwatcher = %{version}-%{release}
Obsoletes:      indi-aagcloudwatcher <= 1.9.0-3

%description -n %{aagcloudwatcher_ng_pkg}
INDI driver for the AAG Cloud Watcher NG.

%package -n %{aagcloudwatcher_ng_pkg}-doc
Summary:        Documentation files for %{aagcloudwatcher_ng_pkg}
Requires:       %{aagcloudwatcher_ng_pkg} = %{version}-%{release}
BuildArch:      noarch

%description -n %{aagcloudwatcher_ng_pkg}-doc
Documentation files of the INDI driver for the AAG Cloud Watcher NG.


%package -n %{ahpxc_pkg}
License:        LGPL-2.1-or-later
Summary:        The INDI driver for AHP XC correlators

BuildRequires:  libahp-xc-devel
Requires:       libindi = %{indi_version}

%description -n %{ahpxc_pkg}
The INDI driver for AHP XC correlators.


%package -n %{aok_pkg}
License:        LGPL-2.1-or-later
Summary:        The INDI driver for AOK Skywalker mounts

Requires:       libindi = %{indi_version}

%description -n %{aok_pkg}
The INDI driver to control the AOK Skywalker mounts.


%package -n %{apogee_pkg}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Summary:        The INDI driver for Apogee Alta (U & E) line of CCDs

Requires:       libindi = %{indi_version}

Provides:       indi-apogee = 1:%{version}-%{release}
Obsoletes:      indi-apogee <= 1:1.9.3-2

%description -n %{apogee_pkg}
The INDI (Instrument Neutral Distributed Interface) driver for Apogee 
Alta (U & E) line of CCDs.


%package -n %{avalon_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for Avalon Instruments mounts

Requires:       libindi = %{indi_version}

%description -n %{avalon_pkg}
INDI driver to control Avalon Instruments mounts with StarGO control.


%package -n %{avalonud_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for AvalonInstruments StarGO+ and StarGO2

BuildRequires:  pkgconfig(libzmq)
Requires:       libindi = %{indi_version}

%description -n %{avalonud_pkg}
This package provides the INDI driver for mounts equipped with
AvalonInstruments StarGO+ and StarGO2 controllers.


%package -n %{beefocus_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for Beefocus

Requires:       libindi = %{indi_version}

%description -n %{beefocus_pkg}
INDI driver for Beefocus.


%package -n %{bresser_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver for Bresser Exos II GoTo

Requires:       libindi = %{indi_version}

%description -n %{bresser_pkg}
INDI driver for Bresser Exos II GoTo Telescope Mount.

%package -n %{bresser_pkg}-doc
Summary:        Documentation files for %{bresser_pkg}
Requires:       %{bresser_pkg} = %{version}-%{release}
BuildArch:      noarch

%description -n %{bresser_pkg}-doc
Documentation files of the INDI driver for Bresser Exos II GoTo
Telescope Mount.


%package -n %{caux_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for Celestron AUX

Requires:       libindi = %{indi_version}

%description -n %{caux_pkg}
INDI driver for Celestron AUX protocol.


%package -n %{eqmod_pkg}
License:        GPL-3.0-or-later AND GPL-2.0-or-later
Summary:        INDI driver providing support for SkyWatcher Protocol

Requires:       libindi = %{indi_version}

Provides:       indi-eqmod = %{version}-%{release}
Obsoletes:      indi-eqmod <= 1.9.3-2

%description -n %{eqmod_pkg}
INDI driver adding support for telescope mounts using the 
SkyWatcher protocol.


%package -n %{fli_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for Finger Lakes Instruments CCDs and focusers

Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{fli_pkg}
INDI driver adding support for Finger Lakes Instruments CCDs
and focusers.


%package -n %{gphoto_pkg}
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        INDI driver providing support for gPhoto

Requires:       libindi = %{indi_version}
Requires:       udev

Provides:       indi-gphoto = %{version}-%{release}
Obsoletes:      indi-gphoto <= 1.9.3-2

%description -n %{gphoto_pkg}
INDI driver using gPhoto to add support for many cameras to INDI.
This includes many DSLR, e.g. Canon or Nikon.


%package -n %{gpsd_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver providing support for gpsd

Requires:       libindi = %{indi_version}

%description -n %{gpsd_pkg}
INDI driver providing support for gpsd.


%package -n %{gpsnmea_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver providing support for gps NMEA

Requires:       libindi = %{indi_version}

%description -n %{gpsnmea_pkg}
INDI driver providing support for gps NMEA.


%package -n %{lunatico_pkg}
License:        LGPL-2.1-or-later
Summary:        The INDI driver for Lunatico Astronomia controllers

Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{lunatico_pkg}
The INDI driver for Lunatico Astronomia Armadillo and
Platypus controllers.


%package -n %{maxdome_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for MaxDome II

Requires:       libindi = %{indi_version}

%description -n %{maxdome_pkg}
INDI driver for MaxDome II.


%package -n %{mgen_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver for Lacerta MGen autoguider

Requires:       libindi = %{indi_version}

%description -n %{mgen_pkg}
INDI driver for Lacerta MGen autoguider.


%package -n %{nexdome_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver for NexDome

Requires:       libindi = %{indi_version}

%description -n %{nexdome_pkg}
INDI driver for NexDome.


%package -n %{nightscape_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver for Celestron Nightscape 8300 series

Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{nightscape_pkg}
INDI driver for for the Celestron Nightscape 8300 line of CCDs.


%package -n %{ocs_pkg}
License:        GPL-2.0-only
Summary:        INDI driver for Observatory Control System

Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{ocs_pkg}
INDI driver for the Observatory Control System (OCS).


%package -n %{orion_pkg}
License:        GPL-3.0-or-later
Summary:        INDI driver for Orion StarShoot G3 cameras

Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{orion_pkg}
INDI driver for for the Orion StarShoot G3 cameras.


%package -n %{rolloffino_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI roll off roof driver

Requires:       libindi = %{indi_version}

%description -n %{rolloffino_pkg}
An Observatory roll off roof driver to automate the opening
and closing of a roll off roof in the INDI environment.


%package -n %{rtklib_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver providing support for RTKLIB

Requires:       libindi = %{indi_version}

%description -n %{rtklib_pkg}
INDI driver providing support for RTKLIB.


%package -n %{shelyak_pkg}
License:        GPL-2.0-or-later
Summary:        INDI driver providing support for Shelyak spectrographs

Requires:       libindi = %{indi_version}

%description -n %{shelyak_pkg}
INDI driver providing support for Shelyak spectrographs.


%package -n %{starbook_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for Vixen Starbook telescope controllers

Requires:       libindi = %{indi_version}

%description -n %{starbook_pkg}
INDI driver for Vixen Starbook telescope controllers. This driver aims
for compatibility with first generation Starbook.
Starbook TEN is working to some extent with this driver.
Commands exclusive to Starbook TEN won't be available.


%package -n %{starbookten_pkg}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Summary:        INDI driver for Vixen Starbook Ten

Requires:       libindi = %{indi_version}

%description -n %{starbookten_pkg}
INDI driver for Vixen Starbook Ten telescope controllers.


%package -n %{sx_pkg}
License:        GPL-2.0-or-later AND ICU
Summary:        INDI driver providing support for Starlight Xpress devices

Requires:       libindi = %{indi_version}
Requires:       udev

Provides:       indi-sx = %{version}-%{release}
Obsoletes:      indi-sx <= 1.9.3-2

%description -n %{sx_pkg}
INDI driver providing support for devices from Starlight Xpress.
This includes SX CCDs, SX wheel and SX Active Optics.


%package -n %{talon6_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for TALON6 Roll Off Roof

Requires:       libindi = %{indi_version}

%description -n %{talon6_pkg}
INDI driver providing support for TALON6 Roll Off Roof.


%package -n %{webcam_pkg}
License:        LGPL-2.1-or-later
Summary:        INDI driver for ffmpeg based webcams

Requires:       libindi = %{indi_version}

%description -n %{webcam_pkg}
INDI driver for ffmpeg based webcams.


%package -n %{weewx_pkg}
License:        GPL-2.0-or-later
Summary:        Use Weewx to provide weather data to INDI

Requires:       libindi = %{indi_version}

%description -n %{weewx_pkg}
This driver uses the WeeWX JSON plugin to provide weather data to INDI.


%prep
%autosetup -p1

# We don't want to apply upstream customized build flags
sed -i 's|include(CMakeCommon)||g' CMakeLists.txt

# libahp_xc comes as pre-built software, but in Fedora we use system's provided
sed -i 's|SET(WITH_AHP_XC Off)|SET(WITH_AHP_XC On)|g' CMakeLists.txt

# For Fedora we want to put udev rules in %%{_udevrulesdir}
find . -mindepth 2 -name CMakeLists.txt \
    -exec echo 'Processing {}' \; \
    -exec sed -i 's#\/\(etc\|lib\)\/udev\/rules\.d#%{_udevrulesdir}#g' {} \;


%build
# Options explanation:
# -DNO_PRE_BUILT=ON         disable all pre-built drivers
# -DINDI_BUILD_UNITTESTS=ON build and run tests
# -DWITH_FFMV=OFF           needs libdc1394 which is not available on s390x
# -DWITH_LIMESDR=OFF        needs limesuite to be packaged
%cmake -DBUILD_LIBS=OFF \
    -DNO_PRE_BUILT=ON \
    -DINDI_BUILD_UNITTESTS=ON \
    -DWITH_FFMV=OFF \
    -DWITH_LIMESDR=OFF \
    -DINDI_SYSTEM_JSONLIB="%{system_jsonlib}"

%cmake_build


%install
%cmake_install


%check
%if 0%{?build_tests}
# Tests cannot be run because we split upstream sources
#%%ctest
%endif


%files
%license LICENSE
%doc README.md


%files -n %{aagcloudwatcher_ng_pkg}
%license indi-aagcloudwatcher-ng/LICENSE.txt
%doc indi-aagcloudwatcher-ng/README.txt
%{_bindir}/indi_aagcloudwatcher_ng
%{_bindir}/aagcloudwatcher_test_ng
%{_datadir}/indi/indi_aagcloudwatcher_ng.xml
%{_datadir}/indi/indi_aagcloudwatcher_ng_sk.xml

%files -n %{aagcloudwatcher_ng_pkg}-doc
%doc indi-aagcloudwatcher-ng/docs


%files -n %{ahpxc_pkg}
%license LICENSE
%{_bindir}/indi_ahp_xc
%{_datadir}/indi/indi_ahp_xc.xml


%files -n %{aok_pkg}
%license LICENSE
%doc indi-aok/ChangeLog
%{_bindir}/indi_lx200aok
%{_datadir}/indi/indi_aok.xml


%files -n %{apogee_pkg}
%license indi-apogee/COPYING.LIB
%doc indi-apogee/AUTHORS indi-apogee/README indi-apogee/ChangeLog
%{_bindir}/indi_apogee_ccd
%{_bindir}/indi_apogee_wheel
%{_datadir}/indi/indi_apogee.xml


%files -n %{avalon_pkg}
%license LICENSE
%doc indi-avalon/README
%{_bindir}/indi_lx200stargo
%{_datadir}/indi/indi_avalon.xml


%files -n %{avalonud_pkg}
%license LICENSE
%doc indi-avalonud/README indi-avalonud/ChangeLog
%{_bindir}/indi_avalonud_aux
%{_bindir}/indi_avalonud_focuser
%{_bindir}/indi_avalonud_telescope
%{_datadir}/indi/indi_avalonud.xml


%files -n %{beefocus_pkg}
%license indi-beefocus/firmware/LICENSE
%doc indi-beefocus/README.md
%{_bindir}/indi_beefocus
%{_datadir}/indi/indi_beefocus.xml


%files -n %{bresser_pkg}
%license LICENSE
%doc indi-bresserexos2/README.md
%{_bindir}/indi_bresserexos2
%{_datadir}/indi/indi_bresserexos2.xml

%files -n %{bresser_pkg}-doc
%doc indi-bresserexos2/Documentation


%files -n %{caux_pkg}
%license LICENSE
%doc indi-celestronaux/README.md
%{_bindir}/indi_celestron_aux
%{_datadir}/indi/indi_celestronaux.xml


%files -n %{eqmod_pkg}
%license indi-eqmod/COPYING
%doc indi-eqmod/AUTHORS indi-eqmod/README
%{_bindir}/indi_eqmod_telescope
%{_bindir}/indi_azgti_telescope
%{_bindir}/indi_staradventurergti_telescope
%{_datadir}/indi/indi_align_sk.xml
%{_datadir}/indi/indi_eqmod*.xml


%files -n %{fli_pkg}
%license LICENSE
%{_bindir}/indi_fli_ccd
%{_bindir}/indi_fli_focus
%{_bindir}/indi_fli_wheel
%{_bindir}/indi_staradventurer2i_telescope
%{_datadir}/indi/indi_fli.xml


%files -n %{gphoto_pkg}
%license indi-gphoto/COPYING.LIB
%doc indi-gphoto/AUTHORS indi-gphoto/README
%{_bindir}/gphoto_camera_test
%{_bindir}/indi_canon_ccd
%{_bindir}/indi_fuji_ccd
%{_bindir}/indi_gphoto_ccd
%{_bindir}/indi_nikon_ccd
%{_bindir}/indi_pentax_ccd
%{_bindir}/indi_sony_ccd
%{_datadir}/indi/indi_gphoto.xml
%{_udevrulesdir}/85-disable-dslr-automout.rules


%files -n %{gpsd_pkg}
%license LICENSE
%{_bindir}/indi_gpsd
%{_datadir}/indi/indi_gpsd.xml


%files -n %{gpsnmea_pkg}
%license LICENSE
%{_bindir}/indi_gpsnmea
%{_datadir}/indi/indi_gpsnmea.xml


%files -n %{lunatico_pkg}
%license LICENSE
%doc indi-armadillo-platypus/AUTHORS indi-armadillo-platypus/README
%{_bindir}/indi_armadillo_focus
%{_bindir}/indi_beaver_dome
%{_bindir}/indi_dragonfly
%{_bindir}/indi_dragonfly_dome
%{_bindir}/indi_platypus_focus
%{_bindir}/indi_seletek_rotator
%{_datadir}/indi/indi_lunatico.xml
%{_udevrulesdir}/99-armadilloplatypus.rules


%files -n %{maxdome_pkg}
%license LICENSE
%{_bindir}/indi_maxdomeii
%{_datadir}/indi/indi_maxdomeii.xml


%files -n %{mgen_pkg}
%license LICENSE
%{_bindir}/indi_mgenautoguider
%{_datadir}/indi/indi_mgenautoguider.xml


%files -n %{nexdome_pkg}
%license LICENSE
%{_bindir}/indi_nexdome
%{_datadir}/indi/indi_nexdome.xml


%files -n %{nightscape_pkg}
%license indi-nightscape/COPYING.LIB
%doc indi-nightscape/AUTHORS indi-nightscape/README
%{_bindir}/indi_nightscape_ccd
%{_datadir}/indi/indi_nightscape.xml
%{_udevrulesdir}/99-nightscape.rules


%files -n %{ocs_pkg}
%license indi-ocs/LICENSE.txt
%doc indi-ocs/README.txt indi-ocs/Documentation
%{_bindir}/indi_ocs
%{_datadir}/indi/indi_ocs.xml


%files -n %{orion_pkg}
%license indi-orion-ssg3/LICENSE
%doc indi-orion-ssg3/README.md
%{_bindir}/indi_orion_ssg3_ccd
%{_datadir}/indi/indi_orion_ssg3.xml
%{_udevrulesdir}/99-orionssg3.rules


%files -n %{rolloffino_pkg}
%license LICENSE
%doc indi-rolloffino/README.md indi-rolloffino/doc
%{_bindir}/indi_rolloffino
%{_datadir}/indi/indi_rolloffino.xml


%files -n %{rtklib_pkg}
%license LICENSE
%{_bindir}/indi_rtklib
%{_datadir}/indi/indi_rtklib.xml


%files -n %{shelyak_pkg}
%license LICENSE
%{_bindir}/indi_shelyakeshel_spectrograph
%{_bindir}/indi_shelyakspox_spectrograph
%{_datadir}/indi/indi_shelyak.xml


%files -n %{starbook_pkg}
%license indi-starbook/COPYING.LGPL
%doc indi-starbook/AUTHORS indi-starbook/README.rst
%{_bindir}/indi_starbook_telescope
%{_datadir}/indi/indi_starbook_telescope.xml


%files -n %{starbookten_pkg}
%license indi-starbook-ten/COPYING indi-starbook-ten/COPYING.LESSER
%license indi-starbook-ten/COPYRIGHT
%doc indi-starbook-ten/AUTHORS indi-starbook-ten/README
%{_bindir}/indi_starbook_ten
%{_datadir}/indi/indi_starbook_ten.xml


%files -n %{sx_pkg}
%license indi-sx/COPYING.LIB
%doc indi-gphoto/AUTHORS indi-gphoto/README
%{_bindir}/indi_sx_ao
%{_bindir}/indi_sx_ccd
%{_bindir}/indi_sx_wheel
%{_bindir}/sx_ccd_test
%{_datadir}/indi/indi_sx.xml
%{_udevrulesdir}/99-sx.rules


%files -n %{talon6_pkg}
%license LICENSE
%doc indi-talon6/AUTHORS indi-talon6/README
%{_bindir}/indi_talon6
%{_datadir}/indi/indi_talon6.xml


%files -n %{webcam_pkg}
%license LICENSE
%{_bindir}/indi_webcam_ccd
%{_datadir}/indi/indi_webcam.xml


%files -n %{weewx_pkg}
%license LICENSE
%{_bindir}/indi_weewx_json
%{_datadir}/indi/indi_weewx_json.xml


%changelog
%autochangelog
