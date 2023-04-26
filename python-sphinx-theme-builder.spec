%global prerel  b2

Name:           python-sphinx-theme-builder
Version:        0.2.0
Release:        0.9.%{prerel}%{?dist}
Summary:        Streamline the Sphinx theme development workflow

# Most of the code is MIT.  However,
# src/sphinx_theme_builder/_internal/passthrough.py is BSD-3-Clause.
License:        MIT and BSD-3-Clause
URL:            https://github.com/pradyunsg/sphinx-theme-builder
Source0:        %{url}/archive/%{version}%{prerel}/sphinx-theme-builder-%{version}%{prerel}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python3-devel

%description
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%package     -n python3-sphinx-theme-builder
Summary:        Streamline the Sphinx theme development workflow

%description -n python3-sphinx-theme-builder
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%pyproject_extras_subpkg -n python3-sphinx-theme-builder cli
%{_bindir}/stb
%{_mandir}/man1/stb.1*

%prep
%autosetup -n sphinx-theme-builder-%{version}%{prerel} -p1

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

# Skip test packages not available in Fedora
sed -i '/pytest-clarity/d;/pytest-pspec/d' tests/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -x cli tests/requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_theme_builder

# Install a man page
mkdir -p %{buildroot}%{_mandir}/man1
%{py3_test_envvars} help2man -N --version-string=%{version}%{prerel} \
  %{buildroot}%{_bindir}/stb > %{buildroot}%{_mandir}/man1/stb.1

%check
%pytest

%files -n python3-sphinx-theme-builder -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Apr 24 2023 Jerry James <loganjerry@gmail.com> - 0.2.0-0.9.b2
- Use %%py3_test_envvars to simplify man page installation

* Wed Apr 19 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.2.0-0.9.b2
- Unused docs BuildRequires were dropped to remove a dependency loop between
python-sphinx-theme-builder and python-furo

* Tue Mar 28 2023 Jerry James <loganjerry@gmail.com> - 0.2.0-0.8.b2
- Version 0.2.0b2
- Drop upstreamed tomllib patch

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.2.0-0.7.b1
- Add cli extras subpackage containing the stb binary
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.6.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-0.5.b1
- Drop dependency on tomli
- Convert License tag to SPDX

* Fri Jul 29 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-0.4.b1
- Version 0.2.0b1
- Depend on pyproject-metadata instead of pep621

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.3.a15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-0.2.a15
- Version 0.2.0a15

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.2.0-0.2.a14
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-0.1.a14
- Initial RPM
