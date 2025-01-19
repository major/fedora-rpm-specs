%bcond tests 1

Name:           mkdocs-bootswatch
Version:        1.1
Release:        8%{?dist}
Summary:        Bootswatch themes for MkDocs

License:        BSD-2-Clause AND MIT
URL:            http://mkdocs.github.io/mkdocs-bootswatch
Source:         %{pypi_source mkdocs-bootswatch}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{summary}.

%prep
%autosetup -p1 -n mkdocs-bootswatch-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_bootswatch

%check
%pyproject_check_import

%if %{with tests}
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
for theme_dir in ../mkdocs_bootswatch/*; do
    if [ -d $theme_dir ]; then
       mkdocs build --theme $(basename $theme_dir)
    fi
done
popd
%endif

%files -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1-7
- Unretire package; Fixes: RHBZ#2332263
- Convert to pyproject macros
- Gate tests behind a bcond

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-2
- No globbing %%{python3_sitelib}
- BR python3dist(setuptools)

* Mon Mar  9 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-1
- Update to 1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.5.0-1
- Update to v0.5.0
- Missing license text, see: https://github.com/mkdocs/mkdocs-bootswatch/pull/47

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.4.0-1
- Update to v0.4.0
- Unblundle js-highlight
- Unbundle fontawesome-webfont

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.2.0-1
- Initial Packaging
