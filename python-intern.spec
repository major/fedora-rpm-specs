Name:           python-intern
Version:        1.4.0
Release:        %autorelease
Summary:        Python SDK for interacting with neuroscience data via the Boss API

License:        Apache-2.0
URL:            https://github.com/jhuapl-boss/intern
Source:         %{pypi_source intern}

# Drop dependency on PyPI mock package
# https://github.com/jhuapl-boss/intern/pull/106
Patch:          %{url}/pull/106.patch

BuildArch:      noarch

BuildRequires:  python3-devel
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

%description doc %{common_description}

This package contains assorted documentation and examples for python-intern.
For the HTML API documentation, please see
https://jhuapl-boss.github.io/intern/.


%prep
%autosetup -n intern-%{version} -p1


%generate_buildrequires
# Neither python-cloud-volume nor python-zmesh is currently packaged, so we do
# not generate BuildRequires for -x cloudmesh,meshing.
%pyproject_buildrequires


%build
%pyproject_wheel

# We do not build the HTML documentation because it requires a fork of
# python3dist(pdoc), which is not currently packaged anyway. However, the
# prebuilt documentation is straightforward with no bundled or precompiled
# JavaScript, CSS, or font issues, so we can package it as long as it appears
# in the source distribution.


%install
%pyproject_install
%pyproject_save_files intern


%check
mkdir _empty
cd _empty
# The following tests require network access.
k="${k-}${k+ and }not TestConvenienceProjectCreation"
k="${k-}${k+ and }not (TestFQURIParser and test_boss_uri_with_token)"
k="${k-}${k+ and }not TestRemoteInferral"
# The following tests require zmesh (meshing extra):
k="${k-}${k+ and }not (TestMesh and test_invalid_voxel_unit)"
# We must ignore test modules that unconditionally import cloudvolume until it
# is packaged (and we can add the cloudmesh extra).
%pytest -k "${k-}" \
    --ignore='%{buildroot}%{python3_sitelib}/intern/remote/cv/tests/test_local_remote.py' \
    '%{buildroot}%{python3_sitelib}/intern'


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
