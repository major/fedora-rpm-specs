Name:           R-odbc
Version:        %R_rpm_version 1.6.4.1
Release:        %autorelease
Summary:        Connect to ODBC Compatible Databases (using the DBI Interface)

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  cctz-devel
BuildRequires:  pkgconfig(odbc)

%description
A DBI-compatible interface to ODBC databases.

%prep
%autosetup -c
# Remove bundled cctz.
rm -r odbc/src/cctz
# Link against system cctz.
sed -i \
    -e '/PKG_CXXFLAGS/s!-Icctz/include!-I/usr/include/cctz!' \
    -e '/PKG_LIBS/s!-Lcctz !!' \
    -e '/$(OBJECTS):/s!cctz/libcctz.a!!' \
    odbc/src/Makevars.in

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
