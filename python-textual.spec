Name:           python-textual
Version:        0.1.18
Release:        1%{?dist}
Summary:        TUI (Text User Interface) framework for Python
License:        MIT
URL:            https://github.com/Textualize/textual
Source0:        %{url}/archive/v%{version}/textual-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  pytest

%global _description %{expand:
Textual is a TUI (Text User Interface) framework for Python inspired
by modern web development. Currently a Work in Progress.}

%description
%{_description}

%package -n python3-textual
Summary:        %{summary}

%description -n python3-textual
%{_description}

%package -n python3-textual-doc
Summary:        Docs and examples for python3-textual

%description -n python3-textual-doc
%{_description}

%prep
%autosetup -n textual-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files textual


%check
%pytest


%files -n python3-textual -f %{pyproject_files}
%license LICENSE

%files -n python3-textual-doc
%license LICENSE
%doc README.md docs/ examples/


%changelog
* Sun Jul 31 2022 Jonathan Wright <jonathan@almalinux.org> - 0.1.18-1
- Initial package build
- rhbz#2121258
