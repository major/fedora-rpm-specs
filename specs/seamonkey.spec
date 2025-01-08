%bcond_without	system_nspr
%bcond_without	system_nss
%bcond_without	system_libvpx
%bcond_without	system_webp
%bcond_with	system_icu
%bcond_without	system_ffi
%bcond_without	system_av1

%bcond_without	langpacks
%bcond_without	clang
%bcond_with	lto
%bcond_with	stylo

%bcond_without	calendar
%bcond_without	dominspector
%bcond_without	irc
%bcond_with	debugqa

%global nspr_version	4.32.0
%global nss_version	3.90.0
%global libvpx_version	1.5.0
%global webp_version	1.0.2
%global icu_version	63.1
%global ffi_version	3.0.9
%global libaom_version	1.0.0
%global dav1d_version	0.5.2

%define homepage http://start.fedoraproject.org/

%define sources_subdir %{name}-%{version}

%define seamonkey_app_id	\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}


Name:           seamonkey
Summary:        Web browser, e-mail, news, IRC client, HTML editor
Version:        2.53.20
Release:        1%{?dist}
URL:            http://www.seamonkey-project.org
License:        MPL-2.0


Source0:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
%if %{with langpacks}
Source1:	http://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
%endif

Source3:	seamonkey-2.53.20-GNUmakefile
Source4:	seamonkey.desktop
Source5:	seamonkey-mail.desktop
Source6:	seamonkey-ua-update.json.in

Patch2:		seamonkey-2.53.20-mozilla-1894423.patch
Patch3:		seamonkey-2.53.17-mozilla-1516803.patch
Patch4:		seamonkey-2.53.18-mozilla-1862601.patch
Patch5:		firefox-35-rhbz-1173156.patch
Patch7:		firefox-51-mozilla-1005640.patch
Patch8:		seamonkey-2.53.19-mozilla-1882209.patch
Patch9:		seamonkey-2.53.1-mozilla-revert-1332139.patch
Patch11:	seamonkey-2.53.16-mozilla-1434478.patch
Patch13:	seamonkey-2.53.10-mozilla-1460295.patch
Patch14:	seamonkey-2.53.11-adjacent-sibling.patch
Patch15:	seamonkey-2.53.17-mozilla-1442861.patch
Patch16:	seamonkey-2.53.14-fix-1485179.patch
Patch17:	seamonkey-2.53.8-mozilla-1661070-1.patch
Patch18:	seamonkey-2.53.8-mozilla-1661070-2.patch
Patch19:	seamonkey-2.53.20-system-av1.patch
Patch21:	seamonkey-2.53.18-media-document.patch
Patch23:	seamonkey-2.53.9-revert-1593550.patch
Patch24:	seamonkey-2.53.20-install_man.patch
Patch25:	seamonkey-2.53.7-mailnews-useragent.patch
Patch26:	seamonkey-2.53.13-userDisabled.patch
Patch27:	seamonkey-2.53.8-ext-if-needed.patch
Patch28:	seamonkey-2.53.20-mozilla-1619108.patch
Patch29:	seamonkey-2.53.15-prtypes.patch
Patch30:	seamonkey-2.53.5-nss_pkcs11_v3.patch
Patch31:	seamonkey-2.53.1-mozilla-526293.patch
Patch34:	seamonkey-2.53.3-startupcache.patch
Patch35:	seamonkey-2.53.8-server-folder.patch
Patch36:	seamonkey-2.53.15-locale-matchos-UI.patch
Patch37:	seamonkey-2.53.20-mozilla-1720968.patch
Patch38:	seamonkey-2.53.8-mozilla-521861.patch
Patch39:	seamonkey-2.53.8.1-dateformat.patch
Patch40:	seamonkey-2.53.10-slowscript.patch
Patch42:	seamonkey-2.53.10-postmessage-event.patch
Patch43:	seamonkey-2.53.20-mozilla-1502802.patch

