%bcond opencl 1

%global blend_version 2.11.1
%global blender_min_version 4.5.0
# Use the manifest ID as the directory name in the system extension repository.
%global blendluxcore_dir %{blender_extensions}/blendluxcore

Name:           luxcorerender
Version:        2.11.2
Release:        %autorelease
Summary:        Physically based unbiased rendering system

License:        Apache-2.0
URL:            https://luxcorerender.org/
Source0:        https://github.com/LuxCoreRender/LuxCore/archive/wheels-v%{version}/LuxCore-%{version}.tar.gz
# BlendLuxCore has an independent release cadence.
Source1:        https://github.com/LuxCoreRender/BlendLuxCore/archive/v%{blend_version}/BlendLuxCore-%{blend_version}.tar.gz
Source3:        org.%{name}.blendluxcore.metainfo.xml
Source4:        luxcoreconsole.1

Patch0:         luxcore-system-dependencies.patch
Patch1:         luxcore-robin-map.patch
Patch2:         luxcore-system-build.patch
Patch3:         luxcore-python-install.patch
Patch4:         blendluxcore-system-python.patch
# Replace obsolete postal addresses with the GNU license URL; preserve terms.
Patch5:         blendluxcore-license-url.patch

ExclusiveArch:  x86_64

BuildRequires:  cmake >= 3.29
BuildRequires:  gcc-c++
BuildRequires:  appstream
BuildRequires:  blender >= %{blender_min_version}
BuildRequires:  blender-rpm-macros
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  python3-devel
# Generate upstream Python metadata without a second CMake build.
BuildRequires:  python3dist(scikit-build-core) >= 0.10
BuildRequires:  python3dist(tomli-w)
BuildRequires:  python3dist(packaging)

BuildRequires:  boost-devel
BuildRequires:  boost-iostreams
BuildRequires:  boost-serialization
BuildRequires:  cmake(Blosc2)
BuildRequires:  cmake(Eigen3)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenImageIO) > 3.0
BuildRequires:  cmake(OpenImageDenoise)
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(OpenSubdiv)
BuildRequires:  cmake(pybind11)
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(TBB)
BuildRequires:  cmake(tsl-robin-map)
BuildRequires:  cmake(zlib-ng)
BuildRequires:  embree-devel
BuildRequires:  openvdb-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openjph)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

# Optional OpenCL
%if %{with opencl}
BuildRequires:  pkgconfig(OpenCL)
%global opencl_flags -DLUXRAYS_ENABLE_OPENCL=ON -DLUXRAYS_DISABLE_OPENCL=OFF
%else
%global opencl_flags -DLUXRAYS_ENABLE_OPENCL=OFF -DLUXRAYS_DISABLE_OPENCL=ON
%endif

# CUDA disabled (not in Fedora)
%global cuda_flags -DLUXRAYS_ENABLE_CUDA=OFF -DLUXRAYS_ENABLE_OPTIX=OFF -DLUXRAYS_DISABLE_CUDA=ON

Obsoletes:      LuxRender < 2.0
Provides:       LuxRender = %{version}-%{release}
Obsoletes:      LuxRender-core < 2.0
Provides:       LuxRender-core = %{version}-%{release}
Obsoletes:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}

%description
LuxCoreRender implements state-of-the-art light transport algorithms for
photorealistic rendering, with CPU rendering, optional OpenCL GPU
acceleration, and advanced material modeling.

%package -n blender-%{name}
Summary:        Blender integration for LuxCoreRender
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       blender >= %{blender_min_version}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-blender < %{blend_version}
Provides:       %{name}-blender = %{blend_version}-%{release}

%description -n blender-%{name}
Blender extension for exporting scenes and materials to LuxCore Renderer.
Supports Cycles material conversion and interactive rendering.

The extension is installed in Blender's system extension repository and is
available to all users. Enable BlendLuxCore in the Blender preferences.
It uses the system-provided LuxCore Python bindings.

