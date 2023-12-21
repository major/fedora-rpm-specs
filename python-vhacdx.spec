Name:           python-vhacdx
Version:        0.0.4
Release:        %autorelease
Summary:        Python bindings for V-HACD

# The entire source is MIT.
#
# There is supposed to be a bundled copy of the header-only V-HACD library
# (https://src.fedoraproject.org/rpms/v-hacd,
# https://github.com/kmammou/v-hacd) at src/vhacdx/VHACD.h, licensed
# BSD-3-CLause. This file would be present in any archive exported from GitHub,
# but it is currently missing from the PyPI sdist. If the bundled library
# appears, we will remove it in %%prep and use the system copy instead.
#
# Regardless of the above, since v-hacd is a header-only library, it is
# effectively a static library and its BSD-3-Clause license still contributes
# to the license of the binary RPMs even when the system copy is used.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/trimesh/vhacdx
Source:         %{pypi_source vhacdx}

# Fix the “test” extra
# https://github.com/trimesh/vhacdx/pull/1
Patch:          %{url}/pull/1.patch

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

BuildRequires:  v-hacd-devel
# For tracking of header-only library dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  v-hacd-static

%global common_description %{expand:
A very simple and raw Python binding for V-HACD that is forked from
https://github.com/thomwolf/pyVHACD which generates an approximate convex
decomposition of a triangle mesh.}

%description %{common_description}


%package -n python3-vhacdx
Summary:        %{summary}

%description -n python3-vhacdx %{common_description}


%prep
%autosetup -n vhacdx-%{version} -p1

# Remove the bundled copy of the V-HACD library (use the system one instead).
# This file is currently missing from the PyPI sdists.
rm -vf src/vhacdx/VHACD.h

# Add the V-HACD license to the LICENSE file
# https://github.com/trimesh/vhacdx/pull/3
#
# Until upstream considers this PR, we copy in the V-HACD license file
# separately.
cp -p /usr/share/licenses/v-hacd-devel/LICENSE ./LICENSE-VHACD


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l vhacdx

# We have no idea what to suggest upstream should change to keep pybind11 from
# installing C++ source files, but it isn’t useful to package them.
find '%{buildroot}%{python3_sitearch}' -type f -name '*.cpp' -print -delete
sed -r -i '/\.cpp$/d' '%{pyproject_files}'


%check
%pytest


%files -n python3-vhacdx -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
