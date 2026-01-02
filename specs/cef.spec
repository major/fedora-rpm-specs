## CEF README
# This spec file is based on chromium.spec, as CEF is largely a Chromium
# wrapper/distribution. To keep things maintainable, the CEF version
# attempts to track the chromium version released in Fedora where possible,
# and the changes in this file are bracketed in `## CEF` and `## END CEF`
# comments. Updates to the underlying Chromium version can be achieved by
# merging in the changes to chromium.spec, or by manually re-applying the
# CEF changes to the new Chromium spec.
## END CEF

%define _lto_cflags %{nil}
%global _default_patch_fuzz 2

# enable|disable system build flags
%global system_build_flags 0

%global numjobs %{_smp_build_ncpus}

# official builds have less debugging and go faster... but we have to shut some things off.
%global official_build 1

# enable|disble use_custom_libcxx
%global use_custom_libcxx 0
%if 0%{?rhel}
# no libcxx in el
%global use_custom_libcxx 1
%endif

# enable|disble bootstrap
%global bootstrap 0
# workaround for old gn on el9, it causes build error: unknown function filter_labels_include()
%if 0%{?rhel} == 9
%global bootstrap 1
%endif

# Fancy build status, so we at least know, where we are..
# %1 where
# %2 what
%global build_target() \
	export NINJA_STATUS="[%2:%f/%t] " ; \
	ninja -j %{numjobs} -C '%1' '%2'

# enable|disable chromedriver
%global build_chromedriver 1
%if 0%{?flatpak}
%global build_chromedriver 0
%endif

# enable|disable headless client build
%global build_headless 1
%if 0%{?flatpak}
%global build_headless 0
%endif

# set nodejs_version
%global nodejs_version v22.14.0

%global system_nodejs 1
# RHEL 9 needs newer nodejs
%if 0%{?rhel} == 9
%global system_nodejs 0
%endif

# enable gtk4 for fedora and el>9
%global gtk_version 4
%if 0%{?rhel} == 9
%global gtk_version 3
%endif

%if 0%{?rhel} == 8
%global chromium_pybin /usr/bin/python3.9
%else
%global chromium_pybin %{__python3}
%endif

# va-api only supported in rhel >= 9 and fedora
%global use_vaapi 1

# v4l2_codec only enable for fedora aarch64
%global use_v4l2_codec 0

# libva is too old on el8
%if 0%{?rhel} == 8
%global use_vaapi 0
%endif

# enable v4l2 and disable vaapi for aarch64 platform
%ifarch aarch64
%if 0%{?fedora} >= 36
%global use_vaapi 0
%global use_v4l2_codec 1
%endif
%endif

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 9
%global noopenh264 1
%endif

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=2239523
# Disable BTI until this is fixed upstream.
%global disable_bti 0
%ifarch aarch64
%if 0%{?fedora}
%global optflags %(echo %{optflags} | sed 's/-mbranch-protection=standard /-mbranch-protection=pac-ret /')
%global disable_bti 1
%endif
%endif

## CEF: Configure CEF build arch & default output build dir
%ifarch aarch64
%global chromium_arch arm64
%endif
%ifarch ppc64le
%global chromium_arch ppc64
%endif
%ifarch x86_64
%global chromium_arch x64
%endif

%global chromebuilddir out/Release_GN_%{chromium_arch}
## END CEF

# enable|disable debuginfo
## CEF: Enable debug info to make it possible to debug CEF/consumer issues
%global enable_debug 1
## END CEF
# disable debuginfo due to a bug in debugedit on el7
# error: canonicalization unexpectedly shrank by one character
# https://bugzilla.redhat.com/show_bug.cgi?id=304121
%if ! %{enable_debug}
%global debug_package %{nil}
%global debug_level 0
%else
%global debug_level 1
# workaround for the error empty file debugsource
%undefine _debugsource_packages
%endif

## CEF: Install directory for build
%global chromium_path %{_libdir}/cef
%global cef_wrapper_src_path %{_usrsrc}/%{name}-%{cef_version}
## END CEF

# We don't want any libs in these directories to generate Provides
# Requires is trickier.

# To generate this list, go into %%{buildroot}%%{chromium_path} and run
# for i in `find . -name "*.so" | sort`; do NAME=`basename -s .so $i`; printf "$NAME|"; done
# for RHEL7, append libfontconfig to the end
# make sure there is not a trailing | at the end of the list
# We always filter provides. We only filter Requires when building shared.
%global __provides_exclude_from ^(%{chromium_path}/.*\\.so|%{chromium_path}/.*\\.so.*)$
%global __requires_exclude ^(%{chromium_path}/.*\\.so|%{chromium_path}/.*\\.so.*)$

# enable|disable control flow integrity support
%global cfi 0

## CEF: QT builds are not relevant
%global use_qt6 0
%global use_qt5 0
## END CEF

# bundle re2, jsoncpp, woff2 - build errors with use_custom_libcxx=true
%global bundlere2 1
%global bundlejsoncpp 1
%global bundlewoff2 1
%global bundlelibaom 1
%global bundlelibavif 1
%global bundlesnappy 1
%global bundlezstd 1
%global bundleicu 1
%global bundledav1d 1
%global bundlebrotli 1
%global bundlelibwebp 1
%global bundlecrc32c 1
%global bundleharfbuzz 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%global bundlefreetype 1
%global bundlelibdrm 1
%global bundlefontconfig 1
%global bundleffmpegfree 1
%global bundlehighway 1
# openjpeg2, need to update to 2.5.x
%global bundlelibopenjpeg2 1
%global bundlelibtiff 1
# libxml2, need to update to 2.14.x for bz#2368923
%global bundlelibxml 1
%global bundlepylibs 0
%global bundlelibxslt 0
%global bundleflac 0
%global bundledoubleconversion 0
%global bundlelibXNVCtrl 0
%global bundlelibusbx 0
%global bundlelibsecret 0
%global bundleopus 0
%global bundlelcms2 0
%global bundlesimdutf 1

# workaround for build error
# disable bundleminizip for Fedora > 39 due to switch to minizip-ng
# disable bundleminizip for epel and Fedora39 due to old minizip version
%global bundleminizip 1

%if 0%{?fedora} || 0%{?rhel} > 8
%global bundlezstd 0
%global bundlefontconfig 0
%global bundledav1d 0
%global bundlelibpng 0
%global bundlelibjpeg 0
%global bundlelibdrm 0
%global bundleffmpegfree 0
%global bundlefreetype 0
%if 0%{?fedora} > 41
# require libtiff-4.6.1 or newer, error: use of undeclared identifier 'TIFFOpenOptionsSetMaxCumulatedMemAlloc'
%global bundlelibtiff 0
%endif
%if 0%{?fedora}
%global bundlecrc32c 0
%endif
%if 0%{?fedora} || 0%{?rhel} > 9
%global bundlelibopenjpeg2 0
%global bundleharfbuzz 0
%global bundlebrotli 0
%global bundlelibwebp 0
%endif
%endif

## CEF: Package version & metadata
%global chromium_major 143
%global chromium_branch 7499
# Where possible, track Chromium versions already released in Fedora.
%global chromium_minor 169
%global chromium_version %{chromium_major}.0.%{chromium_branch}.%{chromium_minor}
%global cef_commit 30cb3bdf337b9c32016d8b892d39d2f2df135ce6
%global cef_branch %{chromium_branch}
%global cef_minor 0
%global cef_patch 13
%global cef_version %{chromium_major}.%{cef_minor}.%{cef_patch}
%global shortcommit %(c=%{cef_commit}; echo ${c:0:7})

Name:	cef
Version: %{cef_version}^chromium%{chromium_version}
Release: %autorelease
Summary: Chromium Embedded Framework
Url: https://bitbucket.org/chromiumembedded/cef
License: BSD-3-Clause AND LGPL-2.1-or-later AND Apache-2.0 AND IJG AND MIT AND GPL-2.0-or-later AND ISC AND OpenSSL AND (MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-only)

# For CEF API dynamic spec generation
BuildRequires: jq

# Tag experimental (unversioned) ABI as the CEF version
# Versioned ABI/API tags are generated in mkspec.sh
Provides: cef(abi) = %{cef_version}
## END CEF

# Use /etc/chromium for initial_prefs
Patch1: chromium-115-initial_prefs-etc-path.patch

