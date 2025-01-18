%if 0%{?fedora}
# With _package_note_file enabled, godot.x11.opt.tools fails to link with:
# g++: fatal error: environment variable 'RPM_ARCH' not defined
%undefine _package_note_file
%ifarch %{arm32}
%global _lto_cflags %nil
%endif
%endif

# Undefine for stable
#define prerel  1
%define status  stable
%define uversion %{version}-%{status}

%define rdnsname org.godotengine.Godot

Name:           godot
Version:        4.3
Release:        4%{?dist}
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor
%if 0%{?mageia}
Group:          Development/Tools
%endif
# Godot itself is MIT-licensed, the rest is from vendored thirdparty libraries
# Automatically converted from old format: MIT and CC-BY and ASL 2.0 and BSD and zlib and OFL and Bitstream Vera and ISC and MPLv2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY AND Apache-2.0 AND LicenseRef-Callaway-BSD AND Zlib AND LicenseRef-Callaway-OFL AND Bitstream-Vera AND ISC AND MPL-2.0
URL:            https://godotengine.org
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{?prerel:%{status}/}%{name}-%{uversion}.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{?prerel:%{status}/}%{name}-%{uversion}.tar.xz.sha256

# Preconfigure Blender and oidnDenoise paths to use system-installed versions.
Patch0:         preconfigure-blender-oidn-paths.patch
# https://github.com/godotengine/godot/pull/95658
Patch1:         0001-OpenXR-Fix-support-for-building-against-distro-packa.patch
# https://github.com/godotengine/godot/commit/4c72d599f0a171a96e47004239f42756115b723f
Patch2:         %{name}-miniupnp228.patch

# Upstream does not support this arch (for now)
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  libsquish-devel
BuildRequires:  mbedtls-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)

%ifarch aarch64 x86_64
BuildRequires:  embree-devel >= 4
%endif

%if 0%{?mageia}
BuildRequires:  scons
%else
BuildRequires:  python3-scons
%endif

# See bundled section for explanations.
%define system_glslang 0
%define system_recastnavigation 0%{?mageia}

%if %{system_glslang}
BuildRequires:  glslang-devel
%endif

%if %{system_recastnavigation}
BuildRequires:  recastnavigation-devel
%endif

# For desktop and appdata files validation
BuildRequires:  desktop-file-utils
%if 0%{?mageia}
BuildRequires:  appstream-util
%else
BuildRequires:  libappstream-glib
%endif

# Ensure the hicolor icon theme dirs exist
Requires:       hicolor-icon-theme

# To support importing .blend files
Recommends:     blender
# For better denoising of lightmaps, using oidnDenoise
Recommends:     oidn

# Bundled libraries: many of the libraries code in `thirdparty` can be
# unbundled when the libraries are provided by the system. Keep in mind
# though that the `thirdparty` folder also contains code which is typically
# not packaged in distros, and is probably best left bundled.

# Has some modifications for IPv6 support, upstream enet is unresponsive.
# Should not be unbundled.
# Cf: https://github.com/godotengine/godot/issues/6992
Provides:       bundled(enet) = 1.3.18
%if ! %{system_glslang}
# Fedora package only provides static libs, needs more work to be usable.
Provides:       bundled(glslang) = 14.2.0
%endif
# Has custom changes to support seeking in zip archives.
# Should not be unbundled.
Provides:       bundled(minizip) = 1.3.1
%if ! %{system_recastnavigation}
# Could be unbundled if packaged.
Provides:       bundled(recastnavigation) = 1.6.0
%endif

Obsoletes:      godot-headless < 4.0-1
Provides:       godot-headless == %{version}-%{release}

%description
Godot is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

To use the editor on the command line in a non-graphical environment (e.g. to
export games from the source code), use the --headless flag.

%files
%doc CHANGELOG.md DONORS.md README.md
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt LOGO_LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%{_datadir}/mime/packages/%{rdnsname}.xml
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%package        runner
Summary:        Shared binary to play games and run servers developed with the Godot engine
%if 0%{?mageia}
Group:          Games/Other
%endif
Obsoletes:      godot-server < 4.0-1
Provides:       godot-server == %{version}-%{release}

%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

To run the game as a dedicated server, use the --headless flag.

%files          runner
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-runner

#----------------------------------------------------------------------

