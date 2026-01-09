Name:           R-S4Vectors
Version:        %R_rpm_version 0.48.0
Release:        %autorelease
Summary:        S4 implementation of vectors and lists

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.48.0

%description
The S4Vectors package defines the Vector and List virtual classes and a set of
generic functions that extend the semantic of ordinary vectors and lists in R.
Package developers can easily implement vector-like or list-like objects as
concrete subclasses of Vector or List. In addition, a few low-level concrete
subclasses of general interest (e.g. DataFrame, Rle, and Hits) are implemented
in the S4Vectors package itself (many more are implemented in the IRanges
package and in other Bioconductor infrastructure packages).

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
