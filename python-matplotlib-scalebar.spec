%global commit 2c57173d67a346b323a4afff7b7dd9c7f1314da4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20230706
%global releasever 0.8.1

Name:           python-matplotlib-scalebar
Version:        %{releasever}^%{snapdate}git%{shortcommit}
Release:        %autorelease
Summary:        Artist for matplotlib to display a scale bar

License:        BSD
URL:            https://github.com/ppinard/matplotlib-scalebar
Source0:        %{url}/archive/%{commit}/matplotlib-scalebar-%{shortcommit}.tar.gz

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
%autosetup -n matplotlib-scalebar-%{commit}


%generate_buildrequires
# Python tools don't like %%version
export SETUPTOOLS_SCM_PRETEND_VERSION=%{releasever}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{releasever}
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{releasever}
%pyproject_install
%pyproject_save_files matplotlib_scalebar


%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{releasever}
%pytest


%files -n python3-matplotlib-scalebar -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.md


%files doc
# Note that the “documentation” currently consists entirely of examples
%doc doc/*


%changelog
%autochangelog
