%global srcname docstring-parser

Name:           python-%{srcname}
Version:        0.15
Release:        1%{?dist}
Summary:        Parse Python docstrings
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%global _description %{expand:
Parse Python docstrings. Currently support ReST, Google, Numpydoc-style and Epydoc docstrings.}


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p 1 -n docstring_parser-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files docstring_parser


%check
%{pytest}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.md


%changelog
* Wed Jan 18 2023 Piotr Szubiakowski <pszubiak@eso.org> - 0.15-1
- Update to 0.15

* Wed Jul 20 2022 Piotr Szubiakowski <pszubiak@eso.org> - 0.14.1-2
- Apply code review fixes

* Thu May 19 2022 Piotr Szubiakowski <pszubiak@eso.org> - 0.14.1-1
- Init
