Name:           R-randomForest
Version:        %R_rpm_version 4.7-1.2
Release:        %autorelease
Summary:        Breiman and Cutler's Random Forests for Classification and Regression

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Classification and regression based on a forest of trees using random
inputs, based on Breiman (2001) <DOI:10.1023/A:1010933404324>.

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
