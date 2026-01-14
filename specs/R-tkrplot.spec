Name:           R-tkrplot
Version:        %R_rpm_version 0.0-30
Release:        %autorelease
Summary:        TK Rplot

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9

%description
Simple mechanism for placing R graphics in a Tk widget.

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
