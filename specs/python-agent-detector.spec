Name:           python-agent-detector
Version:        1.1.0
Release:        %autorelease
Summary:        Detect AI coding agents from their execution environment or User-Agent

License:        MIT
URL:            https://github.com/patrick91/agent-detector
# We must use the PyPI sdist for now. See “Release process tags the wrong
# commit,” https://github.com/patrick91/agent-detector/issues/3.
Source:         %{pypi_source agent_detector}

BuildSystem:    pyproject
BuildOption(install): --assert-license agent_detector

BuildArch:      noarch

BuildRequires:  tomcli
# See the “dev” dependency group, but avoid coverage analysis:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
agent-detector is a small, dependency-free Python package for detecting which
AI coding agent is driving the current process, and for parsing that identity
back out of a User-Agent header on the receiving side.

It returns evidence rather than only a boolean, so callers can distinguish an
explicit identity from a broad environmental hint.}

%description %{common_description}


%package     -n python3-agent-detector
Summary:        %{summary}

%description -n python3-agent-detector %{common_description}


%prep -a
# Remove coverage-analysis options for pytest
tomcli set pyproject.toml str tool.pytest.ini_options.addopts "$(
  tomcli get pyproject.toml tool.pytest.ini_options.addopts |
    sed --regexp-extended 's/ ?--cov\b[^[:blank:]"]*//g'
  # This comment fixes broken vim syntax highlighting: '"
)"
# Makes sense for upstream CI; generally too strict for downstream packaging
tomcli set pyproject.toml lists delitem \
    tool.pytest.ini_options.filterwarnings error


%check -a
%pytest


%files -n python3-agent-detector -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