Patch60:	seamonkey-2.53.11-ua-update.patch
Patch61:	seamonkey-2.53.13-ua-update-preload.patch
Patch62:	seamonkey-2.53.20-compat-version.patch
Patch65:	seamonkey-2.53.17-fix-1406821.patch
Patch66:	seamonkey-2.53.11-startupcache1.patch
Patch69:	seamonkey-2.53.20-stylo_config.patch

%{?with_system_nspr:BuildRequires:      nspr-devel >= %{nspr_version}}
%{?with_system_nss:BuildRequires:       nss-devel >= %{nss_version}}
%{?with_system_nss:BuildRequires:       nss-static >= %{nss_version}}
%{?with_system_libvpx:BuildRequires:    libvpx-devel >= %{libvpx_version}}
%{?with_system_webp:BuildRequires:      libwebp-devel >= %{webp_version}}
%{?with_system_icu:BuildRequires:       libicu-devel >= %{icu_version}}
%{?with_system_ffi:BuildRequires:       libffi-devel >= %{ffi_version}}
%{?with_system_av1:BuildRequires:       libaom-devel >= %{libaom_version}}
%{?with_system_av1:BuildRequires:       libdav1d-devel >= %{dav1d_version}}

BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  zlib-devel
BuildRequires:  zip
BuildRequires:  libIDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  krb5-devel
BuildRequires:  pango-devel
BuildRequires:  freetype-devel >= 2.1.9
BuildRequires:  glib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  coreutils
BuildRequires:  alsa-lib-devel
BuildRequires:  libnotify-devel
BuildRequires:  yasm >= 1.1
BuildRequires:  mesa-libGL-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  startup-notification-devel
BuildRequires:  nasm >= 2.14

BuildRequires:  make
BuildRequires:  m4
BuildRequires:  perl-interpreter

%if %{with clang} || %{with stylo}
BuildRequires:	clang17, llvm-devel
%endif
%if %{without clang}
BuildRequires:	gcc-c++ >= 7.1
%endif

BuildRequires:	rust >= 1.61
BuildRequires:	cargo

# temporary to avoid python-3.12 issues
BuildRequires: python3.11-devel

Requires:       mozilla-filesystem
Requires:       hicolor-icon-theme
Requires:       p11-kit-trust
%{?with_system_nspr:Requires:      nspr >= %{nspr_version}}
%{?with_system_nss:Requires:       nss >= %{nss_version}}

# ppc64:   http://bugzilla.redhat.com/bugzilla/866589
# armv7hl: http://bugzilla.redhat.com/bugzilla/1035485
# %%{ix86}: no more supported upstream
ExclusiveArch:  x86_64

Provides: webclient


%description
SeaMonkey is an all-in-one Internet application suite (previously made
popular by Netscape and Mozilla). It includes an Internet browser,
advanced e-mail, newsgroup and feed client, a calendar, IRC client,
HTML editor and a tool to inspect the DOM for web pages. It is derived
from the application formerly known as Mozilla Application Suite.
 

%prep

%setup -q -c

mv %{sources_subdir} mozilla

%if %{with langpacks}
%setup -q -T -D -c -n %{name}-%{version}/l10n -a 1
#  come back...
%setup -q -T -D
%endif

cd mozilla

cp %{SOURCE3} GNUmakefile

%patch 2 -p1 -b .1894423
%patch 3 -p1 -b .1516803
%patch 4 -p1 -b .1862601
%patch 5 -p2 -b .1173156
%patch 7 -p1 -b .1005640
%patch 8 -p1 -b .1882209
%{?with_system_libvpx:%patch 9 -p1 -b .1332139}
%patch 11 -p1 -b .1434478
%patch 13 -p1 -b .1460295
%patch 14 -p1 -b .adjacent-sibling
%patch 15 -p1 -b .1442861
%patch 16 -p1 -b .1485179
%patch 17 -p1 -b .1661070-1
%patch 18 -p0 -b .1661070-2
%patch 19 -p1 -b .system_av1
%patch 21 -p1 -b .media-document
%patch 23 -p1 -b .1593550
%patch 24 -p0 -b .install_man
%patch 25 -p0 -b .mailnews-useragent
%patch 26 -p1 -b .userDisabled
%patch 27 -p0 -b .ext-if-needed
%patch 28 -p0 -b .1619108