# Try to load widevine from other places
Patch8: chromium-117-widevine-other-locations.patch

# debian patches
# disable font-test
Patch20: chromium-disable-font-tests.patch
# don't download binary blob
Patch21: chromium-123-screen-ai-service.patch

# Fix link error when building with system libcxx
Patch22: chromium-131-fix-qt-ui.pach

# Workaround for build error: ERROR Unresolved dependencies.
#//chrome/test:captured_sites_interactive_tests(//build/toolchain/linux/unbundle:default)
#  needs //third_party/libpng:libpng_for_testonly(//build/toolchain/linux/unbundle:default)
Patch23: chromium-143-revert-libpng_for_testonly.patch

# Get around the problem of auto darkmode webcontent inverting and making them unreadable
Patch30: chromium-143-autodarkmode-workaround.patch

# Disable tests on remoting build
Patch82: chromium-98.0.4758.102-remoting-no-tests.patch

# patch for using system brotli
Patch89: chromium-142-system-brotli.patch

# patch for using system libxml
Patch90: chromium-121-system-libxml.patch

# patch for using system opus
Patch91: chromium-108-system-opus.patch

# patch for Failed NodeJS version check
Patch92: chromium-138-checkversion-nodejs.patch

# fix build error
Patch93: chromium-141-csss_style_sheet.patch

# FTBFS - error: cannot find attribute `sanitize` in this scope
#    --> ../../third_party/crabbyavif/src/src/capi/io.rs:210:41
#     |
# 210 |     #[cfg_attr(feature = "disable_cfi", sanitize(cfi = "off"))]
Patch96: chromium-142-crabbyavif-ftbfs-old-rust.patch

# FTBFS - /usr/include/bits/siginfo-consts.h:219:3: error: expected identifier
# 219 |   SYS_SECCOMP = 1,              /* Seccomp triggered.  */
Patch97: chromium-141-glibc-2.42-SYS_SECCOMP.patch

# system ffmpeg
# need for old ffmpeg 5.x on epel9
Patch128: chromium-138-el9-ffmpeg-deprecated-apis.patch
Patch129: chromium-el9-ffmpeg-AV_CODEC_FLAG_COPY_OPAQUE.patch
Patch130: chromium-142-el9-ffmpeg-5.x-duration.patch
# disable the check
Patch131: chromium-107-proprietary-codecs.patch
# fix tab crash with SIGTRAP error when using system ffmpeg
Patch132: chromium-118-sigtrap_system_ffmpeg.patch
# need for old ffmpeg 6.0/5.x on epel9 and fedora < 40
Patch133: chromium-142-el9-ffmpeg-5.1.x.patch
# revert, it causes build error: use of undeclared identifier 'AVFMT_FLAG_NOH264PARSE'
Patch135: chromium-133-disable-H.264-video-parser-during-demuxing.patch
# Workaround for youtube stop working
Patch136: chromium-133-workaround-system-ffmpeg-whitelist.patch

# file conflict with old kernel on el8/el9
Patch141: chromium-118-dma_buf_export_sync_file-conflict.patch

#  fix ftbfs caused by old python-3.9 on el8
Patch142: chromium-143-python-3.9-ftbfs.patch

# add correct path for Qt6Gui header and libs
Patch150: chromium-124-qt6.patch

# revert, it causes ramdom crash on aarch64
Patch300: chromium-131-revert-decommit-pooled-pages-by-default.patch

# disable memory tagging (epel8 on aarch64) due to new feature IFUNC-Resolver
# it is not supported in old glibc < 2.30, error: fatal error: 'sys/ifunc.h' file not found
Patch305: chromium-124-el8-arm64-memory_tagging.patch
Patch306: chromium-127-el8-ifunc-header.patch

# workaround for build error due to old atk version on el8
Patch307: chromium-134-el8-atk-compiler-error.patch
# Fix build errors due to old clang18 in el8
Patch308: chromium-136-unsupport-clang-flags.patch
Patch309: chromium-132-el8-unsupport-rustc-flags.patch

# Fix rhbz#2387446, FTBFS with rust-1.89.0
Patch310: chromium-139-rust-FTBFS-suppress-warnings.patch

# enable fstack-protector-strong
Patch311: chromium-123-fstack-protector-strong.patch

# Fix FTBFS: undefined symbol: __rust_no_alloc_shim_is_unstable on EL9
# Error: unsafe attribute used without unsafe
#    --> ../../build/rust/allocator/lib.rs:107:7
Patch312: chromium-143-el9-rust-no-alloc-shim-is-unstable.patch

# Fix FTBFS on EL9
# - error: undefined symbol: __rust_alloc_error_handler_should_panic
Patch313: chromium-143-el9-rust_alloc_error_handler_should_panic.patch

# old rust version causes build error on el8:
# error[E0599]: no method named `is_none_or` found for enum `Option` in the current scope
Patch314: chromium-136-rust-skrifa-build-error.patch

# add -ftrivial-auto-var-init=zero and -fwrapv
Patch316: chromium-122-clang-build-flags.patch

# unknown warning option -Wno-nontrivial-memcall
Patch317: chromium-142-clang++-unknown-argument.patch

Patch318: memory-allocator-dcheck-assert-fix.patch

# compile swiftshader against llvm-16.0
Patch319: chromium-143-swiftshader-llvm-16.0.patch

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=2239523
# https://bugs.chromium.org/p/chromium/issues/detail?id=1145581#c60
# Disable BTI until this is fixed upstream.
Patch352: chromium-117-workaround_for_crash_on_BTI_capable_system.patch

# workaround for build error on aarch64
Patch353: chromium-127-aarch64-duplicate-case-value.patch

# remove flag split-threshold-for-reg-with-hint, it's not supported in clang <= 17
Patch354: chromium-142-split-threshold-for-reg-with-hint.patch

# fix build error: no member named 'hardware_destructive_interference_size' in namespace 'std'
Patch355: chromium-130-hardware_destructive_interference_size.patch

# fix build error:
# ../../build/modules/linux-x64/module.modulemap:11:12: error: header '../../linux/debian_bullseye_amd64-sysroot/usr/include/alloca.h' not found
Patch356: chromium-141-use_libcxx_modules.patch

# error: no matching member function for call to 'Append'
Patch357: chromium-134-type-mismatch-error.patch

# set clang_lib path
Patch358: chromium-141-rust-clanglib.patch

# PowerPC64 LE support
# Timothy Pearson's patchset
# https://gitlab.raptorengineering.com/raptor-engineering-public/chromium/openpower-patches
Patch359: add-ppc64-architecture-string.patch
Patch361: 0001-sandbox-Enable-seccomp_bpf-for-ppc64.patch

Patch376: 0001-third_party-angle-Include-missing-header-cstddef-in-.patch
Patch377: 0001-Add-PPC64-support-for-boringssl.patch
Patch378: 0001-third_party-libvpx-Properly-generate-gni-on-ppc64.patch
Patch380: 0001-third_party-pffft-Include-altivec.h-on-ppc64-with-SI.patch
Patch381: 0002-Add-PPC64-generated-files-for-boringssl.patch
Patch382: 0002-third_party-lss-kernel-structs.patch

# error: undefined symbol: llvm::MCAsmInfoXCOFF::MCAsmInfoXCOFF()
Patch383: 0001-swiftshader-fix-build.patch

Patch384: Rtc_base-system-arch.h-PPC.patch

Patch386: 0004-third_party-crashpad-port-curl-transport-ppc64.patch

Patch387: HACK-third_party-libvpx-use-generic-gnu.patch
Patch389: HACK-debian-clang-disable-base-musttail.patch
Patch390: HACK-debian-clang-disable-pa-musttail.patch
Patch391: 0001-Add-ppc64-target-to-libaom.patch
Patch392: 0001-Add-pregenerated-config-for-libaom-on-ppc64.patch

Patch393: 0002-third_party-libvpx-Remove-bad-ppc64-config.patch
Patch394: 0003-third_party-libvpx-Add-ppc64-generated-config.patch
# Enabling VSX causes artifacts to appear in VP9 videos
Patch395: 0004-third_party-libvpx-work-around-ambiguous-vsx.patch

# Enable VSX acceleration in Skia.  Requires POWER8 or higher.
Patch396: skia-vsx-instructions.patch

