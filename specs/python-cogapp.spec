%global srcname cogapp

Name:           python-%{srcname}
Version:        3.5.1
Release:        %autorelease
Summary:        Content generator for executing Python snippets in source files

License:        MIT
URL:            http://nedbatchelder.com/code/cog
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
# tox.ini works with coverage
BuildRequires:  python3-pytest

%global _description %{expand:
Cog is a file generation tool. It lets you use pieces of Python code as
generators in your source files to generate whatever text you need.}

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
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt
%{_bindir}/cog

%changelog
%autochangelog
