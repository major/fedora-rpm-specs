Name:           R-qcc
Version:        %R_rpm_version 2.7
Release:        %autorelease
Summary:        SQC package for R

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
An R package for quality control charting and statistical process control.
The qcc package for the R statistical environment provides:
- Plot Shewhart quality control charts
- Plot Cusum and EMWA charts for continuous data
- Draw operating characteristic curves
- Perform process capability analysis
- Draw Pareto charts and cause-and-effect diagrams

%prep
%autosetup -c
# Fix permissions
find -type f | xargs chmod -x
# Fix line ending
mv qcc/inst/CITATION qcc/inst/CITE
tr -d '\r' <qcc/inst/CITE >qcc/inst/CITATION
rm -f qcc/inst/CITE

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
