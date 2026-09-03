%global forgeurl    https://codeberg.org/sox_ng/sox_ng
%global commit      a4a14b4f58ac2c08c4cc416a7cffe8a4c50a0b7d

Name:           sox
Version:        14.8.1
Summary:        Audio processing utility
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only AND BSD-3-Clause AND MIT
Release:        %autorelease

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  bc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  file-devel
BuildRequires:  flac-devel
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libao-devel
BuildRequires:  libebur128-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opusfile-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  twolame-devel
BuildRequires:  wavpack-devel

%description
SoX (Sound eXchange) is a command-line audio file format converter and effects
processor. This package is based on SoX_ng, the actively maintained fork of
the original SoX codebase. It provides the traditional sox, soxi, play and rec
command names, as well as the native sox_ng, soxi_ng, play_ng and rec_ng names.

%package devel
Summary:        Development files for SoX
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries, pkg-config data and manual pages for developing software
against SoX and SoX_ng.

%prep
%forgesetup

cp -p libdolbyb/COPYING COPYING.libdolbyb
cp -p libebur128/COPYING COPYING.libebur128

%build
autoreconf -fiv

# Work around upstream configure.ac variable-name typo.
export found_libebur128=yes

%configure \
    --enable-replace \
    --disable-static \
    --with-distro=Fedora \
    --with-dyn-default \
    --without-dolbyb \
    --without-lpc10

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%check
# LPC10 is deliberately disabled because Fedora has no compatible
# standalone system liblpc10.
sed -i 's/ ima lpc10 prc/ ima prc/' \
    test/convert-number-of-channels/run

export LD_LIBRARY_PATH="$PWD/src/.libs:"
%make_build check

%files
%license COPYING COPYING.libdolbyb COPYING.libebur128 libgsm/COPYRIGHT
%doc AUTHORS ChangeLog README.md
%{_bindir}/play
%{_bindir}/play_ng
%{_bindir}/rec
%{_bindir}/rec_ng
%{_bindir}/sox
%{_bindir}/sox_ng
%{_bindir}/soxi
%{_bindir}/soxi_ng
%{_libdir}/libsox_ng.so.*
%dir %{_libdir}/sox_ng
%{_libdir}/sox_ng/libsox_ng_fmt_*.so
%{_mandir}/man1/play.1*
%{_mandir}/man1/play_ng.1*
%{_mandir}/man1/rec.1*
%{_mandir}/man1/rec_ng.1*
%{_mandir}/man1/sox.1*
%{_mandir}/man1/sox_ng.1*
%{_mandir}/man1/soxi.1*
%{_mandir}/man1/soxi_ng.1*
%{_mandir}/man7/soxeffect.7*
%{_mandir}/man7/soxeffect_ng.7*
%{_mandir}/man7/soxformat.7*
%{_mandir}/man7/soxformat_ng.7*

%files devel
%{_includedir}/sox.h
%{_includedir}/sox_ng.h
%{_libdir}/libsox.so
%{_libdir}/libsox_ng.so
%{_libdir}/pkgconfig/sox.pc
%{_libdir}/pkgconfig/sox_ng.pc
%{_mandir}/man3/libsox.3*
%{_mandir}/man3/libsox_ng.3*
%{_mandir}/man3/libsoxeffect.3*
%{_mandir}/man3/libsoxeffect_ng.3*
%{_mandir}/man3/libsoxformat.3*
%{_mandir}/man3/libsoxformat_ng.3*

%changelog
%autochangelog
