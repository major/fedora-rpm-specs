%global pkgname sphinx_ansible_theme
%global forgeurl https://github.com/ansible-community/%{pkgname}

Name:           python-%{pkgname}
Version:        0.10.1
%forgemeta
Release:        %autorelease
Summary:        A reusable Ansible Sphinx Theme

License:        MIT
URL:            %{forgeurl}
Source:         https://github.com/ansible-community/sphinx_ansible_theme/archive/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       font(fontawesome)

%global _description %{expand:
A reusable Ansible Sphinx Theme. This theme is built on top
of RTD Theme and adds customizations needed for building projects
which are part of the Ansible ecosystem.}
%description %{_description}

%package -n python-%{pkgname}-doc
Summary: %{summary}
# MIT: the content
# BSD-2-Clause: files injected by Sphinx
License: MIT AND BSD-2-Clause
Provides: bundled(js-jquery)
Provides: bundled(js-underscore)
%description -n python-%{pkgname}-doc
Documentation for sphinx_ansible_theme

%package -n python3-%{pkgname}
Summary: %{summary}
%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -x test

%build
%pyproject_wheel
# generate html docs
sed -i.orig "/html_show_sphinx/ahtml_theme_path=['$PWD/build/lib']" docs/conf.py
PYTHONPATH=$PWD/build/lib sphinx-build docs html
mv docs/conf.py.orig docs/conf.py
# remove the sphinx-build leftovers
rm -vr html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%tox

%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pkgname}*

%files -n python-%{pkgname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
