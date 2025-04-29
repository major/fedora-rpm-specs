%bcond_without tests

%global original_name toml-adapt
%global pretty_name toml_adapt

%global _description %{expand:
Working with TOML files has become inevitable during package maintenance
across different ecosystems. Often, package maintainers must change dependency
versions or add/remove dependencies when building their packages due to
inconsistent base systems. This issue can be solved either by applying patches
or using sed commands, but that can be time-consuming and frustrating.
This project provides a very simple yet user-friendly command-line interface
to make this process easier.}

Name:           python-%{original_name}
Version:        0.3.4
Release:        %autorelease
Summary:        A simple CLI for manipulating TOML files

License:        MIT
URL:            https://github.com/firefly-cpp/%{original_name}
Source0:        %{url}/archive/%{version}/%{original_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{original_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{original_name} %_description

%package doc
Summary:        Documentation for %{pretty_name}

%description doc
Documentation for %{pretty_name}.

%prep
%autosetup -n %{original_name}-%{version}
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pretty_name}

install -D -t '%{buildroot}%{_mandir}/man1' -m 0644 %{original_name}.1

%check
%pyproject_check_import %{pretty_name}

%if %{with tests}
%pytest
%endif

%files -n python3-%{original_name} -f %{pyproject_files}
%{_bindir}/%{original_name}
%license LICENSE
%doc README.md AUTHORS.rst CODE_OF_CONDUCT.md CHANGELOG.md CITATION.cff
%{_mandir}/man1/%{original_name}.1*

%files doc
%license LICENSE
%doc README.md AUTHORS.rst CODE_OF_CONDUCT.md CHANGELOG.md CITATION.cff

%changelog
%autochangelog
