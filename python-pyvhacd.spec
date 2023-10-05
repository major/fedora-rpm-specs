Name:           python-pyvhacd
Version:        0.0.2
Release:        %autorelease
Summary:        Python bindings for V-HACD

# The entire source is MIT except for the bundled src/pyVHACD/VHACD.h, which is
# BSD-3-Clause. We remove this file in %%prep and use the system copy instead,
# but since it is a header-only library, it is treated as a static library and
# its license still contributes to the license of the binary RPMs.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/thomwolf/pyVHACD
# The PyPI sdist lacks tests, so we use the GitHub archive.
# The current tag has a typo or is strangely written (missing one “.”).
%global srcversion 0.02
Source:         %{url}/archive/v%{srcversion}/pyVHACD-%{srcversion}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

BuildRequires:  v-hacd-devel
# For tracking of header-only library dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  v-hacd-static

%global common_description %{expand:
A very simple and raw Python binding for V-HACD
(https://github.com/kmammou/v-hacd).

Generate a set of convex hulls for a triangulated mesh.}

%description %{common_description}


%package -n python3-pyvhacd
Summary:        %{summary}

%description -n python3-pyvhacd %{common_description}


%prep
%autosetup -n pyVHACD-%{srcversion}

# Remove the bundled copy of the V-HACD library (use the system one instead)
rm -v src/pyVHACD/VHACD.h


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyVHACD


%check
# The “test” extra brings in pytest, but upstream never used it (and the tests
# are not written in a style compatible with pytest as a runner).
PYTHONPATH='%{buildroot}%{python3_sitearch}' PYTHONDONTWRITEBYTECODE=1 \
    %{python3} ./tests/test.py


%files -n python3-pyvhacd -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
