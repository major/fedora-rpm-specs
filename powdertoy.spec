Name: powdertoy
Summary: Physics sandbox game
URL: https://powdertoy.co.uk

# Powder Toy itself is GPLv3
# src/bson/ is Apache v.2.0
# src/json/ and src/lua/ are MIT
License: GPLv3 and MIT and ASL 2.0

Version: 96.2.350
Release: 4%{?dist}

%global repo_owner The-Powder-Toy
%global repo_name The-Powder-Toy
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{repo_name}-v%{version}.tar.gz

# Before v96, the game stored user data (config etc.) in $PWD.
# Fedora shipped a patch which put the user data in "$XDG_DATA_HOME/powdertoy".
# Starting with v96, the game stores its user data in "$XDG_DATA_HOME/The Powder Toy".
# This patch changes the data dir to preserve backwards-compatibility.
Patch0: 0000-backwards-compatible-data-dir.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: meson

BuildRequires: bzip2-devel
BuildRequires: fftw-devel
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel

# luajit is not available on these architectures
# See: https://bodhi.fedoraproject.org/updates/FEDORA-2021-00d0ce7adb
%ifnarch ppc64le s390x
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

# We're gonna use "powdertoy" instead of just "powder"
# for the executable name and icon names
sed -e 's/=powder$/=%{name}/' -i resources/powder.desktop
mv resources/powder.desktop resources/%{name}.desktop

sed -e 's/powder.desktop/%{name}.desktop/' -i resources/powder.appdata.xml
mv resources/powder.appdata.xml resources/%{name}.appdata.xml


%build
%meson \
	-Dstatic=none \
	-Dignore_updates=true \
	-Dinstall_check=false \
	-Dgravfft=true \
	-Dlua=%luaver \
	-Dx86_sse=auto \
	-Dnative=false
%meson_build


%install
# Running "%%meson_install" gives "Nothing to install",
# so we gotta do all of this manually.

install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{_vpath_builddir}/powder %{buildroot}%{_bindir}/%{name}

# -- png icons
for ICONSIZE in 128 256; do
  ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${ICONSIZE}x${ICONSIZE}/apps"
  install -m 755 -d "${ICONDIR}"
  install -m 644 -p "resources/icon/new-unused/icon_${ICONSIZE}.png" "${ICONDIR}/%{name}.png"
done

# -- svg icon
ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/scalable/apps"
install -m 755 -d "${ICONDIR}"
install -m 644 -p "resources/icon/new-unused/icon.svg" "${ICONDIR}/%{name}.svg"

# -- .desktop and .appdata.xml file
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 755 -d %{buildroot}%{_metainfodir}/

desktop-file-install \
 --dir %{buildroot}/%{_datadir}/applications/ \
  resources/%{name}.desktop

install -m 644 -p resources/%{name}.appdata.xml %{buildroot}%{_metainfodir}/

# -- savefile mimetype
install -m 755 -d %{buildroot}%{_datadir}/mime/packages/
install -m 644 resources/powdertoy-save.xml %{buildroot}%{_datadir}/mime/packages/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}*


%changelog
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
