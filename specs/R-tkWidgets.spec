Name:           R-tkWidgets
Version:        %R_rpm_version 1.88.0
Release:        %autorelease
Summary:        Widgets to provide user interfaces from bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Widgets to provide user interfaces. tcltk should have been installed for
the widgets to run.

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
