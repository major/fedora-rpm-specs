Name:           python-click-plugins
Version:        1.1.1.2
Release:        %autorelease
Summary:        Click extension to register CLI commands via setuptools

License:        BSD-3-Clause
URL:            https://github.com/click-contrib/click-plugins
Source:         %{pypi_source click_plugins}

BuildArch:      noarch

%global _description %{expand:
An extension module for click to register external CLI commands via setuptools
entry-points.}


%description %{_description}


%package -n python3-click-plugins
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

Provides: deprecated()

%description -n python3-click-plugins %{_description}


%prep
%autosetup -n click_plugins-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l click_plugins


%check
export LANG=C.UTF-8
%{pytest} -ra


%files -n python3-click-plugins -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
