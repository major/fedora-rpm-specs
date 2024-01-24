Name:           reuse
Version:        1.1.1
Release:        5%{?dist}
Summary:        A tool for compliance with the REUSE recommendations
# The CC0-1.0 licence applies to json data files, not code.
# CC-BY-SA-4.0 is applied to documentation.
License:        Apache-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
Url:            https://github.com/fsfe/reuse-tool
Source0:        %pypi_source
# Build
BuildRequires:  python3-devel
BuildRequires:  gettext
# Test
BuildRequires:  git
BuildRequires:  mercurial
# These are development dependencies in the Poetry config, not build
# dependencies. They are build dependencies for Fedora packaging.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
BuildRequires:  %{py3_dist sphinxcontrib-apidoc}
BuildRequires:  %{py3_dist recommonmark}
Recommends:     git
Recommends:     mercurial
BuildArch:      noarch

%description
A tool for compliance with the REUSE recommendations. Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
pushd docs
PBR_VERSION=%{version} sphinx-build-%{python3_version} . html
rm -rf html/.{doctrees,buildinfo}
popd

%install
%pyproject_install

%pyproject_save_files reuse

%check
%pytest

%files -n reuse -f %{pyproject_files}
%license LICENSES/*.txt
%doc README.md CHANGELOG.md docs/html/
%{_bindir}/reuse

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.12

* Mon Feb 06 2023 Carmen Bianca BAKKER <carmenbianca@fedoraproject.org> - 1.1.1-2
- Also package documentation files again.

* Mon Feb 06 2023 Carmen Bianca BAKKER <carmenbianca@fedoraproject.org> - 1.1.1-1
- New version.
- Adapt package to poetry build system.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0. Fixes rhbz#2035754.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Maxwell G <gotmax@e.email> - 0.13.0-1
- Update to 0.13.0. Fixes rhbz#1970928.
- Remove unnecessary pypi_name variable

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.1-2
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.12.1-1
- new version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.11.1-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.8.0-1
- New version
- Additional build dependency on setuptools-scm.
- Performance increase.
- Many additional translations.
- Deprecated licenses are now recognised.
- lint no longer accepts path arguments. Where previously one could do reuse
lint SUBDIRECTORY, this is no longer possible. When linting, you must always
lint the entire project. To change the project's root, use --root. 

* Thu Nov 28 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.7.0-1
- New version.
- Upstream PyPI package renamed from fsfe-reuse to reuse.
- No other changes.

* Fri Nov 22 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.6.0-1
- New upstream version.
- Git submodules are now ignored by default. `--include-submodules` reverses
  this behaviour.

* Mon Oct 28 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.5.2-1
- new version

* Fri Sep 06 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.5.0-1
- New upstream version.
- Now compatible with REUSE v3.0.
- Added Sphinx-generated documentation.
- Now also contains code under ASL 2.0.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.3.4-1
- New upstream version.
- Copyright lines can now start with © in addition to Copyright.

* Fri Nov 23 2018 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.3.3-1
- Initial package.
