Name:           python-vhacdx
Version:        0.0.9
Release:        %autorelease
Summary:        Python bindings for V-HACD

# The entire source is MIT, except:
#
# BSD-3-Clause:
#   A bundled copy of the header-only V-HACD library appears as
#   src/vhacdx/VHACD.h. We remove it in %%prep in favor of the system library,
#   but since header-only libraries are effectively static libraries,
#   BSD-3-Clause still appears in the licenses of the binary RPMs.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/trimesh/vhacdx
Source:         %{pypi_source vhacdx}

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install):   -l vhacdx

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


%prep -a
# Remove the bundled copy of the V-HACD library (use the system one instead).
rm -v src/vhacdx/VHACD.h


%install -a
# We have no idea what to suggest upstream should change to keep pybind11 from
# installing C++ source files, but it isn’t useful to package them.
find '%{buildroot}%{python3_sitearch}' -type f -name '*.cpp' -print -delete
sed -r -i '/\.cpp$/d' '%{pyproject_files}'


%check -a
%pytest


%files -n python3-vhacdx -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
