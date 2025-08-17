Name:           python-deepmerge
Version:        2.0
Release:        3%{?dist}
Summary:        Toolset for deeply merging Python dictionaries

License:        MIT
URL:            http://deepmerge.readthedocs.io/en/latest/
Source:         %{pypi_source deepmerge}

BuildArch:      noarch
BuildRequires:  python3-devel
# Not using auto dev deps to avoid unwanted style and lint dependencies
BuildRequires:  python3-pytest


%global _description \
%{summary}.

%description %_description

%package -n     python3-deepmerge
Summary:        %{summary}

%description -n python3-deepmerge %_description

%prep
%autosetup -p1 -n deepmerge-%{version}

# Move tests out of the package path
mv deepmerge/tests tests


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l deepmerge


%check
%pyproject_check_import
%pytest


%files -n python3-deepmerge -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 2.0-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.0-1
- Initial package

