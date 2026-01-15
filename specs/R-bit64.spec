Name:           R-bit64
Version:        %R_rpm_version 4.6.0-1
Release:        %autorelease
Summary:        A S3 Class for Vectors of 64bit Integers

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Package 'bit64' provides serializable S3 atomic 64bit (signed) integers. These
are useful for handling database keys and exact counting in +-2^63. WARNING: do
not use them as replacement for 32bit integers, integer64 are not supported for
subscripting by R-core and they have different semantics when combined with
double, e.g. integer64 + double => integer64. Class integer64 can be used in
vectors, matrices, arrays and data.frames. Methods are available for coercion
from and to logicals, integers, doubles, characters and factors as well as many
elementwise and summary functions. Many fast algorithmic operations such as
'match' and 'order' support interactive data exploration and manipulation and
optionally leverage caching.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%ifnarch s390x
%R_check
%endif

%files -f %{R_files}

%changelog
%autochangelog
