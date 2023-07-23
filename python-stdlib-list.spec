# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:       python-stdlib-list
Version:    0.9.0
Release:    2%{?dist}
Summary:    A list of Python Standard Libraries

# SPDX
License:    MIT
URL:        https://github.com/pypi/stdlib-list
# pypi is missing docs, so use the github tarball instead
Source:     %{url}/archive/v%{version}/stdlib-list-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
# We BR this manually since the other dependencies in the “test” extra are for
# coverage analysis and are unwanted
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
BuildRequires:  %{py3_dist pytest}

%global desc %{expand:
This package includes lists of all of the standard libraries for Python.}

%description %{desc}

%package -n python3-stdlib-list
Summary:    %{summary}

%description -n python3-stdlib-list %{desc}

%package doc
Summary:   Documentation for python-stdlib-list

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
%{summary}.

%prep
%autosetup -n stdlib-list-%{version}
# We don’t need the HTML theme to build PDF documentation:
sed -r -i 's/, "furo"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:-x doc}

%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files stdlib_list

%check
%pytest

%files -n python3-stdlib-list -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/PythonStandardLibraryList.pdf
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.0-1
- Update to 0.9.0 (fix RHBZ#2216610, fix RHBZ#2155214)
- Confirm License is SPDX MIT

* Thu Jun 29 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.0-9
- Port to pyproject-rpm-macros
- Build docs as PDF instead of HTML
- Use a simplified description from upstream

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.8.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sun Mar 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.0-8
- Build docs
- Use GitHub tarball instead of PyPI

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-5
- Update patch to include lists required by other packages

* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-4
- Update for python 3.9
- TODO: enable tests added in next release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.0-1
- New upstream version

* Mon Nov 11 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 0.5.0-5
- Fix requires
- https://bugzilla.redhat.com/show_bug.cgi?id=1770852

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-2
- Fix comments BZ 1741623

* Thu Aug 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-1
- Initial package.
