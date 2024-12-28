%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We would like to generate PDF documentation as a substitute, but have not
# been able to successfully build the Sphinx-generated LaTeX for this
# particular package.
%bcond_with doc_pdf

%global forgeurl https://github.com/NiaOrg/NiaPy
%global tag %{version}

Name:           python-niapy
Version:        2.5.1
%forgemeta
Release:        2%{?dist}
Summary:        Microframework for building nature-inspired algorithms

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Replace deprecated `np.float_`.
Patch:          %{forgeurl}/commit/99cb246ed483d5961d4ff17395732abcb85dced1.patch

BuildArch:      noarch

%global _description %{expand:
Nature-inspired algorithms are a very popular tool for solving optimization
problems. Numerous variants of nature-inspired algorithms have been developed
since the beginning of their era. Those were tested in various domains on
various applications to prove their versatility, especially when
hybridized, modified, or adapted. However, the implementation of
nature-inspired algorithms is sometimes a complicated, complex, and tedious
task. In order to break this wall, NiaPy is intended for simple and quick
use without spending time implementing algorithms from scratch.}

%description %_description

%package -n python3-niapy
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-toml-adapt

%if %{with tests}
# setup.py: tests_require
#
# flake8 ~= 3.7.7
# astroid >= 2.0.4
# pytest ~= 3.7.1
# coverage ~= 4.4.2
# coverage-space ~= 1.0.2
#
# We do not run flake8:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# …nor do we care about test coverage. Furthermore, we must accept any newer
# version of pytest.
BuildRequires:  python3dist(pytest) >= 3.7.1
%endif

%description -n python3-niapy %_description

%package doc
Summary:        Documentation and examples for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/xindy
%endif

%description doc
%{summary}.

Full HTML documentation is available at
https://niapy.readthedocs.io/en/stable/index.html.

%prep
%forgeautosetup -p1
# Since we aren’t building HTML documentation, we don’t need the HTML theme
# dependency:
sed -r -i 's/^(sphinx-.*theme)/#\1/' docs/requirements.txt
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/source/conf.py
# Avoid: ! LaTeX Error: Too deeply nested.
# Normally we could add a preamble like:
#
#   cat >> docs/source/conf.py <<'EOF'
#   latex_elements['preamble'] = r'''
#   \usepackage{enumitem}
#   \setlistdepth{99}
#   '''
#   EOF
#
# but that does not work well (“Undefined control sequence”).
#
# We can also try:
#
#   echo "latex_elements['maxlistdepth'] = '10'" >> docs/source/conf.py
#
# but this produces errors like:
#
#   ! LaTeX Error: \begin{list} on input line 21785 ended by \end{itemize}.

# optional step but let's ensure that there is no problems with dependency versions
toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep numpy -ver X
toml-adapt -path pyproject.toml -a change -dep pandas -ver X
toml-adapt -path pyproject.toml -a change -dep matplotlib -ver X
toml-adapt -path pyproject.toml -a change -dep openpyxl -ver X

%generate_buildrequires
%pyproject_buildrequires -r %{?with_pdf_doc:docs/requirements.txt}

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet -f'
%endif

%install
%pyproject_install
%pyproject_save_files niapy

%check
%if %{with tests}
#k="${k-}${k+ and }not test_to_skip_sample1"
#k="${k-}${k+ and }not test_to_skip_sample2"
%pytest -ra -k "${k-}"
%endif

%files -n python3-niapy -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md Algorithms.md Problems.md CITATION.cff

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/build/latex/NiaPy.pdf
%endif
%doc examples/
%doc paper/
%doc CONTRIBUTING.md CODE_OF_CONDUCT.md

%changelog
* Thu Dec 26 2024 Sandro <devel@penguinpee.nl> - 2.5.1-2
- Apply patch for NumPy 2.x

* Sun Nov 24 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 2.5.1-1
- Update to 2.5.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.13

* Sun May 19 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 2.3.1-1
- Update to 2.3.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.0-3
- Add missing LICENSE file

* Wed Dec 20 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 2.1.0-1
- Update to 2.1.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.0.5-2
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.5-1
- Upgrade to 2.0.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.4-1
- Upgrade to 2.0.4

* Sun Sep 4 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.3-1
- Upgrade to 2.0.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.0.2-3
- Rebuilt for Python 3.11

* Mon May 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.2-2
- Improve description of package

* Sun May 22 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.2-1
- Update to the latest upstream's release

* Sat Mar 5 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.1-1
- Update to the latest upstream's release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- Update to the latest upstream's release (second stable release)

* Mon Nov 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-0.3rc18
- Port to pyproject-rpm-macros (“new guidelines”)
- Drop HTML documentation
- Stop skipping tests; they all pass now

* Wed Aug 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc18
- Update to the latest upstream's release - rc18

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2rc17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc17
- Update to the latest upstream's release - rc17
- Remove patch

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-0.2rc16
- Rebuilt for Python 3.10

* Wed May 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc16
- Update to the latest upstream's release - rc16

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc15
- Add additional doc files found in repository to docs

* Sat May 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc15
- Update to the latest upstream's release - rc15

* Fri Apr 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc14
- Removing sed commands - dependencies already removed
- Added JOSS paper in documents

* Fri Apr 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc14
- New version of package

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.5rc13
- Add examples in subpackage

* Tue Apr 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.4rc13
- Install additional docs

* Tue Mar 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.3rc13
- Skip one test (it is failing from time to time, because of random)

* Fri Mar 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc13
- Remove dependency generator
- Conditional imports for tests

* Wed Mar 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc13
- New version

* Thu Feb 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.5rc12
- Removing linter errors and typos

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4rc12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 4 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.3rc12
- New release - 2.0.0rc12
- Remove dependencies - xlwt, xlsxwriter
- New dependency - openpyxl

* Fri Nov 20 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc11
- New release - 2.0.0rc11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2rc10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-0.1rc10
- Remove dep on enum34
- Add python_provides for F32

* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.2-1
- Initial package

