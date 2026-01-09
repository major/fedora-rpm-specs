Name:           R-winch
Version:        %R_rpm_version 0.1.2
Release:        %autorelease
Summary:        Portable Native and Joint Stack Traces

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libunwind)

Provides:       bundled(libbacktrace) = 1.0

%description
Obtain the native stack trace and fuse it with R's stack trace for easier
debugging of R packages with native code.

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
