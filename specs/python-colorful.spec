Name:           python-colorful
Version:        0.5.6
Release:        %autorelease
Summary:        Terminal string styling done right
License:        MIT
URL:            https://github.com/timofurrer/colorful
Source:         %{pypi_source colorful}
# https://github.com/timofurrer/colorful/pull/56
Patch:          0001-Read-version-from-ast.Constant-instead-of-ast.Str.patch
BuildArch:      noarch


%description
%{summary}.


%package -n python3-colorful
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-colorful
%{summary}.


%prep
%autosetup -n colorful-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colorful


%check
%pytest --verbose tests


%files -n python3-colorful -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
