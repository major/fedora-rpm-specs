Name:           R-BufferedMatrix
Version:        %R_rpm_version 1.74.0
Release:        %autorelease
Summary:        A matrix data storage object method from bioconductor

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.74.0

%description
A tabular style data object where most data is stored outside main memory.
A buffer is used to speed up access to data.

%prep
%autosetup -c
sed -i -e 's/\r$//' BufferedMatrix/inst/doc/BufferedMatrix.Rnw

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
