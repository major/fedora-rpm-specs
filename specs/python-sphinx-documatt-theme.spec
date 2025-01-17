Name:           python-sphinx-documatt-theme
Version:        0.0.6
Release:        5%{?dist}
Summary:        Mobile-friendly Sphinx theme with beautiful typography

# The project as a whole is MIT.
# sphinx_documatt_theme/{global,local}toc.html are BSD-2-Clause
License:        MIT AND BSD-2-Clause
URL:            https://documatt.com/sphinx-themes/
VCS:            git:https://github.com/documatt/sphinx-themes.git
Source:         %{pypi_source sphinx_documatt_theme}

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
%pyproject_save_files -l sphinx_documatt_theme

%check
%pyproject_check_import

%files -n python3-sphinx-documatt-theme -f %{pyproject_files}
%doc README.html

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.6-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov  1 2023 Jerry James <loganjerry@gmail.com> - 0.0.6-1
- Version 0.0.6
- Drop upstreamed Sphinx 7 compatibility patch

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jerry James <loganjerry@gmail.com> - 0.0.5-4
- Add patch for Sphinx 7 compatibility (rhbz#2221982)

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.0.5-3
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.0.5-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 0.0.5-1
- Initial RPM
