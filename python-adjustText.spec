%global pypi_name adjustText

# Use GitHub sources (license file is missing in PyPI sdidt)
%global forgeurl https://github.com/Phlya/adjustText

%global _description %{expand:
The idea is that often when we want to label multiple points on a graph
the text will start heavily overlapping with both other labels and data
points. This can be a major problem requiring manual solution.

However this can be largely automatized by smart placing of the labels
(difficult) or iterative adjustment of their positions to minimize
overlaps (relatively easy).
This library (well... script) implements the latter option to help with
matplotlib graphs. Usage is very straightforward with usually pretty good
results with no tweaking (most important is to just make text slightly
smaller than default and maybe the figure a little larger).
However the algorithm itself is highly configurable for complicated plots.}

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        %{autorelease}
Summary:        Automatic label placement for matplotlib
BuildArch:      noarch
%global tag v%{version}
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
# Package does not provide any tests
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
