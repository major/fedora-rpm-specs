### Naming ###
# Set to true if it's going to be submitted as update
%global release_build 1

# Set new source-code build version
# This tag indicates a new rebuild for Fedora
%global redhat_ver rh1

#%%global pre_tag .test
%global pre_tag %{nil}

# Exclude ARM for the following error:
#  terminate called after throwing an instance of 'std::bad_alloc'
#   what():  std::bad_alloc
#   error: could not compile `gkrust`
ExcludeArch: %{arm}

####################

### Optimization ###
# Builds for debugging
%global debug_build   0

# Downgrade optimization
%global less_optbuild 0

# Use mozilla hardening option?
%global hardened_build 1
####################

# Build PGO+LTO on x86_64 and aarch64 only due to build issues
# on other arches.
%ifarch x86_64
%if 0%{?release_build}
%global build_with_pgo 0
%global pgo_wayland    0
%else
%global build_with_pgo 0
%endif
%endif

%global launch_wayland_compositor 0
%if 0%{?build_with_pgo}
%global launch_wayland_compositor 1
%endif

# Disable LTO to work around rhbz#1883904
%define _lto_cflags %{nil}
####################

# Active/Deactive language files handling
%global build_langpacks 1

%global default_bookmarks_file %{_datadir}/bookmarks/default-bookmarks.html

# Define installation directories
%global icecatappdir %{_libdir}/%{name}
%global icecat_ver   %{name}-%{version}
%global icecat_devel %{name}-devel-%{version}

# Define language files directory
%global langpackdir  %{icecatappdir}/langpacks

%global toolkit_gtk3  1

# Big endian platforms
%ifarch ppc64 s390x
# Javascript Intl API is not supported on big endian platforms right now:
# https://bugzilla.mozilla.org/show_bug.cgi?id=1322212
%global big_endian    1
%endif

%global system_nss  1
%if %{?system_nss}
%global nspr_version 4.32
%global nspr_build_version %{nspr_version}
%global nss_version 3.80
%global nss_build_version %{nss_version}
%endif

# Audio backends
%bcond_without pulseaudio
%bcond_with alsa

%global with_vpx 1
%if %{?with_vpx}
%global libvpx_version 1.8.2
%endif

%global disable_elfhack 1

# cbingen
%global use_bundled_cbindgen 1

# Use clang?
%global build_with_clang  0

# https://bugzilla.redhat.com/show_bug.cgi?id=1908792
%global __provides_exclude_from ^%{icecatappdir}
%global __requires_exclude_from ^%{icecatappdir}

Name: icecat
Epoch:   1
Version: 102.3.0
Release: 1.%{redhat_ver}%{?pre_tag}%{?dist}
Summary: GNU version of Firefox browser

# Tri-licensing scheme for Gnuzilla/IceCat in parentheses, and licenses for the extensions included
License: (MPLv1.1 or GPLv2+ or LGPLv2+) and GPLv3+ and MIT and BSD and ISC and ASL 2.0 and MPLv2.0
URL:   http://www.gnu.org/software/gnuzilla/

## Source archive created by scripts based on Gnuzilla files.
## Modified files are hosted in a dedicated fork repository:
## https://gitlab.com/anto.trande/icecat
Source0: %{name}-%{version}-%{redhat_ver}.tar.bz2

Source2: %{name}.png
Source3: %{name}-mozconfig-common

# Language files downloaded by source7 script
%if 0%{?build_langpacks}
Source4:  %{name}-%{version}-langpacks.tar.gz
%endif

# All license files
# Download from http://www.gnu.org/licenses
# Download from http://www.mozilla.org/MPL/1.1/index.txt
# Download from https://www.mozilla.org/MPL/2.0/index.txt
Source5: %{name}-COPYING-licensefiles.tar.gz

Source7: %{name}-lang_download.sh

# Desktop files
Source9:  %{name}-wayland.desktop
Source10: %{name}.appdata.xml
Source12: %{name}-wayland.sh.in
Source13: %{name}.sh.in
Source14: %{name}.desktop
Source15: %{name}-x11.sh.in
Source16: %{name}-x11.desktop

# cbingen
Source17: cbindgen-vendor.tar.xz
Source18: node-stdout-nonblocking-wrapper

Source19: run-wayland-compositor

# Build patches
# Fixes installation of those addons which don't have ID on IceCat ("Cannot find id for addon" error).
Patch1: %{name}-fix_addon_installation.patch
Patch2: %{name}-libevent_linkflag.patch
Patch3: mozilla-build-arm.patch
Patch4: %{name}-build-arm-libaom.patch
Patch5: rhbz-1219542-s390-build.patch
Patch6: mozilla-1773336.patch

Patch40: build-aarch64-skia.patch
Patch41: build-disable-elfhack.patch
Patch44: build-arm-libopus.patch
Patch54: mozilla-1669639.patch

# Fedora specific patches
Patch219: rhbz-1173156.patch
Patch220: firefox-nss-version.patch
Patch221: firefox-nss-addon-hack.patch
Patch223: %{name}-glibc-dynstack.patch
Patch224: %{name}-GLIBCXX-fix-for-GCC-12.patch

# ARM run-time patch
Patch226: rhbz-1354671.patch

# Upstream patches
Patch401: icecat-1742849.patch
Patch402: mozilla-1196777.patch
Patch403: icecat-python3.11-open-U.patch
Patch404: icecat-python3.11-regex-inline-flags.patch
Patch412: mozilla-1337988.patch
Patch422: mozilla-1580174-webrtc-popup.patch

# Fix crash on ppc64le (mozilla#1512162)
Patch423: mozilla-1512162.patch

# PGO/LTO patches
Patch600: %{name}-pgo.patch
Patch602: mozilla-1516803.patch

#VA-API patches
Patch584: firefox-disable-ffvpx-with-vapi.patch
Patch585: firefox-vaapi-extra-frames.patch

BuildRequires: alsa-lib-devel
BuildRequires: autoconf213
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: cargo
%if !0%{?use_bundled_cbindgen}
BuildRequires: cbindgen	
%endif
BuildRequires: ccache
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: dbus-x11
BuildRequires: dconf
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: fedora-bookmarks
BuildRequires: freetype-devel
BuildRequires: gdk-pixbuf2
BuildRequires: glib2-devel
BuildRequires: pkgconfig(gtk+-2.0)
%if 0%{?toolkit_gtk3}
BuildRequires: pkgconfig(gtk+-3.0)
%endif
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: hunspell-devel
BuildRequires: ImageMagick, autotrace
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libavcodec-free-devel
BuildRequires: libevent-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libjpeg-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXrender-devel
BuildRequires: libyuv-devel
BuildRequires: libXinerama-devel
BuildRequires: libffi-devel
BuildRequires: libnotify-devel
BuildRequires: libpng-devel
%if %{?with_vpx}
BuildRequires: libvpx-devel >= %{libvpx_version}
%endif
BuildRequires: libzip-devel
BuildRequires: mesa-libGL-devel
BuildRequires: nodejs
BuildRequires: nasm >= 1.13
BuildRequires: strace