Patch397: 0001-Implement-support-for-ppc64-on-Linux.patch
Patch398: 0001-Implement-support-for-PPC64-on-Linux.patch
Patch399: 0001-Force-baseline-POWER8-AltiVec-VSX-CPU-features-when-.patch
Patch400: fix-clang-selection.patch
Patch401: fix-rustc.patch
Patch402: fix-rust-linking.patch
Patch403: fix-breakpad-compile.patch
Patch404: fix-partition-alloc-compile.patch
Patch405: fix-study-crash.patch
Patch407: fix-different-data-layouts.patch
Patch408: 0002-Add-ppc64-trap-instructions.patch

Patch409: fix-page-allocator-overflow.patch
Patch410: 0001-Enable-ppc64-pointer-compression.patch

Patch411: dawn-fix-ppc64le-detection.patch
Patch412: add-ppc64-architecture-to-extensions.diff

# Suppress harmless compiler warning messages that appear on ppc64 due to arch-specific warning flags being passed
Patch413: fix-unknown-warning-option-messages.diff
Patch415: add-ppc64-pthread-stack-size.patch

Patch417: 0001-add-xnn-ppc64el-support.patch
Patch418: 0002-regenerate-xnn-buildgn.patch

# flatpak sandbox patches from
# https://github.com/flathub/org.chromium.Chromium/tree/master/patches/chromium
Patch500: flatpak-Add-initial-sandbox-support.patch
Patch501: flatpak-Adjust-paths-for-the-sandbox.patch
Patch502: flatpak-Expose-Widevine-into-the-sandbox.patch

# nodejs patches
%if ! %{system_nodejs}
Patch510: 0001-Remove-unused-OpenSSL-config.patch
Patch511: 0002-Fix-Missing-OPENSSL_NO_ENGINE-Guard.patch
%endif

# upstream patches
# Fix Wayland URI DnD issues
Patch1001: chromium-142-Add-ExtractData-support-for-text-uri-list.patch
Patch1002: chromium-142-Update-pointer-position-during-draggin.patch

## CEF: CEF-specific fix patches
Patch900: cef-no-sysroot.patch
Patch901: cef-no-libxml-visibility-patch.patch
Patch902: cef-disable-broken-patches.patch
## END CEF

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium Fedora use chromium-latest.py --stable --ffmpegclean --ffmpegarm
# If you want to include the ffmpeg arm sources append the --ffmpegarm switch
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%%{version}.tar.xz
## CEF: Use %%{chromium_version} for tarball name
Source0: chromium-%{chromium_version}-clean.tar.xz
## END CEF
Source1: README.fedora
## CEF (remove): Config files
# Also, only used if you want to reproduce the clean tarball.
Source5: clean_ffmpeg.sh
Source6: chromium-latest.py
Source7: get_free_ffmpeg_source_files.py
## CEF (remove): Test/GNOME sources

%if ! %{system_nodejs}
# nodejs bundles openssl, but we use the system version in el9
# because openssl contains prohibited code, we remove openssl completely from
# the tarball, using the script in Source13
# http://nodejs.org/dist/v${version}/node-${nodejs_version}.tar.gz
Source12: node-%{nodejs_version}-stripped.tar.gz
Source13: nodejs-sources.sh
BuildRequires: openssl-devel
%endif

## CEF: CEF-specific sources
Source22: https://github.com/chromiumembedded/cef/archive/%{cef_commit}.tar.gz
Source23: mkspec.sh
Source24: FindCEF.cmake
## END CEF

BuildRequires: clang
BuildRequires: clang-tools-extra
BuildRequires: llvm
BuildRequires: lld

%if ! %{use_custom_libcxx}
BuildRequires: libcxx-devel
%endif

%if 0%{?rhel} && 0%{?rhel} <= 9
BuildRequires: gcc-toolset-14-libatomic-devel
%endif

BuildRequires: rustc
BuildRequires: bindgen-cli

%if ! %{bundlezstd}
BuildRequires: libzstd-devel
%endif

# build with system ffmpeg-free
%if ! %{bundleffmpegfree}
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
%endif

%if 0%{?noopenh264}
BuildRequires: pkgconfig(openh264)
%endif

# build with system libaom
%if ! %{bundlelibaom}
BuildRequires: libaom-devel
%endif

BuildRequires:	alsa-lib-devel
BuildRequires:	atk-devel
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gperf

%if %{use_qt5}
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
%endif

%if %{use_qt6}
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
%endif

BuildRequires: compiler-rt

%if ! %{bundleharfbuzz}
BuildRequires:	harfbuzz-devel >= 2.4.0
%endif

BuildRequires: libatomic
BuildRequires:	libcap-devel
BuildRequires:	libcurl-devel

%if ! %{bundlelibdrm}
BuildRequires:	libdrm-devel
%endif

BuildRequires:	libgcrypt-devel
BuildRequires:	libudev-devel
BuildRequires:	libuuid-devel

%if 0%{?fedora} >= 37 || 0%{?rhel} > 9
BuildRequires:	libusb-compat-0.1-devel
%else
BuildRequires:	libusb-devel
%endif

BuildRequires:	libutempter-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXtst-devel
BuildRequires:	xcb-proto
BuildRequires:	mesa-libgbm-devel

# Old Fedora (before 30) uses the 1.2 minizip by default.
# Newer Fedora needs to use the compat package
# Fedora > 39 uses minizip-ng
%if ! %{bundleminizip}
%if 0%{?fedora} > 39 || 0%{?rhel} > 9
# BuildRequires: minizip-ng-devel
BuildRequires: minizip-compat-devel
%else
BuildRequires: minizip-compat-devel
%endif
%endif

%if %{system_nodejs}
BuildRequires: nodejs
%endif

%if ! %{bootstrap}
BuildRequires: gn
%endif

BuildRequires:	nss-devel >= 3.26
BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel

# For screen sharing on Wayland
# pipewire is old on el8, chromium needs new version, disable it temporary
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires:	pipewire-devel
%endif

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

%if %{bootstrap}
# gn needs these
BuildRequires: libstdc++-static
%endif

# Fedora tries to use system libs whenever it can.
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel
# For eu-strip
BuildRequires:	elfutils
BuildRequires:	elfutils-libelf-devel

%if ! %{bundleflac}
BuildRequires:	flac-devel
%endif

%if ! %{bundlefreetype}
BuildRequires:	freetype-devel
%endif

%if ! %{bundlecrc32c}
BuildRequires: google-crc32c-devel
%endif

%if ! %{bundlewoff2}
BuildRequires: woff2-devel
%endif

%if ! %{bundledav1d}
BuildRequires: libdav1d-devel
%endif

%if ! %{bundlehighway}
BuildRequires: highway-devel
%endif

%if ! %{bundlelibavif}
BuildRequires: libavif-devel
%endif

%if ! %{bundlejsoncpp}
BuildRequires: jsoncpp-devel
%endif

%if ! %{bundlelibsecret}
BuildRequires: libsecret-devel
%endif

%if ! %{bundledoubleconversion}
BuildRequires: double-conversion-devel
%endif

%if ! %{bundlesnappy}
BuildRequires: snappy-devel
%endif

%if ! %{bundlelibXNVCtrl}
BuildRequires: libXNVCtrl-devel
%endif

# One of the python scripts invokes git to look for a hash. So helpful.
BuildRequires:	git-core
BuildRequires:	hwdata
BuildRequires:	kernel-headers
BuildRequires:	libffi-devel

%if ! %{bundleicu}
# If this is true, we're using the bundled icu.
# We'd like to use the system icu every time, but we cannot always do that.
# Not newer than 54 (at least not right now)
BuildRequires:	libicu-devel >= 68
%endif

%if ! %{bundlelibjpeg}
# If this is true, we're using the bundled libjpeg
# which we need to do because the RHEL 7 libjpeg doesn't work for chromium anymore
BuildRequires:	libjpeg-devel
%endif

%if ! %{bundlelibpng}
# If this is true, we're using the bundled libpng
# which we need to do because the RHEL 7 libpng doesn't work right anymore
BuildRequires:	libpng-devel
%endif

%if ! %{bundlelibopenjpeg2}
BuildRequires: openjpeg2-devel
%endif

%if ! %{bundlelcms2}
BuildRequires: lcms2-devel
%endif

%if ! %{bundlelibtiff}
BuildRequires: libtiff-devel
%endif

BuildRequires:	libudev-devel

