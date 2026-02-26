### Naming ###
# Set to true if it's going to be submitted as update
%global release_build 1

# Set new source-code build version for Fedora and, not necessarily, for upstream too
%global redhat_ver rh1

ExcludeArch: %{ix86} %{arm}

# Bundled cbindgen makes build slow.
# Enable only if system cbindgen is not available.
%global use_bundled_cbindgen  0

####################

### Optimization ###
# Builds for debugging
%global debug_build   0

# Downgrade optimization
%global less_optbuild 0

# Build PGO+LTO on x86_64 and aarch64 only
%ifarch x86_64 %{arm64}
%if 0%{?release_build}
%global build_with_pgo 1
%global pgo_wayland    1
%global launch_wayland_compositor 1
%else
%global build_with_pgo 0
%global pgo_wayland    0
%global launch_wayland_compositor 0
%endif
%endif

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
%ifarch s390x %{power64}
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

# Use clang?
%bcond_without toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1908792
# https://bugzilla.redhat.com/show_bug.cgi?id=2255254
%global __provides_exclude_from ^%{icecatappdir}
%global __requires_exclude ^(%%(find %{buildroot}%{icecatappdir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

Name:    icecat
Epoch:   4
Version: 140.8.0
Release: %autorelease -e %{redhat_ver}
Summary: GNU version of Firefox browser

# Tri-licensing scheme for Gnuzilla/IceCat in parentheses, and licenses for the extensions included
License: (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND GPL-3.0-or-later AND MIT AND BSD-4-Clause-UC AND ISC AND Apache-2.0 AND MPL-2.0
URL:     http://www.gnu.org/software/gnuzilla/

## Source archive created by scripts based on Gnuzilla files.
## All modified files are hosted in a dedicated fork repository:
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

# Fedora specific patches
Patch221: firefox-nss-addon-hack.patch
Patch224: %{name}-GLIBCXX-fix-for-GCC-12.patch
Patch225: %{name}-build-c11-threads-avail.patch
Patch227: %{name}-build-seccomp.patch

# ARM run-time patch
Patch226: rhbz-1354671.patch

# Fix crash on ppc64le (mozilla#1512162)
Patch423: mozilla-1512162.patch

# PGO/LTO patches
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
BuildRequires: nodejs, /usr/bin/node
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
BuildRequires: python3-orjson
BuildRequires: perl-interpreter
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(libcurl)
%if %{with pulseaudio}
BuildRequires: pulseaudio-libs-devel
%endif
BuildRequires: llvm
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10
BuildRequires:  clang19
BuildRequires:  clang19-libs
BuildRequires:  llvm19-devel
BuildRequires:  compiler-rt19
%global llvm_suffix -19
%else
BuildRequires:  clang17
BuildRequires:  clang17-libs
BuildRequires:  llvm17-devel
BuildRequires:  compiler-rt17
%global llvm_suffix -17
%endif
%if "%toolchain" == "clang"
BuildRequires:  lld
%endif
BuildRequires: rust
BuildRequires: rustfmt

%if 0%{?pgo_wayland}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  mutter
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gnome-settings-daemon
BuildRequires:  mesa-dri-drivers
BuildRequires:  mesa-libEGL
BuildRequires:  xorg-x11-server-Xwayland
BuildRequires:  dbus-x11
BuildRequires:  gnome-keyring
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
Requires: %{name} = 4:%{version}-%{release}
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

# Fedora patches
%if 0%{?fedora}
%patch -P 221 -p 1 -b .firefox-nss-addon-hack
%endif
%patch -P 224 -p 1 -b .glibcxx
%if 0%{?fedora} >= 44
%patch -P 225 -p 1 -b .build-c11
%patch -P 227 -p 1 -b .build-seccomp
%endif

# ARM64
%ifarch %{arm64}
%patch -P 226 -p 1 -b .1354671
%endif

%ifarch %{power64}
%patch -P 423 -p 1 -b .1512162
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

%if "%toolchain" == "clang"
echo "ac_add_options --with-libclang-path=`llvm-config%{?llvm_suffix} --libdir`" >> .mozconfig
%endif

%ifarch s390x %{arm64}
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

%ifarch s390x
MOZ_OPT_FLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-g/-g1/')
# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g1 from line above and breaks building on s390
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "
%endif

# We don't want firefox to use CK_GCM_PARAMS_V3 in nss
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DNSS_PKCS11_3_0_STRICT"

%if "%toolchain" != "clang"
%ifarch s390x %{power64} %{arm64}
MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%endif

%ifarch s390x
export RUSTFLAGS="-Cdebuginfo=0"
%endif

#  error "STL code can only be used with -fno-exceptions"
CXXFLAGS=$(echo "$MOZ_OPT_FLAGS" | %{__sed} -e 's/-fexceptions/-fno-exceptions/')
export CXXFLAGS="$CXXFLAGS"
export CXXFLAGS="$CXXFLAGS -fpermissive -std=gnu++17"

export CFLAGS="$MOZ_OPT_FLAGS -std=gnu17"
export LDFLAGS="%{__global_ldflags} $MOZ_LINK_FLAGS -L%{_libdir} -L%{icecatappdir}"
export PREFIX='%{_prefix}'
export LIBDIR='%{_libdir}'
export PKG_CONFIG="`which pkg-config`"
export PYTHON='%{__python3}'

%if "%toolchain" == "clang"
echo "export LLVM_PROFDATA=\"llvm-profdata\"" >> .mozconfig
echo "export AR=\"llvm-ar\"" >> .mozconfig
echo "export NM=\"llvm-nm\"" >> .mozconfig
echo "export RANLIB=\"llvm-ranlib\"" >> .mozconfig
echo "ac_add_options --enable-linker=lld" >> .mozconfig
echo "export CC=clang%{?llvm_suffix}" >> .mozconfig
echo "export CXX=clang++%{?llvm_suffix}" >> .mozconfig
%else
echo "export CC=gcc" >> .mozconfig
echo "export CXX=g++" >> .mozconfig
echo "export AR=\"gcc-ar\"" >> .mozconfig
echo "export NM=\"gcc-nm\"" >> .mozconfig
echo "export RANLIB=\"gcc-ranlib\"" >> .mozconfig
%endif

%if 0%{?build_with_pgo}
echo "ac_add_options MOZ_PGO=1" >> .mozconfig
# PGO build doesn't work with ccache
export CCACHE_DISABLE=1
%endif

# Require 4 GB of RAM per CPU core
%global _smp_tasksize_proc 4096
%if %{?less_optbuild}
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j1\"" >> .mozconfig
%else
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j%{_smp_build_ncpus}\"" >> .mozconfig
%endif

echo "mk_add_options MOZ_SERVICES_SYNC=1" >> .mozconfig
echo "export STRIP=/bin/true" >> .mozconfig

%if 0%{?launch_wayland_compositor}
cp -p %{SOURCE19} .
. ./run-wayland-compositor
%endif

%if %{?debug_build}
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_DEBUG=true
%endif

#Use python 3.11 for mach
sed -i -e 's|#!/usr/bin/env python3|#!/usr/bin/env python3.11|' mach

./mach build -v 2>&1 | cat - || exit 1

%if 0%{?build_with_pgo}
kill $MUTTER_PID
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

%if %{with langpacks_subpkg}
%files
%dir %{langpackdir}
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
%{icecatappdir}/dependentlibs.list
%{icecatappdir}/pingsender
%{icecatappdir}/gmp-clearkey/
%ifarch %{arm64} riscv64
%{icecatappdir}/v4l2test
%endif

%changelog
%autochangelog
