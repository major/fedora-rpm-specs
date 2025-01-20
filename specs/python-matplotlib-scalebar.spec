Name:           python-matplotlib-scalebar
Version:        0.9.0
Release:        %autorelease
Summary:        Artist for matplotlib to display a scale bar

License:        BSD-2-Clause
URL:            https://github.com/ppinard/matplotlib-scalebar
Source0:        %{url}/archive/%{version}/matplotlib-scalebar-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

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
%autosetup -n matplotlib-scalebar-%{version}


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l matplotlib_scalebar


%check
%pytest


%files -n python3-matplotlib-scalebar -f %{pyproject_files}
%doc README.md


%files doc
%license LICENSE
# Note that the “documentation” currently consists entirely of examples
%doc doc/*


%changelog
%autochangelog
