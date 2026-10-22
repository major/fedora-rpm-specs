Summary:        Debug plugin for python-llm
Name:           python-llm-echo
Version:        0.5
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/simonw/llm-echo
Source:         https://github.com/simonw/llm-echo/archive/%{version}/llm-echo-%{version}.tar.gz
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
%autosetup -p1 -n llm-echo-%{version}

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
* Wed Oct 21 2026 Terje Røsten <terjeros@gmail.com> - 0.5-1
- 0.5

* Sat Sep 26 2026 Terje Røsten <terjeros@gmail.com> - 0.4-4
- Fix tests

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 0.4-2
- Rebuilt for Python 3.15

* Sun Apr 05 2026 Terje Røsten <terjeros@gmail.com> - 0.4-1
- 0.4

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.3~a3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Oct 10 2025 Terje Røsten <terjeros@gmail.com> - 0.3~a3-1
- Initial package
