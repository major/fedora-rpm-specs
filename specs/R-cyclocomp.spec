Name:           R-cyclocomp
Version:        %R_rpm_version 1.1.1
Release:        %autorelease
Summary:        Cyclomatic Complexity of R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Cyclomatic complexity is a software metric (measurement), used to indicate
the complexity of a program. It is a quantitative measure of the number of
linearly independent paths through a program's source code. It was
developed by Thomas J. McCabe, Sr. in 1976.

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
