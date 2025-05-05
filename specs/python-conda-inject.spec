Name:           python-conda-inject
Version:        1.3.2
Release:        %autorelease
Summary:        Inject a conda environment into the current python environment 

# SPDX
License:        MIT
URL:            https://github.com/koesterlab/conda-inject
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md; this
# also gives us the tests, but we are unable to run them.
Source:         %{url}/archive/v%{version}/conda-inject-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L conda_inject

BuildArch:      noarch

%global common_description %{expand:
Helper functions for injecting a conda environment into the current python
environment. This happens by modifying sys.path, without actually changing the
current python environment.}

%description %{common_description}


%package -n python3-conda-inject
Summary:        %{summary}

%description -n python3-conda-inject %{common_description}


# Currently, all tests require network access. Furthermore, of the three
# supported package managers (mamba, conda, and micromamba), the one used for
# the tests is mamba, and this is the only one that is not currently packaged.
# We therefore cannot even run the tests in a local mock build with
# --enable-network unless we patch them to use a different package manager.


%files -n python3-conda-inject -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
