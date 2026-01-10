Name:           R-qvalue
Version:        %R_rpm_version 2.42.0
Release:        %autorelease
Summary:        Q-value estimation for false discovery rate control

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
It takes a list of p-values resulting from the simultaneous
testing of many hypotheses and estimates their q-values.
The q-value of a test measures the proportion of false positives
incurred (called the false discovery rate) when that particular
test is called significant. Various plots are automatically
generated, allowing one to make sensible significance cut-offs.
Several mathematical results have recently been shown on the
conservative accuracy of the estimated q-values from this software.
The software can be applied to problems in genomics, brain imaging,
astrophysics, and data mining.

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
