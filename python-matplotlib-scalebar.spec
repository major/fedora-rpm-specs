Name:           python-matplotlib-scalebar
Version:        0.8.1
Release:        %autorelease
Summary:        Artist for matplotlib to display a scale bar

License:        BSD
URL:            https://github.com/ppinard/matplotlib-scalebar
Source0:        %{pypi_source matplotlib-scalebar}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Provides a new artist for matplotlib to display a scale bar, aka micron bar. It
is particularly useful when displaying calibrated images plotted using
plt.imshow(…).

The artist supports customization either directly from the ScaleBar object or
from the matplotlibrc.}

%description %_description


%package -n python3-matplotlib-scalebar
Summary:        %{summary}

%description -n python3-matplotlib-scalebar %_description


%package doc
Summary:        Documentation and examples for matplotlib-scalebar

# For the examples:
Requires:       %{name} = %{version}-%{release}
Requires:       python3dist(numpy)
Requires:       python3dist(pillow)
Requires:       python3dist(requests)

%description doc
%{summary}.


%prep
%autosetup -n matplotlib-scalebar-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -r requirements.txt requirements-test.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files matplotlib_scalebar


%check
%pytest


%files -n python3-matplotlib-scalebar -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.md


%files doc
# Note that the “documentation” currently consists entirely of examples
%doc doc/*


%changelog
%autochangelog