%if ! %{bundlelibusbx}
Requires: libusbx >= 1.0.21-0.1.git448584a
BuildRequires: libusbx-devel >= 1.0.21-0.1.git448584a
%endif

%if %{use_vaapi}
BuildRequires:	libva-devel
%endif

# We don't use libvpx anymore because Chromium loves to
# use bleeding edge revisions here that break other things
# ... so we just use the bundled libvpx.
%if ! %{bundlelibwebp}
BuildRequires:	libwebp-devel
%endif

%if ! %{bundlelibxslt}
BuildRequires:	libxslt-devel
%endif

BuildRequires:	libxshmfence-devel

# Same here, it seems.
# BuildRequires: libyuv-devel
BuildRequires:	mesa-libGL-devel

%if ! %{bundleopus}
BuildRequires:	opus-devel
%endif

BuildRequires: %{chromium_pybin}

## CEF: GTK is not used for CEF
%if 0
## END CEF
%if %{gtk_version} == 4
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xshmfence)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-dri3)
BuildRequires: pkgconfig(xcb-proto)
Requires: gtk4
%else
BuildRequires: pkgconfig(gtk+-3.0)
# GTK modules it expects to find for some reason.
Requires: libcanberra-gtk3%{_isa}
%endif
## CEF: GTK4 is not used for CEF
%endif
## END CEF

# Build deps of Chromium proper which are often transitively pulled in by toolkits (GTK, Qt),
# but are still required without them.
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: wayland-devel

%if ! %{bundlepylibs}
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: python3-jinja2
%else
BuildRequires: python-jinja2
%endif
%endif

%if ! %{bundlere2}
Requires: re2 >= 20160401
BuildRequires: re2-devel >= 20160401
%endif

%if ! %{bundlebrotli}
BuildRequires: brotli-devel
%endif

BuildRequires: speech-dispatcher-devel
BuildRequires: zlib-devel

# remote desktop needs this
BuildRequires:	pam-devel
BuildRequires:	systemd

# using the built from source version on aarch64
BuildRequires: ninja-build

# Yes, java is needed as well..
%if %{build_headless}
BuildRequires:	java-openjdk-headless
%endif

BuildRequires: libevdev-devel

%if ! %{bundlesimdutf}
BuildRequires: simdutf-devel
%endif

# There is a hardcoded check for nss 3.26 in the chromium code (crypto/nss_util.cc)
Requires: nss%{_isa} >= 3.26
Requires: nss-mdns%{_isa}

%if 0%{?fedora} && %{undefined flatpak}
# This enables support for u2f tokens
Requires: u2f-hidraw-policy
%endif

## CEF: Remove chromium-common dep, disable ppc64le
ExclusiveArch: x86_64 aarch64
## END CEF

# Bundled bits (I'm sure I've missed some)
Provides: bundled(bintrees) = 1.0.1
# This is a fork of openssl.
Provides: bundled(boringssl)
%if %{bundlebrotli}
Provides: bundled(brotli) = 222564a95d9ab58865a096b8d9f7324ea5f2e03e
%endif
%if %{bundlesimdutf}
Provides: bundled(simdutf) = 7.0.0
%endif
Provides: bundled(bspatch) = 465265d0d473d107b76e74d969199eaf2cdc8750
Provides: bundled(colorama) = 0.4.6
Provides: bundled(crashpad) = 8f131016b21d986c38ca4a0f091403dbb822d636
Provides: bundled(expat) = 2.7.1
Provides: bundled(fdmlibm) = c512d6173f33c6b8301d3fba9384edc9fc1f9e45

# Don't get too excited. MPEG and other legally problematic stuff is stripped out.
%if %{bundleffmpegfree}
Provides: bundled(ffmpeg) = 7.1.git
%endif

%if %{bundlelibaom}
Provides: bundled(libaom) = 3.12.1
%endif

%if %{bundlefontconfig}
Provides: bundled(fontconfig) = 8cf0ce700a8abe0d97ace4bf7efc7f9534b729ba
%endif

%if %{bundlefreetype}
Provides: bundled(freetype) = VER-2-13-3-230-ge07e56c7f
%endif

%if %{bundleharfbuzz}
Provides: bundled(harfbuzz) = 11.0.0-97
%endif

Provides: bundled(hunspell) = 6d7d19f

%if %{bundleicu}
Provides: bundled(icu) = 74-2
%endif

Provides: bundled(leveldb) = 1.23
Provides: bundled(libaddressinput) = 2610f7b104

%if %{bundlelibdrm}
Provides: bundled(libdrm) = 2.4.122
%endif

Provides: bundled(libjingle) = 5493b8a59deb16cf0481e24707a0ed72d19047dc

%if %{bundlelibjpeg}
Provides: bundled(libjpeg-turbo) = 3.1.0
%endif

Provides: bundled(libphonenumber) = 140dfeb81b753388e8a672900fb7a971e9a0d362

%if %{bundlelibpng}
Provides: bundled(libpng) = 1.6.43
%endif

Provides: bundled(libsrtp) = fd08747fa6800b321d53e15feb34da12dc697dee

%if %{bundlelibusbx}
Provides: bundled(libusbx) = 1.0.17
%endif

Provides: bundled(libvpx) = 1.6.0

%if %{bundlelibwebp}
Provides: bundled(libwebp) = 0.6.0
%endif

%if %{bundlelibxml}
Provides: bundled(libxml) = 2.14.2
%endif

%if %{bundlelibXNVCtrl}
Provides: bundled(libXNVCtrl) = 302.17
%endif
Provides: bundled(libyuv) = 1909
Provides: bundled(lzma) = 24.09

%if %{bundleopus}
Provides: bundled(opus) = 55513e81
%endif

Provides: bundled(ots) = 8d70cffebbfa58f67a5c3ed0e9bc84dccdbc5bc0
Provides: bundled(protobuf) = 3.0.0.beta.3
Provides: bundled(qcms) = 4

%if %{bundlere2}
Provides: bundled(re2)
%endif

Provides: bundled(sfntly) = 04740d2600193b14aa3ef24cd9fbb3d5996b9f77
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0
Provides: bundled(snappy) = 1.1.4-head
Provides: bundled(speech-dispatcher) = 0.7.1
Provides: bundled(sqlite) = 3.17patched
Provides: bundled(superfasthash) = 0
Provides: bundled(talloc) = 2.0.1
Provides: bundled(usrsctp) = 0
Provides: bundled(v8) = 5.9.211.31
Provides: bundled(webrtc) = 90usrsctp
Provides: bundled(woff2) = 445f541996fe8376f3976d35692fd2b9a6eedf2d
Provides: bundled(xdg-mime)
Provides: bundled(xdg-user-dirs)
# Provides: bundled(zlib) = 1.2.11

%if %{undefined flatpak}
# For selinux scriptlet
Requires(post): /usr/sbin/semanage
Requires(post): /usr/sbin/restorecon
%endif

## CEF: Package description, rm subpackages, add devel package
%description
CEF is an embeddable build of Chromium, powered by WebKit (Blink).

%package devel
Summary: Header files for the Chromium Embedded Framework
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for the Chromium Embedded Framework.
## END CEF

%prep
## CEF: Unpack and move CEF/chromium sources into the expected layout
%setup -q -T -n cef-%{cef_commit} -b 22
%setup -q -n chromium-%{chromium_version}
mv %{_builddir}/cef-%{cef_commit} ./cef
## END CEF

### Chromium Fedora Patches ###
%patch -P1 -p1 -b .etc
%patch -P8 -p1 -b .widevine-other-locations

%patch -P20 -p1 -b .disable-font-test
%patch -P21 -p1 -b .screen-ai-service
%if ! %{use_custom_libcxx}
%patch -P22 -p1 -b .fix-qt-ui
%endif

%patch -P23 -p1 -R -b .revert-libpng_for_testonly
%patch -P30 -p1 -b .autodarkmode-workaround
%patch -P82 -p1 -b .remoting-no-tests

%if ! %{bundlebrotli}
%patch -P89 -p1 -b .system-brotli
%endif

%if ! %{bundlelibxml}
%if 0%{?fedora} && 0%{?fedora} < 40 || 0%{?rhel} && 0%{?rhel} < 10
%patch -P90 -p1 -b .system-libxml
%endif
%endif

%if ! %{bundleopus}
%patch -P91 -p1 -b .system-opus
%endif

