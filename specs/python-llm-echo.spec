%global         pypi_version 0.3a3

Summary:        Debug plugin for python-llm
Name:           python-llm-echo
Version:        0.3~a3
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/simonw/llm-echo
Source:         https://github.com/simonw/llm-echo/archive/%{pypi_version}/llm-echo-%{pypi_version}.tar.gz
Patch:          python-llm-0.3a3-format-fix.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
%global _description \
%{expand:
Debug plugin for LLM. Adds a model which echos its input without hitting
an API or executing a local LLM.
}
%description %_description

%package     -n python3-llm-echo
Summary:        %{summary}
%description -n python3-llm-echo %_description

%prep
%autosetup -p1 -n llm-echo-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files llm_echo

%check
%pyproject_check_import
%pytest

%files -n python3-llm-echo -f %{pyproject_files}

%changelog
* Fri Oct 10 2025 Terje Røsten <terjeros@gmail.com> - 0.3~a3-1
- Initial package
