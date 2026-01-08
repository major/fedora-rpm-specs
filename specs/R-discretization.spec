Name:           R-discretization
Version:        %R_rpm_version 1.0-1.1
Release:        %autorelease
Summary:        Data Preprocessing, Discretization for Classification

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of supervised discretization algorithms. It can also
be grouped in terms of top-down or bottom-up, implementing
the discretization algorithms.

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