%if %{?system_nss}
BuildRequires: pkgconfig(nspr) >= %{nspr_version}
BuildRequires: pkgconfig(nss) >= %{nss_version}
BuildRequires: nss-static >= %{nss_version}
%endif

BuildRequires: openjpeg-devel
BuildRequires: pango-devel
BuildRequires: pipewire-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: perl-interpreter
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(libcurl)
%if %{with pulseaudio}
BuildRequires: pulseaudio-libs-devel
%endif
BuildRequires: yasm
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: clang
BuildRequires: clang-libs
BuildRequires: clang-devel
%if 0%{?build_with_clang}
BuildRequires: lld
%endif
BuildRequires: rust
%if 0%{?pgo_wayland}
BuildRequires:  mutter
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gnome-settings-daemon
BuildRequires:  mesa-dri-drivers
BuildRequires:  xorg-x11-server-Xwayland
%endif
%if 0%{?build_with_pgo}
BuildRequires:  xorg-x11-server-Xvfb
%endif

%if 0%{?big_endian}
BuildRequires: icu
%endif

Requires: dconf
Requires: mozilla-filesystem
Requires: p11-kit-trust

%if %{?system_nss}
Requires: nspr >= %{nspr_build_version}
Requires: nss >= %{nss_build_version}
%endif

Requires: fedora-bookmarks
Suggests: mozilla-ublock-origin

Provides: webclient
Provides: bundled(mozilla-https-everywhere) = 2021.7.13

%description
GNU IceCat is the GNU version of the Firefox ESR browser.
Extensions included to this version of IceCat:

 * LibreJS
   GNU LibreJS aims to address the JavaScript problem described in the article
   "The JavaScript Trap" of Richard Stallman.

 * HTTPS Everywhere
   HTTPS Everywhere is an extension that encrypts your communications with
   many major websites, making your browsing more secure.

 * ViewTube
   Watch videos from video sharing websites with extra options.

 * A set of companion extensions for LibreJS by Nathan Nichols
   are pre-installed, and provide workarounds to use some services at USPS,
   RSF.org, SumOfUs.org, pay.gov, McDonalds, goteo.org and Google Docs
   without using nonfree JavaScript.

 * A series of configuration changes and tweaks were applied to ensure that
   IceCat does not initiate network connections that the user has not explicitly
   requested. This implies not downloading feeds, updates, blacklists or any
   other similar data needed during startup.

%package x11
Summary: GNU IceCat X11 launcher
Requires: %{name}%{?_isa}
%description x11
The %{name}-x11 package contains launcher and desktop file
to run GNU IceCat native on X11.

%package wayland
Summary: GNU IceCat Wayland launcher
Requires: %{name}%{?_isa}
Obsoletes: %{name} < 0:78.6.1-1
%description wayland
The icecat-wayland package contains launcher and desktop file
to run GNU IceCat native on Wayland.

%prep
%autosetup -N -n %{name}-%{version}

# Fix permissions
#find . -type f -name "*.h" -exec chmod 0644 '{}' \;
#find . -type f -name "*.cpp" -exec chmod 0644 '{}' \;
#find . -type f -name "*.cc" -exec chmod 0644 '{}' \;
#find . -type f -name "*.c" -exec chmod 0644 '{}' \;

# Copy license files
tar -xf %{SOURCE5}

%patch1 -p1 -b .fix_addon_installation
#patch2 -p0 -b .libevent_linkflag
%patch3 -p1 -b .build-arm-libaom
%patch4 -p1 -b .arm
%ifarch s390
%patch5 -p1 -b .rhbz-1219542-s390
%endif
%patch6 -p1 -b .1773336

%if 0%{?disable_elfhack}
%patch41 -p1 -b .disable-elfhack
%endif

# Fedora patches
%patch219 -p1 -b .rhbz-1173156
%patch221 -p1 -b .firefox-nss-addon-hack
%patch224 -p1 -b .glibcxx

# ARM run-time patch
%ifarch aarch64
%patch40 -p1 -b .aarch64-skia
%patch226 -p1 -b .1354671
%endif

%ifarch %{arm}
%patch44  -p1 -b .build-arm-libopus
%endif

#patch401 -p1 -b .1742849
%patch402 -p1 -b .1196777
%patch403 -p1 -b .python311
%patch404 -p1 -b .python311
%ifarch %{power64}
%patch423 -p1 -b .1512162
%endif

#%%patch584 -p1 -b .firefox-disable-ffvpx-with-vapi
#%%patch585 -p1 -b .firefox-vaapi-extra-frames
%patch54 -p1 -b .1669639

# PGO patches
%if 0%{?build_with_pgo}
%if !%{build_with_clang}
%patch600 -p1 -b .pgo
%patch602 -p1 -b .1516803
%endif
%endif

# Remove default configuration and copy the customized one
rm -f .mozconfig
cp -p %{SOURCE3} .mozconfig

# Disable signature checking for extensions that are bundled with IceCat.
# Add these options to allow loading unsigned add-ons in app and system scopes.
echo "ac_add_options --with-unsigned-addon-scopes=app,system" >> .mozconfig
echo "ac_add_options --allow-addon-sideload" >> .mozconfig

echo "ac_add_options --enable-default-toolkit=cairo-gtk3-wayland" >> .mozconfig
echo "ac_add_options --enable-official-branding" >> .mozconfig
echo "ac_add_options --disable-webrtc" >> .mozconfig

# Hide DRM Content option
# This option does not work on other architectures
%ifarch x86_64 %{ix86}
echo "ac_add_options --disable-eme" >> .mozconfig
%endif

%if %{with pulseaudio}
echo "ac_add_options --enable-pulseaudio" >> .mozconfig
%endif

%if %{with alsa}
echo "ac_add_options --enable-alsa" >> .mozconfig
%endif

%ifarch s390x
echo "ac_add_options --disable-jemalloc" >> .mozconfig
%endif

%if %{?system_nss}
echo "ac_add_options --with-system-nspr" >> .mozconfig
echo "ac_add_options --with-system-nss" >> .mozconfig
echo 'ac_add_options BINDGEN_CFLAGS="%(pkg-config nspr pixman-1 --cflags)"' >> .mozconfig
%else
echo "ac_add_options --without-system-nspr" >> .mozconfig
echo "ac_add_options --without-system-nss" >> .mozconfig
%endif
# Workaround for mozbz#1341234
echo "ac_add_options --allow-addon-sideload" >> .mozconfig
echo "ac_add_options --enable-system-pixman" >> .mozconfig
echo "ac_add_options --with-system-libevent" >> .mozconfig
%if %{?with_vpx}
echo "ac_add_options --with-system-libvpx" >> .mozconfig
%else
echo "ac_add_options --without-system-libvpx" >> .mozconfig
%endif

echo "ac_add_options --with-system-jpeg" >> .mozconfig
echo "ac_add_options --enable-ffmpeg" >> .mozconfig

# This option works on these architectures only
%ifarch %{arm}
echo "ac_add_options --disable-elf-hack" >> .mozconfig
echo "ac_add_options --disable-av1" >> .mozconfig
echo 'export NEON_FLAGS=-mfpu=vfpv3-d16' >> .mozconfig
%endif
%ifnarch %{arm}
echo "ac_add_options --enable-av1" >> .mozconfig
%endif

