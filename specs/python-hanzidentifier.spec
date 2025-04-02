Name:           python-hanzidentifier
Version:        1.3.0
Release:        %autorelease
Summary:        Identify Chinese text as Simplified or Traditional

License:        MIT
URL:            https://github.com/tsroten/hanzidentifier
Source:         %{url}/archive/v%{version}/hanzidentifier-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Hanzi Identifier is a simple Python module that identifies a string of text as
having Simplified or Traditional characters.}

%description %_description

%package -n     python3-hanzidentifier
Summary:        %{summary}

%description -n python3-hanzidentifier %_description


%prep
%autosetup -p1 -n hanzidentifier-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hanzidentifier


%check
%pyproject_check_import
%pytest

%files -n python3-hanzidentifier -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
