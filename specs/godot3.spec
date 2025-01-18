%if 0%{?fedora}
# With _package_note_file enabled, godot.x11.opt.tools fails to link with:
# g++: fatal error: environment variable 'RPM_ARCH' not defined
%undefine _package_note_file
%endif

# Headless is editor binary to run without X11, e.g. for exporting games from CLI
%bcond_without  headless
# Server is template (optimized, no tools) binary to run multiplayer servers
%bcond_without  server

%define status  stable
%define uversion %{version}-%{status}

%define uname   godot
%define urdnsname org.godotengine.Godot
%define rdnsname %{urdnsname}3

Name:           godot3
Version:        3.5.2
Release:        11%{?dist}
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor (version 3)
%if 0%{?mageia}
Group:          Development/Tools
%endif
# Godot itself is MIT-licensed, the rest is from vendored thirdparty libraries
License:        MIT and CC-BY and ASL 2.0 and BSD and zlib and OFL and Bitstream Vera and ISC and MPLv2.0
URL:            https://godotengine.org
Source0:        https://downloads.tuxfamily.org/godotengine/%{version}/%{uname}-%{uversion}.tar.xz
Source1:        https://downloads.tuxfamily.org/godotengine/%{version}/%{uname}-%{uversion}.tar.xz.sha256

Patch0:         godot3-dist-files-rebranding.patch
# https://github.com/transmission/transmission/pull/6907
Patch1:         godot3-miniupnp228.patch

# Upstream does not support those arches (for now)
ExcludeArch:    ppc64 ppc64le s390x

# See bundled section for explanations.
%define system_bullet 0%{?mageia} || 0%{?fedora} >= 34
%define system_embree 0%{?mageia} || (0%{?fedora} && 0%{?fedora} < 38)

BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(alsa)
%if %{system_bullet}
BuildRequires:  pkgconfig(bullet) >= 2.89
%endif
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
%if 0%{?mageia}
BuildRequires:  scons
%else
BuildRequires:  python3-scons
%endif

%if %{system_embree}
%ifarch aarch64 x86_64
BuildRequires:  embree-devel < 4
%endif
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

# Bundled libraries: many of the libraries code in `thirdparty` can be
# unbundled when the libraries are provided by the system. Keep in mind
# though that the `thirdparty` folder also contains code which is typically
# not packaged in distros, and is probably best left bundled.

%if ! %{system_bullet}
# Needs at least bullet 2.89 (with a patch, see linked PR) or later (unpatched).
# https://github.com/bulletphysics/bullet3/pull/2748
Provides:       bundled(bullet) = 3.24
%endif
# Godot requires Embree 3, and recent Fedora upgraded to Embree 4 which breaks the API.
Provides:       bundled(embree) = 3.13.0
# Has some modifications for IPv6 support, upstream enet is unresponsive.
# Should not be unbundled.
# Cf: https://github.com/godotengine/godot/issues/6992
Provides:       bundled(enet) = 1.3.17
# Upstream commit from 2016 (32d5ac49414a8914ec1e1f285f3f927c6e8ec29d),
# newer than 1.0.0.27 which is the last tag.
# Could be unbundled if packaged.
Provides:       bundled(libwebm)
# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.2.12
# Upstream commit ccdb1995134d340a93fb20e3a3d323ccb3838dd0, no releases.
# Could be unbundled if packaged.
Provides:       bundled(nanosvg)
%ifarch x86_64
# Could be unbundled but requires some upstream work, and it's not clear if
# upstream code would be compatible with more recent OIDN releases.
Provides:       bundled(oidn) = 1.1.0
%endif
# Could be unbundled if packaged.
Provides:       bundled(squish) = 1.15
# Could be unbundled if packaged.
Provides:       bundled(tinyexr) = 1.0.1

%description
Godot 3 is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

%files
%doc CHANGELOG.md DONORS.md README.md
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt LOGO_LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%{_datadir}/mime/application/%{rdnsname}.xml
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%if %{with headless}
%package        headless
Summary:        Godot 3 headless editor binary for CLI usage
%if 0%{?mageia}
Group:          Development/Tools
%endif

