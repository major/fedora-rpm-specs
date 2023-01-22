%global srcname sphinx-ansible-theme
%global pkgname sphinx_ansible_theme
%global forgeurl https://github.com/ansible-community/%{pkgname}

Name:           python-%{pkgname}
Version:        0.9.1
%forgemeta
Release:        4%{?dist}
Summary:        A reusable Ansible Sphinx Theme

License:        MIT and BSD
URL:            %{forgeurl}
Source:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(sphinx-notfound-page)

%global _description %{expand:
A reusable Ansible Sphinx Theme. This theme is building on top
of RTD Theme and adds customization's needed for building projects
which are part of Ansible ecosystem}
%description %{_description}

%package -n python-%{pkgname}-doc
Summary: %{summary}
%description -n python-%{pkgname}-doc
Documentation for sphinx_ansible_theme

%package -n python3-%{pkgname}
Summary: %{summary}
%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=. sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -vr html/.{doctrees,buildinfo}

%install
%pyproject_install
ln -s %{_datadir}/fonts/fontawesome/FontAwesome.otf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2 .

%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pkgname}*

%files -n python-%{pkgname}-doc
%doc html
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.11

%autochangelog
