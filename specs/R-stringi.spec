Name:           R-stringi
Version:        %R_rpm_version 1.8.7
Release:        %autorelease
Summary:        Character String Processing Facilities

# See `LICENSE` for breakdown, but ignore the ICU parts that have been unbundled.
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  libicu-devel >= 61

Obsoletes:      %{name}-devel <= 1.8.7

%description
A multitude of character string/text/natural language processing tools: pattern
searching (e.g., with 'Java'-like regular expressions or the 'Unicode'
collation algorithm), random string generation, case mapping, string
transliteration, concatenation, sorting, padding, wrapping, Unicode
normalisation, date-time formatting and parsing, and many more. They are fast,
consistent, convenient, and - owing to the use of the 'ICU' (International
Components for Unicode) library - portable across all locales and platforms.

%prep
%autosetup -c

# Remove bundled code.
rm -r stringi/src/icu74
sed -i -e '/src\/icu74\//d' stringi/MD5

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install \--configure-args="--disable-icu-bundle"
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
