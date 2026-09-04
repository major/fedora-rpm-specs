Name:           python-agent-detector
Version:        2.0.0
Release:        %autorelease
Summary:        Detect AI coding agents from their execution environment or User-Agent

License:        MIT
URL:            https://github.com/patrick91/agent-detector
Source0:        %{url}/archive/%{version}/agent-detector-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help text
Source1:        agent-detector.1

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


%install -a
install -D --target='%{buildroot}%{_mandir}/man1' \
    --preserve-timestamps --mode=0644 '%{SOURCE1}'


%check -a
%pytest


%files -n python3-agent-detector -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%{_bindir}/agent-detector
%{_mandir}/man1/agent-detector.1*


%changelog
%autochangelog
