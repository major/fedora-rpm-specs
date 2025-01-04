Name:           python-intern
Version:        1.4.0
Release:        %autorelease
Summary:        Python SDK for interacting with neuroscience data via the Boss API

License:        Apache-2.0
URL:            https://github.com/jhuapl-boss/intern
Source:         %{pypi_source intern}

BuildSystem:            pyproject
BuildOption(install):   intern
# Neither python-cloud-volume nor python-zmesh is currently packaged, so we do
# not generate BuildRequires for -x cloudmesh,meshing.
# BuildOption(generate_buildrequires): -x cloudmesh,meshing
# Skip import-checking modules that require cloudmesh or meshing extras.
BuildOption(check):     -e 'intern.*.cv' -e 'intern.*.cv.*'

# Drop dependency on PyPI mock package
# https://github.com/jhuapl-boss/intern/pull/106
Patch:          %{url}/pull/106.patch

BuildArch:      noarch

# Tests can be executed with unittest, but pytest is more convenient,
# especially when we need to skip some tests.
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
intern (Integrated Toolkit for Extensible and Reproducible Neuroscience) is a
Python 3 module that enables big-data neuroscience. Currently, it provides an
interface to common big-data neuroimaging databases such as BossDB,
CloudVolume, DVID, and other standard formats.}

%description %{common_description}


%package -n python3-intern
Summary:        %{summary}

%description -n python3-intern %{common_description}


# Neither python-cloud-volume nor python-zmesh is currently packaged.
# %%pyproject_extras_subpkg -n python3-intern cloudvolume meshing


%package doc
Summary:        Documentation and examples for python-intern

# We do not build the HTML documentation because it requires a fork of
# python3dist(pdoc), which is not currently packaged anyway. However, the
# prebuilt documentation is straightforward with no bundled or precompiled
# JavaScript, CSS, or font issues, so we can package it as long as it appears
# in the source distribution.

%description doc %{common_description}

This package contains assorted documentation and examples for python-intern.
For the HTML API documentation, please see
https://jhuapl-boss.github.io/intern/.


%prep
%autosetup -n intern-%{version} -p1


%check -a
# The following tests require network access.
k="${k-}${k+ and }not TestConvenienceProjectCreation"
k="${k-}${k+ and }not (TestFQURIParser and test_boss_uri_with_token)"
k="${k-}${k+ and }not TestRemoteInferral"
# The following tests require zmesh (meshing extra):
k="${k-}${k+ and }not (TestMesh and test_invalid_voxel_unit)"

# We must ignore test modules that unconditionally import cloudvolume until it
# is packaged (and we can add the cloudmesh extra).
installed_package='%{buildroot}%{python3_sitelib}/intern'
ignore="${ignore-} --ignore=${installed_package}/remote/cv/tests/test_local_remote.py"

# For --import-mode=append, which ensures we import the installed copy from the
# buildroot, see: https://docs.pytest.org/en/stable/explanation/pythonpath.html
%pytest --import-mode=append -k "${k-}" ${ignore-} "${installed_package}"


%files -n python3-intern -f %{pyproject_files}
%license license


%files doc
%license license
%doc CHANGELOG.md
%doc README.md
%doc docs/
%doc examples/


%changelog
%autochangelog