%patch -P92 -p1 -b .nodejs-checkversion
%patch -P93 -p1 -b .ftbfs-csss_style_sheet
%patch -P96 -p1 -b .crabbyavif-ftbfs-old-rust

%if 0%{?fedora} > 43
%patch -P97 -p1 -b .glibc-2.42-SYS_SECCOMP
%endif

%if ! %{bundleffmpegfree}
%if 0%{?rhel} == 9
%patch -P128 -p1 -b .el9-ffmpeg-deprecated-apis
%patch -P129 -p1 -b .el9-ffmpeg-AV_CODEC_FLAG_COPY_OPAQUE
%patch -P130 -p1 -b .el9-ffmpeg-5.x-duration
%patch -P133 -p1 -b .el9-ffmpeg-5.1.x
%endif
%patch -P131 -p1 -b .prop-codecs
%patch -P132 -p1 -b .sigtrap_system_ffmpeg
%patch -P135 -p1 -b .disable-H.264-video-parser-during-demuxing
%patch -P136 -p1 -b .workaround-system-ffmpeg-whitelist
%endif

%if 0%{?rhel} == 8 || 0%{?rhel} == 9
%patch -P141 -p1 -b .dma_buf_export_sync_file-conflict
%patch -P142 -p1 -b .python-3.9-ftbfs
%endif

%patch -P150 -p1 -b .qt6

%ifarch aarch64 ppc64le
%patch -P300 -p1 -R -b .revert-decommit-pooled-pages-by-default
%endif

%if 0%{?rhel} == 8
%ifarch aarch64
%patch -P305 -p1 -b .el8-memory_tagging
%patch -P306 -p1 -b .el8-ifunc-header
%endif
%patch -P307 -p1 -b .el8-atk-compiler-error
%patch -P308 -p1 -b .unsupport-clang-flags
%patch -P309 -p1 -b .el8-unsupport-rustc-flags
%patch -P314 -p1 -b .rust-skrifa-build-error
%endif

%patch -P310 -p1 -b .rust-FTBFS-suppress-warnings
%patch -P311 -p1 -b .fstack-protector-strong

%if 0%{?rhel} == 9
%patch -P312 -p1 -b .el9-rust-no-alloc-shim-is-unstable
%patch -P313 -p1 -b .el9-rust_alloc_error_handler_should_panic
%endif

%if 0%{?rhel} && 0%{?rhel} < 10
%patch -P354 -p1 -b .split-threshold-for-reg-with-hint
%endif
%patch -P316 -p1 -b .clang-build-flags

%if 0%{?fedora} && 0%{?fedora} < 42 || 0%{?rhel} && 0%{?rhel} < 10
%patch -P317 -p1 -b .clang++-unsupported-argument
%endif

%patch -P318 -p1 -b .memory-allocator-dcheck-assert-fix
%patch -P319 -p1 -b .swiftshader-llvm-16.0

%if %{disable_bti}
%patch -P352 -p1 -b .workaround_for_crash_on_BTI_capable_system
%endif

%ifarch aarch64 && 0%{?fedora} > 40
%patch -P353 -p1 -b .duplicate-case-value
%endif

%patch -P355 -p1 -b .hardware_destructive_interference_size

%patch -P356 -p1 -b .disable_use_libcxx_modules

%patch -P357 -p1 -b .type-mismatch-error

%patch -P358 -p1 -b .rust-clang_lib

%ifarch ppc64le
%patch -P359 -p1 -b .add-ppc64-architecture-string
%patch -P361 -p1 -b .0001-sandbox-Enable-seccomp_bpf-for-ppc64
%patch -P376 -p1 -b .0001-third_party-angle-Include-missing-header-cstddef-in-
%patch -P377 -p1 -b .0001-Add-PPC64-support-for-boringssl
%patch -P378 -p1 -b .0001-third_party-libvpx-Properly-generate-gni-on-ppc64
%patch -P380 -p1 -b .0001-third_party-pffft-Include-altivec.h-on-ppc64-with-SI
%patch -P381 -p1 -b .0002-Add-PPC64-generated-files-for-boringssl
%patch -P382 -p1 -b .0002-third_party-lss-kernel-structs
%patch -P383 -p1 -b .0001-swiftshader-fix-build
%patch -P384 -p1 -b .Rtc_base-system-arch.h-PPC
%patch -P386 -p1 -b .0004-third_party-crashpad-port-curl-transport-ppc64
%patch -P387 -p1 -b .HACK-third_party-libvpx-use-generic-gnu
%patch -P389 -p1 -b .HACK-debian-clang-disable-base-musttail
%patch -P390 -p1 -b .HACK-debian-clang-disable-pa-musttail
%patch -P391 -p1 -b .0001-Add-ppc64-target-to-libaom
%patch -P392 -p1 -b .0001-Add-pregenerated-config-for-libaom-on-ppc64
%patch -P393 -p1 -b .0002-third_party-libvpx-Remove-bad-ppc64-config
%patch -P394 -p1 -b .0003-third_party-libvpx-Add-ppc64-generated-config
%patch -P395 -p1 -b .0004-third_party-libvpx-work-around-ambiguous-vsx
%patch -P396 -p1 -b .skia-vsx-instructions
%patch -P397 -p1 -b .0001-Implement-support-for-ppc64-on-Linux
%patch -P398 -p1 -b .0001-Implement-support-for-PPC64-on-Linux
%patch -P399 -p1 -b .0001-Force-baseline-POWER8-AltiVec-VSX-CPU-features-when-
%patch -P400 -p1 -b .fix-clang-selection
%patch -P401 -p1 -b .fix-rustc
%patch -P402 -p1 -b .fix-rust-linking
%patch -P403 -p1 -b .fix-breakpad-compile
%patch -P404 -p1 -b .fix-partition-alloc-compile
%patch -P405 -p1 -b .fix-study-crash
%patch -P407 -p1 -b .fix-different-data-layouts
%patch -P408 -p1 -b .0002-Add-ppc64-trap-instructions
%patch -P409 -p1 -b .fix-page-allocator-overflow
%patch -P410 -p1 -b .0001-Enable-ppc64-pointer-compression
%patch -P411 -p1 -b .dawn-fix-ppc64le-detection
%patch -P412 -p1 -b .add-ppc64-architecture-to-extensions
%patch -P413 -p1 -b .fix-unknown-warning-option-messages
%patch -P415 -p1 -b .add-ppc64-pthread-stack-size
%patch -P417 -p1 -b .0001-add-xnn-ppc64el-support
%patch -P418 -p1 -b .0002-regenerate-xnn-buildgn
%endif

%if 0%{?flatpak}
%patch -P500 -p1 -b .flatpak-initial-sandbox
%patch -P501 -p1 -b .flatpak-sandbox-paths
%patch -P502 -p1 -b .flatpak-widevine
%endif

# Upstream patches
%patch -P1001 -p1 -b .Add-ExtractData-support-for-text-uri-list.patch
%patch -P1002 -p1 -b .Update-pointer-position-during-draggin.patch

## CEF: CEF-specific fix patches & other fixup
%patch -P900 -p1 -b .cef-no-sysroot
%if ! %{bundlelibxml}
%patch -P901 -p1 -b .cef-no-libxml-visibility-patch
%endif
%patch -P902 -p1 -b .cef-disable-broken-patches

# Redirect the git version stuff to use the version file contents instead
cat >>cef/VERSION.in <<EOF
HASH=%{cef_commit}
MINOR=%{cef_minor}
PATCH=%{cef_patch}
EOF
cat > cef/.git-version <<EOF
COMMIT_HASH=%{cef_commit}
URL=https://bitbucket.org/chromiumembedded/cef
EOF
cat > .git-version <<EOF
COMMIT_HASH=refs/tags/%{chromium_version}
URL=https://chromium.googlesource.com/chromium/src.git
EOF
sed -i -e 's/\.get_cef_commit_components/.get_cef_version_components/g' \
  -e 's/\.get_cef_branch_version_components/.get_cef_version_components/g' \
  -e 's/if not on_release_branch/if False/g' \
  -e 's/%d/%s/g' \
  cef/tools/cef_version.py

# Use system clang
echo 'clang_exe = "clang"' >> cef/tools/clang_util.py

# Mock the git functions
cat <<EOF >>cef/tools/git_util.py
import subprocess

