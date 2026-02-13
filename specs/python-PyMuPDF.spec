%global pypi_name PyMuPDF
%global module_name pymupdf
%global module_name_compat fitz

%bcond docs %{defined fedora}

# mupdf barcode support is available on Fedora only
%bcond barcode 0%{?fedora} 

Name:		python-%{pypi_name}
Version:	1.27.1
Release:	%autorelease
Summary:	Python binding for MuPDF - a lightweight PDF and XPS viewer

License:	AGPL-3.0-or-later
URL:		https://github.com/pymupdf/PyMuPDF
Source0:	%{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz


# Fedora specific patches:
Patch:		0001-fix-test_-font.patch
Patch:		0001-test_pixmap-adjust-to-turbojpeg.patch
Patch:		0001-setup.py-do-not-require-libclang-and-swig.patch
Patch:		0001-tests-adjust-to-verbose-font-warning.patch
Patch:		0001-adjust-tests-to-tesseract-5.5.1.patch
Patch:		0001-tests-conftest-do-not-call-pip.patch

# test dependencies not picked up by generator
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(psutil)
BuildRequires:	tesseract-langpack-eng
%if %{with docs}
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx-copybutton
BuildRequires:	python3-sphinx-notfound-page
BuildRequires:	python3-furo
BuildRequires:	rst2pdf
# work around rst2pdf incompatibility with docutils 0.22
BuildRequires:	python3-roman
%endif
BuildRequires:	gcc gcc-c++
BuildRequires:	swig
BuildRequires:	zlib-devel
BuildRequires:	mupdf-devel mupdf-cpp-devel
BuildRequires:	freetype-devel
BuildRequires:	python3-mupdf
Buildrequires:	python3-mypy

%global _description %{expand:
This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS
viewer. MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats, and it is known for its top performance and high rendering
quality. With PyMuPDF you therefore can also access files with extensions
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.}

%description %_description

%package -n	python3-%{pypi_name}
Summary:	%{summary}
# provide the importable module:
%py_provides python3-%{module_name}
%py_provides python3-%{module_name_compat}
# upstream pyproject.toml is borked so add manually:
Requires:	python3-mupdf

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package	doc
Summary:	Documentation for python-%{pypi_name}
BuildArch:	noarch

%description	doc
python-%{pypi_name}-doc contains documentation and examples for PyMuPDF
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p 1
# disable google analytics for installed doc
sed -i -e "s/,'sphinxcontrib.googleanalytics'//" docs/conf.py
# swig < 4.3 (RHEL 9, Fedora 41) needs this
sed -i -e 's/{swig} --version/{swig} -version/' setup.py

%generate_buildrequires
%pyproject_buildrequires -R

%build
# generate debug symbols via FLAGS
export PYMUPDF_SETUP_MUPDF_BUILD_TYPE='release'
# build against system mupdf:
export PYMUPDF_SETUP_MUPDF_BUILD=''
# build rebased implementation only:
export PYMUPDF_SETUP_IMPLEMENTATIONS='b'
# build breaks on F39/EL9 with limited API, and we depend on py version anyways:
export PYMUPDF_SETUP_PY_LIMITED_API=0
%if 0%{?rhel} && 0%{?rhel} <= 9
%set_build_flags
%endif
CFLAGS="$CFLAGS -I/usr/include -I/usr/include/freetype2 -I/usr/include/mupdf"
LDFLAGS="$LDFLAGS -lfreetype -lmupdf"
%pyproject_wheel
%if %{with docs}
sphinx-build docs docs_built
%endif

%install
%pyproject_install
%pyproject_save_files -L %{module_name} %{module_name_compat}

%check
# linters have no place in distro build tests
SKIP="not test_codespell and not test_pylint"
# test_fontarchives tries to download special module via pip
SKIP="$SKIP and not test_fontarchive"
# test_open2 requires a git checkout
SKIP="$SKIP and not test_open2"
# flake8 has no place in downstream packaging
SKIP="$SKIP and not test_flake8"
# test_2791 fails sporadically with its empiric bounds
SKIP="$SKIP and not test_2791"
# test_3050 is known to fail for distribution builds
SKIP="$SKIP and not test_3050"
# test_subset_fonts needs pymupdf_fonts
SKIP="$SKIP and not test_subset_fonts"
# test_fit_springer depends on font library version (harfbuzz etc)
SKIP="$SKIP and not test_fit_springer"
# test_spikes uses a binary diff on rendered images
SKIP="$SKIP and not test_spikes"
# these compare renderings with system fonts or missing fonts
SKIP="$SKIP and not test_4180 and not test_4613 and not test_htmlbox1"
# test downloads data from the internet
SKIP="$SKIP and not test_4445 and not test_4457 and not test_4533 and not test_4702"
# test requires additional packages
SKIP="$SKIP and not test_4751"
# Fedora's swig returns different results
SKIP="$SKIP and not test_4392"
%if %{without barcode}
# we build mupdf without barcode support
SKIP="$SKIP and not test_barcode"
%endif
%ifarch s390 s390x
# test_3087 crashes on s390 s390x (bigendian mask problem?)
SKIP="$SKIP and not test_3087"
# test_htmlbox1 fails on s390 s390x (bigendian unicode problem?)
SKIP="$SKIP and not test_htmlbox1"
%endif
%ifarch %{ix86}
# test gives the same failure on i686 as on pyodide
SKIP="$SKIP and not test_4435"
%endif
# spuriously failing tests (several archs)
SKIP="$SKIP and not test_insert and not test_3087"
# tests are known to fail with mupdf 1.27.x (reported)
sed -i -e '/^import pymupdf/i import pytest' tests/test_nonpdf.py
sed -i -e '/^def test_layout/i @pytest.mark.xfail(reason="mupdf 1.27.x", strict=True)' tests/test_nonpdf.py
sed -i -e '/^def test_pageids/i @pytest.mark.xfail(reason="mupdf 1.27.x", strict=True)' tests/test_nonpdf.py
export PYMUPDF_SYSINSTALL_TEST=1
%pytest -k "$SKIP"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%{_bindir}/pymupdf

%if %{with docs}
%files doc
%doc docs_built/* README.md
%endif

%changelog
%autochangelog
