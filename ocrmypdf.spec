%global srcname ocrmypdf

Name:           %{srcname}
Version:        14.0.4
Release:        %autorelease
Summary:        Add an OCR text layer to scanned PDF files

# See all SPDX-License-Identifier tags in files.
# No docs or tests are included in RPM.
License:        MPL-2.0 and Zlib
URL:            https://github.com/ocrmypdf/OCRmyPDF
Source0:        %pypi_source
# Fedora specific.
Patch0001:      0001-Remove-unnecessary-dependencies.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  ghostscript >= 9.50
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

%pyproject_extras_subpkg -n %{srcname} webservice
%{_bindir}/%{srcname}-webservice


%generate_buildrequires
%pyproject_buildrequires -r -x docs -x test


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# Cleanup shebang and executable bits.
for f in src/%{srcname}/*.py src/%{srcname}/*/*.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
    chmod -x $f
done


%build
%pyproject_wheel

# generate html docs
PYTHONPATH="%{pyproject_build_lib}" OCRMYPDF_VERSION="%{version}" sphinx-build-3 docs html
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
install -Dpm 0755 misc/webservice.py %{buildroot}%{_bindir}/%{srcname}-webservice


%check
%{pytest} -ra -n auto --runslow -k 'not test_tesseract_config_invalid'
# For some reason these break and 'work' when run in parallel.
%{pytest} -ra --runslow -k 'test_tesseract_config_invalid'


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
