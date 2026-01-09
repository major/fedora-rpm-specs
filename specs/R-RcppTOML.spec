Name:           R-RcppTOML
Version:        %R_rpm_version 0.2.3
Release:        %autorelease
Summary:        'Rcpp' Bindings to Parser for "Tom's Obvious Markup Language"

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  tomlplusplus-devel
Requires:       tomlplusplus-devel
Requires:       R-core-devel%{?_isa}
Obsoletes:      %{name}-devel <= 0.2.3

%description
The configuration format defined by 'TOML' (which expands to "Tom's
Obvious Markup Language") specifies an excellent format (described
at <https://toml.io/en/>) suitable for both human editing as well as
the common uses of a machine-readable format. This package uses 'Rcpp'
to connect to the 'toml++' parser written by Mark Gillard to R.

%prep
%autosetup -c
# unbundle toml++
rm -r RcppTOML/inst/include/toml++
ln -s %{_includedir}/toml++ RcppTOML/inst/include/toml++

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# and again
rm -r %{buildroot}%{_R_libdir}/RcppTOML/include/toml++
ln -s %{_includedir}/toml++ %{buildroot}%{_R_libdir}/RcppTOML/include/toml++
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
