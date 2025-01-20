%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We would like to generate PDF documentation as a substitute, but have not
# been able to successfully build the Sphinx-generated LaTeX for this
# particular package.
%bcond_without doc_pdf

Name:           python-pdf2image
Version:        1.16.3
Release:        8%{?dist}
Summary:        Convert PDF to PIL Image object

License:        MIT
URL:            https://github.com/Belval/pdf2image
Source:         %{url}/archive/v.%{version}/pdf2image-v.%{version}.tar.gz

# Import memory_profiler only when it is enabled
# https://github.com/Belval/pdf2image/pull/269
Patch:          %{url}/pull/269.patch

BuildArch:      noarch

%global _description %{expand:
A wrapper around the pdftoppm and pdftocairo
command line tools to convert PDF to a PIL
Image list.}

%description %_description

%package -n python3-pdf2image
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:  poppler

%if %{with tests}
BuildRequires:  python3dist(pytest) >= 3.7.1
BuildRequires:  poppler
%endif

%description -n python3-pdf2image %_description

%package doc
Summary:        Documentation and examples for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-recommonmark
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
%endif

%description doc
%{summary}.

Full HTML documentation is available at
https://belval.github.io/pdf2image/

%prep
%autosetup -n pdf2image-v.%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet -f'
%endif

%install
%pyproject_install
%pyproject_save_files pdf2image

%check
%if %{with tests}
%pytest tests.py
%endif

%files -n python3-pdf2image -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/pdf2image.pdf
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.16.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.16.3-2
- Rebuilt for Python 3.12

* Mon Apr 17 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.16.3-1
- Initial package
