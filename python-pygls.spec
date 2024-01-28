Name:           python-pygls
Version:        1.2.1
Release:        %autorelease
Summary:        A pythonic generic language server

License:        Apache-2.0
URL:            https://github.com/openlawlibrary/pygls
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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

%pyproject_extras_subpkg -n python3-pygls ws

%prep
%autosetup -p1 -n pygls-%{version}

# relax version requirements of websockets
sed -i 's/\^11\.0\.3/>=11.0.3/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x ws

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygls

%check
%pytest

%files -n python3-pygls -f %{pyproject_files}

%changelog
%autochangelog
