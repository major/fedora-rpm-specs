### Naming ###
# Set to true if it's going to be submitted as update
%global release_build 1

# Set new source-code build version for Fedora and, not necessarily, for upstream too
%global redhat_ver rh1

ExcludeArch: %{ix86} %{arm}

# Bundled cbindgen makes build slow.
# Enable only if system cbindgen is not available.
%global use_bundled_cbindgen  1

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
%global pgo_wayland    0
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
%bcond_without langpacks

%if %{with langpacks}
%bcond_without langpacks_subpkg
%endif

# Define installation directories
%global icecatappdir %{_libdir}/%{name}
# Define language files directory
%global langpackdir  %{icecatappdir}/langpacks

%global icecat_ver   %{name}-%{version}
%global icecat_devel %{name}-devel-%{version}

%global toolkit_gtk3  1

# Big endian platforms
%ifarch s390x
# Javascript Intl API is not supported on big endian platforms right now:
# https://bugzilla.mozilla.org/show_bug.cgi?id=1322212
%global big_endian    1
%endif

%if 0%{?fedora}
%global system_nss  1
%else
%global system_nss  0
%endif
%if %{?system_nss}
%global nspr_version 4.32
%global nspr_build_version %{nspr_version}
%global nss_version 3.100
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

# Use clang?
%global build_with_clang  1

