Name:           R-Rcpp
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Seamless R and C++ Integration

#		The following three files uses the Boost Software License:
#		- Rcpp/inst/include/Rcpp/utils/tinyformat/tinyformat.h
#		- Rcpp/inst/include/Rcpp/macros/config.hpp
#		- Rcpp/inst/include/Rcpp/macros/cat.hpp
License:        GPL-2.0-or-later AND BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:	dos2unix
Obsoletes:      %{name}-devel <= 1.1.0

%description
The Rcpp package provides R functions as well as C++ classes which
offer a seamless integration of R and C++. Many R data types and
objects can be mapped back and forth to C++ equivalents which
facilitates both writing of new code as well as easier integration of
third-party libraries.
Documentation about Rcpp is provided by several vignettes included in
this package, via the Rcpp Gallery site at http://gallery.rcpp.org,
the paper by Eddelbuettel and Francois (2011, JSS), and the book by
Eddelbuettel (2013, Springer).
See citation("Rcpp") for details on the last two.

%package        examples
Summary:        Rcpp Examples
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
Examples for using Rcpp.

%prep
%autosetup -c

dos2unix -k \
    Rcpp/inst/tinytest/cpp/InternalFunction.cpp \
    Rcpp/inst/tinytest/cpp/InternalFunctionCPP11.cpp

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
rm -rf %{buildroot}%{_R_libdir}/Rcpp/tinytest

sed 's!/bin/env Rscript!/usr/bin/Rscript!' \
    -i %{buildroot}%{_R_libdir}/Rcpp/discovery/cxx0x.R
chmod 755 %{buildroot}%{_R_libdir}/Rcpp/discovery/cxx0x.R

for f in ConvolveBenchmarks/overhead.r ConvolveBenchmarks/overhead.sh \
	 Misc/ifelseLooped.r Misc/newFib.r OpenMP/OpenMPandInline.r ; do
    chmod 755 %{buildroot}%{_R_libdir}/Rcpp/examples/$f
done

for f in `find %{buildroot}%{_R_libdir}/Rcpp/examples -type f` ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done

%R_save_files
grep -v examples %{R_files} > %{R_files}.main
grep examples %{R_files} > %{R_files}.examples

%check
%R_check

%files -f %{R_files}.main

%files examples -f %{R_files}.examples

%changelog
%autochangelog
