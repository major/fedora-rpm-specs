Name: lazpaint
%global prettyname LazPaint

Summary: Simple image editor
URL: https://lazpaint.github.io

# LazPaint itself is GPLv3
# BGRABitmap and BGRAControls libraries are modified LGPLv2 (allow static linking in closed-source programs)
# BGRAControls also borrows some Boost-licensed code
License: GPL-3.0-only AND LGPL-3.0-only

Version: 7.2.2
Release: 9%{?dist}

# Versions taken from lazpaint/lazpaint.lpi
%global bitmap_version   11.5.8
%global controls_version 7.7

%global github https://github.com/bgrabitmap
Source0: %{github}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10: %{github}/bgrabitmap/archive/v%{bitmap_version}/bgrabitmap-%{bitmap_version}.tar.gz
Source20: %{github}/bgracontrols/archive/v%{controls_version}/bgracontrols-%{controls_version}.tar.gz

Source100: %{name}.appdata.xml

%global widgetset gtk2

BuildRequires: desktop-file-utils
BuildRequires: file
BuildRequires: fpc
BuildRequires: fpc-srpm-macros
BuildRequires: lazarus-lcl-%{widgetset}
BuildRequires: lazarus-tools
BuildRequires: libappstream-glib

BuildRequires: dos2unix

Requires: hicolor-icon-theme

ExclusiveArch: %{fpc_arches}


%description
%{prettyname} is a simple image editor, like PaintBrush or Paint.Net,
written in Lazarus (Free Pascal), using the BGRABitmap library.

It supports a variety of file formats, including layered bitmaps
and even 3D files.

%{prettyname} also offers a command-line interface for using it from a terminal,
as well as a Python script system that allows the user
to write their own layer effects.


%prep
%setup -q
ln %{SOURCE100} lazpaint/release/%{name}.appdata.xml

# unpack BGRABitmap
tar xzf %{SOURCE10}
mv bgrabitmap-%{bitmap_version}/bgrabitmap  ./bgrabitmap
rm -rf bgrabitmap-%{bitmap_version}/

# unpack BGRAControls
tar xzf %{SOURCE20}
mv bgracontrols-%{controls_version}  ./bgracontrols
rm -rf bgracontrols-%{controls_version}/

# Apply patches.
# We do it only now, and not right after %%setup, since some patches affect bgrabitmap/bgracontrols, too.
# -- no patches currently --

# Some of the .po files have DOS line endings. Fix those.
dos2unix lazpaint/release/bin/i18n/*.po


%global laz_packages  %{expand:
	bgrabitmap/bgrabitmappack.lpk
	bgracontrols/bgracontrols.lpk
	lazpaintcontrols/lazpaintcontrols.lpk
}

%global laz_projects  %{expand:
	%{laz_packages}
	lazpaint/lazpaint.lpi
}

# Patch the project configuration files to enable debuginfo generation
LAZ_PROJECTS=(%{laz_projects})
for PROJECT in ${LAZ_PROJECTS[@]}; do
	sed  \
		-e 's|<GenerateDebugInfo Value="False"[ ]*/>|<GenerateDebugInfo Value="True"/>\n\t\t\t<DebugInfoType Value="dsDwarf2"/>|g'  \
		-e 's|<StripSymbols Value="True"[ ]*/>|<StripSymbols Value="False"/>|g'  \
		-i "${PROJECT}"
done


%build
LAZ_PACKAGES=(%{laz_packages})
LAZ_PROJECTS=(%{laz_projects})

# Inform lazbuild where to look for dependencies
for PACKAGE in ${LAZ_PACKAGES[@]}; do
	lazbuild --add-package-link "${PACKAGE}"
done

# lazbuild has a "--recursive" option for automatically compiling dependencies,
# but using this option triggers random crashes during the build.
# See: - https://bugs.freepascal.org/view.php?id=36318
#      - https://bugs.freepascal.org/view.php?id=36959
#
# As a workaround, we build everything manually in order.
for PROJECT in ${LAZ_PROJECTS[@]}; do
	lazbuild --build-mode=Release --widgetset=%{widgetset} --skip-dependencies "${PROJECT}"
