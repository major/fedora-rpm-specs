%global pypi_name PyMuPDF
%global module_name fitz

Name:           python-%{pypi_name}
Version:        1.23.8
Release:        %autorelease
Summary:        Python binding for MuPDF - a lightweight PDF and XPS viewer

License:        AGPL-3.0-or-later
URL:            https://github.com/pymupdf/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-fix-test_-font.patch
Patch1:         0001-test_pixmap-adjust-to-turbojpeg.patch
Patch2:         0001-adjust-tesseract-tessdata-path-to-Fedora-default.patch
Patch3:         0001-fix-type-error-with-GCC-14.patch

BuildRequires:  python3-devel
BuildRequires:  python3-fonttools
BuildRequires:  python3-pillow
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-furo
BuildRequires:  rst2pdf
BuildRequires:  gcc gcc-c++
BuildRequires:  swig
BuildRequires:  zlib-devel
BuildRequires:  mupdf-devel
BuildRequires:  freetype-devel

%global _description %{expand:
This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats, and it is known for its top performance and high rendering
quality.  With PyMuPDF you therefore can also access files with extensions
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# provide the importable module:
%py_provides python3-%{module_name}

%description -n python3-%{pypi_name} %_description

%package        doc
Summary:        Documentation for python-%{pypi_name}
BuildArch:      noarch

%description    doc
python-%{pypi_name}-doc contains documentation and examples for PyMuPDF

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%build
# generate debug symbols
export PYMUPDF_SETUP_MUPDF_BUILD_TYPE='debug'
# build against system mupdf:
export PYMUPDF_SETUP_MUPDF_BUILD=''
# build original implementation only:
export PYMUPDF_SETUP_IMPLEMENTATIONS='a'
CFLAGS="$CFLAGS -I/usr/include -I/usr/include/freetype2 -I/usr/include/mupdf"
LDFLAGS="$LDFLAGS -lfreetype -lmupdf"
%pyproject_wheel
sphinx-build docs docs_built

%install
%pyproject_install

%check
# FIXME: Crashes with Aborted, corrupted double-linked list
%ifarch s390 s390x
%pytest || :
%else
# test_fontarchives tries to download special module via pip
%pytest -k 'not test_fontarchive'
%endif

%files -n python3-%{pypi_name}
%license COPYING
%{python3_sitearch}/%{module_name}/
%{python3_sitearch}/PyMuPDF*

%files doc
%doc docs_built/* README.md

%changelog
%autochangelog
