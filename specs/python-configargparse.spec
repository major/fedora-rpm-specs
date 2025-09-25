Name:           python-configargparse
Version:        1.7.1
Release:        %autorelease
Summary:        Replacement for argparse that allows options to be set via config files

# SPDX
License:        MIT
URL:            https://github.com/bw2/ConfigArgParse
Source:         %{url}/archive/%{version}/ConfigArgParse-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l configargparse
BuildOption(generate_buildrequires): -x yaml

BuildArch:      noarch

# See (obsolete) tests_require in setup.py:
BuildRequires:  %{py3_dist pytest}

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
%pytest -v


%files -n python3-configargparse -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