done

# Upstream provides a desktop file, but it's a bit of a mess
# and doesn't pass desktop-file-validate.
# Instead of trying to fix it, let's just write a desktop file ourselves.
cat > lazpaint/release/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{prettyname}
GenericName=Image editor
Comment=%{summary}
Icon=%{name}
Exec=%{_bindir}/%{name}
Terminal=false
Categories=Graphics
EOF


%install
# -- executable
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 lazpaint/release/bin/%{name} %{buildroot}%{_bindir}/

# -- run-time resources

RESDIR="%{buildroot}%{_datadir}/%{name}"
install -m 755 -d "${RESDIR}"
cp -a lazpaint/release/bin/models/ "${RESDIR}/models"

cp -a resources/scripts/ "${RESDIR}/scripts"
rm -rf "${RESDIR}/scripts/test/"

install -m 755 -d "${RESDIR}/i18n"
install -m 644 lazpaint/release/bin/i18n/*.po "${RESDIR}/i18n/"

# -- icons

for ICON_SIZE in 16 20 24 32 40 48 64 96 128 256 512 1024 2048; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/icon/${ICON_SIZE}x${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done

# -- desktop file and appstream data

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p lazpaint/release/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p lazpaint/release/%{name}.appdata.xml %{buildroot}%{_metainfodir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license COPYING.txt
%license bgracontrols/docs/COPYING.LGPL.txt
%license bgracontrols/docs/COPYING.modifiedLGPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 08 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.2.2-7
- Update BGRABitmap to v11.5.8 and BGRAControls to v7.7 (fixes build failure under Lazarus 3.0)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.2.2-3
- BuildRequire only selected Lazarus sub-packages
- Convert License tag to SPDX
- Remove Boost from License tag (used only in some test files)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.2.2-1
- Update to v7.2.2

* Mon Aug 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.2.1-1
- Update to v7.2.1 (with BGRABitmap v11.5.2)

* Sat Aug 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.2-1
- Update to v7.2 (with BGRABitmap v11.5 and BGRAControls v7.5)
- Do not run msgfmt (LazPaint uses the source .po files, not compiled .mo files)
- Drop Patch0 (invalid headers in .po files - no longer relevant)
- Drop Patch1 (fix compilation under Lazarus 2.2.0 - backport from this release)

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.6-6
- Add a patch to fix builds under Lazarus 2.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.6-1
- Update to v7.1.6 (with BGRABitmap v11.3.1 and BGRAControls v7.1)

* Mon Nov 02 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.5-2
- Fix installing translation files (Lazpaint expects them in a non-standard location)

* Mon Oct 19 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.5-1
- Update to v7.1.5 (with BGRABitmap v11.2.5 and BGRAControls v7.0)
- Update upstream URL
- Drop Patch0 (mangled headers in .po files - accepted upstream)
- Drop dependency on iconv (file encoding issues fixed upstream)

* Wed Oct 07 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.4-1
- Update to v7.1.4 (with BGRABitmap v11.2.4 and BGRAControls v6.9)
- Drop Patch0 (BGRABitmap conditional compilation failure - issue fixed upstream)
- Include models in the package
- Include translations in the package

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.3-3
- Add a patch to fix build failures with Lazarus 2.0.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.3-1
- Update to v7.1.3 (with BGRABitmap v11 and BGRAControls v6.7.1)
- Fix the Comment field in the auto-generated .desktop file
- Add an .appdata.xml file
- Preserve timestamps on icons

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.2-1
- Update to v7.1.2 (with BGRABitmap v10.9 and BGRAControls v6.6.1)
- Include lazpaint scripts in the package
- Install hi-res icons from the resources/icon/ directory
- Create a desktop entry file during build instead of using the upstream one

* Sun Apr 19 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.1-1
- Initial packaging
