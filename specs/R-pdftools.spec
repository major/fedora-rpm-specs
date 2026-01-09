Name:           R-pdftools
Version:        %R_rpm_version 3.6.0
Release:        %autorelease
Summary:        Text Extraction, Rendering and Converting of PDF Documents

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-data

%description
Utilities based on 'libpoppler' for extracting text, fonts, attachments and
metadata from a PDF file. Also supports high quality rendering of PDF documents
into PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing
in R.

%prep
%autosetup -c

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
