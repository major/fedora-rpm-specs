Name:           python-configargparse
Version:        1.7.3
Release:        %autorelease
Summary:        Replacement for argparse that allows options to be set via config files

# SPDX
License:        MIT
URL:            https://github.com/bw2/ConfigArgParse
Source:         %{url}/archive/v%{version}/ConfigArgParse-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l configargparse
BuildOption(generate_buildrequires): -x yaml

BuildArch:      noarch

# See tests_require in setup.py; it also contains unwanted linters, coverage
# analysis tools, etc.:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-subtests}

%global common_description %{expand:
A drop-in replacement for argparse that allows options to also be set via
config files and/or environment variables.

Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard-coded
defaults, and in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.}

%description %{common_description}


%package -n python3-configargparse
Summary:        %{summary}

%description -n python3-configargparse %{common_description}


%pyproject_extras_subpkg -n python3-configargparse yaml


%check -a
%pytest -v -rs


%files -n python3-configargparse -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