# https://bugzilla.redhat.com/show_bug.cgi?id=1908792
# https://bugzilla.redhat.com/show_bug.cgi?id=2255254
%global __provides_exclude_from ^%{icecatappdir}
%global __requires_exclude ^(%%(find %{buildroot}%{icecatappdir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

Name:    icecat
Epoch:   2
Version: 115.19.0
Release: %autorelease -e %{redhat_ver}
Summary: GNU version of Firefox browser

# Tri-licensing scheme for Gnuzilla/IceCat in parentheses, and licenses for the extensions included
License: (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND GPL-3.0-or-later AND MIT AND BSD-4-Clause-UC AND ISC AND Apache-2.0 AND MPL-2.0
URL:   http://www.gnu.org/software/gnuzilla/

## Source archive created by scripts based on Gnuzilla files.
## Modified files are hosted in a dedicated fork repository:
## https://gitlab.com/anto.trande/icecat
Source0: %{name}-%{version}-%{redhat_ver}.tar.bz2

Source2: %{name}.png
Source3: %{name}-mozconfig-common

# Language files downloaded by source7 script
%if %{with langpacks}
Source4:  %{name}-%{version}-langpacks.tar.gz
%endif

# All license files
# Download from http://www.gnu.org/licenses
# Download from http://www.mozilla.org/MPL/1.1/index.txt
# Download from https://www.mozilla.org/MPL/2.0/index.txt
Source5: %{name}-COPYING-licensefiles.tar.gz

Source7: %{name}-lang_download.sh

# Desktop files
Source10: %{name}.appdata.xml
Source13: %{name}.sh.in
Source14: %{name}.desktop

# cbingen
Source17: cbindgen-vendor.tar.xz
Source18: node-stdout-nonblocking-wrapper

Source19: run-wayland-compositor

# Build patches
# Fixes installation of those addons which don't have ID on IceCat ("Cannot find id for addon" error).
Patch1: %{name}-fix_addon_installation.patch
Patch2: %{name}-commasplit.patch
Patch5: rhbz-1219542-s390-build.patch

# With clang LLVM 16 rust-bindgen 0.56.0 is too old, combined
# https://github.com/rust-lang/rust-bindgen/pull/2319
# https://github.com/rust-lang/rust-bindgen/pull/2339
Patch7:  rust-bindgen-2319-2339.patch

# Needed with rust 1.70
# https://github.com/mozilla/mp4parse-rust/commit/8b5b652d38e007e736bb442ccd5aa5ed699db100
Patch8:  mp4parse-rust-8b5b652d38e007e736bb442ccd5aa5ed699db100.patch 

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
Patch603: %{name}-gcc-always-inline.patch

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

BuildRequires: pango-devel
BuildRequires: pciutils-libs
BuildRequires: pipewire-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3.11-devel
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
%if 0%{?build_with_clang}
BuildRequires:  clang17
BuildRequires:  clang17-libs
BuildRequires:  llvm17-devel
BuildRequires:  lld
%global llvm_suffix -17
%else
BuildRequires:  clang
BuildRequires:  clang-libs
BuildRequires:  llvm-devel
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

%if 0%{?fedora}
BuildRequires: fedora-bookmarks
Requires: fedora-bookmarks
%endif

Suggests: mozilla-ublock-origin
Provides: webclient

%if 0%{?fedora} >= 40
Obsoletes:  icecat-wayland < 2:115.19.0-1
Obsoletes:  icecat-x11 < 2:115.19.0-1
%endif

%description
GNU IceCat is the GNU version of the Firefox ESR browser.
Extensions included to this version of IceCat:

 * LibreJS
   GNU LibreJS aims to address the JavaScript problem described in the article
   "The JavaScript Trap" of Richard Stallman.
   
 * JShelter: Mitigates potential threats from JavaScript, including fingerprinting,
   tracking, and data collection. Slightly modifies the results of API calls,
   differently on different domains, so that the cross-site fingerprint is not
   stable. Applies security counter-measures that are likely not to break web pages.
   Allows fine-grained control over the restrictions and counter-measures applied
   to each domain. 

 * A set of companion extensions for LibreJS by Nathan Nichols
   are pre-installed, and provide workarounds to use some services at USPS,
   RSF.org, SumOfUs.org, pay.gov, McDonalds, goteo.org and Google Docs
   without using nonfree JavaScript.

 * A series of configuration changes and tweaks were applied to ensure that
   IceCat does not initiate network connections that the user has not explicitly
   requested. This implies not downloading feeds, updates, blacklists or any
   other similar data needed during startup.

%if %{with langpacks_subpkg}
%package langpacks
Summary: IceCat langpacks
Requires: %{name} = 2:%{version}-%{release}
%description langpacks
The icecat-langpacks package contains all the localization
and translations langpack add-ons.
%files langpacks -f %{name}.lang
%dir %{langpackdir}
%endif

%prep
%autosetup -N -n %{name}-%{version}

# Copy license files
tar -xf %{SOURCE5}

%patch -P 1 -p 1 -b .fix_addon_installation
%patch -P 2 -p 1 -b .commasplit
%ifarch s390x
%patch -P 5 -p 1 -b .rhbz-1219542-s390
%endif

%if 0%{?disable_elfhack}
%patch -P 41 -p 1 -b .disable-elfhack
%endif

# Fedora patches
%patch -P 219 -p 1 -b .rhbz-1173156
%if 0%{?fedora}
%patch -P 221 -p 1 -b .firefox-nss-addon-hack
%endif
%patch -P 224 -p 1 -b .glibcxx

# ARM64
%ifarch %{arm64}
%patch -P 40 -p 1 -b .aarch64-skia
%patch -P 226 -p 1 -b .1354671
%endif

%patch -P 402 -p 1 -b .1196777
%ifarch %{power64}
%patch -P 423 -p 1 -b .1512162
%endif

%patch -P 54 -p 1 -b .1669639

# PGO patches
%if 0%{?build_with_pgo}
%if !%{build_with_clang}
%patch -P 600 -p 1 -b .pgo
%patch -P 602 -p 1 -b .1516803
%endif
%endif
%patch -P 603 -p1 -b .inline

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
%ifarch x86_64
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
echo "ac_add_options --enable-av1" >> .mozconfig

%if 0%{?debug_build}
echo "ac_add_options --enable-debug" >> .mozconfig
echo "ac_add_options --disable-optimize" >> .mozconfig
echo "ac_add_options --enable-rust-debug" >> .mozconfig
%else
%global optimize_flags "none"
%ifarch s390x
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
%if %{with langpacks}
echo "ac_add_options --with-l10n-base=$PWD/l10n" >> .mozconfig
%endif

# Clang
%if 0%{?build_with_clang}
echo "ac_add_options --with-clang-path=`which clang%{?llvm_suffix}`" >> .mozconfig
%endif
echo "ac_add_options --with-libclang-path=`llvm-config%{?llvm_suffix} --libdir`" >> .mozconfig

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

# note: if you need to support cargo 1.38 or earlier, you can symlink `config` to `config.toml`
pushd .cargo
mv config config.toml
popd

env CARGO_HOME=.cargo cargo install cbindgen
export PATH=`pwd`/.cargo/bin:$PATH
%else
export CBINDGEN=/usr/bin/cbindgen
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

%ifarch s390x
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-g/-g1/')
# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g1 from line above and breaks building on s390
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "
%endif

# We don't wantfirefox to use CK_GCM_PARAMS_V3 in nss
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DNSS_PKCS11_3_0_STRICT"

%if !0%{?build_with_clang}
%ifarch s390x %{power64} %{arm64}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads -Wl,--print-memory-usage"
%endif
%endif
%ifarch s390x
export RUSTFLAGS="-Cdebuginfo=0"
%endif

export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS="$MOZ_OPT_FLAGS -fpermissive"
export LDFLAGS=$MOZ_LINK_FLAGS

export PREFIX='%{_prefix}'
export LIBDIR='%{_libdir}'
export PKG_CONFIG="`which pkg-config`"
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
%ifarch s390x %{arm64}
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

%if %{?debug_build}
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_DEBUG=true
%endif

	
export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=system
#Use python 3.11 for mach
sed -i -e 's|#!/usr/bin/env python3|#!/usr/bin/env python3.11|' mach
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
%if 0%{?fedora}
%global default_bookmarks_file %{_datadir}/bookmarks/default-bookmarks.html
cp -p %{default_bookmarks_file} objdir/dist/bin/browser/chrome/en-US/locale/browser/bookmarks.html
%endif

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
#

##Extract langpacks, make any mods needed, repack the langpack, and install it.
echo > %{name}.lang
%if %{with langpacks}
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

%if %{with langpacks_subpkg}
%files
%else
%files -f %{name}.lang
%endif
%doc README.* AUTHORS
%license LICENSE COPYING-*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}*.png
%{_metainfodir}/*.appdata.xml
%dir %{icecatappdir}
%{icecatappdir}/glxtest
%{icecatappdir}/vaapitest
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
%if %{without langpacks_subpkg}
%if %{with langpacks}
%dir %{icecatappdir}/langpacks
%endif
%endif

%changelog
%autochangelog
