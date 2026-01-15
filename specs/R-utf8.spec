Name:           R-utf8
Version:        %R_rpm_version 1.2.6
Release:        %autorelease
Summary:        Unicode Text Processing

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Process and print 'UTF-8' encoded international text (Unicode). Input,
validate, normalize, encode, format, and display.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