# libluxcore.so.2 is a downstream SONAME: audit ABI compatibility on upgrades.
%package devel
Summary:        Development headers and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing LuxCore-based applications.

%prep
# Require the corrected blender-rpm-macros path; older macros use addons_core.
if [ "%{blender_extensions}" != "%{blender_datadir}/extensions/system" ]; then
    echo "blender-rpm-macros must define blender_extensions as %{blender_datadir}/extensions/system" >&2
    exit 1
fi
%autosetup -p1 -a1 -n LuxCore-wheels-v%{version}

# Match the Python distribution metadata to Fedora's CMake installation.
# CUDA is disabled and the wheel-only Python tools are not installed here.
# Use the RPM version rather than upstream's SKVERSION file.
%{python3} - <<'PYTHON'
from pathlib import Path
import tomllib
import tomli_w
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

path = Path("pyproject.toml")
data = tomllib.loads(path.read_text())
project = data["project"]
assert project["name"] == "pyluxcore"
project["version"] = "%{version}"
project["dynamic"] = [field for field in project.get("dynamic", [])
                      if field != "version"]
data["tool"]["scikit-build"].get("metadata", {}).pop("version", None)
project["dependencies"] = [
    requirement for requirement in project.get("dependencies", [])
    if canonicalize_name(Requirement(requirement).name) != "nvidia-cuda-nvrtc-cu12"
]
project.pop("scripts", None)
project.pop("gui-scripts", None)
path.write_text(tomli_w.dumps(data))
PYTHON

%build
# Build the main LuxCore library
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DPYTHON_SITEARCH=%{python3_sitearch} \
    -DLUXCORE_VERSION=%{version} \
    -DLUXCOREDEPS_VERSION=2.2.3 \
    %{opencl_flags} \
    %{cuda_flags}
%cmake_build

# The PEP 517 metadata hook uses the upstream backend, without compiling again.
%{python3} - <<'PYTHON'
from pathlib import Path
from scikit_build_core.build import prepare_metadata_for_build_wheel

metadata_root = Path(".pyluxcore-metadata")
metadata_root.mkdir(exist_ok=True)
dist_info = prepare_metadata_for_build_wheel(
    str(metadata_root),
    config_settings={"wheel.cmake": "false", "wheel.platlib": "true"},
)
assert dist_info == "pyluxcore-%{version}.dist-info", dist_info
PYTHON

# Build the BlendLuxCore Blender extension
pushd BlendLuxCore-%{blend_version}
%{_bindir}/blender --command extension build --source-dir . \
    --output-filepath ./BlendLuxCore.zip
popd

%install
# Install the main LuxCore libraries
%cmake_install

# Install backend-generated metadata beside the CMake-installed extension.
cp -a .pyluxcore-metadata/pyluxcore-%{version}.dist-info \
    %{buildroot}%{python3_sitearch}/

# Upstream does not install its public C++ headers yet.
install -d %{buildroot}%{_includedir}
cp -a include/{luxcore,luxrays,slg} %{buildroot}%{_includedir}/
install -Dpm 0644 %{__cmake_builddir}/generated/include/luxcore/cfg.h \
    %{buildroot}%{_includedir}/luxcore/cfg.h
install -Dpm 0644 %{__cmake_builddir}/generated/include/luxrays/cfg.h \
    %{buildroot}%{_includedir}/luxrays/cfg.h

# Unpack the validated extension into the system repository. Blender discovers
# installed directories containing a manifest, rather than ZIP archives.
install -d %{buildroot}%{blendluxcore_dir}
%{python3} -m zipfile -e BlendLuxCore-%{blend_version}/BlendLuxCore.zip \
    %{buildroot}%{blendluxcore_dir}
