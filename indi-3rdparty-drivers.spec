%global aagcloudwatcher_ng_pkg indi-3rdparty-aagcloudwatcher-ng
%global aok_pkg indi-3rdparty-aok
%global apogee_pkg indi-3rdparty-apogee
%global eqmod_pkg indi-3rdparty-eqmod
%global fli_pkg indi-3rdparty-fli
%global gphoto_pkg indi-3rdparty-gphoto
%global sx_pkg indi-3rdparty-sx
%global webcam_pkg indi-3rdparty-webcam

%global indi_version 1.9.9

Name:           indi-3rdparty-drivers
Version:        1.9.9
Release:        %autorelease
Summary:        INDI 3rdparty drivers
License:        LGPLv2+
URL:            http://indilib.org

# Tar is generated from the huge all-in-one tar from INDI
# by using ./generate-drivers-tarball.sh %%{version}
# The main source from upstream is at
# https://github.com/indilib/indi-3rdparty/archive/refs/tags/v%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.xz
Source1:        generate-drivers-tarball.sh

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ffmpeg-free-devel
# Weak dependencies are not pulled in
# BuildRequires:  indi-3rdparty-libraries = %%{version}
BuildRequires:  indi-3rdparty-libapogee-devel = %{version}
BuildRequires:  indi-3rdparty-libfli-devel = %{version}
BuildRequires:  libnova-devel
BuildRequires:  libindi = %{indi_version}
BuildRequires:  zlib-devel

BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libindi) = %{version}
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libusb-1.0)