def git_apply_patch_file(patch_path, patch_dir):
    try:
        subprocess.run(["patch", "-p0", "--ignore-whitespace",
                        "-N", "-i", patch_path], cwd=patch_dir, check=True)
    except subprocess.CalledProcessError:
        return "fail"
    return "apply"

def ver_info(path):
    info = {}
    for line in open(os.path.join(path, '.git-version')):
        key, val = line.strip().split("=")
        info[key] = val
    return info

def is_checkout(path):
    return os.path.exists(os.path.join(path, '.git-version'))

def get_hash(path='.', branch='HEAD'):
    return ver_info(path)["COMMIT_HASH"]

def get_url(path):
    return ver_info(path)["URL"]

def get_commit_number(path='.', branch='HEAD'):
    return 0
EOF
## END CEF

# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
find -type f \( -iname "*.py" \) -exec sed -i '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{chromium_pybin}=' {} +

# Add correct path for nodejs binary
%if ! %{system_nodejs}
  ln -s ../../../node-%{nodejs_version}/node-%{nodejs_version}-linux-x64 third_party/node/linux/node-linux-x64
%else
  mkdir -p third_party/node/linux/node-linux-x64/bin
  ln -s $(which node) third_party/node/linux/node-linux-x64/bin/node
%endif

# Get rid of the prebuilt esbuild binary
rm -rf third_party/devtools-frontend/src/third_party/esbuild

# Remove bundle gn and replace it with a system gn or bootstrap gn as it is x86_64 and causes
# FTBFS on other arch like aarch64/ppc64le
%if %{bootstrap}
ln -sf ../../%{chromebuilddir}/gn buildtools/linux64/gn
%else
ln -sf $(which gn) buildtools/linux64/gn
%endif

%if %{bundlelibusbx}
# no hackity hack hack
%else
# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h
# we _shouldn't need to do this, but it looks like we do.
cp -a $(pkg-config --variable=includedir libusb-1.0)/libusb-1.0/libusb.h third_party/libusb/src/libusb/libusb.h
%endif

# Hard code extra version
sed -i 's/getenv("CHROME_VERSION_EXTRA")/"Fedora Project"/' chrome/common/channel_info_posix.cc

# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc

# bz#2265957, add correct platform
sed -i "s/Linux x86_64/Linux %{_arch}/" components/embedder_support/user_agent_utils.cc

%if ! %{bundlesimdutf}
ln -sf %{_includedir}/simdutf.h third_party/simdutf/simdutf.h
%endif

%build

%if ! %{system_nodejs}
# Build nodejs and Replace bundle binary
export CXX=c++
tar xf %{SOURCE12}
pushd node-%{nodejs_version}
patch -p1 < %{_sourcedir}/0001-Remove-unused-OpenSSL-config.patch
patch -p1 < %{_sourcedir}/0002-Fix-Missing-OPENSSL_NO_ENGINE-Guard.patch
./configure --ninja --shared-openssl --openssl-conf-name=openssl_conf --enable-static --prefix=node-%{nodejs_version}-linux-x64
ninja -j %{numjobs} -C %{chromebuilddir}
make install
popd
%endif

# reduce warnings
FLAGS=' -Wno-deprecated-declarations -Wno-unknown-warning-option -Wno-unused-command-line-argument'
FLAGS+=' -Wno-unused-but-set-variable -Wno-unused-result -Wno-unused-function -Wno-unused-variable'
FLAGS+=' -Wno-unused-const-variable -Wno-unneeded-internal-declaration -Wno-unknown-attributes -Wno-unknown-pragmas'

%if %{system_build_flags}
CFLAGS=${CFLAGS/-fexceptions}
CFLAGS=${CFLAGS/-Wp,-D_GLIBCXX_ASSERTIONS}
CFLAGS="$CFLAGS $FLAGS"
CXXFLAGS="$CFLAGS"
%else
# override system build flags
CFLAGS="$FLAGS"
CXXFLAGS="$FLAGS"
%endif

%ifarch ppc64le
CXXFLAGS+=' -faltivec-src-compat=mixed -Wno-deprecated-altivec-src-compat'
%endif

%if ! %{use_custom_libcxx}
LDFLAGS="${LDFLAGS} -stdlib=libc++"
CXXFLAGS="${CXXFLAGS} -stdlib=libc++"
%endif

export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
export READELF=llvm-readelf
export CFLAGS
export CXXFLAGS
export LDFLAGS

# need for error: the option `Z` is only accepted on the nightly compiler
export RUSTC_BOOTSTRAP=1

# set rustc version
rustc_version="$(rustc --version)"
# set rust bindgen root
rust_bindgen_root="$(which bindgen | sed 's#/s\?bin/.*##')"
rust_sysroot_absolute="$(rustc --print sysroot)"

# set clang version
clang_version="$(clang --version | sed -n 's/clang version //p' | cut -d. -f1)"
%if 0%{?fedora} > 41 || 0%{?rhel} > 9
clang_base_path="$(PATH=/usr/bin:/usr/sbin which clang | sed 's#/bin/.*##')"
%else
clang_base_path="$(clang --version | grep InstalledDir | cut -d' ' -f2 | sed 's#/bin##')"
%endif

# Core defines are flags that are true for both the browser and headless.
CHROMIUM_CORE_GN_DEFINES=""
# using system toolchain
CHROMIUM_CORE_GN_DEFINES+=' custom_toolchain="//build/toolchain/linux/unbundle:default"'
CHROMIUM_CORE_GN_DEFINES+=' host_toolchain="//build/toolchain/linux/unbundle:default"'
%if ! %{use_custom_libcxx}
CHROMIUM_BROWSER_GN_DEFINES+=' use_custom_libcxx=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' is_debug=false dcheck_always_on=false dcheck_is_configurable=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_enterprise_companion=false'
CHROMIUM_CORE_GN_DEFINES+=' system_libdir="%{_lib}"'

%if %{official_build}
CHROMIUM_CORE_GN_DEFINES+=' is_official_build=true'
sed -i 's|OFFICIAL_BUILD|GOOGLE_CHROME_BUILD|g' tools/generate_shim_headers/generate_shim_headers.py
%endif

CHROMIUM_CORE_GN_DEFINES+=' chrome_pgo_phase=0'

%if ! %{cfi}
CHROMIUM_CORE_GN_DEFINES+=' is_cfi=false use_thin_lto=false'
%endif

CHROMIUM_CORE_GN_DEFINES+=' is_clang=true'
CHROMIUM_CORE_GN_DEFINES+=" clang_base_path=\"$clang_base_path\""
CHROMIUM_CORE_GN_DEFINES+=" clang_version=$clang_version"
CHROMIUM_CORE_GN_DEFINES+=' clang_use_chrome_plugins=false'
CHROMIUM_CORE_GN_DEFINES+=' use_lld=true'

# enable system rust
CHROMIUM_CORE_GN_DEFINES+=" rust_sysroot_absolute=\"$rust_sysroot_absolute\""
CHROMIUM_CORE_GN_DEFINES+=" rust_bindgen_root=\"$rust_bindgen_root\""
CHROMIUM_CORE_GN_DEFINES+=" rustc_version=\"$rustc_version\""

CHROMIUM_CORE_GN_DEFINES+=' use_sysroot=false'

%ifarch aarch64
CHROMIUM_CORE_GN_DEFINES+=' target_cpu="arm64"'
%endif

%ifarch ppc64le
CHROMIUM_CORE_GN_DEFINES+=' target_cpu="ppc64"'
%endif

CHROMIUM_CORE_GN_DEFINES+=' icu_use_data_file=true'
CHROMIUM_CORE_GN_DEFINES+=' target_os="linux"'
CHROMIUM_CORE_GN_DEFINES+=' current_os="linux"'
CHROMIUM_CORE_GN_DEFINES+=' treat_warnings_as_errors=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_iterator_debugging=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_vr=false'
CHROMIUM_CORE_GN_DEFINES+=' build_dawn_tests=false enable_perfetto_unittests=false'
CHROMIUM_CORE_GN_DEFINES+=' disable_fieldtrial_testing_config=true'
CHROMIUM_CORE_GN_DEFINES+=' symbol_level=%{debug_level} blink_symbol_level=%{debug_level}'
CHROMIUM_CORE_GN_DEFINES+=' angle_has_histograms=false'
# drop unrar
CHROMIUM_CORE_GN_DEFINES+=' safe_browsing_use_unrar=false'
CHROMIUM_CORE_GN_DEFINES+=' v8_enable_backtrace=true'
export CHROMIUM_CORE_GN_DEFINES