%{?with_system_nss:%patch 29 -p1 -b .prtypes}
%{?with_system_nss:%patch 30 -p3 -b .nss_pkcs11_v3}
%patch 31 -p3 -b .526293
%patch 34 -p2 -b .startupcache
%patch 35 -p0 -b .server-folder
%patch 36 -p0 -b .locale_matchos
%patch 37 -p1 -b .1720968
%patch 38 -p0 -b .521861
%patch 39 -p1 -b .dateformat
%patch 40 -p0 -b .slowscript
%patch 42 -p1 -b .postmessage-event
%patch 43 -p1 -b .1502802

%patch 60 -p1 -b .ua-update
%patch 61 -p1 -b .ua-update-preload
%patch 62 -p1 -b .compat-version
%patch 65 -p1 -b .1406821
%patch 66 -p1 -b .startupcache1
%patch 69 -p1 -b .stylo_config

%if %{without calendar}
sed -i 's/MOZ_CALENDAR/UNDEF_MOZ_CALENDAR/' comm/suite/installer/package-manifest.in
%endif

cp %{SOURCE6} comm/suite/app/ua-update.json.in


#
#   generate .mozconfig
#

cat >.mozconfig <<EOF
ac_add_options --enable-application=comm/suite

export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1

mk_add_options MOZ_OBJDIR=../obj-@CONFIG_GUESS@

ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --mandir=%{_mandir}

#  to know where to remove extra things...
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}

ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --disable-tests
ac_add_options --disable-install-strip
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --enable-chrome-format=omni
ac_add_options --disable-necko-wifi
ac_add_options --enable-optimize=-O2

ac_add_options --enable-startupcache

%define with_sys()	ac_add_options --with%%{!?with_system_%1:out}-system-%1
%define endis_sys()	ac_add_options --%%{?with_system_%1:enable}%%{!?with_system_%1:disable}-system-%1
%define endis()		ac_add_options --%%{?with_%1:enable}%%{!?with_%1:disable}-%1

%{expand:%with_sys   nspr}
%{expand:%with_sys   nss}
%{expand:%with_sys   libvpx}
%{expand:%with_sys   webp}
%{expand:%with_sys   icu}
%{expand:%with_sys   av1}

%{expand:%endis_sys  ffi}

#  always enable calendar to build needed internal components required for both bundled and external addons
ac_add_options --enable-calendar

%{expand:%endis dominspector}
%{expand:%endis irc}
%{expand:%endis debugqa}


ac_add_options --disable-webrender
ac_add_options %{?with_stylo:--enable-stylo=build}%{!?with_stylo:--disable-stylo}


%if %{with langpacks}
ac_add_options --with-l10n-base=../l10n
%endif

EOF
#  .mozconfig


#
#   generate default prefs
#
cat >all-fedora.js <<EOF

pref("app.update.auto", false);
pref("app.update.enabled", false);
pref("app.updatecheck.override", true);
pref("extensions.update.autoUpdateDefault", false);
pref("browser.helperApps.deleteTempFileOnExit", true);
pref("general.smoothScroll", true);
pref("extensions.shownSelectionUI", true);
pref("extensions.autoDisableScopes", 0);
pref("shell.checkDefaultApps",   0);
pref("media.gmp-gmpopenh264.provider.enabled", false);
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.enabled", false);
pref("gfx.xrender.enabled", true);
pref("devtools.webide.enabled", false);
pref("general.warnOnAboutConfig", false);
pref("nglayout.enable_drag_images", false);

pref("browser.startup.homepage", "data:text/plain,browser.startup.homepage=%{homepage}");

/*  point user to the addons page at the first run   */
pref("startup.homepage_override_url", "about:addons|http://www.seamonkey-project.org/releases/seamonkey%VERSION%/");
pref("extensions.ui.lastCategory", "addons://list/extension");

