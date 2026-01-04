Name:           python-tvb-data
Version:        3.0.0
Release:        %autorelease
Summary:        Demo data for The Virtual Brain software

License:        GPL-3.0-or-later
# See also: https://zenodo.org/records/14992335 (for version 3.0.0)
URL:            https://gitlab.ebrains.eu/ri/tech-hub/apps/tvb/tvb-data
Source:         %{pypi_source tvb_data}

BuildSystem:    pyproject
BuildOption(install):   -l tvb_data
# Upstream provides no tests

BuildArch:      noarch

%global desc %{expand:
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

Various demonstration datasets for use with The Virtual Brain are provided
here.}

%description %{desc}


%package -n python3-tvb-data
Summary:        %{summary}

%description -n python3-tvb-data %{desc}


%files -n python3-tvb-data -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