%if 0%{?debug_build}
echo "ac_add_options --enable-debug" >> .mozconfig
echo "ac_add_options --disable-optimize" >> .mozconfig
echo "ac_add_options --enable-rust-debug" >> .mozconfig
%else
%global optimize_flags "none"
%ifarch %{arm} s390x
# ARMv7 need that (rhbz#1426850)
%define optimize_flags " -fno-schedule-insns"
%endif
%if %{?optimize_flags} != "none"
echo 'ac_add_options --enable-optimize=%{?optimize_flags}' >> .mozconfig
%else
echo 'ac_add_options --enable-optimize' >> .mozconfig
%endif
echo "ac_add_options --disable-debug" >> .mozconfig
%endif
echo "ac_add_options --disable-strip" >> .mozconfig
echo "ac_add_options --disable-install-strip" >> .mozconfig
echo "ac_add_options --disable-tests" >> .mozconfig
echo "ac_add_options --disable-crashreporter" >> .mozconfig

# Localization
%if 0%{?build_langpacks}
echo "ac_add_options --with-l10n-base=$PWD/l10n" >> .mozconfig
%endif

%ifarch s390x
echo "ac_add_options --disable-jit" >> .mozconfig
%endif

%if 0%{?build_with_pgo}
echo "ac_add_options MOZ_PGO=1" >> .mozconfig
echo "ac_add_options --enable-lto" >> .mozconfig
%else
echo "ac_add_options --disable-lto" >> .mozconfig
%endif

echo 'export NODEJS="%{_buildrootdir}/bin/node-stdout-nonblocking-wrapper"' >> .mozconfig