# browser gn defines
CHROMIUM_BROWSER_GN_DEFINES=""

# if systemwide ffmpeg free is used, the proprietary codecs can be set to true to load the codecs from ffmpeg-free
# the codecs computation is passed to ffmpeg-free in this case
%if ! %{bundleffmpegfree}
CHROMIUM_BROWSER_GN_DEFINES+=' ffmpeg_branding="Chrome" proprietary_codecs=true is_component_ffmpeg=true enable_ffmpeg_video_decoders=true media_use_ffmpeg=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' ffmpeg_branding="Chromium" proprietary_codecs=false is_component_ffmpeg=false enable_ffmpeg_video_decoders=false media_use_ffmpeg=true'
%endif
# link against noopenh264 library
%if 0%{?noopenh264}
CHROMIUM_BROWSER_GN_DEFINES+=' media_use_openh264=true'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_h264=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' media_use_openh264=false'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_h264=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' use_kerberos=true'
# Workaround for FTBFS, error: no member named 'bPsnrY' in 'Source_Picture_s'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_video_psnr=false'

%if %{use_qt5}
CHROMIUM_BROWSER_GN_DEFINES+=" use_qt5=true moc_qt5_path=\"$(%{_qt5_qmake} -query QT_HOST_BINS)\""
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_qt5=false'
%endif

%if %{use_qt6}
CHROMIUM_BROWSER_GN_DEFINES+=" use_qt6=true moc_qt6_path=\"$(%{_qt6_qmake} -query QT_HOST_LIBEXECS)\""
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_qt6=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk=true gtk_version=%{gtk_version}'

CHROMIUM_BROWSER_GN_DEFINES+=' use_gio=true use_pulseaudio=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_hangout_services_extension=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_widevine=true'

%if %{use_vaapi}
CHROMIUM_BROWSER_GN_DEFINES+=' use_vaapi=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_vaapi=false'
%endif

%if %{use_v4l2_codec}
CHROMIUM_BROWSER_GN_DEFINES+=' use_v4l2_codec=true'
%endif

%if 0%{?fedora} || 0%{?rhel} > 8
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_pipewire=true rtc_link_pipewire=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_pipewire=false rtc_link_pipewire=false'
%endif

%if ! %{bundlelibjpeg}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libjpeg=true'
%endif

%if ! %{bundlelibpng}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libpng=true'
%endif

%if ! %{bundlelibopenjpeg2}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libopenjpeg2=true'
%endif

%if ! %{bundlelcms2}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_lcms2=true'
%endif

%if ! %{bundlelibtiff}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libtiff=true'
%endif

CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libffi=true'

export CHROMIUM_BROWSER_GN_DEFINES

# headless gn defines
CHROMIUM_HEADLESS_GN_DEFINES=""
CHROMIUM_HEADLESS_GN_DEFINES+=' use_ozone=true ozone_auto_platforms=false ozone_platform="headless" ozone_platform_headless=true'
CHROMIUM_HEADLESS_GN_DEFINES+=' angle_enable_vulkan=true angle_enable_swiftshader=true headless_use_embedded_resources=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' headless_use_prefs=false headless_use_policy=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' v8_use_external_startup_data=false enable_print_preview=false enable_remoting=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_alsa=false use_bluez=false use_cups=false use_dbus=false use_gio=false use_kerberos=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_libpci=false use_pulseaudio=false use_udev=false rtc_use_pipewire=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' v8_enable_lazy_source_positions=false use_glib=false use_gtk=false use_pangocairo=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_qt5=false use_qt6=false is_component_build=false enable_ffmpeg_video_decoders=false media_use_ffmpeg=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' media_use_libvpx=false proprietary_codecs=false'
export CHROMIUM_HEADLESS_GN_DEFINES

# use system libraries
system_libs=()
%if ! %{bundlelibaom}
	system_libs+=(libaom)
%endif
%if ! %{bundlelibavif}
	system_libs+=(libavif)
%endif
%if ! %{bundlebrotli}
	system_libs+=(brotli)
%endif
%if ! %{bundlecrc32c}
	system_libs+=(crc32c)
%endif
%if ! %{bundledav1d}
	system_libs+=(dav1d)
%endif
%if ! %{bundlehighway}
	system_libs+=(highway)
%endif
%if ! %{bundlefontconfig}
	system_libs+=(fontconfig)
%endif
%if ! %{bundleffmpegfree}
	system_libs+=(ffmpeg)
%endif
%if ! %{bundlefreetype}
	system_libs+=(freetype)
%endif
%if ! %{bundleharfbuzz}
	system_libs+=(harfbuzz-ng)
%endif
%if ! %{bundleicu}
	system_libs+=(icu)
%endif
%if ! %{bundlelibdrm}
	system_libs+=(libdrm)
%endif
%if ! %{bundlelibjpeg}
	system_libs+=(libjpeg)
%endif
%if ! %{bundlelibpng}
	system_libs+=(libpng)
%endif
%if ! %{bundlelibusbx}
	system_libs+=(libusb)
%endif
%if ! %{bundlelibwebp}
	system_libs+=(libwebp)
%endif
%if ! %{bundlelibxml}
	system_libs+=(libxml)
%endif
%if ! %{bundlelibxslt}
	system_libs+=(libxslt)
%endif
%if ! %{bundleopus}
	system_libs+=(opus)
%endif
%if ! %{bundlere2}
	system_libs+=(re2)
%endif
%if ! %{bundlewoff2}
	system_libs+=(woff2)
%endif
%if ! %{bundleminizip}
	system_libs+=(zlib)
%endif
%if ! %{bundlejsoncpp}
	system_libs+=(jsoncpp)
%endif
%if ! %{bundledoubleconversion}
	system_libs+=(double-conversion)
%endif
%if ! %{bundlelibsecret}
	system_libs+=(libsecret)
%endif
%if ! %{bundlesnappy}
	system_libs+=(snappy)
%endif
%if ! %{bundlelibXNVCtrl}
	system_libs+=(libXNVCtrl)
%endif
%if ! %{bundleflac}
	system_libs+=(flac)
%endif
%if ! %{bundlezstd}
	system_libs+=(zstd)
%endif
%if 0%{?noopenh264}
	system_libs+=(openh264)
%endif
%if ! %{bundlesimdutf}
   system_libs+=(simdutf)
%endif

build/linux/unbundle/replace_gn_files.py --system-libraries ${system_libs[@]}

# Check that there is no system 'google' module, shadowing bundled ones:
if python3 -c 'import google ; print google.__path__' 2> /dev/null ; then \
    echo "Python 3 'google' module is defined, this will shadow modules of this build"; \
    exit 1 ; \
fi

%if %{bootstrap}
tools/gn/bootstrap/bootstrap.py --gn-gen-args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES"
%else
mkdir -p %{chromebuilddir} && cp -a $(which gn) %{chromebuilddir}/
%endif

## CEF: CEF-specific configure/build process
DEPOT_TOOLS=%{_builddir}/chromium-%{chromium_version}/third_party/depot_tools
# Use system ninja, remove the wrapper which only supports x86_64
rm -f ${DEPOT_TOOLS}/ninja
export PATH=$PATH:$DEPOT_TOOLS

CEF_GN_DEFINES=""
# Disable features inappropriate for CEF build
CEF_GN_DEFINES+=' use_gtk=false use_qt5=false use_qt6=false enable_remoting=false'
CEF_GN_DEFINES+=' use_cups=false use_gio=false use_kerberos=false'
CEF_GN_DEFINES+=' use_libpci=false use_udev=false'
CEF_GN_DEFINES+=' cef_use_gtk=false'

GN_DEFINES="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES $CEF_GN_DEFINES" \
GN_ARGUMENTS="--script-executable=%{chromium_pybin}" \
%{chromium_pybin} cef/tools/gclient_hook.py

%build_target %{chromebuilddir} libcef
%build_target %{chromebuilddir} chrome_sandbox

# Generate CEF API version subpackages
sh %SOURCE23 cef/cef_api_versions.json > %{specpartsdir}/cef-api-versions.specpart

# Build the CEF binary "distribution"
python3 cef/tools/make_distrib.py --distrib-subdir=distrib --output-dir=.. --ninja-build --%{chromium_arch}-build --minimal --no-docs --no-archive
## END CEF