%{lua: function get_godot_arch()
  arch = rpm.expand("%{_target_cpu}")
  if string.match(rpm.expand("%{arm32}"), arch) then
    arch = "arm32"
  elseif string.match(rpm.expand("%{arm64}"), arch) then
    arch = "arm64"
  elseif string.match(rpm.expand("%{ix86}"), arch) then
    arch = "x86_32"
  elseif string.match(rpm.expand("%{power64}"), arch) then
    arch = "ppc64"
  elseif string.match(rpm.expand("%{riscv64}"), arch) then
    arch = "rv64"
  end
  return arch
end}

%define godot_arch %{lua: print(get_godot_arch())}

%prep
%autosetup -p1 -n %{name}-%{uversion}

%build
# Needs to be in %%build so that system_libs stays in scope
# We don't unbundle enet and minizip as they have necessary custom changes
to_unbundle="brotli embree freetype graphite harfbuzz icu4c libogg libpng libtheora libvorbis libwebp mbedtls miniupnpc openxr pcre2 squish wslay zlib zstd"

%if %{system_glslang}
to_unbundle+=" glslang"
%endif
%if %{system_recastnavigation}
to_unbundle+=" recastnavigation"
%endif

# Disable dlopen wrappers for Linux deps, we link them dynamically.
system_libs="use_sowrap=no "
rm -rf thirdparty/linuxbsd_headers

for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done

%define _scons scons %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" arch=%{godot_arch} $system_libs use_lto=yes use_static_cpp=no debug_symbols=yes progress=no

%if 0%{?fedora}
export BUILD_NAME="fedora"
%endif
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif

# Build graphical editor.
%_scons p=linuxbsd target=editor

# Build game runner.
%_scons p=linuxbsd target=template_release

%install
install -d %{buildroot}%{_bindir}
install -m755 bin/%{name}.linuxbsd.editor.%{godot_arch} %{buildroot}%{_bindir}/%{name}
install -m755 bin/%{name}.linuxbsd.template_release.%{godot_arch} %{buildroot}%{_bindir}/%{name}-runner

install -D -m644 icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m644 misc/dist/linux/%{rdnsname}.desktop \
    %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
install -D -m644 misc/dist/linux/%{rdnsname}.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
install -D -m644 misc/dist/linux/%{rdnsname}.xml \
    %{buildroot}%{_datadir}/mime/packages/%{rdnsname}.xml
install -D -m644 misc/dist/linux/%{name}.6 \
    %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m644 misc/dist/shell/%{name}.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m644 misc/dist/shell/%{name}.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m644 misc/dist/shell/_%{name}.zsh-completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
# Validate desktop and appdata files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 4.3-3
- Rebuild for ICU 76

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 4.3-2
- Rebuild for updated miniupnpc.

* Wed Sep 04 2024 Rémi Verschelde <akien@fedoraproject.org> - 4.3-1
- Version 4.3-stable
- Adds Wayland support (opt-in)
- Use system embree4 and openxr on all supported Fedora versions

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.2.2-4
- Rebuilt for mbedTLS 3.6.1

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 17 2024 Rémi Verschelde <akien@fedoraproject.org> - 4.2.2-1
- Version 4.2.2-stable

* Mon Mar 25 2024 Nianqing Yao <imbearchild@outlook.com> - 4.2.1-5
- Fix build on riscv64

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-4
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.2.1-1
- Version 4.2.1-stable
- OIDN no longer bundled, recommend system package for the oidnDenoise binary

