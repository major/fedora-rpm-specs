Name:           R-AUC
Version:        %R_rpm_version 0.3.2
Release:        %autorelease
Summary:        Threshold independent performance measures for probabilistic classifiers

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
This package includes functions to compute the area under the curve of
selected measures: The area under the sensitivity curve (AUSEC), the area
under the specificity curve (AUSPC), the area under the accuracy curve
(AUACC), and the area under the receiver operating characteristic curve
(AUROC). The curves can also be visualized. Support for partial areas is

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
