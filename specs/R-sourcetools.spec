Name:           R-sourcetools
Version:        %R_rpm_version 0.1.7-1
Release:        %autorelease
Summary:        Tools for Reading, Tokenizing and Parsing R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.1.7

%description
Tools for the reading and tokenization of R code. The 'sourcetools' package
provides both an R and C++ interface for the tokenization of R code, and
helpers for interacting with the tokenized representation of R code.

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
