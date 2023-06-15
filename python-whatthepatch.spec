%global pypi_name whatthepatch
%global pypi_version 1.0.2


Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        6%{?dist}
Summary:        A patch parsing and application library

License:        MIT
URL:            https://github.com/cscorley/whatthepatch
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
What The Patch!? is a library for both parsing and applying
patch files.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
/usr/bin/sed -i 's|\r$||' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.2-3
- Drop license macro (avoids duplication) and fix line endings
- Sanitize description

* Sat Jul 16 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.2-2
- Modernize spec file

* Sat Jul 16 2022 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.2-1
- Initial package.
