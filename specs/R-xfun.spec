Name:           R-xfun
Version:        %R_rpm_version 0.56
Release:        %autorelease
Summary:        Miscellaneous Functions to Support Packages Maintained by 'Yihui Xie'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Miscellaneous functions commonly used in other packages maintained by
'Yihui Xie'.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
