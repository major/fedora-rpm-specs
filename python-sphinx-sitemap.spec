Name:           python-sphinx-sitemap
Version:        2.5.1
Release:        2%{?dist}
Summary:        Sitemap generator for Sphinx

License:        MIT
URL:            https://github.com/jdillard/sphinx-sitemap
Source0:        %{url}/archive/v%{version}/sphinx-sitemap-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package contains a Sphinx extension to generate multiversion and
multilanguage sitemaps.org-compliant sitemaps for the HTML version of
your Sphinx documentation.}

%description %_description

%package     -n python3-sphinx-sitemap
Summary:        Sitemap generator for Sphinx

%description -n python3-sphinx-sitemap %_description

%prep
%autosetup -n sphinx-sitemap-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files sphinx_sitemap

%check
%pytest

%files -n python3-sphinx-sitemap -f %{pyproject_files}
%doc README.html

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 18 2023 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Version 2.5.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- Dynamically generate BuildRequires

* Sat Jan 28 2023 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- Version 2.5.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- Version 2.4.0
- Verify that MIT is the correct SPDX identifier

* Wed Dec 21 2022 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- Version 2.3.0
- Test with pytest

* Sat Nov 12 2022 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- Version 2.2.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Initial RPM