/*  use system dictionaries (hunspell)   */
pref("spellchecker.dictionary_path", "%{_datadir}/hunspell");

/*  provide "locale match OS" behaviour   */
pref("intl.locale.requested", "");
pref("intl.regional_prefs.use_os_locales", true);

/* Allow sending credetials to all https:// sites */
pref("network.negotiate-auth.trusted-uris", "https://");

/* To avoid UA string garbling by the old instances of Lightning  */
pref("calendar.useragent.extra", "", locked);

/* Completely mimic to Firefox for compatibility with this World nowadays...  */
pref("general.useragent.compatMode.strict-firefox", true);
pref("general.useragent.compatMode.version", "91.0");

pref("network.http.sendOriginHeader", 1);

/* Keep the same behaviour as for years  */
pref("browser.tabs.autoHide", true);
pref("mail.tabs.autoHide", true);

/* Avoid new "pulse-rust" for a while for stability reasons  */
pref("media.cubeb.backend", "pulse");

EOF
# all-fedora.js


%build

cd mozilla

# temporary to avoid python-3.12 issues
sed -i -e 's/python3/python3.11/' mach

%if %{with clang}
%define toolchain  clang
export CC=clang-17
export CXX=clang++-17
%endif

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-Wall//')
MOZ_LINK_FLAGS=

# Elfhack is incompatible with "rosegment" linker option,
# which became default with binutils >= 2.43 .
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--no-rosegment"

