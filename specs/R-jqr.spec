Name:           R-jqr
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Client for 'jq', a 'JSON' Processor

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  jq-devel

%description
Client for 'jq', a 'JSON' processor (<https://jqlang.github.io/jq/>),
written in C. 'jq' allows the following with 'JSON' data: index into,
parse, do calculations, cut up and filter, change key names and values,
perform conditionals and comparisons, and more.

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