%description    headless
This package contains the headless binary for the Godot 3 game engine,
particularly suited for CLI usage, e.g. to export projects from a server
or build system.

To run game servers, see the godot-server package which contains an
optimized template build.

%files          headless
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-headless
%endif

#----------------------------------------------------------------------

%if %{with server}
%package        server
Summary:        Godot 3 headless runtime binary for hosting game servers
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    server
This package contains the headless binary for the Godot 3 game engine's
runtime, useful to host standalone game servers.

To use editor tools from the command line, see the godot-headless
package.

%files          server
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-server
%endif

#----------------------------------------------------------------------

%package        runner
Summary:        Shared binary to play games developed with the Godot 3 game engine
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot 3 game engine
simply by pointing to the location of the game's data package.

%files          runner
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-runner

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{uname}-%{uversion}

%build
# Needs to be in %%build so that system_libs stays in scope
# We don't unbundle enet and minizip as they have necessary custom changes
to_unbundle="freetype libogg libpng libtheora libvorbis libvpx libwebp mbedtls miniupnpc opus pcre2 wslay zlib zstd"

%if %{system_bullet}
to_unbundle+=" bullet"
%endif
%if %{system_embree}
to_unbundle+=" embree"
%endif

system_libs=""
for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done

# The denoise module depends on OIDN which is x86_64 only (in the vendored version).
# Godot's own logic to disable it on other arches is a bit brittle when it comes to cross-compiling currently.
%ifnarch x86_64
%define disable_modules module_denoise_enabled=no
%endif

%define _scons scons %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" $system_libs use_lto=yes use_static_cpp=no progress=no %{?disable_modules}

%if 0%{?fedora}
export BUILD_NAME="fedora"
%endif
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif

# Build graphical editor (tools)
%_scons p=x11 tools=yes target=release_debug

# Build game runner (without tools)
%_scons p=x11 tools=no target=release

%if %{with headless}
# Build headless version of the editor
%_scons p=server tools=yes target=release_debug
%endif

%if %{with server}
# Build headless version of the runtime for servers
%_scons p=server tools=no target=release
%endif

%install
%ifarch riscv64
suffix=rv64
%else
suffix=%{__isa_bits}
%endif
install -d %{buildroot}%{_bindir}
install -m755 bin/%{uname}.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}
install -m755 bin/%{uname}.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-runner
%if %{with headless}
install -m755 bin/%{uname}_server.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}-headless
%endif
%if %{with server}
install -m755 bin/%{uname}_server.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-server
%endif

install -D -m644 icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m644 misc/dist/linux/%{urdnsname}.desktop \
    %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
install -D -m644 misc/dist/linux/%{urdnsname}.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
install -D -m644 misc/dist/linux/%{urdnsname}.xml \
    %{buildroot}%{_datadir}/mime/application/%{rdnsname}.xml
install -D -m644 misc/dist/linux/%{uname}.6 \
    %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m644 misc/dist/shell/%{uname}.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m644 misc/dist/shell/%{uname}.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m644 misc/dist/shell/_%{uname}.zsh-completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
# Validate desktop and appdata files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 3.5.2-10
- Rebuild for updated miniupnpc.

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 3.5.2-9
- Rebuilt for mbedTLS 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 3.5.2-7
- Add riscv64 support

* Wed Feb 07 2024 Pete Walter <pwalter@fedoraproject.org> - 3.5.2-6
- Rebuild for libvpx 1.14.x

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 05 2023 Rémi Verschelde <akien@fedoraproject.org> - 3.5.2-2
- Fix desktop and other dist files for godot3 binary name (rhbz#2184360)

* Fri Mar 10 2023 Rémi Verschelde <akien@fedoraproject.org> - 3.5.2-1
- Rename package to godot3 in preparation for the incompatible update to Godot 4.0
- Version 3.5.2-stable
- Unbundle newly packaged libwslay

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
