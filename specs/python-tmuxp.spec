%bcond tests 1
%bcond all_tests 0

%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.74.0
Release:        %autorelease
Summary:        Tmux session manager

# This is the proper SPDX license
License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}
Patch0:         fix-python315-argparse-theme.patch

BuildArch:      noarch

%global _description %{expand:
Session manager for tmux, which allows users to save and load tmux sessions
through simple configuration files.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(sphinx)
BuildRequires:  tmux
BuildRequires:  python3dist(typing-extensions)
%endif

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i -e '/^#!\//d' src/tmuxp/log.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tmuxp


%check
%pyproject_check_import
%pytest -v tests \
%if %{without all_tests}
  --deselect tests/workspace/test_builder.py::test_window_shell \
  --deselect tests/workspace/test_builder.py::test_pane_readiness_call_count \
  --deselect tests/workspace/test_builder.py::test_pane_readiness_custom_shell_skips_under_always
%else
%nil
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES examples
%{_bindir}/tmuxp


%changelog
%autochangelog
