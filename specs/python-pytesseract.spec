Name:           python-pytesseract
Version:        0.3.13
Release:        %autorelease
Summary:        Python-tesseract is a python wrapper for Google's Tesseract-OCR
License:        Apache-2.0
URL:            https://github.com/madmaze/pytesseract
Source0:        %{url}/archive/v%{version}/pytesseract-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  %{py3_dist pytest}
BuildRequires:  tesseract
BuildRequires:  tesseract-langpack-fra
BuildRequires:  tesseract-langpack-eng
BuildRequires:  tesseract-osd

%global _description %{expand:
Python-tesseract is an optical character recognition (OCR) tool for python. That
is, it will recognize and "read" the text embedded in images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine. It is also
useful as a stand-alone invocation script to tesseract, as it can read all image
types supported by the Pillow and Leptonica imaging libraries, including jpeg,
png, gif, bmp, tiff, and others. Additionally, if used as a script,
Python-tesseract will print the recognized text instead of writing it to a file.}

%description %_description

%package -n     python3-pytesseract
Summary:        %{summary}
Requires:       tesseract

%description -n python3-pytesseract %_description

%prep
%autosetup -p1 -n pytesseract-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytesseract

sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
    %{buildroot}%{python3_sitelib}/pytesseract/pytesseract.py
chmod +x %{buildroot}/%{python3_sitelib}/pytesseract/pytesseract.py

%check
%pyproject_check_import
# https://github.com/madmaze/pytesseract/issues/419
# https://github.com/madmaze/pytesseract/pull/559
%pytest -k 'not test_image_to_string_with_image_type[jpeg2000] and not test_get_languages[incorrect_tessdata_dir] and not test_get_languages[invalid_tessdata_dir]'

%files -n python3-pytesseract -f %{pyproject_files}
%{_bindir}/pytesseract

%changelog
%autochangelog
