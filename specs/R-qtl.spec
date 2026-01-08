Name:           R-qtl
Version:        %R_rpm_version 1.74
Release:        %autorelease
Summary:        Tools for analyzing QTL experiments

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
R-qtl is an extensible, interactive environment for mapping
quantitative trait loci (QTLs) in experimental crosses. Our goal is to
make complex QTL mapping methods widely accessible and allow users to
focus on modeling rather than computing.

A key component of computational methods for QTL mapping is the hidden
Markov model (HMM) technology for dealing with missing genotype
data. We have implemented the main HMM algorithms, with allowance for
the presence of genotyping errors, for backcrosses, intercrosses, and
phase-known four-way crosses.

The current version of R-qtl includes facilities for estimating
genetic maps, identifying genotyping errors, and performing single-QTL
genome scans and two-QTL, two-dimensional genome scans, by interval
mapping (with the EM algorithm), Haley-Knott regression, and multiple
imputation. All of this may be done in the presence of covariates
(such as sex, age or treatment). One may also fit higher-order QTL
models by multiple imputation and Haley-Knott regression.

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
