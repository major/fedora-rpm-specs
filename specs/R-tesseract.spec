Name:           R-tesseract
Version:        %R_rpm_version 5.2.4
Release:        %autorelease
Summary:        Open Source OCR Engine

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  tesseract-langpack-eng

%description
Bindings to 'Tesseract' <https://opensource.google/projects/tesseract>: a
powerful optical character recognition (OCR) engine that supports over 100
languages. The engine is highly configurable in order to tune the detection
algorithms and obtain the best possible results.

%prep
%autosetup -c
rm -f tesseract/tests/spelling.R # unconditional suggest, should be fixed

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