# Remove executable bit to make brp-mangle-shebangs happy.
chmod -x third_party/rust/itertools/src/lib.rs
chmod a-x third_party/rust/ash/src/extensions/ext/*.rs
chmod a-x third_party/rust/ash/src/extensions/khr/*.rs
chmod a-x third_party/rust/ash/src/extensions/nv/*.rs

# Remove unrecognized files
find extensions/gnu -name cose.manifest -delete

#---------------------------------------------------------------------

%build
# cbindgen
%if 0%{?use_bundled_cbindgen}

mkdir -p my_rust_vendor
cd my_rust_vendor
%{__tar} xf %{SOURCE17}
cd -
mkdir -p .cargo
cat > .cargo/config <<EOL
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "`pwd`/my_rust_vendor"
EOL

env CARGO_HOME=.cargo cargo install cbindgen
export PATH=`pwd`/.cargo/bin:$PATH
%endif

mkdir %{_buildrootdir}/bin || :
cp %{SOURCE18} %{_buildrootdir}/bin || :

# Update the various config.guess to upstream release for aarch64 support
find ./ -path ./third_party/rust -prune -o -name config.guess -exec cp /usr/lib/rpm/config.guess {} ';'

MOZ_OPT_FLAGS=$(echo "%{optflags}" | %{__sed} -e 's/-Wall//')
%if %{?less_optbuild}
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-O2/-O1/')
%endif
%if %{?debug_build}
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-O2/-O0/')
%endif

#rhbz#1037063
# -Werror=format-security causes build failures when -Wno-format is explicitly given
# for some sources
# Explicitly force the hardening flags for Firefox so it passes the checksec test;
# See also https://fedoraproject.org/wiki/Changes/Harden_All_Packages
# Workaround for mozbz#1531309
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-Werror=format-security//')

# Use hardened build?
%if %{?hardened_build}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fPIC -Wl,-z,relro -Wl,-z,now"
%endif

%ifarch s390x %{arm}
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-g/-g1/' -e 's/-O2/-O1/')
# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g1 from line above and breaks building on s390
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "
%endif

# We don't wantfirefox to use CK_GCM_PARAMS_V3 in nss
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DNSS_PKCS11_3_0_STRICT"

%if !0%{?build_with_clang}
%ifarch s390x %{power64} aarch64 %{ix86}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads -Wl,--print-memory-usage"
%endif
%ifarch %{arm}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory"
echo "ac_add_options --enable-linker=gold" >> .mozconfig
%endif
%endif
%ifarch %{arm} %{ix86} %{power64}
export RUSTFLAGS="-Cdebuginfo=0"
export MOZ_RUST_DEFAULT_FLAGS="-Cdebuginfo=0 -Copt-level=0"
%endif
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS="$MOZ_OPT_FLAGS -fpermissive"
export LDFLAGS=$MOZ_LINK_FLAGS

export PREFIX='%{_prefix}'
export LIBDIR='%{_libdir}'
export PKG_CONFIG='%{_bindir}/pkg-config'
export PYTHON='%{__python3}'

%if 0%{?build_with_clang}
export LLVM_PROFDATA="llvm-profdata"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
echo "ac_add_options --enable-linker=lld" >> .mozconfig
%else
export CC=gcc
export CXX=g++
export AR="gcc-ar"
export NM="gcc-nm"
export RANLIB="gcc-ranlib"
%endif
export CCACHE_DISABLE=1

%if %{?less_optbuild}
MOZ_SMP_FLAGS=-j1
%else
MOZ_SMP_FLAGS=-j1
# On x86_64 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %{ix86} s390x %{arm} aarch64
[ -z "$RPM_BUILD_NCPUS" ] && \
     RPM_BUILD_NCPUS="`/usr/bin/getconf _NPROCESSORS_ONLN`"
[ "$RPM_BUILD_NCPUS" -ge 2 ] && MOZ_SMP_FLAGS=-j2
%endif
%ifarch x86_64 ppc ppc64 ppc64le
[ -z "$RPM_BUILD_NCPUS" ] && \
     RPM_BUILD_NCPUS="`/usr/bin/getconf _NPROCESSORS_ONLN`"
[ "$RPM_BUILD_NCPUS" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "$RPM_BUILD_NCPUS" -ge 4 ] && MOZ_SMP_FLAGS=-j4
[ "$RPM_BUILD_NCPUS" -ge 8 ] && MOZ_SMP_FLAGS=-j8
[ "$RPM_BUILD_NCPUS" -ge 16 ] && MOZ_SMP_FLAGS=-j16
[ "$RPM_BUILD_NCPUS" -ge 24 ] && MOZ_SMP_FLAGS=-j24
[ "$RPM_BUILD_NCPUS" -ge 32 ] && MOZ_SMP_FLAGS=-j32
[ "$RPM_BUILD_NCPUS" -ge 64 ] && MOZ_SMP_FLAGS=-j64
%endif
%endif

echo "mk_add_options MOZ_MAKE_FLAGS=\"$MOZ_SMP_FLAGS\"" >> .mozconfig
echo "mk_add_options MOZ_SERVICES_SYNC=1" >> .mozconfig
echo "export STRIP=/bin/true" >> .mozconfig

%if 0%{?launch_wayland_compositor}
cp -p %{SOURCE19} .
. ./run-wayland-compositor	
%endif

export MACH_USE_SYSTEM_PYTHON=1
%if 0%{?build_with_pgo}
%if 0%{?pgo_wayland}
env | grep "WAYLAND"
MOZ_ENABLE_WAYLAND=1 ./mach build -v 2>&1 | cat - && exit 1
%else
xvfb-run ./mach build  2>&1 | cat - || exit 1
%endif
%else
./mach build -v 2>&1 | cat - || exit 1
%endif

%install
# set up our default bookmarks
cp -p %{default_bookmarks_file} objdir/dist/bin/browser/chrome/en-US/locale/browser/bookmarks.html

%make_install -C objdir

##Resize IceCat icon
for i in 16 22 24 32 36 48 64 72 96 128 256 ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  convert -geometry ${i} %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

##desktop file installation
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE14}

rm -rf %{buildroot}%{_bindir}/%{name}
%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE13} > %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE15} > %{buildroot}%{_bindir}/%{name}-x11
chmod 755 %{buildroot}%{_bindir}/%{name}-x11
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE16}

%{__sed} -e 's,/__PREFIX__,%{_prefix},g' %{SOURCE12} > %{buildroot}%{_bindir}/%{name}-wayland
chmod 755 %{buildroot}%{_bindir}/%{name}-wayland
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE9}

#

##Install man page
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

##Extract langpacks, make any mods needed, repack the langpack, and install it.
%if 0%{?build_langpacks}
echo > %{name}.lang
mkdir -p %{buildroot}%{langpackdir}
tar xf %{SOURCE4}
 for langpack in `ls langpacks/*.xpi`; do
  language=`basename $langpack .xpi`
  extensionID=langpack-$language@icecat.mozilla.org
  mkdir -p $extensionID
  unzip -qq $langpack -d $extensionID
  find $extensionID -type f | xargs chmod 644

  cd $extensionID
  zip -qq -r9mX ../${extensionID}.xpi *
  cd -

  install -p -m 644 ${extensionID}.xpi %{buildroot}%{langpackdir}
  language=`echo $language | sed -e 's/-/_/g'`
  echo "%%lang($language) %{langpackdir}/${extensionID}.xpi" >> %{name}.lang
 done
rm -rf %{name}-langpacks

##Install langpack workaround (see #707100, #821169)
function create_default_langpack() {
language_long=$1
language_short=$2
cd %{buildroot}%{langpackdir}
ln -s langpack-$language_long@icecat.mozilla.org.xpi langpack-$language_short@icecat.mozilla.org.xpi
cd -
echo "%%lang($language_short) %{langpackdir}/langpack-$language_short@icecat.mozilla.org.xpi" >> %{name}.lang
}

# Table of fallbacks for each language
#create_default_langpack "bn-IN" "bn"
create_default_langpack "es-AR" "es"
create_default_langpack "fy-NL" "fy"
create_default_langpack "ga-IE" "ga"
create_default_langpack "gu-IN" "gu"
create_default_langpack "hi-IN" "hi"
create_default_langpack "hy-AM" "hy"
create_default_langpack "nb-NO" "nb"
create_default_langpack "nn-NO" "nn"
create_default_langpack "pa-IN" "pa"
create_default_langpack "pt-PT" "pt"
create_default_langpack "sv-SE" "sv"
create_default_langpack "zh-TW" "zh"
%endif

# Remove copied libraries to speed up build
rm -f ${RPM_BUILD_ROOT}%{_libdir}/%{icecat_devel}/sdk/lib/libmozjs.so
rm -f ${RPM_BUILD_ROOT}%{_libdir}/%{icecat_devel}/sdk/lib/libmozalloc.so
rm -f ${RPM_BUILD_ROOT}%{_libdir}/%{icecat_devel}/sdk/lib/libxul.so

# Remove useless backup files
rm -rf ${RPM_BUILD_ROOT}%{icecatappdir}/browser/extensions/SimpleSumOfUs@0xbeef.coffee

# Link identical binaries
ln -sf %{icecatappdir}/%{name}-bin ${RPM_BUILD_ROOT}%{icecatappdir}/%{name}

# Use the system hunspell dictionaries
rm -rf ${RPM_BUILD_ROOT}%{icecatappdir}/dictionaries
ln -s %{_datadir}/hunspell ${RPM_BUILD_ROOT}%{icecatappdir}/dictionaries

# Copy over run-icecat.sh
cp -p build/unix/run-%{name}.sh %{buildroot}%{icecatappdir}/

# Remove unused directories
rm -rf %{buildroot}%{_libdir}/%{icecat_devel}
rm -rf %{buildroot}%{_datadir}/idl/%{icecat_ver}
rm -rf %{buildroot}%{_includedir}/%{icecat_ver}
rm -rf %{buildroot}%{icecatappdir}/removed-files

# Remove gtk2 support as flash plugin is no longer supported
rm -rf %{buildroot}%{icecatappdir}/gtk2

mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE10} %{buildroot}%{_metainfodir}/

# Moves defaults/preferences to browser/defaults/preferences
%pretrans -p <lua>
require 'posix'
require 'os'
if (posix.stat("%{icecatappdir}/browser/defaults/preferences", "type") == "link") then
  posix.unlink("%{icecatappdir}/browser/defaults/preferences")
  posix.mkdir("%{icecatappdir}/browser/defaults/preferences")
  if (posix.stat("%{icecatappdir}/defaults/preferences", "type") == "directory") then
    for i,filename in pairs(posix.dir("%{icecatappdir}/defaults/preferences")) do
      os.rename("%{icecatappdir}/defaults/preferences/"..filename, "%{icecatappdir}/browser/defaults/preferences/"..filename)
    end
    f = io.open("%{icecatappdir}/defaults/preferences/README","w")
    if f then
      f:write("Content of this directory has been moved to %{icecatappdir}/browser/defaults/preferences.")
      f:close()
    end
  end
end

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%if 0%{?build_langpacks}
%files -f %{name}.lang
%else
%files
%endif
%doc README.* AUTHORS
%license LICENSE COPYING-*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}*.png
%{_metainfodir}/*.appdata.xml
%{_mandir}/man1/%{name}*
%dir %{icecatappdir}
%{icecatappdir}/browser/
%{icecatappdir}/defaults/
%{icecatappdir}/dictionaries
%{icecatappdir}/icecat*
%{icecatappdir}/fonts/
%{icecatappdir}/*.so
%{icecatappdir}/*.ini
%{icecatappdir}/omni.ja
%{icecatappdir}/run-icecat.sh
%{icecatappdir}/dependentlibs.list
%{icecatappdir}/plugin-container
%{icecatappdir}/pingsender
%{icecatappdir}/gmp-clearkey/
%if 0%{?build_langpacks}
%dir %{langpackdir}
%endif

%files x11
%{_bindir}/%{name}-x11
%{_datadir}/applications/%{name}-x11.desktop

%files wayland
%{_bindir}/%{name}-wayland
%{_datadir}/applications/%{name}-wayland.desktop

%changelog
* Tue Sep 20 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:102.3.0-1.rh1
- Release 102.3.0

* Sat Sep 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:102.2.0-1.rh1
- Release 102.2.0
- Epoch 1

* Mon Aug 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.13.0-1.rh1
- Release 91.13.0

* Wed Jul 27 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.12.0-2.rh1
- Patched for Python3.11

* Mon Jul 25 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.12.0-1.rh1
- Release 91.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 91.11.0-4.rh1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.11.0-3.rh1
- Drop Java dependency (rhbz#2104050)

* Fri Jul 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.11.0-2.rh1.test
- Release 91.11.0
- Less optbuild activated
- Add patch for mozilla bug #1773336

* Wed Jun 29 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.11.0-1.rh1
- Release 91.11.0 rh1

* Sun Jun 12 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.10.0-3.rh3
- Release 91.10.0 rh3
- Add libavcodec-free dependency

* Thu Jun 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.10.0-2.rh2
- Release 91.10.0 rh2

* Wed Jun 01 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.10.0-1.rh1
- Release 91.10.0

* Sun May 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.9.1-1.rh1
- Release 91.9.1

* Mon May 09 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.9.0-2.rh1
- Fix rhbz#20831110

* Tue May 03 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.9.0-1.rh1
- Release 91.9.0

* Wed Apr 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.8.0-1.rh1
- Release 91.8.0

* Thu Mar 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.7.1-1.rh1
- Release 91.7.1

* Tue Mar 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.7.0-1.rh1
- Release 91.7.0

* Sun Mar 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.6.1-1.rh1
- Release 91.6.1

* Fri Feb 18 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.6.0-2.rh1
- Patched for GCC-12

* Tue Feb 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.6.0-1.rh1
- Release 91.6.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 91.5.0-4.rh1
- Rebuilt for java-17-openjdk as system jdk

* Tue Jan 25 2022 Parag Nemade <pnemade AT redhat DOT com> - 91.5.0-3.rh1
- Update hunspell directory path
  F36 Change https://fedoraproject.org/wiki/Changes/Hunspell_dictionary_dir_change

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 91.5.0-2.rh1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Antonio Trande <sagitter@fedoraproject.org> - 91.5.0-1.rh1
- Release 91.5.0

* Wed Dec 22 2021 Antonio Trande <sagitter@fedoraproject.org> - 91.4.1-2.rh1
- Patched for Mozilla bug #1745560

* Wed Dec 22 2021 Antonio Trande <sagitter@fedoraproject.org> - 91.4.1-1.rh1
- Release 91.4.1

* Mon Dec 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 91.4.0-1.rh1
- Release 91.4.0

* Thu Nov 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 91.3.0-1.rh1
- Release 91.3.0
- Update cbindgen to 0.20.0
- Exclude ARM builds

* Tue Oct 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 91.2.0-1.rh1
- Release 91.2.0

* Tue Oct 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.15.0-1.rh1
- Release 78.15.0

* Tue Sep 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.14.0-1.rh1
- Release 78.14.0

* Wed Aug 11 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-2.rh3
- Enable build on PPC64le

* Tue Aug 10 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-1.rh3
- Release 78.13.0

* Sun Aug 08 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-0.5.rh2
- Patched for Mozilla bug 1715254 (rhbz#1990612)

* Sat Aug 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-0.4.rh2
- Update cbindgen to 0.19.0

* Thu Aug 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-0.3.rh2
- Release Candidate 78.13.0-rc2
- Disable PGO build (incomplete porting to Python 3.10) 

* Tue Aug 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-0.2.rh1
- Enable PGO build

* Mon Aug 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.13.0-0.1.rh1
- Release Candidate 78.13.0-rc1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 78.12.0-4.rh2.test
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild 

* Tue Jul 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.12.0-3.rh2.test
- Disable debug build mode
- Patched for Mozilla bug #1721326

* Thu Jul 15 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.12.0-2.rh2.test
- Enable debug build mode

* Wed Jul 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.12.0-1.rh2
- Release 78.12.0
- HTTPS Everywhere 2021.7.13

* Tue Jun 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.11.0-1.rh1
- Release 78.11.0

* Fri May 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.10.1-2.rh1
- Hide DRM Content option in Preference

* Wed May 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.10.1-1.rh1
- Release 78.10.1

* Sat Apr 24 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.10.0-2.rh1
- Patched for rhbz#1945720 (Mozilla bug #1680166)

* Mon Apr 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.10.0-1.rh1
- Release 78.10.0

* Fri Apr 09 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.9.0-3.rh1
- Patched for bug #1613672
- Use cbindgen 0.18.0
- Debug build on

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 78.9.0-2.rh1
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Mar 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.9.0-1.rh1
- Release 78.9.0

* Thu Feb 25 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.8.0-3.rh1
- Add patch #1692706

* Tue Feb 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.8.0-2.rh1
- Exclude Power64 (rhbz#1932204)
- Fix build option for s390x

* Tue Feb 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.8.0-1.rh1
- Release 78.8.0

* Fri Feb 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.7.1-1.rh1
- Release 78.7.1

* Fri Feb 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.7.0-3.rh2
- Fix parameter passing on ppc64le (mozb#1690152)
- Remove gtk2 support as flash plugin is no longer supported

* Wed Jan 27 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.7.0-2.rh2
- Build Release 78.7.0-rh2
- HTTPS Everywhere 2021.1.27

* Tue Jan 26 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.7.0-1.rh1
- Release 78.7.0

* Mon Jan 11 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.6.1-3.rh1
- Added a workaround for rhbz#1908018

* Wed Jan 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.6.1-2.rh1
- Fix desktop files

* Wed Jan 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 78.6.1-1.rh1
- Release 78.6.1

* Sat Dec 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.6.0-6.rh1
- Use wayland/x11 launchers
- Test ARM build with gcc-11.0.0-0.11

* Tue Dec 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.6.0-5.rh1
- Add __requires_exclude_from

* Sun Dec 20 2020 Miro Hrončok <mhroncok@redhat.com> - 78.6.0-4.rh1
- Filter out private libraries provides
- Fixes: rhbz#1908792

* Sun Dec 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.6.0-3.rh1
- Add build-arm-libaom patch
- Exclude ARM architectures

* Sat Dec 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.6.0-2.rh1
- Re-enable system NSS (rhbz#1908792)
- Disable PGO builds (x86_64)

* Tue Dec 15 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.6.0-1.rh1
- Release 78.6.0
- Disable system nss (rhbz#1908018)

* Thu Nov 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.5.0-2.rh2
- Build Release 78.5.0-rh2
- HTTPS Everywhere 2020.11.17

* Mon Nov 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.5.0-1.rh1
- Release 78.5.0

* Tue Oct 27 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.4.0-2.rh1
- Patched for rhbz#1891234

* Fri Oct 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.4.0-1.rh1
- Release 78.4.0
- Regenerate cbindgen-0.14.3
- Patched for using Rust-1.47 (mzbz#1663715)

* Wed Oct 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.3.1-2.rh1.test
- PGO build test

* Thu Oct 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.3.1-1.rh1
- Release 78.3.1 (rh1)
- Patched for mzbz#1640567

* Wed Sep 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.3.0-2.rh1
- Rebuild for libevent-2.1.12

* Mon Sep 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.3.0-1.rh1
- Release 78.3.0 (rh1)

* Fri Sep 18 2020 Miro Hrončok <mhroncok@redhat.com> - 78.2.0-7.rh6
- Use python3 instead of python2 for build

* Wed Sep 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-6.rh6
- Build Release 78.2.0-rh6

* Tue Sep 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-5.rh5
- Add configure options to allow loading unsigned bundled addons

* Sun Sep 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-4.rh5
- Build Release 78.2.0-rh5

* Sun Sep 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-3.rh4
- Build Release 78.2.0-rh4
- PPC64le build disabled on Fedora 33

* Thu Sep 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-2.rh3
- Build Release 78.2.0-rh3
- Reintroduce PPC64LE builds

* Tue Aug 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-1.rh2
- Release 78.2.0

* Sun Aug 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.2.0-0.1.rc1.rh1.test
- Release Candidate 78.2.0

* Wed Jul 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.0.1-2.rh1.test
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.0.1-1.rh1.test
- Release 78.0.1
- Disable crash reporter

* Wed Jul 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 78.0-1.rh1.test
- Release 78.0

* Tue Jun 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.9.0-1.rh2
- Release 68.9.0

* Thu May 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.9.0-0.1.rc1.rh1
- Release candidate 68.9.0 build1

* Wed May 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.8.0-5.rh1
- Explicit perl-interpreter BR dependency

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 68.8.0-4.rh1
- Rebuild for ICU 67

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 68.8.0-3.rh1
- Rebuild for ICU 67
- Remove libgen references

* Fri May 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 68.8.0-2.rh1
- Don't exclude aarch64 architecture

* Tue May 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.8.0-1.rh1
- Release 68.8.0
- Exclude s390x architecture

* Tue Apr 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.7.0-1.rh1
- Release 68.7.0

* Sun Mar 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.6.0-4.rh4
- Remove libgen addon

* Sat Mar 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.6.0-3.rh3
- Source code archive regenerated
- HTTPS-everywhere updated to the 2020.3.16

* Wed Mar 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.6.0-2.rh2
- Remove useless build dependency

* Tue Mar 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.6.0-1.rh2
- Release 68.6.0

* Sat Mar 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.6.0-0.1.rc1.rh1
- Release candidate 68.6.0

* Mon Feb 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.5.0-1.rh1
- Release 68.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 68.4.1-2.rh1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Undefine strict symbol checks on s390x

* Sat Jan 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.4.1-1.rh1
- Release 68.4.1 (release build)

* Wed Jan 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.4.0-2.rh2
- Release 68.4.0 (release build)

* Tue Jan 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.4.0-1.rh2.test
- Release 68.4.0
- Test build for ARM and s390x
- Patched for mzbz#1526653 to disable wasm on ARM
- Add --disable-av1 build option for ARM

* Fri Jan 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.4.0-0.2.rc1.rh1
- New rebuild of source archive (extensions updated)
- Use rh prefix instead of gnu

* Wed Jan 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 68.4.0-0.1.rc1.gnu1
- Release candidate 68.4.0
- Fix rhbz#1785956

* Thu Dec 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.3.0-2.gnu1
- Appdata file updated
- Description updated

* Wed Dec 04 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.3.0-1.gnu1
- Release 68.3.0
- Patch for cbindgen/rust-1.39

* Wed Nov 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.3.0-0.1.rc2.gnu1
- Release candidate 68.3.0

* Fri Nov 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.2.0-4.gnu3.test
- Build release 68.2.0-gnu3
- Undo latest change
- Patched for rust-1.39+

* Sun Nov 10 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.2.0-3.gnu2
- Do not remove cose.manifest files

* Fri Nov 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.2.0-2.gnu2
- Build release 68.2.0-gnu2
- HTTPS-Everywhere 2019_11_7
- Use always system vpx (Fedora 30+)
- Patched for Mozilla bug #1556602

* Tue Oct 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.2.0-1.gnu1
- Release 68.2.0

* Tue Sep 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.1.0-1.gnu1
- Release 68.1.0
- Incorporate Wayland patches from Firefox 68

* Sun Sep 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.0.2-5.gnu3
- Rebuild after retiring of Python2

* Fri Aug 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.0.2-4.gnu3
- Enable langpacks

* Wed Aug 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.0.2-3.gnu3
- gnu3 build release

* Mon Aug 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.0.2-2.gnu2
- WebRTC always disabled
- Do not build langpacks
- gnu2 build release
- Disable MOZ_SERVICES_SYNC

* Thu Aug 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 68.0.2-1.gnu1
- Release 68.0.2
- Import cbindgen stuff from Firefox package
- Do not use sqlite from system

* Sun Jul 28 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-6.gnu1
- Add patch to fix the addon installation

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 60.8.0-6.gnu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-5.gnu1
- Enable WebRTC on ppc64le

* Fri Jul 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-4.gnu1
- Remove redundant Python2 dependencies 

* Thu Jul 11 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-3.gnu1
- Remove filtering of private libraries
- Enable webrtc on %%{ix86} x86_64 only

* Wed Jul 10 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-2.gnu1
- Use mozilla-1512162.patch on Fedora 30+ only (GCC-9)

* Tue Jul 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.8.0-1.gnu1
- Release 60.8.0

* Sat Jun 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.7.2-1.gnu1
- Release 60.7.2

* Wed Jun 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.7.1-1.gnu1
- Release 60.7.1
- Do not list Git-tracked icecat.rpmlintrc as source

* Tue May 28 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.7.0-2.gnu2
- Build release 60.7.0-gnu2

* Mon May 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.7.0-1.gnu1
- Release 60.7.0

* Sun May 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.3-2.gnu2
- Build release 60.6.3-gnu2

* Thu May 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.3-1.gnu1
- Release 60.6.3 (bugfix mozb #1549249)

* Mon May 06 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.2-1.gnu1
- Release 60.6.2 (bugfix mozb #1549061)

* Sat Apr 06 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.1-2.gnu2
- Source archive rebuilt (gnu2)
- Update extensions
- Use bundled https-everywhere extension

* Fri Mar 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.1-1
- Release 60.6.1
- Wayland backend made default starting from Fedora 31 (rhbz#1691852)

* Thu Mar 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.0-2
- Patched for building with newer glibc (2.29.9000-4) (mozilla #1533969)
- Excluded on ARM (rhbz #1658940)
- Language files re-based

* Tue Mar 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.6.0-1
- Release 60.6.0
- Enable languages

* Sun Mar 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.5.2-1
- Release 60.5.2
- Disable Werror-format-security flags
- Enable linker=gold on ARM
- Try to fix libevent LD path

* Thu Feb 14 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.5.1-1
- Release 60.5.1
- Conditional macro for libvpx support

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 60.5.0-2
- rebuilt (libvpx)

* Tue Jan 29 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.5.0-1
- Release 60.5.0

* Sun Jan 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 60.4.0-2
- Make Wayland support default on fedora 30+
- Enable Wayland support
- Drop old patches
- Backported Wayland related code from Firefox 63
- Added fix for mozbz#1507475 - crash when display changes 

* Wed Dec 12 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.4.0-1
- Upstream release 60.4.0

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 60.3.0-4
- rebuild for hunspell-1.7.0

* Sat Nov 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.3.0-3
- Rebuild with latest changes from Gnuzilla

* Wed Oct 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.3.0-2
- Drop UserAgent patch (rhbz#1644898)

* Wed Oct 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.3.0-1
- Upstream release 60.3.0

* Wed Oct 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.2.2-2
- Drop UserAgent patch (rhbz#1644898)

* Wed Oct 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.2.2-1
- Upstream release 60.2.2

* Fri Sep 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.2.1-1
- Upstream release 60.2.1

* Fri Sep 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 60.2.0-0.1
- Pre-release 60.2.0
- Integrate firefox patches for wayland (disabled)
- Setting of upstream patches for 60 releases
- Manpage updated
- Include languages
- Use options to reduce memory requirements at ld runtime on ix86

* Sun Aug 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.9.0-1
- Update to 52.9.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 52.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 52.8.1-2
- Rebuild for ICU 62

* Thu Jun 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.8.1-1
- Update to 52.8.1
- Add icecat.rpmlintrc

* Wed Jun 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.8.0-3
- Source tarball re-created without non-free code

* Tue Jun  5 2018 Tom Callaway <spot@fedoraproject.org> - 52.8.0-2
- remove non-free files from tarball

* Sat May 12 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.8.0-1
- Update to 52.8.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 52.7.3-2
- Rebuild for ICU 61.1

* Tue Mar 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.7.3-1
- Update to 52.7.3

* Tue Mar 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.7.2-1
- Update to 52.7.2

* Sat Mar 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.7.0-1
- Update to 52.7.0

* Tue Feb 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.6.0-7
- HTTPS Everywhere updated to 2018.1.11
- "goteo.org payments with free JS" updated to 1.1
- "LibreJS compatible Pay.gov" updated to 1.3
- "Reveal hidden HTML" updated to 1.6
- Enabled WebRTC, but prevent leaking the LAN ip

* Sun Feb 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.6.0-6
- Add gcc gcc-c++ BR

* Sun Feb 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.6.0-5
- Rebuild for libevent-2.1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 52.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.6.0-3
- Rebuild for libvpx again

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> - 52.6.0-2
- rebuild for new libvpx

* Wed Jan 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.6.0-1
- Update to 52.6.0

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 52.5.3-4
- Remove obsolete scriptlets

* Sun Jan 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.5.3-3
- Set build against NSS-3.34/NSPR-4.17.0 at least

* Sun Jan 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 52.5.3-2
- Patched for mozilla bug-1427870

* Sun Dec 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.5.3-1
- Update to 52.5.3
- Use 'with-l10n' option

* Fri Dec 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.5.2-1
- Update to 52.5.2
- WebRTC is always disabled
- Add JACK audio backend (bz#1528742)

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.3.0-4
- Appdata file moved into metainfo data directory

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 52.3.0-3
- rebuild for hunspell-1.5.2

* Sat Sep 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.3.0-2
- Enable language files

* Wed Aug 16 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.3.0-1
- Update to 52.3.0

* Thu Aug 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.2.1-1
- Update to 52.2.1
- ICU source code patched to work on big-endian architectures

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 52.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 52.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat May 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.1.0-2
- Fix language files

* Sat May 06 2017 Jens Lody <fedora@jenslody.de> - 52.1.0-1
- Update to 52.1.0
- Remove obsolete firefox-debug.patch
- Spec-file: fix typo in description

* Sun Apr 16 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.2-3
- Enable languages

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.2-2
- Update to 52.0.2
- Add patch for mozbz#1158076 - enable dark theme by pref

* Sun Mar 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.1-5
- Skia support disabled on ARM/ix86 builds (failed for memory exhausted)

* Sun Mar 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.1-4
- Downgrade optimization level on ARM builds (failed for memory exhausted)
- Use one job with Make on ix86

* Wed Mar 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.1-3
- Added fix for mozbz#1158076

* Mon Mar 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.1-2
- Set cflags/libs options for NSS/NSPR
- Add --disable-elf-hack

* Sun Mar 19 2017 Antonio Trande <sagitter@fedoraproject.org> - 52.0.1-1
- Update to 52.0.1
- All patches synchronized with firefox

* Mon Mar 06 2017 Jens Lody <fedora@jenslody.de> - 45.7.0-8
- aarch64build-fix (taken from mozjs45)
- include aarch64 again

* Sun Mar 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.7.0-7
- Build with language files
- Use new source archive
- Exclude aarch64

* Sun Mar 05 2017 Jens Lody <fedora@jenslody.de> - 45.7.0-6
- do not set debug-build-flag

* Sun Mar 05 2017 Jens Lody <fedora@jenslody.de> - 45.7.0-5
- (Re-)add language-download.script and make Source-tag unconditional.
- Fix debug build.

* Sat Feb 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.7.0-3
- Optimization flags disabled on arm/arm64

* Thu Feb 16 2017 Jens Lody <fedora@jenslody.de> - - 45.7.0-3
- Fix gcc7 build, with backport of fix for mozb#1269171

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 45.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.7.0-1
- Update to 45.7.0

* Sat Jan 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-7
- Test for trying ICU patch

* Fri Jan 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-6
- System ICU disabled on Fedora > 25

* Fri Jan 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-5
- Patched to make compatible with NSS 3.28.1 (bz#1414987)

* Thu Jan 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-4
- Conformed to new rules for scriptlets

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 45.5.1-3
- rebuild for hunspell-1.5.4

* Fri Dec 02 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-2
- Keep workaround for bz#1332926

* Fri Dec 02 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.5.1-1
- Update to 45.5.1

* Sun Nov 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.6.beta
- Debug build
- Debug builds patched (mozb#1013882)
- Patched for removing unnecessary warns

* Sun Sep 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.5.beta
- Drop obsolete patch

* Sat Sep 03 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.4.beta
- Use MOZ_SMP_FLAGS instead of MOZ_MAKE_FLAGS

* Thu Sep 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.3.beta
- Update desktop file's translations
- Enable jemalloc

* Thu Sep 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.2.beta
- Disable optimization on ARM

* Mon Aug 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 45.3.0-0.1.beta
- Update to 45.3.0 (beta)
- Drop old patches
- Reset default compiler flags
- Filtering private libraries

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 38.8.0-13
- rebuild for libvpx 1.6.0

* Wed Jun 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-12
- Optimization level increased to -O1

* Tue Jun 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-11
- Fix appadata file's tags

* Sun Jun 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-10
- Rebuild with newest icecat-38.8.0-gnu2 source archive (24 June)

* Sun Jun 26 2016 Jens Lody <fedora@jenslody.de> - 38.8.0-9
- Workaround for #1332926

* Sat Jun 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-8
- Set MOZ_SMP_FLAGS

* Sat Jun 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-7
- Undo latest change

* Sat Jun 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-6
- Set C++14 standard flag

* Fri Jun 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-5
- Set C++ standard flag

* Fri Jun 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-4
- Disable install stripping
- Disable builds for debugging

* Fri Jun 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-3
- Enable builds for debugging

* Fri May 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-2
- Remove additional flag

* Fri May 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.8.0-1
- Update to 38.8.0

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 38.7.1-4
- rebuild for hunspell 1.4.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 38.7.1-3
- rebuild for ICU 57.1

* Sat Apr 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.7.1-2
- Downgrade optimization level on ARM

* Fri Apr 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.7.1-1
- Update to 38.7.1

* Thu Feb 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.6.0-1
- Update to 38.6.0
- Patched for GCC6 builds
- Cut off Provides bundled libraries except xulrunner

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 38.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild 

* Mon Jan 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.5.2-4
- Fix description of appdata file

* Mon Jan 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.5.2-3
- Fix validating of desktop file

* Sun Jan 03 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.5.2-2
- .desktop .appdata and .metainfo files renamed (bz#1295234)

* Fri Jan 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 38.5.2-1
- Update to 38.5.2

* Fri Dec 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.5.0-1
- Update to 38.5.0

* Tue Dec 08 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.4.0-3
- Force -fstack-protector-all flag (bz#1283307)

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 38.4.0-2
- rebuild for libvpx 1.5.0

* Tue Nov 17 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.4.0-1
- Update to 38.4.0

* Tue Nov 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-12
- ARM neon support disabled on aarch64

* Sat Oct 31 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-11
- Rebuild for ICU 56

* Wed Oct 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-10
- Rebuild with RPM_LD_FLAGS

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 38.3.0-9
- rebuild for ICU 56.1

* Tue Oct 20 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-8
- Active hardened_build

* Tue Oct 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-7
- Rebuilt with updated Addons

* Mon Oct 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-6
- Fixed header files directory for freetype-2.6.1

* Mon Oct 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-5
- Languages packaged

* Tue Oct 06 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-4
- WebRTC disabled on extra arches

* Tue Oct 06 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-3
- Updated appdata and manpage files

* Mon Oct 05 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-2
- Disabled crashreporter on F22+

* Sat Oct 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 38.3.0-1
- Update to 38.3.0
- Patches updated
- Language files not packaged
- Build defined for Gtk3 

* Thu Aug 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.8.0-5
- Added backported patch for CVE-2015-4473_4482_4488_4489_4491_4492 vulnerabilities

* Thu Aug 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.8.0-4
- Added backported patch for CVE-2015-4495 vulnerability

* Tue Jul 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.8.0-3
- Fixed on secondary arches

* Mon Jul 20 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.8.0-2
- Un-bundle libvpx-1.4

* Fri Jul 17 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.8.0-1
- Update to 31.8.0

* Sun Jul 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-8
- Packaged IceCat 31.7 in Fedora 21

* Fri Jul 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-7
- Fix .metainfo.xml file

* Thu Jul 02 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-6
- Added .metainfo.xml file

* Thu Jun 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-5
- Added options --enable-tree-freetype --enable-stdcxx-compat
- Added patch for Freetype-2.6 headers

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-3
- Re-built locale files
- Re-organized mozconfig options
- Compiled with ccache

* Wed Jun 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-2
- Unpacked files found

* Mon Jun 08 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.7.0-1
- Update to 31.7.0
- Make sure locale works for langpacks
- Set default bookmarks
- Made appdata file
- devel package obsoleted

* Mon May 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.6.0-6
- Required VPX from system for < F23

* Sun May 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.6.0-5
- libvpx-1.3.0 bundled only in >= F23

* Tue Apr 07 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.6.0-4
- Disable optimization flags (when GCC5 compiles) on ARM

* Tue Apr 07 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.6.0-3
- Compiled against bundle libvpx-1.3.0

* Mon Apr 06 2015 Tom Callaway <spot@fedoraproject.org> - 31.6.0-2
- Rebuild for libvpx 1.4.0

* Sat Apr 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.6.0-1
- Update to 31.6.0

* Mon Mar 16 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.5.0-2
- New rebuild to fix profile's storage problem

* Thu Mar 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.5.0-1
- Update to 31.5.0
- Patched to fix Mozilla Bug1021171
- crashreporter disabled on > F21
- Improved .desktop file

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 31.4.0-5
- Bump for rebuild.

* Mon Feb 02 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.4.0-4
- Desktop file missing %%u (bz#1188078)

* Sat Jan 31 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.4.0-3
- Annulled the user-agent string customization

* Thu Jan 29 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.4.0-2
- Added %%license macro

* Thu Jan 29 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.4.0-1
- Update to 31.4.0
- Added MPLv2.0 license of HTML5-video-everywhere extension
- Description updated

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 31.2.0-8
- rebuild for ICU 54.1

* Wed Jan 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-7
- Package now requires system-bookmarks (bz#1184297)

* Wed Nov 26 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-6
- libjpeg-turbo unbundled (bz#1164815)

* Thu Nov 06 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-5
- Added -Wno-error=declaration-after-statement
- Built against GStreamer-1.0
- Package compiled against bundled JPEG

* Sat Oct 25 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-4
- Removed -fexceptions flags from Fedora optflags

* Thu Oct 23 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-3
- Added -Wformat-security flags
- Added special link flags for ARM

* Wed Oct 22 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-2
- Fixed compiler flags

* Tue Oct 21 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.2.0-1
- Update to 31.2.0
- Added 'configure' options
- Built against system NSS/NSPR

* Thu Oct 16 2014 Antonio Trande <sagitter@fedoraproject.org> - 31.1.1-1
- Update to 31.1.1
- New bundled files (bz#1153135)
- Static sub-package is not built anymore
- Man-page updated
- Spyblock addon included

* Tue Aug 26 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-14
- Added "Provides: webclient"
- Installed manpage file

* Tue Aug 19 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-13
- Removed system xulrunner conditional
- Ghosted all .xpi language files (handled by %%find_lang)
- Added BSD, ISC, MIT, Apache2.0 licenses

* Sat Aug 09 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-12
- Removed HTTPS-everywhere RequestPolicy extensions (patch7)

* Thu Jul 24 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-11
- Remove precompiled .egg files
- Remove bundled jar/class files
- Delete chrpaths
- Added 'Public Domain' license
- Added a patch for using system Python Virtualenv (patch6)

* Wed Jul 16 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-10
- Added freetype2 system-headers list for Fedora>=21 (patch5)

* Fri Apr 04 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-9
- Defined other bundled() Provides

* Sat Mar 29 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-8
- Use system nspr

* Wed Mar 26 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-7
- Removed much more bundled files (added related BR packages)
- Build browser and xulrunner
- Added freetype2 reference patch

* Thu Feb 27 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-6
- Sources patched to use system ogg/opus/vorbis libraries
- Build browser alone

* Wed Feb 05 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-5
- Fix some executable permissions
- Added some tricks
- Build browser and xulrunner
- Defined a conditional macro for xulrunner
- Built a static sub-package
- Added COPYING separated license files
- Added bundled() Provides

* Mon Jan 27 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-4
- Build browser alone
- Added libffi/libpng linkage from system to .mozconfig file
- Added a patch to exclude APNG support missing error for libpng
- Added libpng-devel BR

* Tue Jan 14 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-3
- Removed bundled files
- Added nspr/nss Requires

* Wed Jan 08 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-2
- Timestamp preserving for the 'install' commands
- Added a comment interpretation to the License tag
- Defined all command calls in normal mode 

* Sun Jan 05 2014 Antonio Trande <sagitter@fedoraproject.org> - 24.0-1
- Initial package

