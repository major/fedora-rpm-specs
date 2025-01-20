%global pypi_name pyflame
%global pypi_version 0.3.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        2%{?dist}
Summary:        A Flamegraph generator for Python

License:        MIT
URL:            https://gitlab.com/living180/pyflame
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Generate flamegraphs for Python code, using
Brendan Gregg's excellent FlameGraph_ project to perform the heavy
lifting.pyflame can be used to invoke a Python script from the command line and
generate a flamegraph of its execution. It also provides a panel for Django
Debug Toolbar

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Recommends:       python3dist(django) >= 3.2
Recommends:       python3dist(django-debug-toolbar)
Recommends:       python3dist(ipython)
Recommends:       python3dist(traitlets) >= 5
Requires:       flamegraph
%description -n python3-%{pypi_name}
Generate flamegraphs for Python code, using
Brendan Gregg's excellent FlameGraph_ project to perform the heavy
lifting.pyflame can be used to invoke a Python script from the command line and
generate a flamegraph of its execution. It also provides a panel for Django
Debug Toolbar


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} -l

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-1
- Initial package.
