Name:           python-types-psutil
Version:        7.0.0.20251001
Release:        %autorelease
Summary:        Typing stubs for psutil

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         %{pypi_source types_psutil}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This is a PEP 561 type stub package for the psutil package. It can be used by
type-checking tools like mypy, pyright, pytype, PyCharm, etc. to check code
that uses psutil.}

%description %_description

%package -n     python3-types-psutil
Summary:        %{summary}

%description -n python3-types-psutil %_description


%prep
%autosetup -p1 -n types_psutil-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L psutil-stubs


%files -n python3-types-psutil -f %{pyproject_files}


%changelog
%autochangelog
