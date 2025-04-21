%global packname  timeDate
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          4041.110
Release:          %autorelease
Summary:          Rmetrics - chronological and calendar objects

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-graphics, R-utils, R-stats, R-methods
# Imports:
# Suggests:  R-date, R-RUnit
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel >= 3.0.0
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-methods
BuildRequires:    R-date
BuildRequires:    R-RUnit

%description
The 'timeDate' class fulfils the conventions of the ISO 8601 standard as well
as of the ANSI C and POSIX standards. Beyond these standards it provides the
"Financial Center" concept which allows to handle data records collected in
different time zones and mix them up to have always the proper time stamps with
respect to your personal financial center, or alternatively to the GMT
reference time. It can thus also handle time stamps from historical data
records from the same time zone, even if the financial centers changed day
light saving times at different calendar dates.


%prep
%setup -q -c -n %{packname}

# Fix line endings.
for file in %{packname}/NAMESPACE %{packname}/man/00timeDate-package.Rd \
            %{packname}/inst/COPYRIGHT.html %{packname}/R/*.R; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/COPYRIGHT.html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/_pkgdown.yml
%{rlibdir}/%{packname}/pkgdown.yml
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests


%changelog
%autochangelog
