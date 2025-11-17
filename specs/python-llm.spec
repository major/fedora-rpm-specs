# Disable tests/docs until llm-echo (circular dependency)/markdown-builder
# are available

%bcond_with     tests
%bcond_without  docs

Summary:        Tool and Python library for interacting with Large Language Models
Name:           python-llm
Version:        0.27.1
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/simonw/llm
Source:         https://github.com/simonw/llm/archive/%{version}/llm-%{version}.tar.gz
Patch:          python-llm-0.27.1-format-fix.patch
Patch:          python-llm-0.27.1-disable-tests.patch
BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-httpx
BuildRequires:  python3-pytest-vcr
%endif
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-furo
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinx-markdown-builder
%endif
%global _description \
%{expand:
A CLI tool and Python library for interacting with Large Language Models,
both via remote APIs and with models that can be installed and run on
your own machine.
}
%description %_description

%package     -n python3-llm
Summary:        %{summary}
%description -n python3-llm %_description

%if %{with docs}
%package     -n python3-llm-docs
Summary:        Documentation of python3-llm
%description -n python3-llm-docs %_description
Package contains documentation of python-llm
%endif

%prep
%autosetup -p1 -n llm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
(pushd docs && make man html)
%endif

%install
%pyproject_install
%pyproject_save_files llm
%if %{with docs}
install -D -m0644 docs/_build/man/llm.1 %{buildroot}%{_mandir}/man1/llm.1
%endif

%check
%pyproject_check_import
%if %{with tests}
export ISOLATED_CI_ENV=1
%pytest
%endif

%files -n python3-llm -f %{pyproject_files}
%doc README.*
%{_bindir}/llm
%if %{with docs}
%{_mandir}/man1/llm.1*
%endif

%if %{with docs}
%files -n python3-llm-docs
%doc docs/_build/html/
%endif

%changelog
* Mon Aug 25 2025 Terje Røsten <terjeros@gmail.com> - 0.27.1-1
- Initial package
