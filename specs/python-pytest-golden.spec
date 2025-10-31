%global date            20250215
%global commit          6a7b6776be95040d67bc6f709ab9ec8937b5be27
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python-pytest-golden
Version:        0.2.2^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Plugin for pytest that offloads expected outputs to data files

License:        MIT
URL:            https://github.com/oprypin/pytest-golden
# PyPI tarball doesn't include tests
#Source:         %%{url}/archive/v%%{version}/pytest-golden-%%{version}.tar.gz
# latest release too old, will ask upstream to mergee PR =#8 and release
Source:         %{url}/archive/%{commit}/pytest-golden-%{version}.tar.gz
# Drop deprecated atomicwrites dependency
Patch:          https://github.com/oprypin/pytest-golden/pull/8.patch#/pytest-golden-drop-atomicwrites.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides a plugin for pytest that offloads expected outputs to
data files.}

%description %_description

%package -n     python3-pytest-golden
Summary:        %{summary}

%description -n python3-pytest-golden %_description

%prep
#autosetup -p1 -n pytest-golden-%%{version}
%autosetup -p1 -n pytest-golden-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_golden

%check
%pytest -v

%files -n python3-pytest-golden -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
