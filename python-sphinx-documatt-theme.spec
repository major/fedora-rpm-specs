Name:           python-sphinx-documatt-theme
Version:        0.0.5
Release:        3%{?dist}
Summary:        Mobile-friendly Sphinx theme with beautiful typography

# The project as a whole is MIT.
# sphinx_documatt_theme/{global,local}toc.html are BSD-2-Clause
License:        MIT AND BSD-2-Clause
URL:            https://documatt.gitlab.io/sphinx-themes/themes/documatt.html
Source0:        %{pypi_source sphinx_documatt_theme}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A mobile-friendly Sphinx theme designed to provide a great documentation
reading experience with beautiful typography.}

%description %_description

%package     -n python3-sphinx-documatt-theme
Summary:        Mobile-friendly Sphinx theme with beautiful typography

%description -n python3-sphinx-documatt-theme %_description

%prep
%autosetup -n sphinx_documatt_theme-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files sphinx_documatt_theme

%check
%pyproject_check_import

%files -n python3-sphinx-documatt-theme -f %{pyproject_files}
%doc README.html

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.0.5-3
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.0.5-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 0.0.5-1
- Initial RPM
