Name:           python-jupyter-events
Version:        0.12.0
Release:        %autorelease
Summary:        Jupyter Event System library
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_events}
BuildArch:      noarch
BuildRequires:  python3-devel
# Manual test deps - upstream contains coverage, pre-commit, …
BuildRequires:  python3-click
BuildRequires:  python3-rich
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-console-scripts

%global _description %{expand:
An event system for Jupyter Applications and extensions.}


%description %_description

%package -n     python3-jupyter-events
Summary:        %{summary}

%description -n python3-jupyter-events %_description


%prep
%autosetup -p1 -n jupyter_events-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_events


%check
%pytest


%files -n python3-jupyter-events -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-events

%changelog
%autochangelog
