Name:           R-gtools
Version:        %R_rpm_version 3.9.5
Release:        %autorelease
Summary:        Various R Programming Tools

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions to assist in R programming, including:
    - assist in developing, updating, and maintaining R and R packages,
    - calculate the logit and inverse logit transformations,
    - test if a value is missing, empty or contains only NA and NULL values,
    - manipulate R's .Last function,
    - define macros,
    - detect odd and even integers,
    - convert strings containing non-ASCII characters (like single quotes) to
      plain ASCII,
    - perform a binary search,
    - sort strings containing both numeric and character components,
    - create a factor variable from the quantiles of a continuous variable,
    - enumerate permutations and combinations,
    - calculate and convert between fold-change and log-ratio,
    - calculate probabilities and generate random numbers from Dirichlet
      distributions,
    - apply a function over adjacent subsets of a vector,
    - modify the TCP_NODELAY flag for socket objects,
    - efficient 'rbind' of data frames, even if the column names don't match,
    - generate significance stars from p-values,
    - convert characters to/from ASCII codes,
    - convert character vector to ASCII representation.

%prep
%autosetup -c

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
