# most tests currently fail
%bcond tests 0

%global srcname libtmux
%global tmux_minver 1.8

Name:           python-%{srcname}
Version:        0.42.0
Release:        %autorelease
Summary:        Scripting library for tmux

License:        MIT
URL:            https://github.com/tmux-python/libtmux
Source:         %{pypi_source}
# Patch to remove gp-libs test dependency; still unpackaged
Patch:          %{srcname}-no-gp-libs.diff

BuildArch:      noarch

%global _description %{expand:
libtmux is the tool behind tmuxp, a tmux workspace manager in
python.  It builds upon tmux's target and formats to create an object
mapping to traverse, inspect and interact with live tmux sessions.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  tmux >= %{tmux_minver}
%endif
Requires:       tmux >= %{tmux_minver}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
%if %{without tests}
# this depends on pytest, we don't want it installed
rm src/libtmux/pytest_plugin.py
rm src/libtmux/test.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l libtmux

%check
%pyproject_check_import
%if %{with tests}
PYTHONPATH=src %pytest tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES

%changelog
%autochangelog