%install
rm -rf %{buildroot}

## CEF: CEF-specific install section
mkdir -p %{buildroot}%{chromium_path}
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{cef_wrapper_src_path}
mkdir -p %{buildroot}%{_includedir}/cef
mkdir -p %{buildroot}%{_datadir}/cmake/Modules

pushd ../distrib_minimal/Resources
  cp -a *.pak locales %{buildroot}%{chromium_path}
%if %{bundleicu}
  cp -a icudtl.dat %{buildroot}%{chromium_path}
%endif
popd

pushd ../distrib_minimal/Release
  cp -a libvk_swiftshader.so* %{buildroot}%{chromium_path}
  cp -a libvulkan.so* %{buildroot}%{chromium_path}
  cp -a vk_swiftshader_icd.json %{buildroot}%{chromium_path}

  cp -a libcef.so %{buildroot}%{chromium_path}
  cp -a chrome-sandbox %{buildroot}%{chromium_path}/chrome-sandbox

  # V8 initial snapshots
  # https://code.google.com/p/chromium/issues/detail?id=421063
  cp -a v8_context_snapshot.bin %{buildroot}%{chromium_path}
  # This is ANGLE, not to be confused with the similarly named files under swiftshader/
  cp -a libEGL.so* libGLESv2.so* %{buildroot}%{chromium_path}
popd

cp -a ../distrib_minimal/include %{buildroot}%{_includedir}/cef/include
cp -a ../distrib_minimal/libcef_dll %{buildroot}%{cef_wrapper_src_path}/libcef_dll

# Remove include file targets, since includes are in a different path
sed -i -e '/\.\.\/include/d' %{buildroot}%{cef_wrapper_src_path}/libcef_dll/CMakeLists.txt
sed \
  -e "s,__CEF_INCLUDE__,%{_includedir}/cef," \
  -e "s,__CEF_LIB__,%{chromium_path}," \
  -e "s,__CEF_SRC__,%{cef_wrapper_src_path}," \
  %{SOURCE24} >%{buildroot}%{_datadir}/cmake/Modules/FindCEF.cmake

echo '%%_cef_api_requires() Requires: cef%%{?1:(api) = %%1}%%{!?1:(abi) = %{cef_version}}' > %{buildroot}%{_rpmmacrodir}/macros.cef

mkdir -p .fedora-rpm/docs/
cp AUTHORS .fedora-rpm/docs/AUTHORS-CHROMIUM
cp cef/AUTHORS.txt .fedora-rpm/docs/AUTHORS-CEF

mkdir -p .fedora-rpm/license/
cp LICENSE .fedora-rpm/license/LICENSE-CHROMIUM
cp cef/LICENSE.txt .fedora-rpm/license/LICENSE-CEF

# README.fedora
cp %{SOURCE1} .

%if %{undefined flatpak}
%post
# Set SELinux labels - semanage itself will adjust the lib directory naming
# But only do it when selinux is enabled, otherwise, it gets noisy.
if selinuxenabled; then
	semanage fcontext -a -t bin_t %{chromium_path} &>/dev/null || :
	semanage fcontext -a -t chrome_sandbox_exec_t %{chromium_path}/chrome-sandbox &>/dev/null || :
	restorecon -R -v %{chromium_path} &>/dev/null || :
fi
%endif
## END CEF

%files
## CEF: CEF-specific file list
%doc README.fedora
%doc .fedora-rpm/docs/AUTHORS*
%license .fedora-rpm/license/LICENSE*
%{chromium_path}/chrome_*.pak
%{chromium_path}/resources.pak
%attr(4755, root, root) %{chromium_path}/chrome-sandbox
%{chromium_path}/libcef.so
## END CEF (rest of files are verbatim from chromium-common)
%{chromium_path}/libvk_swiftshader.so*
%{chromium_path}/libvulkan.so*
%{chromium_path}/vk_swiftshader_icd.json
%{chromium_path}/libEGL.so*
%{chromium_path}/libGLESv2.so*
%{chromium_path}/*.bin
%if %{bundleicu}
%{chromium_path}/icudtl.dat
%endif
%dir %{chromium_path}/
%dir %{chromium_path}/locales/
%lang(af) %{chromium_path}/locales/af*.pak
%lang(am) %{chromium_path}/locales/am*.pak
%lang(ar) %{chromium_path}/locales/ar*.pak
%lang(bg) %{chromium_path}/locales/bg*.pak
%lang(bn) %{chromium_path}/locales/bn*.pak
%lang(ca) %{chromium_path}/locales/ca*.pak
%lang(cs) %{chromium_path}/locales/cs*.pak
%lang(da) %{chromium_path}/locales/da*.pak
%lang(de) %{chromium_path}/locales/de*.pak
%lang(el) %{chromium_path}/locales/el*.pak
%lang(en_GB) %{chromium_path}/locales/en-GB*.pak
# Chromium _ALWAYS_ needs en-US.pak as a fallback
# This means we cannot apply the lang code here.
# Otherwise, it is filtered out on install.
%{chromium_path}/locales/en-US*.pak
%lang(es) %{chromium_path}/locales/es*.pak
%lang(et) %{chromium_path}/locales/et*.pak
%lang(fa) %{chromium_path}/locales/fa*.pak
%lang(fi) %{chromium_path}/locales/fi{.pak,_*.pak}
%lang(fil) %{chromium_path}/locales/fil*.pak
%lang(fr) %{chromium_path}/locales/fr*.pak
%lang(gu) %{chromium_path}/locales/gu*.pak
%lang(he) %{chromium_path}/locales/he*.pak
%lang(hi) %{chromium_path}/locales/hi*.pak
%lang(hr) %{chromium_path}/locales/hr*.pak
%lang(hu) %{chromium_path}/locales/hu*.pak
%lang(id) %{chromium_path}/locales/id*.pak
%lang(it) %{chromium_path}/locales/it*.pak
%lang(ja) %{chromium_path}/locales/ja*.pak
%lang(kn) %{chromium_path}/locales/kn*.pak
%lang(ko) %{chromium_path}/locales/ko*.pak
%lang(lt) %{chromium_path}/locales/lt*.pak
%lang(lv) %{chromium_path}/locales/lv*.pak
%lang(ml) %{chromium_path}/locales/ml*.pak
%lang(mr) %{chromium_path}/locales/mr*.pak
%lang(ms) %{chromium_path}/locales/ms*.pak
%lang(nb) %{chromium_path}/locales/nb*.pak
%lang(nl) %{chromium_path}/locales/nl*.pak
%lang(pl) %{chromium_path}/locales/pl*.pak
%lang(pt_BR) %{chromium_path}/locales/pt-BR*.pak
%lang(pt_PT) %{chromium_path}/locales/pt-PT*.pak
%lang(ro) %{chromium_path}/locales/ro*.pak
%lang(ru) %{chromium_path}/locales/ru*.pak
%lang(sk) %{chromium_path}/locales/sk*.pak
%lang(sl) %{chromium_path}/locales/sl*.pak
%lang(sr) %{chromium_path}/locales/sr*.pak
%lang(sv) %{chromium_path}/locales/sv*.pak
%lang(sw) %{chromium_path}/locales/sw*.pak
%lang(ta) %{chromium_path}/locales/ta*.pak
%lang(te) %{chromium_path}/locales/te*.pak
%lang(th) %{chromium_path}/locales/th*.pak
%lang(tr) %{chromium_path}/locales/tr*.pak
%lang(uk) %{chromium_path}/locales/uk*.pak
%lang(ur) %{chromium_path}/locales/ur*.pak
%lang(vi) %{chromium_path}/locales/vi*.pak
%lang(zh_CN) %{chromium_path}/locales/zh-CN*.pak
%lang(zh_TW) %{chromium_path}/locales/zh-TW*.pak
# These are psuedolocales, not real ones.
# They only get generated when is_official_build=false
%if ! %{official_build}
%{chromium_path}/locales/ar-XB.pak
%{chromium_path}/locales/en-XA.pak
%endif

## CEF: rm headless/chromedriver subpackages, add devel subpackage
%files devel
%{_includedir}/cef/
%{_rpmmacrodir}/macros.cef
%{cef_wrapper_src_path}
%{_datadir}/cmake/Modules/FindCEF.cmake
## END CEF

%changelog
%autochangelog
