Name:           R-xml2
Version:        %R_rpm_version 1.5.1
Release:        %autorelease
Summary:        Parse XML

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  libxml2-devel
Obsoletes:      %{name}-devel <= 1.5.1

%description
Work with XML files using a simple, consistent interface. Built on top of
the 'libxml2' C library.

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
