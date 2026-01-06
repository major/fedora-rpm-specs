# Conditional build options (1=enabled by default)
%bcond          openimageio 1  # OIIO plugin support
%bcond          python      1  # Python bindings
%bcond          viewer      0  # Graphical viewer

Name:           materialx
Version:        1.39.4
Release:        %autorelease
Summary:        Vendor-neutral specification for 3D material interchange

License:        %{shrink:
                Apache-2.0 AND
                BSD-3-Clause AND
                BSL-1.0 AND
                CC0-1.0 AND
                ISC AND
                MIT AND
                MIT-Khronos-old AND
                Zlib
                }
# All files under Apache 2.0 License expect the following
# MIT
# source/MaterialXRender/External/Cgltf/cgltf.h
# BSD-3-Clause
# libraries/stdlib/genglsl/lib/
# libraries/stdlib/genosl/include
# source/PyMaterialX/External/PyBind11/tools/FindPythonLibsNew.cmake
# BSL-1.0
# source/MaterialXTest/External/Catch/catch.hpp
# MIT-Khronos-old
# source/MaterialXRenderGlsl/External/Glad/khrplatform.h
# MIT
# documents/DoxygenAwesome/
# source/MaterialXFormat/External/PugiXML
# source/MaterialXRender/External/TinyObjLoader/tiny_obj_loader.h
# source/MaterialXRender/External/StbImage/stb_image.h
# source/MaterialXRender/External/StbImage/stb_image_write.h
# Zlib
# source/MaterialXGraphEditor/External/Glfw/src/mappings.h
# source/MaterialXGraphEditor/External/Glfw/src/mappings.h.in

URL:            https://materialx.org/
Source0:        https://github.com/AcademySoftwareFoundation/MaterialX/releases/download/v%{version}/MaterialX-%{version}.tar.gz

# Use GNUInstallDirs for proper Fedora filesystem layout
Patch0:         materialx-gnuinstalldirs.patch
# Fix configure_file writing to install prefix during configure phase
Patch1:         materialx-fix-python-setup-configure.patch
# Fix installation paths - remove doc install (handled by RPM macros) and
# fix incorrect MDL installation to absolute build path
Patch2:         materialx-fix-install-paths.patch

#========================================
# Build Requirements
#========================================

# Core toolchain
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  ninja-build
BuildRequires:  pkgconfig

# Graphics dependencies
BuildRequires:  OpenImageIO-plugin-osl
BuildRequires:  openshadinglanguage
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(oslcomp)
BuildRequires:  pkgconfig(wayland-client) >= 0.2.7
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xt)
# Optional components
%if %{with openimageio}
BuildRequires:  pkgconfig(OpenImageIO)
%endif

%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(pybind11)
%endif

# Viewer needs access to upstream git submodule
%if %{with viewer}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
%endif

# Only 64-bits architectures supported
ExcludeArch: %{ix86} %{arm}

#========================================
# Package Definitions
#========================================

%description
Physically-based material interchange specification for 3D rendering workflows.

%package data
Summary:        MaterialX examples and resources
License:        Apache-2.0
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description data
Examples and resources for MaterialX.

%package devel
Summary:        Development files for MaterialX
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for building applications using MaterialX.

%if %{with python}
%package -n python3-%{name}
Summary:        Python 3 bindings for MaterialX
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python bindings for MaterialX material standard.
%endif

%if %{with viewer}
%package viewer
Summary:        MaterialX graphical viewer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description viewer
Interactive viewer for MaterialX materials.
%endif

#========================================
# Build Preparation
#========================================

%prep
%autosetup -p1 -n MaterialX-%{version}

# Remove bundled assets
find . -type f \( -name '*.tt[cf]' -o -name '*.ot[cf]' -o -name '*.woff*' \) -delete

# Fix executable
%py3_shebang_fix .

#========================================
# Build Configuration
#========================================

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DMATERIALX_BUILD_SHARED_LIBS=ON \
    -DMATERIALX_BUILD_TESTS=ON \
%if %{with viewer}
    -DMATERIALX_BUILD_VIEWER=ON \
    -DMATERIALX_BUILD_GRAPH_EDITOR=ON \