# Developer helpers are not runtime tools. Documentation and license copies
# are installed separately by the doc and license directives below.
rm -rf %{buildroot}%{blendluxcore_dir}/debug-helpers
rm -f %{buildroot}%{blendluxcore_dir}/wf-debug.sh \
    %{buildroot}%{blendluxcore_dir}/AUTHORS.txt \
    %{buildroot}%{blendluxcore_dir}/readme.md \
    %{buildroot}%{blendluxcore_dir}/LICENSE

# The repository is managed by RPM and remains read-only for ordinary users.
find %{buildroot}%{blendluxcore_dir} -type d -exec chmod 0755 {} +
find %{buildroot}%{blendluxcore_dir} -type f -exec chmod 0644 {} +

install -Dpm 0644 %{SOURCE4} %{buildroot}%{_mandir}/man1/luxcoreconsole.1

# Install the AppStream metadata
install -Dpm 644 %{SOURCE3} %{buildroot}%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml

%check
# Test the staged RPM files, so an already-installed binding cannot hide errors.
LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH} \
%{python3} - <<'PYTHON'
from pathlib import Path
import sys
from importlib.metadata import distribution, version
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

sitearch = Path("%{buildroot}%{python3_sitearch}").resolve()
sys.path.insert(0, str(sitearch))
import pyluxcore

assert Path(pyluxcore.__file__).resolve().parent == sitearch
assert version("pyluxcore") == "%{version}"
dist = distribution("pyluxcore")
assert Path(dist.locate_file("")).resolve() == sitearch
assert not dist.entry_points
assert all(canonicalize_name(Requirement(req).name) != "nvidia-cuda-nvrtc-cu12"
           for req in (dist.requires or []))
print("PyLuxCore:", pyluxcore.__file__)
print("PyLuxCore distribution version:", dist.version)
PYTHON

# Exercise the bindings in Blender's embedded Python as well as system Python.
cat > blender-pyluxcore-smoke.py <<'PYTHON'
from pathlib import Path
import sys
from importlib.metadata import version
sitearch = Path("%{buildroot}%{python3_sitearch}").resolve()
sys.path.insert(0, str(sitearch))
import pyluxcore
assert Path(pyluxcore.__file__).resolve().parent == sitearch
assert version("pyluxcore") == "%{version}"
print("Blender staged PyLuxCore import: OK")
PYTHON
LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH} \
%{_bindir}/blender --background --factory-startup --python-exit-code 1 \
    --python blender-pyluxcore-smoke.py

# Check the installed extension layout and manifest, not just the build ZIP.
%{python3} - <<'PYTHON'
from pathlib import Path
import tomllib

extension_dir = Path("%{buildroot}%{blendluxcore_dir}")
manifest = tomllib.loads((extension_dir / "blender_manifest.toml").read_text())
assert manifest["id"] == extension_dir.name == "blendluxcore"
assert manifest["version"] == "%{blend_version}"
assert manifest["type"] == "add-on"
assert manifest["blender_version_min"] == "%{blender_min_version}"
assert not manifest.get("wheels")
assert (extension_dir / "__init__.py").is_file()
assert "luxloader.ensure_pyluxcore()" not in (extension_dir / "__init__.py").read_text()
PYTHON
%{_bindir}/blender --command extension validate %{buildroot}%{blendluxcore_dir}

appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml

%files
%license COPYING.txt
%doc README.md AUTHORS.txt
%{_bindir}/luxcore*
%{_mandir}/man1/luxcoreconsole.1*
%{_libdir}/liblux*.so.*
%{python3_sitearch}/pyluxcore*.so
%{python3_sitearch}/pyluxcore-%{version}.dist-info/

%files -n blender-%{name}
%license BlendLuxCore-%{blend_version}/LICENSE
%doc BlendLuxCore-%{blend_version}/{AUTHORS.txt,readme.md}
%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml
%{blendluxcore_dir}/

%files devel
%doc README.md
%{_includedir}/{luxcore,luxrays,slg}
%{_libdir}/libluxcore.so

%changelog
%autochangelog
