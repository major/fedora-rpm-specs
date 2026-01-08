Name:           R-mlbench
Version:        %R_rpm_version 2.1-6
Release:        %autorelease
Summary:        Machine Learning Benchmark Problems

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A collection of artificial and real-world machine learning benchmark
problems, including, e.g., several data sets from the UCI repository.

%prep
%autosetup -c
# Fix encoding.
iconv --from=ISO-8859-1 --to=UTF-8 mlbench/NEWS > NEWS.new && \
    touch -r mlbench/NEWS NEWS.new && \
    mv NEWS.new mlbench/NEWS

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
