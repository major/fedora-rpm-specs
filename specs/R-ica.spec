Name:           R-ica
Version:        %R_rpm_version 1.0-3
Release:        %autorelease
Summary:        Independent Component Analysis

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Independent Component Analysis (ICA) using various algorithms:
FastICA, Information-Maximization (Infomax), and Joint
Approximate Diagonalization of Eigenmatrices (JADE).

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
