Name:           R-hunspell
Version:        %R_rpm_version 3.0.6
Release:        %autorelease
Summary:        High-Performance Stemmer, Tokenizer, and Spell Checker

License:        GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

# Not currently possible to unbundle at the moment.
# https://github.com/ropensci/hunspell/issues/34
Provides: bundled(hunspell) = 1.7.0

%description
Low level spell checker and morphological analyzer based on the famous
'hunspell' library <https://hunspell.github.io>. The package can analyze or
check individual words as well as parse text, latex, html or xml documents.
For a more user-friendly interface use the 'spelling' package which builds
on this package to automate checking of files, documentation and vignettes
in all common formats.

%prep
%autosetup -c
rm -f hunspell/tests/spelling.R # dev stuff

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
