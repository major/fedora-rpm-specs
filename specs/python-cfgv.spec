Name:           python-cfgv
Version:        3.5.0
Release:        %autorelease
Summary:        Validate configuration and produce human readable error messages

# SPDX
License:        MIT
URL:            https://github.com/asottile/cfgv
Source:         %{url}/archive/v%{version}/cfgv-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l cfgv

BuildArch:      noarch

# See requirements-dev.txt, which is mostly unwanted coverage tools:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-cfgv
Summary:        %{summary}

%description -n python3-cfgv %{common_description}


%check -a
%pytest


%files -n python3-cfgv -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