# We want this metapackage to install all drivers at once.
# Just use weak dependencies to avoid possible errors.
Recommends:     %{aagcloudwatcher_ng_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{aok_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{apogee_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{eqmod_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{fli_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{gphoto_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{sx_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{webcam_pkg}%{?_isa} = %{version}-%{release}

%description
This is a metapackage for installing all INDI 3rdparty drivers
at once. You probably don't want to install everything, but just pick
the drivers you need from the appropriate subpackage.

We currently ship the following drivers:
- %{aagcloudwatcher_ng_pkg}
- %{aok_pkg}
- %{apogee_pkg}
- %{eqmod_pkg}
- %{fli_pkg}
- %{gphoto_pkg}
- %{sx_pkg}
- %{webcam_pkg}


%package -n %{aagcloudwatcher_ng_pkg}
License:        GPLv3+
Summary:        INDI driver for the AAG Cloud Watcher NG

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
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


%package -n %{aok_pkg}
# No license in the drivers directory, assuming the same as main package
License:        LGPLv2+
Summary:        The INDI driver for AOK Skywalker mounts

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}

%description -n %{aok_pkg}
The INDI driver to control the AOK Skywalker mounts.


%package -n %{apogee_pkg}
License:        GPLv3+
Summary:        The INDI driver for Apogee Alta (U & E) line of CCDs

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}

Provides:       indi-apogee = 1:%{version}-%{release}
Obsoletes:      indi-apogee <= 1:1.9.3-2

%description -n %{apogee_pkg}
The INDI (Instrument Neutral Distributed Interface) driver for Apogee 
Alta (U & E) line of CCDs.


%package -n %{eqmod_pkg}
License:        GPLv3+
Summary:        INDI driver providing support for SkyWatcher Protocol

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}

Provides:       indi-eqmod = %{version}-%{release}
Obsoletes:      indi-eqmod <= 1.9.3-2

%description -n %{eqmod_pkg}
INDI driver adding support for telescope mounts using the 
SkyWatcher protocol.


%package -n %{fli_pkg}
# No license in the drivers directory, assuming the same as main package
License:        LGPLv2+
Summary:        INDI driver for Finger Lakes Instruments CCDs and focusers

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}
Requires:       udev

%description -n %{fli_pkg}
INDI driver adding support for Finger Lakes Instruments CCDs
and focusers.


%package -n %{gphoto_pkg}
License:        GPLv3+
Summary:        INDI driver providing support for gPhoto

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}
Requires:       udev

Provides:       indi-gphoto = %{version}-%{release}
Obsoletes:      indi-gphoto <= 1.9.3-2

%description -n %{gphoto_pkg}
INDI driver using gPhoto to add support for many cameras to INDI.
This includes many DSLR, e.g. Canon or Nikon.


%package -n %{sx_pkg}
License:        GPLv3+
Summary:        INDI driver providing support for Starlight Xpress devices

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}
Requires:       udev

Provides:       indi-sx = %{version}-%{release}
Obsoletes:      indi-sx <= 1.9.3-2

%description -n %{sx_pkg}
INDI driver providing support for devices from Starlight Xpress.
This includes SX CCDs, SX wheel and SX Active Optics.


%package -n %{webcam_pkg}
# No license in the drivers directory, assuming the same as main package
License:        LGPLv2+
Summary:        INDI driver for ffmpeg based webcams

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{indi_version}

%description -n %{webcam_pkg}
INDI driver for ffmpeg based webcams.


%prep
%autosetup -p1

# We don't want to apply upstream customized build flags
sed -i 's|include(CMakeCommon)||g' CMakeLists.txt

# For Fedora we want to put udev rules in %%{_udevrulesdir}
find . -mindepth 2 -name CMakeLists.txt \
    -exec echo 'Processing {}' \; \
    -exec sed -i 's#\/\(etc\|lib\)\/udev\/rules\.d#%{_udevrulesdir}#g' {} \;


%build
%cmake -DBUILD_LIBS=OFF \
    -DWITH_EQMOD=ON \
    -DWITH_ASTROLINK4=OFF \
    -DWITH_SKYWALKER=ON \
    -DWITH_STARBOOK=OFF \
    -DWITH_STARBOOK_TEN=OFF \
    -DWITH_SX=ON \
    -DWITH_MAXDOME=OFF \
    -DWITH_NEXDOME=OFF \
    -DWITH_TALON6=OFF \
    -DWITH_SPECTRACYBER=OFF \
    -DWITH_SHELYAK=OFF \
    -DWITH_CLOUDWATCHER=ON \
    -DWITH_CAUX=OFF \
    -DWITH_GPHOTO=ON \
    -DWITH_QSI=OFF \
    -DWITH_SBIG=OFF \
    -DWITH_ATIK=OFF \
    -DWITH_TOUPBASE=OFF \
    -DWITH_BEEFOCUS=OFF \
    -DWITH_INOVAPLX=OFF \
    -DWITH_FLI=ON \
    -DWITH_APOGEE=ON \
    -DWITH_FFMV=OFF \
    -DWITH_MI=OFF \
    -DWITH_DUINO=OFF \
    -DWITH_FISHCAMP=OFF \
    -DWITH_ASICAM=OFF \
    -DWITH_DSI=OFF \
    -DWITH_QHY=OFF \
    -DWITH_GPSD=OFF \
    -DWITH_GPSNMEA=OFF \
    -DWITH_RTKLIB=OFF \
    -DWITH_GIGE=OFF \
    -DWITH_MGEN=OFF \
    -DWITH_ASTROMECHFOC=OFF \
    -DWITH_LIMESDR=OFF \
    -DWITH_ARMADILLO=OFF \
    -DWITH_WEBCAM=ON \
    -DWITH_NIGHTSCAPE=OFF \
    -DWITH_DREAMFOCUSER=OFF \
    -DWITH_AVALON=OFF \
    -DWITH_PENTAX=OFF \
    -DWITH_AHP_XC=OFF \
    -DWITH_SVBONY=OFF \
    -DWITH_RPICAM=OFF \
    -DWITH_BRESSEREXOS2=OFF \
    -DWITH_ORION_SSG3=OFF \
    -DWITH_PLAYERONE=OFF \
    -DWITH_WEEWX_JSON=OFF

%cmake_build


%install
%cmake_install


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


%files -n %{eqmod_pkg}
%license indi-eqmod/COPYING
%doc indi-eqmod/AUTHORS indi-eqmod/README
%{_bindir}/indi_eqmod_telescope
%{_bindir}/indi_azgti_telescope
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
%{_bindir}/indi_canon_ccd
%{_bindir}/indi_fuji_ccd
%{_bindir}/indi_gphoto_ccd
%{_bindir}/indi_nikon_ccd
%{_bindir}/indi_pentax_ccd
%{_bindir}/indi_sony_ccd
%{_datadir}/indi/indi_gphoto.xml
%{_udevrulesdir}/85-disable-dslr-automout.rules


%files -n %{sx_pkg}
%license indi-sx/COPYING.LIB
%doc indi-gphoto/AUTHORS indi-gphoto/README
%{_bindir}/indi_sx_ao
%{_bindir}/indi_sx_ccd
%{_bindir}/indi_sx_wheel
%{_bindir}/sx_ccd_test
%{_datadir}/indi/indi_sx.xml
%{_udevrulesdir}/99-sx.rules


%files -n %{webcam_pkg}
%license LICENSE
%{_bindir}/indi_webcam_ccd
%{_datadir}/indi/indi_webcam.xml


%changelog
%autochangelog
