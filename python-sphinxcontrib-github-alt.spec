Name:           python-sphinxcontrib-github-alt
Version:        1.2
Release:        10%{?dist}
Summary:        Link to GitHub issues, pull requests, commits and users from Sphinx docs
License:        BSD-2-Clause
URL:            https://github.com/jupyter/sphinxcontrib_github_alt
Source:         %{pypi_source sphinxcontrib_github_alt}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Link to GitHub issues, pull requests, commits and users for a particular
project.
It's called 'alt' because sphinxcontrib-github already exists. IPython &
Jupyter projects have been using the syntax defined in this extension for
some time before we made it into its own package, so we didn't want to
switch to sphinxcontrib-github.}

%description %_description


%package -n     python3-sphinxcontrib-github-alt
Summary:        %{summary}
%py_provides python3-sphinxcontrib_github_alt

%description -n python3-sphinxcontrib-github-alt %_description


%prep
%autosetup -n sphinxcontrib_github_alt-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinxcontrib_github_alt


%check
# there are no tests upstream
%pyproject_check_import


%files -n python3-sphinxcontrib-github-alt -f %{pyproject_files}
%doc README.rst
%license COPYING.md


%changelog
* Mon Feb 13 2023 Miro Hrončok <mhroncok@redhat.com> - 1.2-10
- Convert to pyproject-rpm-macros
- The INSTALLER file now says "rpm" instead of "pip"
- Run basic import check during the build
- Use a SPDX license identifier in the License tag

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 1 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.2-1
- Update to 1.2 (#1828203)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- initial package
