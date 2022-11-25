%global pypi_name adjustText

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
Version:        0.7.3
Release:        %{autorelease}
Summary:        Automatic label placement for matplotlib
BuildArch:      noarch

License:        MIT
URL:            https://pypi.org/pypi/{pypi_name}
Source0:        %{pypi_source %{pypi_name}}
# LICENSE file as published on GitHub, but missing in tarball
# https://github.com/Phlya/adjustText/issues/131
Patch:          add_license_file.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git

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
%license LICENSE

%changelog
%autochangelog
