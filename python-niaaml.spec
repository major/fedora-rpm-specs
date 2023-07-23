%bcond_without tests
# It’s nice to be able to run the examples as additional tests, but we normally
# choose not to do so since some examples take as much as several hours to run.
%bcond_with test_examples
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global pypi_name niaaml
%global pretty_name NiaAML

%global _description %{expand:
NiaAML is a framework for Automated Machine Learning based on nature-inspired
algorithms for optimization. The framework is written fully in Python. The
name NiaAML comes from the Automated Machine Learning method of the same name.
Its goal is to compose the best possible classification pipeline for the given
task efficiently using components on the input. The components are divided
into three groups: feature selection algorithms, feature transformation
algorithms and classifiers. The framework uses nature-inspired algorithms
for optimization to choose the best set of components for the
classification pipeline, and optimize their hyperparameters.}

Name:           python-%{pypi_name}
Version:        1.1.12
Release:        3%{?dist}
Summary:        Python automated machine learning framework

License:        MIT
URL:            https://github.com/lukapecnik/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

# Ensure the Python interpreter path is correct in the example runner script:
sed -r -i 's|\bpython3\b|%{python3}|' examples/run_all.sh

%generate_buildrequires
# There exists a docs/requirements.txt, but it seems to be inaccurate, with a
# large number of unnecessary dependencies, so we do not use it to generate
# BR’s.
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaaml

%check
%if %{with tests}
%pytest
%endif
%if %{with test_examples}
# See also: examples/run_all.sh
find examples -type f -name '*.py' |
  env PYTHONPATH="${PWD}" xargs -r -n 1 -t -P %{_smp_build_ncpus} -I '{}' \
      '%{python3}' '{}'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md COMPONENTS.md CITATION.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/
%doc paper/
%doc docs/paper/10.21105.joss.02949.pdf
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md CITATION.md

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 1.1.12-2
- Rebuilt for Python 3.12

* Sun Apr 30 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.12-1
- Update to 1.1.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.11-2
- Update documentation with additional paper

* Fri Sep 16 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.11-1
- Update to the latest upstream's release

* Sun Aug 21 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.10-1
- Update to the latest upstream's release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 1.1.9-2
- Rebuilt for Python 3.11

* Thu May 26 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.9-1
- Update to the latest upstream's release

* Tue May 24 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.8-1
- Update to the latest upstream's release

* Tue Feb 22 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.7-2
- No longer need to skip load_pipeline_object_file when running examples as
  tests (https://github.com/lukapecnik/NiaAML/issues/60)

* Mon Feb 21 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.7-1
- Update to the latest upstream's release
- Remove patches

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.6-6
- Update description of package

* Fri Nov 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.6-5
- Add missing BR: python3-devel; drop implied pyproject-rpm-macros
- Remove various unnecessary BR’s
- Build documentation as PDF instead of HTML
- Drop obsolete python_provide macro
- Fix version check in setup.py for Python 3.10+
- Send PR upstream to fix text files in site-packages
- Allow running the examples as an additional test, but do not do so by default
  because some of them take too long

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.6-2
- Minor corrections

* Mon Jun 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.6-1
- Update to the latest upstream's major release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.5-2
- Rebuilt for Python 3.10

* Wed Jun 2 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.5-1
- Update to the latest release

* Tue May 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.4-1
- Update to the latest release

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.2-1
- Update to the latest release
- Remove patch

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-4
- Install additional files

* Thu Apr 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-3
- Minor corrections (path)

* Mon Mar 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-2
- Enable tests

* Tue Mar 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-1
- New version - 1.1.1

* Wed Mar 3 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-3
- Add make dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
