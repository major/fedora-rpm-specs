Name:           python-pygls
Version:        2.0.1
Release:        %autorelease
Summary:        A pythonic generic language server

License:        Apache-2.0
URL:            https://github.com/openlawlibrary/pygls
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): -L pygls
BuildOption(generate_buildrequires): -x ws

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  %{py3_dist pytest_asyncio}

%global _description %{expand:
pygls (pronounced like "pie glass") is a pythonic generic implementation of the
Language Server Protocol for use as a foundation for writing your own Language
Servers in just a few lines of code.}

%description %_description

%package -n     python3-pygls
Summary:        %{summary}

%description -n python3-pygls %_description

%check -a
%pytest -rs

%files -n python3-pygls -f %{pyproject_files}
%license LICENSE.txt

%changelog
%autochangelog
