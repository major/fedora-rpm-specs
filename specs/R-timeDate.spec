Name:           R-timeDate
Version:        %R_rpm_version 4051.111
Release:        %autorelease
Summary:        Rmetrics - chronological and calendar objects

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

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
%autosetup -c
# Fix line endings.
for file in timeDate/NAMESPACE timeDate/man/00timeDate-package.Rd \
            timeDate/inst/COPYRIGHT.html timeDate/R/*.R; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done

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
