Name:           R-XVector
Version:        %R_rpm_version 0.50.0
Release:        %autorelease
Summary:        Representation and manipulation of external sequences

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.50.0

%description
Memory efficient S4 classes for storing sequences "externally" (behind an R
external pointer, or on disk).

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
