Name: powdertoy
%global rtld_name uk.co.powdertoy.tpt

Summary: Physics sandbox game
URL: https://powdertoy.co.uk

# Powder Toy itself is GPLv3
# src/bson/ is Apache v2.0
# src/lua/ is MIT
License: GPL-3.0-only AND Apache-2.0 AND MIT

Version: 99.1.380
Release: 1%{?dist}

%global repo_owner The-Powder-Toy
%global repo_name The-Powder-Toy
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{repo_name}-v%{version}.tar.gz

# Upstream defaults to naming the executable just "powder",
# but in Fedora we always used "powdertoy". This patch edits some files
# which refer to "powder" and makes them use "powdertoy" instead.
Patch0: 0000-use-powdertoy-instead-of-powder-as-name.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: meson

BuildRequires: bzip2-devel
BuildRequires: fftw-devel
BuildRequires: jsoncpp-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: mesa-libGL-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel

# luajit is not available on these architectures
%ifnarch ppc64le
BuildRequires: lua-devel
BuildRequires: luajit-devel
%global luaver luajit
%else
%global luaver none
%endif

Requires: hicolor-icon-theme


%description
The Powder Toy is a free physics sandbox game, which simulates air pressure
and velocity, heat, gravity and a countless number of interactions between
different substances! The game provides you with various building materials,
liquids, gases and electronic components which can be used to construct complex
machines, guns, bombs, realistic terrains and almost anything else.
You can then mine them and watch cool explosions, add intricate wirings,
play with little stickmen or operate your machine. You can also browse and play
thousands of different saves made by the community or upload your own!


%prep
%autosetup -p1 -n %{repo_name}-%{version}


%build
# -Dapp_exe:
#   Upstream defaults to naming the executable file "powder",
#   but in Fedora we always renamed it to "powdertoy".
# -Dapp_data:
#   Before v96, the game stored user data (config etc.) in $PWD.
#   Fedora shipped a patch which put the user data in "$XDG_DATA_HOME/powdertoy".
#   Starting with v96, the game stores its user data in "$XDG_DATA_HOME/The Powder Toy".
#   We modify this value to preserve backwards-compatibility.
%meson \
	-Dignore_updates=true \
	-Dcan_install=no \
	-Dapp_exe=powdertoy \
	-Dapp_data=powdertoy \
	-Dstatic=none \
	-Dhttp=true \
	-Denforce_https=true \
	-Dlua=%{luaver} \
	-Dx86_sse=auto
%meson_build


%install
# Running "%%meson_install" gives "Nothing to install",
# so we gotta do all of this manually.

install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{_vpath_builddir}/powdertoy %{buildroot}%{_bindir}/%{name}

# -- icons: for the app and for the savefile mimetype
for ICONSET in "icon_exe:apps:powdertoy" "icon_cps:mimetypes:application-vnd.powdertoy.save"; do
	ICON_SRC="$(echo "${ICONSET}" | cut -d: -f1)"
	ICON_CATEGORY="$(echo "${ICONSET}" | cut -d: -f2)"
	ICON_DST="$(echo "${ICONSET}" | cut -d: -f3)"

	# -- png icons
	ln -sr "resources/generated_icons/${ICON_SRC}.png" "resources/generated_icons/${ICON_SRC}_256.png"
	for ICON_SIZE in 16 32 48 256; do
		ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/${ICON_CATEGORY}"
		install -m 755 -d "${ICON_DIR}"
		install -m 644 -p "resources/generated_icons/${ICON_SRC}_${ICON_SIZE}.png" "${ICON_DIR}/${ICON_DST}.png"
	done

	# -- svg icon
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/scalable/${ICON_CATEGORY}"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/${ICON_SRC}.svg" "${ICON_DIR}/${ICON_DST}.svg"
done

# -- .desktop and .appdata.xml file
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p "%{_vpath_builddir}/resources/powder.desktop" "%{buildroot}%{_datadir}/applications/%{rtld_name}.desktop"

install -m 755 -d %{buildroot}%{_metainfodir}/
install -m 644 -p "%{_vpath_builddir}/resources/appdata.xml" "%{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml"

# -- savefile mimetype
install -m 755 -d %{buildroot}%{_datadir}/mime/packages/
install -m 644 resources/save.xml %{buildroot}%{_datadir}/mime/packages/powdertoy-save.xml

# -- man page
install -m 755 -d %{buildroot}%{_mandir}/man6/
install -m 644 resources/powder.man %{buildroot}%{_mandir}/man6/powdertoy.6


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.powdertoy.save.png
%{_datadir}/icons/hicolor/scalable/mimetypes/application-vnd.powdertoy.save.svg
%{_datadir}/mime/packages/%{name}*
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}.metainfo.xml
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Jan 25 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 99.1.380-1
- Update to v99.1.380

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 99.0.377-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 27 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 99.0.377-1
- Update to v99.0.377

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 98.2.365-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 98.2.365-1
- Update to v98.2.365

* Thu Mar 28 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 98.0.363-1
- Update to v98.0.363
- Drop Patch1 (fixes for GCC13 - solved upstream)
- Re-enable luajit support on s390x

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 97.0.352-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 97.0.352-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 97.0.352-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 97.0.352-3
- Add a patch to fix build failures with GCC13

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 97.0.352-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 97.0.352-1
- Update to v97.0.352 (stable release)

* Wed Dec 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 97.0.351b-1
- Update to v97.0.351b (beta release)
- Drop Patch0 (no longer needed, changes now done via config values)
- Install icons for the savefile mimetype as well
- Use a patch for renaming files instead of relying on sed

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 96.2.350-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 96.2.350-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 96.2.350-2
- Disable Lua support on ppc64le and s390x (luajit no longer available)

* Mon Aug 30 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 96.2.350-1
- Update to v96.2.350

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 96.1.349-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 96.1.349-1
- Update to latest upstream release

* Wed Jul 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 96.0.348-1
- Update to latest upstream release
- Drop Patch0 (store "powder.pref" in user's home directory) - fixed upstream
- Drop Patch1 (option to disable the update checker) - accepted upstream
- Add Patch0 - edit "powder.pref" storage path to preserve compatibility

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 95.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 95.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 04 2020 Artur Iwicki <fedora@svgames.pl> - 95.0-2
- Add a patch to disable the built-in update checker

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 95.0-1
- Update to latest upstream release
- Drop Patch1 (no "install me" prompt) - accepted upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 94.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Artur Iwicki <fedora@svgames.pl> - 94.1-4
- Fix the License: tag and include %%{dist} in the Release: tag
- Edit the "store data in HOME" patch

* Fri Sep 06 2019 Artur Iwicki <fedora@svgames.pl> - 94.1-3
- Add Patch0: store the preference file in XDG_CONFIG_DIR
- Add Patch1: disable the "install me" in-game prompt

* Mon Sep 02 2019 Artur Iwicki <fedora@svgames.pl> - 94.1-2
- Set the build flags properly
- Install the savegame MIME info file
- Fix build failures on non-x86 arches (due to auto-enabled SSE code)

* Wed Aug 28 2019 Artur Iwicki <fedora@svgames.pl> - 94.1-1
- Initial packaging