* Thu Oct 12 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.1.2-1
- Version 4.1.2-stable
- Updates tinyexr to 1.0.7, fixes CVE-2022-34300 (rhbz#2233637)
- Preconfigure Blender path for .blend file import (rhbz#2177897)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 4.1-2
- Rebuilt for ICU 73.2

* Thu Jul 06 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.1-1
- Version 4.1-stable
- Enable pcc64le support, added in Godot 4.0
- Unbundle brotli

* Sun May 21 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.0.3-1
- Version 4.0.3-stable
- Fix MIME type definition file location

* Tue Apr 04 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.0.2-1
- Version 4.0.2-stable

* Tue Mar 28 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.0.1-1
- Version 4.0.1-stable

* Fri Mar 10 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.0-2
- Obsolete headless/server packages
- Fix F36 armv7hl build by forcing LTO off

* Fri Mar 10 2023 Rémi Verschelde <akien@fedoraproject.org> - 4.0-1
- Version 4.0-stable, major release with compatibility breakage
- Remove headless and server packages, base godot and godot-runner can now be ran with --headless
- New dependencies: dbus-1, fontconfig, harfbuzz, graphite2, icu, libsquish, openxr, speech-dispatcher, wslay, xext, xkbcommon
- The 3.x branch is still provided in the new godot3 package

* Tue Feb 21 2023 Rémi Verschelde <akien@fedoraproject.org> - 3.4.5-4
- Use bundled embree3 for F38 and later, not compatible with embree4 yet

* Wed Feb 15 2023 Tom Callaway <spot@fedoraproject.org> - 3.4.5-3
- rebuild for libvpx
- fix issue where uint32_t was undefined (add #include <cstdint>)
- undefine _package_note_file to fix "RPM_ARCH not defined" failure at linktime

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Rémi Verschelde <akien@fedoraproject.org> - 3.4.5-1
- Version 3.4.5-stable

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Rémi Verschelde <akien@fedoraproject.org> - 3.4.4-1
- Version 3.4.4-stable

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 3.3.3-3
- rebuild for libvpx

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 3.3.3-2
- Rebuilt for mbedTLS 2.28.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Rémi Verschelde <akien@fedoraproject.org> - 3.3.3-1
- Version 3.3.3-stable

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Rémi Verschelde <akien@fedoraproject.org> - 3.3.2-1
- Version 3.3.2-stable
- Embree (raycast module) now available for aarch64

* Fri Apr 23 2021 Rémi Verschelde <akien@fedoraproject.org> - 3.3-1
- Version 3.3-stable
- New lightmapper (x86_64 only) uses embree (system) and oidn (bundled)

* Thu Apr 01 2021 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-2
- Fix release tag

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-1.1
- Rebuilt for removed libstdc++ symbol (#1937698)

* Fri Feb 12 2021 Rémi Verschelde <akien@fedoraproject.org> - 3.2.3-1
- Version 3.2.3-stable
- Drop tentative support for building for RHEL8
- Backport upstream patch to fix TGA loader crash (CVE-2021-26825, CVE-2021-26826)
- Adds fish completion files

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Rémi Verschelde <akien@fedoraproject.org> - 3.2.1-1
- Version 3.2.1-stable
- Bundles assimp, requires development version not packaged anywhere
- Bundles libwslay, not packaged on Fedora (replaces libwebsockets)
- Adds bash and zsh completion files

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Rémi Verschelde <akien@fedoraproject.org> - 3.1.2-1
- Version 3.1.2-stable
- Bundled libwebsockets was downgraded to 3.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Rémi Verschelde <akien@fedoraproject.org> - 3.1.1-1
- Version 3.1.1-stable
- Adds dependency on system mbedtls and miniupnpc
- Removes dependency on openssl
- Bundles libwebsockets, can't build against system one for now
- Bundles tinyexr, not packaged (and likely not relevant to package)
- Rename -server build to -headless, add an actual server runtime package
- Build with LTO, improves performance a lot (but slow linking)
- Adds MIME type for .godot project files

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.6-3
- rebuilt (libvpx)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.6-1
- Version 3.0.6-stable (fixes CVE-2018-1000224)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.4-1
- Version 3.0.4-stable

* Wed Jun 20 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.3-1
- Version 3.0.3-stable
- Enable aarch64 support

* Mon Mar 26 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.2-2
- Fix inclusion of armv7hl-specific patch in SRPM

* Tue Mar 20 2018 Rémi Verschelde <akien@fedoraproject.org> - 3.0.2-1
- Initial Godot package for Fedora, based on my own Mageia package.
- Exclude unsupported arches: aarch64 ppc64 ppc64le s390x
- Workaround GCC < 8.1 ICE on armv7hl

* Wed Mar 14 2018 Rémi Verschelde <akien@mageia.org> 3.0.2-2.mga7
+ Revision: 1209402
- Fix launch argument of desktop file

* Sun Mar 04 2018 Rémi Verschelde <akien@mageia.org> 3.0.2-1.mga7
+ Revision: 1206473
- Add upstream patch to fix server platform build
- Version 3.0.2-stable

* Fri Feb 02 2018 Rémi Verschelde <akien@mageia.org> 3.0-3.mga7
+ Revision: 1198620
- Update tarball to final 3.0-stable

* Fri Feb 02 2018 David GEIGER <daviddavid@mageia.org> 3.0-2.mga7
+ Revision: 1198552
- rebuild for new libvpx 1.7.0

* Fri Jan 26 2018 Rémi Verschelde <akien@mageia.org> 3.0-1.mga7
+ Revision: 1197290
- Disable LTO, seems to break debuginfo
- New upstream tarball with fixed debuginfo stripping
- Prevent stripping binaries
- Don't unbundle zstd yet as Godot uses experimental APIs exposed only in the static library
- Keep bundled bullet, needs >= 2.88 which is not released yet
- Version 3.0-stable
- No longer provide demos, they can be downloaded from the editor
- Disable server binary, not available in 3.0
- Compile with GCC and LTO
- Document bundled() provides thoroughly
- Document bundled() provides

* Sun Dec 03 2017 David GEIGER <daviddavid@mageia.org> 2.1.4-4.mga7
+ Revision: 1180794
- rebuild for new glew 2.1.0

* Sun Sep 24 2017 Rémi Verschelde <akien@mageia.org> 2.1.4-3.mga7
+ Revision: 1158526
- Add upstream patches to improve packaging:
  * P0: OpenSSL 1.1.0 support, adjust BRs accordingly
  * P1: Upstream desktop and AppStream files
  * P2: Help output improvements
  * P3: Upstream man page
- Add license files to server package
- Remove ExclusiveArch, should be possible to build on ARMv7
- Clarify why clang and openssl-compat10 are used
- Package doc for demos

* Sat Sep 23 2017 Rémi Verschelde <akien@mageia.org> 2.1.4-2.mga7
+ Revision: 1157793
- Add debug_release symbols
- Enable udev support for joypads
- Package COPYRIGHT.txt and AUTHORS.md in docs

* Mon Sep 11 2017 Guillaume Rousse <guillomovitch@mageia.org> 2.1.4-1.mga7
+ Revision: 1152942
- new version 2.1.4
- use llvm, as gcc 7 is not supported upstream

* Tue Apr 11 2017 Rémi Verschelde <akien@mageia.org> 2.1.3-1.mga6
+ Revision: 1096424
- Version 2.1.3

* Sat Jan 21 2017 Rémi Verschelde <akien@mageia.org> 2.1.2-1.mga6
+ Revision: 1082732
- Version 2.1.2-stable

* Wed Nov 16 2016 Rémi Verschelde <akien@mageia.org> 2.1.1-1.mga6
+ Revision: 1067563
- Version 2.1.1
- Unbundle libraries thanks to upstream work to facilitate this:
  freetype, glew, libogg, libpng, libtheora, libvorbis, libwebp, openssl, opus, zlib
- Drop packaged templates for x11 32-bit and 64-bit
  o It was too much work for building templates just for Linux, and 32-bit systems
    would not have had access to the 64-bit templates anyway.
  o Godot 3.0 (next major) will let users download official templates directly,
    which is much better for the many supported platforms the Linux editor can
    export to.

* Tue Aug 09 2016 Rémi Verschelde <akien@mageia.org> 2.1-1.mga6
+ Revision: 1045186
- Enable conditional server build, for testing purposes
- Sync new 2.1 tarball
- Add tarball for demos, provided separately upstream
- Version 2.1
  o BRs xrandr for dpi detection
  o No longer links statically against stdc++-static

* Sun Jul 10 2016 Rémi Verschelde <akien@mageia.org> 2.0.4.1-1.mga6
+ Revision: 1040624
- Version 2.0.4.1, hotfix for a regression
- Version 2.0.4

* Thu Jun 16 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-4.mga6
+ Revision: 1021639
- Fix Comment in desktop file
- Force starting the project manager in the desktop file

* Tue May 17 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-3.mga6
+ Revision: 1016575
- Resync tarball with upstream, makes Patch0 obsolete

* Fri May 13 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-2.mga6
+ Revision: 1014571
- Patch upstream regression in ItemList

* Thu May 12 2016 Rémi Verschelde <akien@mageia.org> 2.0.3-1.mga6
+ Revision: 1014421
- Version 2.0.3
- No longer compress templates with upx

* Tue Mar 08 2016 Rémi Verschelde <akien@mageia.org> 2.0.1-1.mga6
+ Revision: 987284
- Version 2.0.1

* Wed Mar 02 2016 Sysadmin Bot <umeabot@mageia.org> 2.0-3.mga6
+ Revision: 983443
- Rebuild for openssl

* Sat Feb 27 2016 Rémi Verschelde <akien@mageia.org> 2.0-2.mga6
+ Revision: 979993
- Install demos (in a separate package)
- Set build revision to mageia instead of custom_build
- Use Mageia optflags and linkflags for builds (apart from debug template, no optflags)

* Tue Feb 23 2016 Rémi Verschelde <akien@mageia.org> 2.0-1.mga6
+ Revision: 977125
- Version 2.0-stable

* Sun Feb 21 2016 Rémi Verschelde <akien@mageia.org> 2.0-0.dev.1.mga6
+ Revision: 975107
- imported package godot
