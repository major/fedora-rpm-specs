%global srcname ocrmypdf

Name:           %{srcname}
Version:        16.11.0
Release:        %autorelease
Summary:        Add an OCR text layer to scanned PDF files

# See all SPDX-License-Identifier tags in files.
# No docs or tests are included in RPM.
License:        MPL-2.0 AND Zlib
URL:            https://github.com/ocrmypdf/OCRmyPDF
Source:         %pypi_source %{srcname}
# Fedora specific.
# We drop pi-heif for now, as it is optional.
Patch:          0001-Remove-unnecessary-dependencies.patch
# Fix test_semfree for Python 3.14.
Patch:          https://github.com/ocrmypdf/OCRmyPDF/commit/599fb1a1f6c74918c56c2fac7aa73434fca8d731.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  ghostscript >= 9.50
BuildRequires:  /usr/bin/pdftotext
BuildRequires:  pngquant >= 2.0.0
BuildRequires:  tesseract >= 4.1.1
BuildRequires:  tesseract-osd
BuildRequires:  tesseract-langpack-deu
BuildRequires:  unpaper >= 6.1
BuildRequires:  python3-devel

Requires:       ghostscript >= 9.15
Recommends:     pngquant >= 2.0.0
Requires:       tesseract >= 4.1.1
Recommends:     unpaper >= 6.1

# Dropped because we don't have streamlit.
Obsoletes:      ocrmypdf+webservice < 16.7.0-3

%description
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be
searched or copy-pasted.


%package -n %{srcname}-doc
Summary:        ocrmypdf documentation
License:        CC-BY-SA-4.0

%description -n %{srcname}-doc
Documentation for ocrmypdf


%pyproject_extras_subpkg -n %{srcname} watcher
%{_bindir}/%{srcname}-watcher


%prep
%autosetup -n %{srcname}-%{version} -p1

# Cleanup shebang and executable bits.
for f in src/%{srcname}/*.py src/%{srcname}/*/*.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
    chmod -x $f
done


%generate_buildrequires
%pyproject_buildrequires -x docs -x test -x watcher


%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" OCRMYPDF_VERSION="%{version}" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{srcname}

# Install completion files.
install -Dpm 0644 misc/completion/ocrmypdf.bash %{buildroot}%{_datadir}/bash-completion/completions/ocrmypdf
install -Dpm 0644 misc/completion/ocrmypdf.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ocrmypdf.fish

# Install optional programs.
install -Dpm 0755 misc/watcher.py %{buildroot}%{_bindir}/%{srcname}-watcher


%check
k="${k-}${k+ and }not test_tesseract_config_invalid"

%{pytest} -ra -n auto --runslow -k "${k-}"


%files -n %{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ocrmypdf
%{_datadir}/bash-completion/completions/ocrmypdf
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ocrmypdf.fish

%files -n %{srcname}-doc
%doc html
%license LICENSE


%changelog
%autochangelog
