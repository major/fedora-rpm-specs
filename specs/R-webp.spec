Name:           R-webp
Version:        %R_rpm_version 1.3.0
Release:        %autorelease
Summary:        A New Format for Lossless and Lossy Image Compression

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  libwebp-devel

%description
Lossless webp images are 26% smaller in size compared to PNG. Lossy webp
images are 25-34% smaller in size compared to JPEG. This package reads and
writes webp images into a 3 (rgb) or 4 (rgba) channel bitmap array using
conventions from the 'jpeg' and 'png' packages.

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