%endif
%if %{with python}
    -DMATERIALX_BUILD_PYTHON=ON \
    -DMATERIALX_PYTHON_FOLDER_NAME=%{python3_sitelib}/%{name} \
    -DPYTHON_EXECUTABLE=%{__python3} \
%endif

%cmake_build

#========================================
# Installation
#========================================

%install
%cmake_install

%if %{with python}
install -dp %{buildroot}%{_bindir}
rm %{buildroot}%{_prefix}/python/Scripts/README.md
for file in %{buildroot}%{_prefix}/python/Scripts/*.py; do
          name="${file%.py}"
          chmod +x "$file"
          mv "$file" $name
done
chmod +x %{buildroot}%{_prefix}/python/MaterialX/*.py
mv %{buildroot}%{_prefix}/python/Scripts/* %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/python/MaterialX/* %{buildroot}%{python3_sitelib}/%{name}
rm -rvf %{buildroot}%{_prefix}/python
rm -rvf %{buildroot}%{python3_sitelib}/%{name}/%{_prefix}
%endif

# License documentation
install -Dpm644 LICENSE -t %{buildroot}%{_licensedir}/%{name}/
# Boost Software License 1.0
install -Dpm644 source/MaterialXTest/External/Catch/LICENSE.txt \
    licensepack/BSL-license
# MIT-Khronos-old License
install -Dpm644 source/MaterialXRenderGlsl/External/Glad/LICENSE \
    licensepack/MIT-Khronos-old-license
# BSD 3-Clause License
install -Dpm644 source/PyMaterialX/External/PyBind11/LICENSE \
    licensepack/BSD-license
# MIT License
install -Dpm644 source/MaterialXRender/External/Cgltf/LICENSE \
    licensepack/MIT-license


%if %{with viewer}
# Desktop integration
install -Dpm644 documents/Images/MaterialXLogo_200x155.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Generate desktop files
for app in viewer graph-editor; do
  desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    --add-category Graphics \
    --add-category 3DGraphics \
    --set-key Name --set-value "MaterialX ${app%-*}" \
    --set-key Exec --set-value "MaterialX${app//-}" \
    --set-key Icon --set-value "%{name}" \
    --set-key Comment --set-value "MaterialX ${app%-*}" \
    %{name}-${app}.desktop
done
%endif

# Generate and install man pages.
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

#========================================
# Test
#========================================
%check
# Exclude tests that require a display (GLSL) or have OSL rendering issues in mock environment
%ctest -- -E "Render_GLSL_TestSuite|GenReference_OSL_Reference|Render_OSL_TestSuite"

#========================================
# File Manifest
#========================================

%files
%license LICENSE licensepack/*
%doc README.md CHANGELOG.md THIRD-PARTY.md
%dir %{_datadir}/%{name}
%if %{with openimageio}
%{_bindir}/baketextures
%{_bindir}/creatematerial
%{_bindir}/generateshader
%{_bindir}/genmdl
%{_bindir}/mxdoc
%{_bindir}/mxformat
%{_bindir}/mxvalidate
%{_bindir}/translateshader
%{_bindir}/writenodegraphs
%{_mandir}/man1/baketextures.1.gz
%{_mandir}/man1/creatematerial.1.gz
%{_mandir}/man1/generateshader.1.gz
%{_mandir}/man1/genmdl.1.gz
%{_mandir}/man1/mxdoc.1.gz
%{_mandir}/man1/mxformat.1.gz
%{_mandir}/man1/mxvalidate.1.gz
%{_mandir}/man1/translateshader.1.gz
%{_mandir}/man1/writenodegraphs.1.gz
%endif
%{_libdir}/libMaterialX*.so.{1,%{version}}

%files data
%{_datadir}/%{name}/

%files devel
%{_includedir}/MaterialX*
%{_libdir}/libMaterialX*.so
%{_libdir}/cmake/MaterialX/

%if %{with python}
%files -n python3-%{name}
%{python3_sitelib}/%{name}
%endif

%if %{with viewer}
%files viewer
%{_bindir}/MaterialX{View,GraphEditor}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}-{graph-editor,viewer}.desktop
%endif

%changelog
%autochangelog


