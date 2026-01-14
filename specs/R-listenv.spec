Name:           R-listenv
Version:        %R_rpm_version 0.10.0
Release:        %autorelease
Summary:        Environments Behaving (Almost) as Lists

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
List environments are environments that have list-like properties.  For
instance, the elements of a list environment are ordered and can be
accessed and iterated over using index subsetting, e.g. 'x <- listenv(a =
1, b = 2); for (i in seq_along(x)) x[[i]] <- x[[i]] ^ 2; y <- as.list(x)'.

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
