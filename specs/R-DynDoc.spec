Name:           R-DynDoc
Version:        %R_rpm_version 1.88.0
Release:        %autorelease
Summary:        Functions for dynamic documents

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A set of functions to create and interact with dynamic documents and
vignettes.

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
