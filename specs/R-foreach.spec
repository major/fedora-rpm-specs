Name:           R-foreach
Version:        %R_rpm_version 1.5.2
Release:        %autorelease
Summary:        Provides Foreach Looping Construct

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for the foreach looping construct.  Foreach is an idiom that allows for
iterating over elements in a collection, without the use of an explicit loop
counter.  This package in particular is intended to be used for its return
value, rather than for its side effects.  In that sense, it is similar to the
standard lapply function, but doesn't require the evaluation of a function.
Using foreach without side effects also facilitates executing the loop in
parallel.

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
