# Build options - default on
%bcond_without bundled_openxr

# Disable LTO, it breaks how this all works
%global _lto_cflags %nil

%global forgeurl0  https://gitlab.com/znixian/OpenOVR
%global commit0    effe0a8783937c5a3cfe7a72cf6f81152150b6cb
%global date       20241226

# Bundled openxr 1.0.x for the bubblewraped environments (i.e. steam)
# https://gitlab.com/znixian/OpenOVR/-/issues/416
# https://gitlab.com/znixian/OpenOVR/-/issues/437
%global forgeurl1  https://github.com/KhronosGroup/OpenXR-SDK
%global commit1    91a8a8d9d70f4b469bca0726122c3b5a6096010e

%forgemeta

Name:           opencomposite
Version:        0.0.1
Release:        %autorelease
Summary:        Reimplementation of OpenVR, translating calls to OpenXR

License:        GPL-3.0-or-later AND MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND CC-BY-4.0 AND BSL-1.0
# BSD-3-Clause
# OpenOVR/Misc/ini.{c,h}
# CC-BY-4.0
# assets/*
# Apache-2.0
# RuntimeExtensions/openxr_extension_helpers.h
# BSD-2-Clause
# OpenOVR/Misc/debugbreak.h
# BSL-1.0
# RuntimeExtensions/XR_MNDX_xdev_space.h
# MIT
# BundledLibs/d3dx12.h
# zlib
# OpenOVR/Misc/lodepng.{cpp,h}

URL:            %{forgeurl0}
Source0:        %{forgesource0}
# Apache-2.0
Source1:        %{forgeurl1}/archive/%{commit1}/openxr-sdk-%{commit1}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(jsoncpp)
%if %{without bundled_openxr}
BuildRequires:  pkgconfig(openxr)
%endif
BuildRequires:  pkgconfig(vulkan)
       

%if %{with bundled_openxr}
Provides:       bundled(openxr) = 1.0.12
%endif

%description
OpenComposite OpenXR is an implementation of SteamVR's API - OpenVR, 
forwarding calls directly to the OpenXR runtime.


%prep
%forgeautosetup -p1

%if %{with bundled_openxr}
mkdir -p libs/openxr-sdk
tar -xvf %{SOURCE1} --strip-components 1 -C libs/openxr-sdk
%endif


%build
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=on \
%if %{with bundled_openxr}
    -DUSE_SYSTEM_OPENXR=off \
%else
    -DUSE_SYSTEM_OPENXR=on \
%endif
    -DUSE_SYSTEM_GLM=on \
    -DGLM_ENABLE_EXPERIMENTAL=on \

%cmake_build


%install
%ifarch %{ix86}
mkdir -p %{buildroot}%{_libdir}/%{name}/runtime/bin/
install -Dpm0755 -t %{buildroot}%{_libdir}/%{name}/runtime/bin/ redhat-linux-build/bin/vrclient.so
%else
mkdir -p %{buildroot}%{_libdir}/%{name}/runtime/bin/linux64
install -Dpm0755 -t %{buildroot}%{_libdir}/%{name}/runtime/bin/linux64 redhat-linux-build/bin/linux64/vrclient.so
%endif


%files
%license LICENSE.txt LICENCE_BUILD_UTIL.txt LICENCE_DEBUG_BREAK.txt LICENSE_INIH.txt LICENSE_OPENVR.txt
%if %{with bundled_openxr}
%license libs/openxr-sdk/LICENSE
%endif
%doc doc/*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/runtime/
%dir %{_libdir}/%{name}/runtime/bin/
%ifarch %{ix86}
%{_libdir}/%{name}/runtime/bin/vrclient.so
%else
%dir %{_libdir}/%{name}/runtime/bin/linux64
%{_libdir}/%{name}/runtime/bin/linux64/vrclient.so
%endif


%changelog
%autochangelog
