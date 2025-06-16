%global forgeurl     https://github.com/maluoi/openxr-explorer
%global commit       721a4a94ddac30c4f8bcb1d4d4c1cb9655d45712
%global date         20250525
%global cpm_version  0.32.2
%forgemeta

Name:           openxr-explorer
Version:        1.7
Release:        %autorelease
Summary:        Debug tool for OpenXR developers

License:        MIT AND BSL-1.0
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/cpm-cmake/CPM.cmake/releases/download/v%{cpm_version}/CPM.cmake
# https://github.com/maluoi/openxr-explorer/issues/26
Source2:        openxr-explorer.desktop
# https://github.com/maluoi/openxr-explorer/pull/25
Patch0:         openxr-explorer-e59a26e38a5caab768a0bd4ab021ec1c1e461d12-enable-pie.patch


BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)


# src/openxrexplorer/imgui MIT
Provides:       bundled(imgui)
# CPM.cmake MIT
Provides:       bundled(cpm-cmake) = %{cpm_version}
      

%description
OpenXR Explorer is a handy debug tool for OpenXR developers. It allows 
for easy switching between OpenXR runtimes, shows lists of the runtime's 
supported extensions, and allows for inspection of common properties and 
enumerations, with direct links to relevant parts of the OpenXR specification!


%prep
%forgeautosetup -p1
install -m 0755 -vd cache/cpm
install -m 0644 %{SOURCE1} cache/cpm/CPM_%{cpm_version}.cmake

# Disable using CPM for NLOHMANN_JSON, use system lib instead
sed -i 's@.*cmake/json.cmake@#&@g' CMakeLists.txt

%build
#  W: no-manual-page-for-binary openxr-explorer
#  W: no-manual-page-for-binary xrsetruntime
%cmake \
  -DCPM_SOURCE_CACHE=cache \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_build
# Convert icon for desktop file png
convert src/openxrexplorer/oxr-explorer-icon.ico openxr-explorer.png
mv openxr-explorer-4.png openxr-explorer.png


%install
%cmake_install

# Desktop file and icon install
install -m 0755 -vd %{buildroot}%{_datarootdir}/applications
install -m 0755 -vd %{buildroot}%{_datarootdir}/icons/hicolor/64x64/apps
desktop-file-install --dir=%{buildroot}%{_datarootdir}/applications %{SOURCE2}
install -m 0644 -t %{buildroot}%{_datarootdir}/icons/hicolor/64x64/apps openxr-explorer.png


%files
%license LICENSE
%doc README.md
%{_bindir}/openxr-explorer
%{_bindir}/xrsetruntime
%{_datarootdir}/applications/openxr-explorer.desktop
%{_datarootdir}/icons/hicolor/64x64/apps/openxr-explorer.png


%changelog
%autochangelog