%if %{with lto}
%if %{with clang}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto=thin"
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -flto=thin -fuse-ld=lld -Wl,-plugin-opt=-import-instr-limit=10"
export AR=llvm-ar
export RANLIB=llvm-ranlib
%else
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto -flifetime-dse=1"
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -flto=${MOZ_SMP_FLAGS#-j} -flifetime-dse=1"
export AR=gcc-ar
export RANLIB=gcc-ranlib
%endif
%else
#  avoid system-wide lto
%define _lto_cflags %{nil}
%endif

%if %(awk '/^MemTotal:/ { print $2 }' /proc/meminfo) <= 4200000
MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--no-keep-memory"
${CC:-%{__cc}} -x c $MOZ_LINK_FLAGS -Wl,--version -o /dev/null /dev/null | grep '^GNU ld ' && \
	MOZ_LINK_FLAGS="$MOZ_LINK_FLAGS -Wl,--reduce-memory-overheads"
%endif
  
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS
export LDFLAGS=$MOZ_LINK_FLAGS

unset RUSTFLAGS


make %{?_smp_mflags}

%if %{with langpacks}
make -j1 locales
%endif


%install

cd mozilla

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/removed-files
rm -f $RPM_BUILD_ROOT/%{_libdir}/seamonkey/libnssckbi.so

#   default prefs
install -p -m 644 all-fedora.js \
	$RPM_BUILD_ROOT/%{_libdir}/seamonkey/defaults/pref/all-fedora.js

install -d -m 755 $RPM_BUILD_ROOT/%{_libdir}/seamonkey/plugins || :

# system hunspell dictionaries are used instead
rm -rf $RPM_BUILD_ROOT%{_libdir}/seamonkey/dictionaries/*


for ext in $RPM_BUILD_ROOT/%{_libdir}/seamonkey/extensions/langpack-*@seamonkey.mozilla.org.xpi
do
    [ -f $ext ] || continue
    lang=${ext##*langpack-}
    lang=${lang%@*}
    lang=${lang/-/_}
    echo "%%lang($lang) ${ext#$RPM_BUILD_ROOT}"
done >../seamonkey.lang


# install desktop files in correct directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE5}


# install icons
icons=$RPM_BUILD_ROOT%{_datadir}/icons/hicolor

pushd $RPM_BUILD_ROOT%{_libdir}/seamonkey/chrome/icons/default
install -p -m 644 -D default16.png	$icons/16x16/apps/seamonkey.png
install -p -m 644 -D default22.png	$icons/22x22/apps/seamonkey.png
install -p -m 644 -D default24.png	$icons/24x24/apps/seamonkey.png
install -p -m 644 -D default32.png	$icons/32x32/apps/seamonkey.png
install -p -m 644 -D default48.png	$icons/48x48/apps/seamonkey.png
install -p -m 644 -D default64.png	$icons/64x64/apps/seamonkey.png
install -p -m 644 -D default128.png	$icons/128x128/apps/seamonkey.png
install -p -m 644 -D default256.png	$icons/256x256/apps/seamonkey.png
install -p -m 644 -D messengerWindow16.png	$icons/16x16/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow.png	$icons/32x32/apps/seamonkey-mail.png
install -p -m 644 -D messengerWindow48.png	$icons/48x48/apps/seamonkey-mail.png
popd

pushd comm/suite/branding/seamonkey/icons/svg
install -p -m 644 -D seamonkey.svg	$icons/scalable/apps/seamonkey.svg
install -p -m 644 -D messengerWindow.svg	$icons/scalable/apps/seamonkey-mail.svg
popd


# System extensions
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/extensions/%{seamonkey_app_id}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/%{seamonkey_app_id}


#  Only now and just define (not global)
%define __provides_exclude_from ^%{_libdir}/seamonkey
%define __requires_exclude     ^(%(find %{buildroot}%{_libdir}/seamonkey -name "lib*.so" -printf "%%f " | sed -e 's/.so /|/g' -e 's/|$//'))\\.so.*


%files -f seamonkey.lang

%license %{_libdir}/seamonkey/license.txt

%{_libdir}/seamonkey

%{_bindir}/seamonkey
%{_mandir}/*/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop

%dir %{_datadir}/mozilla/extensions/%{seamonkey_app_id}
%dir %{_libdir}/mozilla/extensions/%{seamonkey_app_id}


%changelog
* Mon Jan  6 2025 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.20-1
- update to 2.53.20

* Sat Aug 31 2024 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.19-1
- update to 2.53.19

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Nicolas Chauvet <kwizart@gmail.com> - 2.53.18.2-3
- Rebuilt for libplacebo/vmaf

* Sat Apr  13 2024 Miroslav Suchý <msuchy@redhat.com> - 2.53.18.2-2
- convert license to SPDX

* Sat Mar 23 2024 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.18.2-1
- update to 2.53.18.2
- add patch for system icu-74.1 (mozbz 1862601)

* Wed Mar 13 2024 Sérgio Basto <sergio@serjux.com> - 2.53.18.1-4
- Rebuild for jpegxl (libjxl) 0.10.2
- Fix build with icu_74.1

* Wed Feb 14 2024 Sérgio Basto <sergio@serjux.com> - 2.53.18.1-3
- Rebuild for jpegxl (libjxl) 0.9.2 with soname bump

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.18.1-1
- update to 2.53.18.1

* Fri Jan 12 2024 Fabio Valentini <decathorpe@gmail.com> - 2.53.18-2
- Rebuild for dav1d 1.3.0

* Fri Dec  8 2023 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.18-1
- update to 2.53.18
- add patch for binutils >= 2.36

* Sun Jul 30 2023 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.17-1
- update to 2.53.17
- enable webcomponents and pointer-events (upcoming upstream changes)
- send origin header (for same-origin only) to satisfy client checking sites
- backport fixes for mozbz 1502801 and mozbz 1502802
- fix mozbz 1406821 to avoid extra debug output
- add support for ffmpeg-6.0
- no more needed python2.7 for build
- drop obsoleted gconf2 support

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 2.53.16-3
- Rebuilt for ICU 73.2

* Sun Jun 18 2023 Sérgio Basto <sergio@serjux.com> - 2.53.16-2
- Mass rebuild for jpegxl-0.8.1

* Thu Mar 30 2023 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.16-1
- update to 2.53.16
- backport fix for mozbz 1769631

* Wed Feb 15 2023 Tom Callaway <spot@fedoraproject.org> - 2.53.15-2
- rebuild for libvpx

* Sat Jan 21 2023 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.15-1
- update to 2.53.15
- add fix for mozbz 1464782

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 2.53.14-4
- Rebuild for ICU 72

* Mon Oct  3 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.14-3
- add fix for mozbz 1443429 and mozbz 1443746,
  return no more broken patches

* Sun Oct  2 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.14-2
- rebuild without potentially broken patches

* Tue Sep 27 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.14-1
- update to 2.53.14

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.53.13-3
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  8 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.13-1
- update to 2.53.13
- add support for ffmpeg-5.0

* Thu Jun 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.53.12-2
- Rebuilt for new aom, dav1d and jpegxl

* Tue May  3 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.12-1
- update to 2.53.12

* Mon Apr 11 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.11.1-2
- backport fix for wasm gc (mozbz 1459761 and others)
- fix adjacent sibling patch

* Sat Mar 26 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.11.1-1
- update to 2.53.11.1

* Wed Feb 23 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.11-1
- update to 2.53.11
- use ua-update.json mechanism for site-specific user-agent overrides
- fix some minor issues

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 2.53.10.2-4
- rebuild for libvpx

* Tue Jan 25 2022 Parag Nemade <pnemade AT redhat DOT com> - 2.53.10.2-3
- Update hunspell directory path
  F36 Change https://fedoraproject.org/wiki/Changes/Hunspell_dictionary_dir_change

* Sat Jan 22 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.10.2-2
- fix baselinejit for optional chaining support
- fix compile with libstdc++ >= 12

* Wed Jan 12 2022 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.10.2-1
- update to 2.53.10.2
- backport nullish coalescing support (mozbz 1566141 and others)
- backport optional chaining support (mozbz 1566143 and others)

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 2.53.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Dec 15 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.10.1-1
- update to 2.53.10.1
- backport new regexp stuff (derived from Waterfox-Classic)
- backport fixes for mozbz 1434478, 1449641, 1460295
- fix possible postMessage race conditions

* Tue Nov 30 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.10-2
- add allsettled patch

* Tue Nov 23 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.10-1
- update to 2.53.10
- backport support for custom date format (mozbz#1426907)
- fix compile with rust >= 1.56

* Thu Jul 22 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.8.1-1
- update to 2.53.8.1
- no more set nglayout.enable_drag_images by default
- fix mailnews account creation after subscribing by a news URL (mozbz#521861)
- avoid staring drag-and-drop in full mailnews's Wide View (mozbz#1720968)
- fix clearing in download manager (mozbz#1501277)

* Mon Jun 28 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.8-1
- update to 2.53.8
- fix irc link behaviour and websearch (mozbz#1712498, mozbz#1713458, mozbz#1713467)
- fix handling of mail attachments (mozbz#1661070)
- no more set browser.display.use_system_colors by default

* Sun Jun 13 2021 Robert-Andre Mauchin <zebob.m@gmail.com> - 2.53.7-5
- Rebuilt for aom v3.1.1
- Add patch to build against nss 3.66

* Thu May 20 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.7-4
- move extensions' localization data into the common langpack
- fix cpu hogging on network link change when websockets are in use (mozbz#1633339)
- better support of the obsoleting javascript versioning stuff (mozbz#1702903)
- fix number formats (mozbz#1403319)
- fix build with rust >= 1.52 (mozbz#1670538)

* Sat Apr 10 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.7-3
- better support obsoleting javascript stuff (mozbz#1702903)
- fixed selection of tab to return on tab close (mozbz#1623054)
- fixed opening tabs in background in some cases (mozbz#1619108)
- provide a way to auto-select es-AR locale on any Spanish one but es-ES

* Fri Apr  2 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.7-2
- fix obsoleting "for each" javascript statements support
- no need to provide own dictionaries (system are used anyway)

* Tue Mar 30 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.7-1
- update to 2.53.7
- fix keyboard input with gtk3 >= 3.24.26 (mozbz #1701288)
- backport some refresh driver improvements from upcoming 2.53.8
- avoid spurious update of intersection observers in a case
  of throbber animation
- restore traditional security-button background (to match the location bar
  highlighting, revert mozbz #1593550)
- for new installs add about:addons to the initial pages and
  don't enable inspector and calendar there by default
- enable upcoming module scripts support

* Fri Jan 22 2021 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.6-1
- update to 2.53.6
- build with own GNUmakefile, spec file cleanup

* Tue Nov 17 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-3
- add media-document patch (mozbz#1677768)
- add packed_simd patch (mozbz#1617782)

* Sun Nov 15 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-2
- fix for av1 (mozbz#1490877)
- fix main svg icon

* Thu Nov 12 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.5-1
- update to 2.53.5
- add patch to build with system libaom and libdav1d
- add official logo icon in svg format

* Wed Sep  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.4-1
- update to 2.53.4
- replace all the distributed extensions (calendar, dominspector and irc)
  as intergated app-global extensions (ie. moved from distribution/extensions/
  just to extensions/ , mozbz#1659298)
- update seamonkey(1) manual page
- update description in spec file

* Thu Jul 30 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-3
- fix requires filter

* Wed Jul 29 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-2
- add "Default zoom" support (mozbz#1655362)
- add "Use system locale" switch in preferences (mozbz#1655842)
- backport WebP image format support (mozbz#1653869)
- update elfhack code up to esr68
- add fix for rust >= 1.45 (mozbz#1654465)
- properly filter provides and requires from the application dir
- spec file cleanups and fixes

* Mon Jul  6 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.3-1
- update to 2.53.3
- use sql nss databases (cert9.db, key4.db etc.) since the old format
  is stopping be supported.

* Mon May  4 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.2-1
- update to 2.53.2
- drop startup shell script (no more needed)

* Thu Apr  9 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-5
- rebuild with rust-1.42

* Wed Mar 25 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-4
- drop system-bookmarks dependencies

* Sat Mar 21 2020 Dmitry Butskoy <Dmitry@Butskoy.name> 2.53.1-3
- fix localization for bundled calendar and chatzilla (#1815109)
- clear obsolete stuff from desktop-file-install

* Tue Mar  3 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-2
- add patch for classic theme (#1808197)

* Fri Feb 28 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.53.1-1
- Upgrade to 2.53.1
- use clang to build

* Mon Sep  9 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-2
- rebuid to properly handle external lightning extension (#1750450)

* Sat Aug 24 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.5-1
- update to 2.49.5
- add support for conditional build of inspector and irc

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-5
- add patch for new gettid() in glibc >= 2.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.49.4-4
- rebuilt (libvpx)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.49.4-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.49.4-1
- update to 2.49.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-3
- Rebuild for ICU 62

* Wed May 16 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.3-2
- Rebuild for ICU 61.1

* Fri May  4 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.3-1
- update to 2.49.3

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.49.2-3
- Rebuild for ICU 61.1

* Sun Feb 18 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-2
- revert some upstream gtk3-related changes to avoid regressions
  since we still build with gtk2 (mozbz#1269145, mozbz#1398973)
- spec file cleanup from old deprecated stuff

* Sat Feb 17 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.2-1
- update to 2.49.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-4
- rebuild for libvpx 1.7.0

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> 2.49.1-3
- rebuild for new libvpx

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> 2.49.1-2
- rebuild for hunspell 1.6.2

* Sat Oct 21 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.49.1-1
- update to 2.49.1
- apply some patches from firefox-52.4.0 package
- disable webide by default to avoid autoload of broken addons

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.48-1
- update to 2.48
- apply some patches from firefox-51 package
- use standard optimize level -O2 for compiling
- new langpacks obtaining stuff for more easier maintaining
- revert broken mozbz#1148544 changes for site-specific overrides

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-2
- fix for new system nss (#1414982, mozbz#1290037)
- fix build with system icu (mozbz#1329272)

* Fri Dec 23 2016 Dmitry Butskoy <Dmitry@Butskoy.name> 2.46-1
- update to 2.46
- apply some patches from firefox-49 package
- avoid runtime linking with too old ffmpeg libraries (#1330898)
- still enable XRender extension by default

