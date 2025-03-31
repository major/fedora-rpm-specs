%global forgeurl  https://gitlab.freedesktop.org/monado/demos/openxr-simple-playground
%global commit    b7f23921db6c8829275c9f194713ae7cfc302ae8
%global date      20250323
%forgemeta

Name:           openxr-simple-playground
Version:        0
Release:        %autorelease
Summary:        OpenXR C Playground

License:        BSL-1.0 AND MIT AND Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}


ExcludeArch:    %{ix86}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)

# external/openxr_headers/*.h Apache-2.0
Provides:       bundled(openxr)
# external/math_3d/math_3d.h MIT
Provides:       bundled(math3d)


%description
This example exercises many areas of the OpenXR API. Some 
parts of the API are abstracted, though the abstractions 
are intentionally kept simple for simple editing.

Note: Currently this application only supports the 
XrGraphicsBindingOpenGLXlibKHR (glx) graphics binding.


%prep
%forgeautosetup -p1
mv external/math_3d/LICENSE LICENSE.MIT
mv external/openxr_headers/LICENSE LICENSE.Apache-2.0


%build
# W: no-manual-page-for-binary openxr-playground
%cmake 
%cmake_build


%install
%cmake_install


%files
%doc Readme.md
%license LICENSE LICENSE.MIT LICENSE.Apache-2.0
%{_bindir}/openxr-playground


%changelog
%autochangelog
