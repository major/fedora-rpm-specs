%global srcname mathics-pygments

Name:           python-%{srcname}
Version:        1.0.2
Release:        %autorelease
Summary:        Mathematica/Wolfram Language Lexer for Pygments

License:        MIT
URL:            http://github.com/Mathics3/mathics-pygments
# PyPI source tarball is misnamed
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This is package provides a lexer and highlighter for Mathematica/Wolfram
Language source code using the pygments engine.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_pygments

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.rst

%changelog
%autochangelog
