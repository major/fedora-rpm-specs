Name:           R-R.methodsS3
Version:        %R_rpm_version 1.8.2
Release:        %autorelease
Summary:        S3 Methods Simplified

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Methods that simplify the setup of S3 generic functions and S3 methods.  Major
effort has been made in making definition of methods as simple as possible with
a minimum of maintenance for package developers.  For example, generic
functions are created automatically, if missing, and naming conflict are
automatically solved, if possible.  The method setMethodS3() is a good start
for those who in the future may want to migrate to S4.  This is a
cross-platform package implemented in pure R that generates standard S3
methods.

%prep
%autosetup -c
sed -i 's/\r$//' R.methodsS3/inst/CITATION

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
