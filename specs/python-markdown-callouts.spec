%bcond tests 1

Name:           python-markdown-callouts
Version:        0.4.0
Release:        %autorelease
Summary:        Markdown extension to provide a classier syntax for admonitions

License:        MIT
URL:            https://oprypin.github.io/markdown-callouts
Source:         %{pypi_source markdown_callouts}

# https://github.com/oprypin/markdown-callouts/pull/24
Patch:          0001-Fix-compatibility-with-Markdown-3.10.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides an extension for Python-Markdown that adds a classier
syntax for admonitions.}

%description %_description

%package -n     python3-markdown-callouts
Summary:        %{summary}

%description -n python3-markdown-callouts %_description

%prep
%autosetup -p1 -n markdown_callouts-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l markdown_callouts

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-markdown-callouts -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
